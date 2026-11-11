# Nand2Tetris Capstone – Make the Computer Draw a Box

## Student Details

- **Name:** Ankit Kumar Pandey
- **Roll Number:** 2501350030
- **K:** 30
- **Course:** ETCCNT301
- **Project:** Make the Computer Draw a Box

## Project Overview

This capstone project focuses on understanding computer architecture and the internal working of a computer using the Nand2Tetris platform.

The project is divided into three parts:

- **Part A – HDL Implementation:** Implementation and testing of CPU, Memory, and Computer chips.
- **Part B – Hack Assembler:** Development of a Python-based two-pass assembler to translate Hack assembly instructions into machine code.
- **Part C – Box Program:** Development of a Hack Assembly program that draws and clears a rectangular box using keyboard input and screen memory.

## Box Specifications

The box dimensions are calculated using my university roll number.

- K = 30
- Starting row = 30
- Height = 20 rows
- Width = 16 × ((K mod 4) + 1) = 48 pixels
- Number of screen words per row = 3

Starting screen memory address:

`SCREEN + (32 × 30) = 16384 + 960 = 17344`

The program draws the box when a keyboard key is pressed and clears it when no key is pressed.

## Project Structure

```text
capstone/
│
├── README.md
│
├── PartA/
│   ├── CPU.hdl
│   ├── Memory.hdl
│   ├── Computer.hdl
│   ├── CPU.tst
│   ├── CPU.cmp
│   ├── Memory.tst
│   ├── Memory.cmp
│   ├── ComputerAdd.tst
│   ├── ComputerAdd.cmp
│   ├── ComputerMax.tst
│   ├── ComputerMax.cmp
│   ├── ComputerRect.tst
│   └── ComputerRect.cmp
│
├── PartB/
│   ├── assembler.py
│   ├── Add.asm
│   ├── Add.hack
│   ├── Max.asm
│   ├── Max.hack
│   ├── Rect.asm
│   ├── Rect.hack
│   ├── Pong.asm
│   ├── Pong.hack
│   ├── symbols.txt
│   └── README.md
│
└── PartC/
    ├── assembler.py
    ├── Box.asm
    ├── Box.hack
    └── symbols.txt
```

## Requirements

- Python 3.8 or newer
- Nand2Tetris Software Suite
- VS Code (recommended)
- Windows PowerShell

No third-party Python packages are required for the assembler.

## Running the Project

### Part A – HDL Testing

1. Open the Nand2Tetris Hardware Simulator.
2. Load the required HDL files from `PartA/`.
3. Run the corresponding `.tst` test files.
4. Verify the results against the provided `.cmp` files.

### Part B – Hack Assembler

Open PowerShell inside the `PartB` folder and execute:

```powershell
python assembler.py Add.asm Max.asm Rect.asm Pong.asm
```

The assembler generates the corresponding `.hack` files and saves the user-defined labels and variables in `symbols.txt`.

Refer to `PartB/README.md` for more details.

### Part C – Box Program

Open PowerShell inside the `PartC` folder and execute:

```powershell
python assembler.py Box.asm
```

Load the generated `Box.hack` file into the Nand2Tetris CPU Emulator.

1. Start the program.
2. Press and hold a key in the emulator's keyboard panel.
3. Observe the rectangular box appearing on the screen.
4. Release the key and observe the box being cleared.

## Testing and Evidence

Screenshots of the implementation and testing are maintained separately in the project report folder:

```text
report/
└── screenshots/
    ├── PartA/
    ├── PartB/
    └── PartC/
```

## Submission

The `capstone/` folder contains the HDL source files, Python assembler, Hack assembly programs, generated machine-code files, and symbol tables.

The short capstone report and actual test screenshots are submitted through ZOSIMA as required by the assignment.

**Declaration:** I will verify and explain my submitted implementation during the viva.