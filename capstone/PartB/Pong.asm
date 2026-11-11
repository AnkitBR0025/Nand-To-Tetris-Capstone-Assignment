
// Mini Pong-style demonstration
// Alternates a marker between two screen positions.

(LOOP)

// Draw at first position
@SCREEN
M=0

@SCREEN
D=A
@32
A=D+A
M=-1

// Draw at second position
@SCREEN
D=A
@64
A=D+A
M=0

@SCREEN
D=A
@96
A=D+A
M=-1

@LOOP
0;JMP
