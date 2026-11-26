# Nand2Tetris Capstone – Make the Computer Draw a Box

This folder contains the HDL, assembler and Hack assembly files for my capstone project.

## Student details

- **Name:** Ankit Kumar Pandey
- **University roll number:** 2501350030
- **K:** 30
- **Course:** ETCCNT301 – Nand to Tetris I

## What the project does

The capstone is divided into three parts:

1. **Part A – HDL implementation:** builds logic and sequential hardware components and combines the CPU, memory and computer.
2. **Part B – Hack assembler:** uses Python to translate Hack assembly instructions into 16-bit machine code and records labels and variables in a symbol table.
3. **Part C – Box program:** draws a box on the Hack screen while a key is pressed and clears it after the key is released.

## Box calculation

Using `K = 30`:

- Starting row = `30`
- Height = `20` rows
- Width = `16 × ((30 mod 4) + 1) = 48` pixels
- Words per row = `48 / 16 = 3`
- Starting screen address = `16384 + (32 × 30) = 17344`

The program writes three consecutive screen words on each row. It then adds 29 more words to the pointer, so the next row begins 32 words after the previous row's starting address.

## Folder structure

```text
capstone/
├── README.md
├── assembler.py
├── PartA/
│   ├── PartA1/   # Logic gates, ALU, register, RAM and PC
│   └── PartA2/   # CPU, Memory, Computer and test files
├── PartB/
│   ├── assembler.py
│   ├── Add.asm / Add.hack
│   ├── Max.asm / Max.hack
│   ├── Rect.asm / Rect.hack
│   ├── Pong.asm / Pong.hack
│   └── symbols.txt
└── PartC/
    ├── assembler.py
    ├── Box.asm
    ├── Box.hack
    └── symbols.txt
```

## Requirements

- Python 3.8+
- Nand2Tetris Hardware Simulator and CPU Emulator
- No external Python packages

## Run instructions

**Part A:** Open the Hardware Simulator, load the HDL files and run the available `.tst` files from `PartA/PartA2/`. Compare the result with the matching `.cmp` file.

**Part B:** Open a terminal in `PartB/` and run:

```powershell
python assembler.py Add.asm Max.asm Rect.asm Pong.asm
```

**Part C:** Open a terminal in `PartC/` and run:

```powershell
python assembler.py Box.asm
```

Load `Box.hack` into the CPU Emulator. Start the program, press a key to draw the box, and release the key to clear it.

## Testing evidence

The repository-level Python tests can be run from the project root:

```powershell
python -m unittest discover -s tests -v
```

Screenshots and the full project explanation are in the sibling `report/` folder. See the repository-root `README.md` for the complete project guide.
