# Part B – Python Hack Assembler

## Overview

In Part B, I developed a Python-based two-pass Hack Assembler that translates Hack Assembly Language instructions into 16-bit binary machine code.

The assembler supports:

- A-instructions and C-instructions.
- Predefined Hack symbols.
- User-defined labels.
- Automatic variable allocation starting from RAM address 16.
- Symbol table generation.
- Assembly of multiple `.asm` files in one execution.

## Project Files

```text
PartB/
├── assembler.py
├── Add.asm
├── Add.hack
├── Max.asm
├── Max.hack
├── Rect.asm
├── Rect.hack
├── Pong.asm
├── Pong.hack
├── symbols.txt
└── README.md
```

## Requirements

- Python 3.8 or newer
- Nand2Tetris CPU Emulator
- VS Code or any Python-compatible editor

No third-party Python packages are required.

## How to Run

Open PowerShell inside the `PartB` directory.

Check Python:

```powershell
python --version
```

Run the assembler:

```powershell
python assembler.py Add.asm Max.asm Rect.asm Pong.asm
```

The assembler processes all four programs and generates:

- `Add.hack`
- `Max.hack`
- `Rect.hack`
- `Pong.hack`
- `symbols.txt`

The generated `.hack` files are saved directly in the `PartB` directory.

## Assembler Working

The assembler uses two passes.

### Pass 1 – Label Processing

- Reads the assembly program.
- Removes comments and blank lines.
- Identifies labels.
- Stores label names with their ROM addresses.

### Pass 2 – Machine Code Generation

- Converts A-instructions into 16-bit binary.
- Converts C-instructions using the destination, computation, and jump tables.
- Allocates variables starting from RAM address 16.
- Generates the final `.hack` file.

## Symbol Table – Personalized Feature

My university roll number is 2501350030.

Therefore:

`K = 30`

`K mod 3 = 0`

For the personalized requirement, the assembler saves user-defined labels and allocated variables with their addresses and types in `symbols.txt`.

The symbol table contains separate sections for each assembled program.

## Testing

The generated machine-code files were loaded into the Nand2Tetris CPU Emulator.

- **Add.asm:** Tests addition and stores the result in RAM[0].
- **Max.asm:** Compares two values and stores the maximum in RAM[2].
- **Rect.asm:** Tests rectangular screen drawing.
- **Pong.asm:** Tests the supplied compact Pong-style screen-write program.

**Note:** The included `Pong.asm` is a compact demonstration program, not the complete official Nand2Tetris Pong game.

## Expected Output

A successful assembly displays messages similar to:

```text
Successfully assembled: Add.asm
Successfully assembled: Max.asm
Successfully assembled: Rect.asm
Successfully assembled: Pong.asm

Symbol table saved successfully!
All files assembled successfully!
```

The exact instruction counts depend on the source files.