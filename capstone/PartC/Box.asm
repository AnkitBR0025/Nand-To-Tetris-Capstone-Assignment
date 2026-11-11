// Capstone Box program for roll number 2501350030 (K = 30)
// Box: rows 30 through 49; 20 rows tall; 48 pixels wide (3 words).
// A key press draws the box; releasing all keys clears it.

(LOOP)
    @KBD
    D=M
    @DRAW
    D;JNE

// No key pressed: clear the 20 x 3-word rectangle.
    @17344
    D=A
    @R13
    M=D
    @20
    D=A
    @R14
    M=D
(CLEAR_ROW)
    @R13
    A=M
    M=0
    @R13
    M=M+1
    @R13
    A=M
    M=0
    @R13
    M=M+1
    @R13
    A=M
    M=0
    @R13
    M=M+1
    @29
    D=A
    @R13
    M=D+M
    @R14
    MD=M-1
    @CLEAR_ROW
    D;JGT
    @LOOP
    0;JMP

// A key is pressed: fill each of the 20 rows with three all-black words.
(DRAW)
    @17344
    D=A
    @R13
    M=D
    @20
    D=A
    @R14
    M=D
(DRAW_ROW)
    @R13
    A=M
    M=-1
    @R13
    M=M+1
    @R13
    A=M
    M=-1
    @R13
    M=M+1
    @R13
    A=M
    M=-1
    @R13
    M=M+1
    @29
    D=A
    @R13
    M=D+M
    @R14
    MD=M-1
    @DRAW_ROW
    D;JGT
    @LOOP
    0;JMP
