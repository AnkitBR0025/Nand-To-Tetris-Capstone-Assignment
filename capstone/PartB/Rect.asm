
// Draws a rectangle of width 16 pixels.
// Height is stored in RAM[0].

@SCREEN
D=A
@addr
M=D

@0
D=M
@n
M=D

(LOOP)
@n
D=M
@END
D;JEQ

@addr
A=M
M=-1

// Move to the same column in the next screen row.
// Each screen row contains 32 words.
@addr
D=M
@32
D=D+A
@addr
M=D

@n
M=M-1

@LOOP
0;JMP

(END)
@END
0;JMP
