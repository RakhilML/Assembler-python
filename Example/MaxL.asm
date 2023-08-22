// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/06/max/MaxL.asm

// Symbol-less version of the Max.asm program.

@R0
D=M
@R1
D=D-M  //D = first input - second input

@R10
D;JGT
@R1
D=M
@R12
0;JMP
@R0
D=M  // first input

@R2     
M=D  // greatest input
@R14
0;JMP
