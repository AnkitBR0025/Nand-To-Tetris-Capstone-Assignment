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
