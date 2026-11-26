# Part B – Python Hack Assembler

## Overview

For Part B, I implemented a Python-based **two-pass Hack assembler**. It reads Hack assembly (`.asm`) files and converts each instruction into a 16-bit binary machine instruction (`.hack`). The program can assemble more than one input file in a single run.

## Features

- Handles A-instructions and C-instructions.
- Removes comments, blank lines and unnecessary whitespace before processing.
- Recognises predefined symbols such as `SP`, `LCL`, `R0`–`R15`, `SCREEN` and `KBD`.
- Finds user-defined labels and stores their ROM addresses.
- Allocates new variables starting at RAM address 16.
- Writes a symbol table with the symbol name, address and type (`LABEL` or `VARIABLE`).
- Checks invalid destinations, computations, jumps and symbol formats.

## Files

- `assembler.py` – assembler implementation.
- `Add.asm`, `Max.asm`, `Rect.asm`, `Pong.asm` – input assembly programs.
- `Add.hack`, `Max.hack`, `Rect.hack`, `Pong.hack` – generated machine-code files.
- `symbols.txt` – labels and variables found during assembly.

## Requirements

- Python 3.8 or newer
- Nand2Tetris CPU Emulator for running the generated programs
- No third-party Python packages

## Run the assembler

Open PowerShell or a terminal in this `PartB` folder and run:

```powershell
python assembler.py Add.asm Max.asm Rect.asm Pong.asm
```

The generated `.hack` files and `symbols.txt` are saved in the same folder. To assemble only one program, provide just its filename, for example:

```powershell
python assembler.py Add.asm
```

## How the two passes work

### Pass 1 – label collection

1. Read each line and remove comments and whitespace.
2. Ignore empty lines.
3. Find label declarations such as `(LOOP)`.
4. Store each label with the ROM address of the next instruction. Labels do not take up a ROM instruction address.

### Pass 2 – machine-code generation

1. Skip label declarations.
2. Convert an A-instruction (`@value`) to a 16-bit binary value. A numeric value is converted directly; a known symbol is replaced with its address.
3. Allocate an address to a new variable, beginning at RAM address 16.
4. Convert a C-instruction using the computation, destination and jump lookup tables.
5. Write the generated binary instructions to the `.hack` output file.

## Personalised symbol table

My university roll number is `2501350030`, so `K = 30` and `K mod 3 = 0`. The assembler writes the labels and variables found in each input program to `symbols.txt`, grouped by program. The table records the symbol, its address and whether it is a label or a variable.

## Testing the output

Load each generated `.hack` file into the Nand2Tetris CPU Emulator and run it:

- **Add.asm** – adds the values used by the supplied program and stores the result in RAM.
- **Max.asm** – compares the supplied values and stores the larger value.
- **Rect.asm** – runs the supplied rectangle screen program.
- **Pong.asm** – runs a compact screen-write demonstration. It is not the complete official Nand2Tetris Pong game.

The project screenshots in `report/screenshots/PartB/` show assembler execution, emulator runs and the generated symbol table.
