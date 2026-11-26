import re
import argparse
from pathlib import Path


# 1. Predefined symbols
SYMBOLS = {
    "SP": 0, "LCL": 1, "ARG": 2,
    "THIS": 3, "THAT": 4,
    "SCREEN": 16384, "KBD": 24576
}

for i in range(16):
    SYMBOLS["R" + str(i)] = i


# 2. Machine code tables
DEST = {
    "": "000", "M": "001", "D": "010",
    "MD": "011", "A": "100", "AM": "101",
    "AD": "110", "AMD": "111"
}

JUMP = {
    "": "000", "JGT": "001", "JEQ": "010",
    "JGE": "011", "JLT": "100", "JNE": "101",
    "JLE": "110", "JMP": "111"
}

COMP = {
    "0": "0101010", "1": "0111111",
    "-1": "0111010", "D": "0001100",
    "A": "0110000", "M": "1110000",
    "!D": "0001101", "!A": "0110001",
    "!M": "1110001", "-D": "0001111",
    "-A": "0110011", "-M": "1110011",
    "D+1": "0011111", "A+1": "0110111",
    "M+1": "1110111", "D-1": "0001110",
    "A-1": "0110010", "M-1": "1110010",
    "D+A": "0000010", "D+M": "1000010",
    "D-A": "0010011", "D-M": "1010011",
    "A-D": "0000111", "M-D": "1000111",
    "D&A": "0000000", "D&M": "1000000",
    "D|A": "0010101", "D|M": "1010101"
}


# 3. Read and clean assembly file
def read_file(filename):

    instructions = []

    with open(filename, "r") as file:

        for line in file:

            # Remove comments
            line = line.split("//")[0].strip()

            # Remove spaces
            line = "".join(line.split())

            if line:
                instructions.append(line)

    return instructions


def read_file_with_lines(filename):

    instructions = []
    line_numbers = []

    with open(filename, "r") as file:

        for line_number, line in enumerate(file, start=1):
            line = line.split("//")[0].strip()
            line = "".join(line.split())

            if line:
                instructions.append(line)
                line_numbers.append(line_number)

    return instructions, line_numbers


# 4. First pass: Find labels
def first_pass(instructions):

    symbols = SYMBOLS.copy()
    labels = {}

    rom_address = 0

    for line in instructions:

        if line.startswith("(") and line.endswith(")"):

            label = line[1:-1]

            if not re.fullmatch(r"[A-Za-z_.$:][A-Za-z0-9_.$:]*", label):
                raise ValueError("Invalid label: " + label)

            if label in symbols:
                raise ValueError("Duplicate or reserved label: " + label)

            symbols[label] = rom_address
            labels[label] = rom_address

        else:
            rom_address += 1

    return symbols, labels


# 5. Convert C-instruction
def convert_c_instruction(line):

    if line.count("=") > 1 or line.count(";") > 1:
        raise ValueError("Invalid C-instruction: " + line)

    if "=" in line:
        dest, remaining = line.split("=")
    else:
        dest = ""
        remaining = line

    if ";" in remaining:
        comp, jump = remaining.split(";")
    else:
        comp = remaining
        jump = ""

    if dest not in DEST:
        raise ValueError("Invalid destination: " + dest)

    if comp not in COMP:
        raise ValueError("Invalid computation: " + comp)

    if jump not in JUMP:
        raise ValueError("Invalid jump: " + jump)

    return "111" + COMP[comp] + DEST[dest] + JUMP[jump]


# 6. Second pass: Generate machine code
def second_pass(instructions, symbols, line_numbers=None):

    machine_code = []
    variables = {}

    next_address = 16

    for index, line in enumerate(instructions):

        # Skip labels
        if line.startswith("(") and line.endswith(")"):
            continue

        # A-instruction
        if line.startswith("@"):

            symbol = line[1:]

            if not symbol:
                raise ValueError("Empty A-instruction")

            if symbol.isdigit():

                address = int(symbol)

            else:

                if not re.fullmatch(
                    r"[A-Za-z_.$:][A-Za-z0-9_.$:]*", symbol
                ):
                    raise ValueError("Invalid symbol: " + symbol)

                if symbol not in symbols:

                    symbols[symbol] = next_address
                    variables[symbol] = next_address

                    next_address += 1

                address = symbols[symbol]

            if address > 32767:
                raise ValueError("Address out of range: " + symbol)

            machine_code.append(format(address, "016b"))

        # C-instruction
        else:

            try:
                binary = convert_c_instruction(line)
            except ValueError as error:
                if line_numbers:
                    raise ValueError(
                        "Line " + str(line_numbers[index]) + ": " + str(error)
                    ) from error
                raise
            machine_code.append(binary)

    return machine_code, variables


# 7. Save symbol table
def save_symbols(all_symbols, filename):

    with open(filename, "w") as file:

        file.write("Symbol\tAddress\tType\n")

        for program, labels, variables in all_symbols:

            file.write("\nProgram: " + program + "\n")

            for name, address in labels.items():
                file.write(
                    name + "\t" + str(address) + "\tLABEL\n"
                )

            for name, address in variables.items():
                file.write(
                    name + "\t" + str(address) + "\tVARIABLE\n"
                )


def assemble(source, output=None, symbols_file=None):
    source = Path(source)
    instructions, line_numbers = read_file_with_lines(source)

    symbols, labels = first_pass(instructions)
    machine_code, variables = second_pass(
        instructions, symbols, line_numbers
    )

    if output is None:
        output = source.with_suffix(".hack")
    else:
        output = Path(output)
    output.write_text(
        "\n".join(machine_code) + ("\n" if machine_code else ""),
        encoding="utf-8"
    )

    if symbols_file is not None:
        symbols_file = Path(symbols_file)
        save_symbols(
            [(source.name, labels, variables)],
            symbols_file
        )

    return len(machine_code), labels, variables


# 8. Main assembler function
def main():

    parser = argparse.ArgumentParser(
        description="Nand2Tetris Hack Assembler"
    )

    parser.add_argument(
        "files",
        nargs="+",
        help="Input assembly files"
    )

    args = parser.parse_args()

    folder = Path(__file__).resolve().parent
    output_folder = folder

    all_symbols = []

    for filename in args.files:

        try:

            instructions = read_file(filename)

            # First pass
            symbols, labels = first_pass(instructions)

            # Second pass
            machine_code, variables = second_pass(
                instructions, symbols
            )

            # Save machine code
            output_file = output_folder / (
                Path(filename).stem + ".hack"
            )

            with open(output_file, "w") as file:
                file.write("\n".join(machine_code) + "\n")

            all_symbols.append(
                (Path(filename).name, labels, variables)
            )

            print("Successfully assembled:", filename)
            print("Instructions:", len(machine_code))

        except (ValueError, OSError) as error:

            print("Error:", error)
            return

    # Roll number 30: 30 mod 3 = 0
    # Save labels and variables
    save_symbols(
        all_symbols,
        folder / "symbols.txt"
    )

    print("\nSymbol table saved successfully!")
    print("All files assembled successfully!")


# 9. Program execution starts here
if __name__ == "__main__":
    main()
