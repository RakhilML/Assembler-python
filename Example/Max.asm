// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/06/max/Max.asm

// Computes R2 = max(R0, R1)  (R0,R1,R2 refering to RAM[0],RAM[1],RAM[2])

@R0
D=M              // D = first input
@R1
D=D-M            // D = first input - second input
@OUTPUT_FIRST
D;JGT            // if D>0 (if first input is greater) goto OUTPUT_FIRST
@R1
D=M              // D = second input
@OUTPUT_D
0;JMP            // goto OUTPUT_D
                 (OUTPUT_FIRST)
@R0             
D=M              // D = first input
                 (OUTPUT_D)
@R2
M=D              // M[2] = D (greatest input)
                 (INFINITE LOOP)
@INFINITE_LOOP

0;JMP            // infinite loop
