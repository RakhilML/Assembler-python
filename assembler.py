import re               #Importing re(Regular Expression) module to check whether
                        #to check if a particular string matches a given regular expression
    
acommands=[]
asm=[]                  #Empty list to store the values as the asm file is processed


"""Dictionary to correctly parse a C instruction
C-instruction syntax: dest = comp;jump

For example if my dest is M Register in asm file, Python will accesss my dest dictionary
and the binary code corresponding to it i.e. 001 is stored"""

#Similarly we can do it for jump and comp 
dest={'':'000','M=':'001','D=':'010','MD=':'011',
      'A=':'100','AM=':'101','AD=':'110','AMD=':'111'}
jump={'':'000',';JGT':'001',';JEQ':'010',';JGE':'011',
      ';JLT':'100',';JNE':'101',';JLE':'110',';JMP':'111'}
comp={'0':'0101010','1':'0111111','-1':'0111010','D':'0001100',
      'A':'0110000','M':'1110000','!D':'0001101','!A':'0110001',
      '!M':'1110001','-D':'0001111','-A':'0110011','-M':'1110011',
      'D+1':'0011111','A+1':'0110111','M+1':'1110111','D-1':'0001110',
      'A-1':'0110010','M-1':'1110010','D+A':'0000010','D+M':'1000010',
      'D-A':'0010011','D-M':'1010011','A-D':'0000111','M-D':'1000111',
      'D&A':'00000000','D&M':'1000000','D|A':'0010101','D|M':'1010101'}

#Adding the predefined symbols in a Symbol table

symbols={'SP':0,'LCL':1,'ARG':2,'THIS':3,'THAT':4,'SCREEN':16384,'KBD':24576,
         'R0':0,'R1':1,'R1':1,'R2':2,'R3':3,'R4':4,'R5':5,'R6':6,'R7':7,
         'R8':8,'R9':9,'R10':10,'R11':11,'R12':12,'R13':13,'R14':14,'R15':15}


#Opening the asm file
f=input('File:')        #Mentioning File to be opened
asmfile=open(f+'.asm','r')
for line in asmfile:        #Traversing the file using for loop
    ln=re.sub(r'\/+.*\n|\n| *','',line) #Replacing new line with whitespace
    if ln!='':
        acommands.append(ln)    # Appending the file contents in list acommands
asmfile.close()             #Closing the asmfile

lineno=0         
for command in acommands:
    symbol=re.findall(r'\(.+\)',command)  #Will return all the values of command from given string
    if symbol!=[]:
        if symbol[0][1:-1] not in symbols:
            symbols[symbol[0][1:-1]] = lineno
            lineno-=1
    lineno+=1               #Moving to next line                

for line in acommands:
    ln=re.sub(r'\(.+\)','',line)
    if ln!='':
        asm.append(ln)
 
variableno=16   
for command in asm:
    symbol=re.findall(r'@[a-zA-Z]+.*',command)  #Matching all strings with command
    if symbol!=[]:          #Checking if our asm file contains any symbol
        if symbol[0][1:] not in symbols:
            symbols[symbol[0][1:]] = variableno
            variableno+=1

hackfile=open(f+'.hack','w')        #Making our Hack file
for command in asm:
    if command[0]=='@':             #Checking if it is A instruction
        address=0
        if command[1:] in symbols:
            address=symbols[command[1:]]+32768
        else:
            address=int(command[1:])+32768
        hackfile.write('0'+bin(address)[3:]+'\n')
    else:
        de=re.findall(r'.+=',command)
        if de!=[]:
            d=dest[str(de[0])]              #Checking dest command
        else:
            d=dest['']
        
        je=re.findall(r';.+',command)
        if je!=[]:
            j=jump[str(je[0])]              #Checking jump command
        else:
            j=jump['']
            
        c=comp[re.sub(r'.+=|;.+','',command)]       #Writing our C instruction
        hackfile.write('111'+c+d+j+'\n')            
        
hackfile.close()            #Closing the hackfile

