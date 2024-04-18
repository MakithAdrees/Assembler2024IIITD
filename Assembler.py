import os
import argparse
#Format $python3 Assembler.py input_assembly_code_file_path output_machine_code_file_path
register = {'zero':'00000','ra':'00001','sp':'00010','gp':'00011','tp':'00100','t0':'00101','t1':'00110','t2':'00111','s0':'01000','fp':'01000','s1':'01001','a0':'01010','a1':'01011','a2':'01100','a3':'01101','a4':'01110','a5':'01111','a6':'10000','a7':'10001','s2':'10010','s3':'10011','s4':'10100','s5':'10101','s6':'10110','s7':'10111','s8':'11000','s9':'11001','s10':'11010','s11':'11011','t3':'11100','t4':'11101','t5':'11110','t6':'11111'}
output = []
register = {'zero':'00000','ra':'00001','sp':'00010','gp':'00011','tp':'00100','t0':'00101','t1':'00110','t2':'00111','s0':'01000','fp':'01000','s1':'01001','a0':'01010','a1':'01011','a2':'01100','a3':'01101','a4':'01110','a5':'01111','a6':'10000','a7':'10001','s2':'10010','s3':'10011','s4':'10100','s5':'10101','s6':'10110','s7':'10111','s8':'11000','s9':'11001','s10':'11010','s11':'11011','t3':'11100','t4':'11101','t5':'11110','t6':'11111'}

def ImmToBin(imm):
    binabs = ''
    absolute = abs(imm)
    maxx = 31
    while maxx != -1:
        s = absolute - 2**maxx
        if s < 0:
            binabs += '0'
        else:
            binabs += '1'
            absolute = s
        maxx -= 1
    
    if imm >= 0:
        return binabs
    else:
        binabs = ImmToBin(abs(imm)-1)
        binimm = ''
        for i in binabs:
            if i == '0':
                binimm += '1'
            else:
                binimm += '0'
        return binimm


# all instructions....
    
# R type instructions_______________________________________________________________________________________

def Add(rd, rs1, rs2, register , line_no):
    try:
        return '0000000'+register[rs2]+register[rs1]+'000'+register[rd]+'0110011'
    except:
        if rs1 or rs2 or rd not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)
    
def Sub(rd, rs1, rs2, register , line_no):
    try:
        if rs1=='x0':
            return('0100000'+register[rs2]+register['zero']+'000'+register[rd]+'0110011')
        else:
            return('0100000'+register[rs2]+register[rs1]+'000'+register[rd]+'0110011')
    except:
        if rs1 or rs2 or rd not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

def Slt(rd, rs1, rs2, register , line_no):
    try:
        return ('0000000' + register[rs2] + register[rs1] + '010' + register[rd] + '0110011')
    except:
        if rd or rs1 or rs2 not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

def Sltu(rd, rs1, rs2, register , line_no):
    try:
        return '0000000'+register[rs2]+register[rs1]+'011'+register[rd]+'0110011'
    except:
        if rs1 or rs2 or rd not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

def Xor(rd, rs1, rs2, register , line_no):
    try:
        return('0000000'+register[rs2]+register[rs1]+'100'+register[rd]+'0110011')
    except:
        if rs1 or rs2 or rd not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

def Sll(rd, rs1, rs2, register , line_no):
    try:
        return '0000000'+register[rs2]+register[rs1]+'001'+register[rd]+'0110011'
    except:
        if rs1 or rs2 or rd not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)
    
def Srl(rd, rs1, rs2, register , line_no):
    try:
        return ('0000000' + register[rs2] + register[rs1] + '101' + register[rd] + '0110011')
    except:
        if rd or rs1 or rs2 not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

def Or(rd, rs1, rs2, register , line_no):
    try:
        return '0000000'+register[rs2]+register[rs1]+'110'+register[rd]+'0110011'
    except:
        if rs1 or rs2 or rd not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

def And(rd, rs1, rs2, register , line_no):
    try:
        return('0000000'+register[rs2]+register[rs1]+'111'+register[rd]+'0110011')
    except:
        if rs1 or rs2 or rd not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

# I type instructions______________________________________________________________________________________

def Lw(rd, rs1, imm, register , line_no):
    try:
        if imm >= 2**11 or imm < -2**11:
            return ('ImmediateOutOfRange in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        return ImmToBin(imm)[-12:]+register[rs1]+'010'+register[rd]+'0000011'
    except:
        if rs1 or rd not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

def Addi(rd, rs1, imm, register , line_no):
    try:
        if imm >= 2**11 or imm < -2**11:
            return ('ImmediateOutOfRange in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    
    try:
        return (ImmToBin(imm)[-12:] + register[rs1] + '000' + register[rd] + '0010011')  #using only the last 12 LSBs
    except:
        if rd or rs1 not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

def Sltiu(rd, rs1, imm, register , line_no):
    try:
        if imm >= 2**11 or imm < -2**11:
            return ('ImmediateOutOfRange in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        return ImmToBin(imm)[-12:]+register[rs1]+'011'+register[rd]+'0010011'
    except:
        if rs1 or rd not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

def Jalr(rd, rs1, imm, register , line_no):
    try:
        if imm >= 2**31 or imm < -2**31:
            return ('ImmediateOutOfRange in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        if rs1=='x6':
            return(ImmToBin(imm)[-12:]+register['t1']+'000'+register[rd]+'1100111')
        else:
            return(ImmToBin(imm)[-12:]+register[rs1]+'000'+register[rd]+'1100111')
    except:
        if rs1 or rd not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

# S type instructions______________________________________________________________________________________

def Sw(rs2, rs1, imm, register , line_no):
    try:
        if imm >= 2**11 or imm < -2**11:
            return ('ImmediateOutOfRange in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        return ImmToBin(imm)[-12:-5]+register[rs2]+register[rs1]+'010'+ImmToBin(imm)[-5:]+'0100011'
    except:
        return 'SyntaxError in line ' + str(line_no)

# B type instructions______________________________________________________________________________________

def Beq(rs1, rs2, imm, register , line_no):
    try:
        if imm >= 2**12 or imm < -2**12:
            return ('ImmediateOutOfRange in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        s = ImmToBin(imm)
        return s[-13]+s[-11:-5]+register[rs2]+register[rs1]+'000'+s[-5:-1]+s[-12]+'1100011'
    except:
        return 'SyntaxError in line ' + str(line_no)

def Bne(rs1, rs2, imm, register , line_no):
    try:
        if imm >= 2**12 or imm < -2**12:
            return ('InvalideImmediate in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        s = ImmToBin(imm)
        return s[-13]+s[-11:-5]+register[rs2]+register[rs1]+'001'+s[-5:-1]+s[-12]+'1100011'
    except:
        return 'SyntaxError in line ' + str(line_no)

def Bge(rs1, rs2, imm, register , line_no):
    try:
        if imm >= 2**12 or imm < -2**12:
            return ('InvalideImmediate in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        s = ImmToBin(imm)
        return s[-13]+s[-11:-5]+register[rs2]+register[rs1]+'101'+s[-5:-1]+s[-12]+'1100011'
    except:
        return 'SyntaxError in line ' + str(line_no)

def Bgeu(rs1, rs2, imm, register , line_no):
    try:
        if imm >= 2**12 or imm < -2**12:
            return ('InvalideImmediate in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        return (ImmToBin(imm)[-13] + ImmToBin(imm)[-11:-5] + register[rs2] + register[rs1] + '111' + ImmToBin(imm)[-5:-1] + ImmToBin(imm)[-12] + '1100011')
    except:
        if rs1 or rs2 not in register:
            return ('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

def Blt(rs1, rs2, imm, register , line_no):
    try:
        if imm >= 2**12 or imm < -2**12:
            return ('InvalideImmediate in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        return(ImmToBin(imm)[-13]+ImmToBin(imm)[-11:-5]+register[rs2]+register[rs1]+'100'+ImmToBin(imm)[-5:-1]+ImmToBin(imm)[-12]+'1100011')
    except:
        return 'SyntaxError in line ' + str(line_no)

def Bltu(rs1, rs2, imm, register , line_no):
    try:
        if imm >= 2**12 or imm < -2**12:
            return ('InvalideImmediate in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        s = ImmToBin(imm)
        return s[-13]+s[-11:-5]+register[rs2]+register[rs1]+'110'+s[-5:-1]+s[-12]+'1100011'
    except:
        return 'SyntaxError in line ' + str(line_no)

# U type instructions______________________________________________________________________________________

def Auipc(rd, imm, register , line_no):
    try:
        if imm >= 2**31 or imm < -2**31:
            return ('ImmediateOutOfRange in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        return (ImmToBin(imm)[-32:-12] + register[rd] + '0010111')
    except:
        if rd not in register:
            return ('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

def Lui(rd, imm, register , line_no):
    try:
        if imm >= 2**31 or imm < -2**31:
            return ('ImmediateOutOfRange in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        return(ImmToBin(imm)[-32:-12]+register[rd]+'0110111')
    except:
        return 'SyntaxError in line ' + str(line_no)

# J type instructions______________________________________________________________________________________

def Jal(rd, imm, register , line_no):
    try:
        if imm >= 2**20 or imm < -2**20:
            return ('ImmediateOutOfRange in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        return (ImmToBin(imm)[-21]+ImmToBin(imm)[-11:-1]+ImmToBin(imm)[-12]+ImmToBin(imm)[-20:-12]+register[rd]+'1101111')
    except:
        if rd not in register:
            return ('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

# Bonus Type Instruction______________________________________________________________________________________4

def Mul(rd, rs1, rs2, register, line_no):
    try:
        return('0000000'+register[rs2]+register[rs1]+'000'+register[rd]+'1111111')
    except:
        if rs1 or rs2 or rd not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)
    
def Rst(register, line_no):
    return '00000000000000000001000001111111'

def Halt(register, line_no):
    return '00000000000000000010000001111111'

def Rvrs(rd, rs1, register, line_no):
    try:
        return('000000000000'+register[rs1]+'011'+register[rd]+'1111111')
    except:
        if rs1 or rd not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)
    

# Function that checks which instruction is called and then calls that function

def ff(inst, rd=None, rs1 = None, rs2 = None , line_no = None):
    register = {'zero':'00000','ra':'00001','sp':'00010','gp':'00011','tp':'00100','t0':'00101','t1':'00110','t2':'00111','s0':'01000','fp':'01000','s1':'01001','a0':'01010','a1':'01011','a2':'01100','a3':'01101','a4':'01110','a5':'01111','a6':'10000','a7':'10001','s2':'10010','s3':'10011','s4':'10100','s5':'10101','s6':'10110','s7':'10111','s8':'11000','s9':'11001','s10':'11010','s11':'11011','t3':'11100','t4':'11101','t5':'11110','t6':'11111'}
    # if rs1 or rs2 or rd not in register:
    #         return('Error, Register Index out of range')
    if inst=="add":
        return Add(rd, rs1, rs2, register , line_no)
    elif inst=="sub":
        return Sub(rd, rs1, rs2, register , line_no)
    elif inst=="slt":
        return Slt(rd, rs1, rs2, register , line_no)
    elif inst=="sltu":
        return Sltu(rd, rs1, rs2, register , line_no)
    elif inst=="xor":
        return Xor(rd, rs1, rs2, register , line_no)
    elif inst=="sll":
        return Sll(rd, rs1, rs2, register , line_no)
    elif inst=="srl":
        return Srl(rd, rs1, rs2, register , line_no)
    elif inst=="or":
        return Or(rd, rs1, rs2, register , line_no)
    elif inst=="and":
        return And(rd, rs1, rs2, register , line_no)
    elif inst=="lw":
        return Lw(rd, rs1, rs2, register , line_no)
    elif inst=="addi":
        return Addi(rd, rs1, rs2, register , line_no)
    elif inst=="sltiu":
        return Sltiu(rd, rs1, rs2, register , line_no)
    elif inst=="jalr":
        return Jalr(rd, rs1, rs2, register , line_no)
    elif inst =="sw":
        return Sw(rd,rs1,rs2,register , line_no)
    elif inst =="beq":
        return Beq(rd,rs1,rs2,register , line_no)
    elif inst =="bne":
        return Bne(rd,rs1,rs2,register , line_no)
    elif inst =="blt":
        return Blt(rd,rs1,rs2,register , line_no)
    elif inst =="bge":
        return Bge(rd,rs1,rs2,register ,line_no)
    elif inst =="bltu":
        return Bltu(rd,rs1,rs2,register,line_no)
    elif inst =="bgeu":
        return Bgeu(rd,rs1,rs2,register,line_no)
    elif inst =="lui":
        return Lui(rd,rs1,register,line_no)
    elif inst =="auipc":
        return Auipc(rd,rs1,register,line_no)
    elif inst =="jal":
        return Jal(rd,rs1,register,line_no)
    elif inst =="mul":
        return Mul(rd,rs1,rs2,register,line_no)
    elif inst =="rst":
        return Rst(register,line_no)
    elif inst =="halt":
        return Halt(register,line_no)
    elif inst =="rvrs":
        return Rvrs(rd,rs1,register,line_no)
    return('IncorrectInstruction in line ' + str(line_no))
# function to import file(data) from the txt file
def import_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            lines = [x.strip() for x in lines]
            return lines
    except:
        print('File not found')
        exit()

#function to export the binary converted data to a txt file
def export_file(file_path, lines):
    with open(file_path, 'w') as file:
        for a in lines:
            file.write(a+'\n')

parser = argparse.ArgumentParser(description='Assembler for RISC-V')
parser.add_argument('input', type=str, help='Input file path')
parser.add_argument('output', type=str, help='Output file path')
args = parser.parse_args()

lines = import_file(args.input)

# function for splitting the labels, instruction, registers and the rest of the part
for a in range(len(lines)):
    lines[a] = lines[a].split(' ')

def LabelToImm(labels, a, label):
    lst = labels[label]
    minn = lst[0]
    for i in lst:
        if abs(i-a) < abs(minn-a):
            minn = i
    return  (minn)


#function if there is a label in the line, the function stores the label in a dict....
def label(lines):
    labels = {}
    for a in range(len(lines)):
        if len(lines[a]) == 1:
            continue
        if lines[a][0][-1] == ':':
            if lines[a][0][:-1] not in labels:
                labels[lines[a][0][:-1]] = [a]
            else:
                labels[lines[a][0][:-1]] += [a]
            lines[a] = lines[a][1:]
    return labels

#This is the main program that checks for the number of registers, labels, instructions and more
# The function checks for errors too
def main(lines, register):
    for a in range(len(lines)):
        if len(lines[a]) == 1 :
            continue
        if len(lines[a]) > 3:                                          #if there are more than 2 spaces in the instruction line(string) then print error
            print('InvalidInstruction in line', a+1)
        # try:
        #     if len(lines[a]) == 2 and lines[a][0][-1] == ':':          #if there is only 1 space in the string but the first element is a label then it prints error as the format is incorrect
        #         print('InvalidInstruction in line', a+1)
        # except:
        #     continue

        if len(lines[a]) == 1:                                         #if there are no spaces in the string then it prints error as the format is incorrect
            print('InvalidInstruction in line', a+1)     

    labels = label(lines)
    
    for a in range(len(lines)):
        if lines[a] == [''] :
            continue
        # if len(lines[a]) > 2:
        #     print('InvalidInstruction in line', a+1)

        try:
            if lines[a][0][-1] != ':':                                  
                instruction = lines[a][0]
                if lines[a][0] == lines[a][-1]:
                    output.append(ff(instruction, line_no = a+1))       #executes when only name instruction is given
                    continue
                if lines[a][1].count(',') >2:                           #prints error is number of commas are greater than 2
                    output.append(f'InvalidInstruction in line {a+1}')
                if lines[a][1].count(',') == 0:                         #prints error if there are no commas in the string
                    output.append(f'InvalidArguments in line {a+1}')
                if lines[a][1].count(',') == 2:                         #checks if there are 2 or 1 commas
                    reg = lines[a][1].split(',')
                    try:
                        output.append(ff(instruction, reg[0], reg[1], int(reg[2]) , line_no = a+1))           #it executes when there are 2 registers and one immediate value
                    except:   
                        if reg[2] in register:
                            output.append(ff(instruction, reg[0], reg[1], reg[2] , line_no = a+1))            #it executes when all 3 are registers
                        elif reg[2] in labels:
                            minn = LabelToImm(labels, a, reg[2])
                            output.append(ff(instruction, reg[0], reg[1], 4*(minn-a) , line_no = a+1))        #it executes when there are 2 registers and one label
                        else:
                            output.append(ff(instruction, reg[0], reg[1], 'invalid' , line_no = a+1))         #it executes when the 3rd register is none of the above

                elif '(' in lines[a][1] and ')' in lines[a][1]:
                    reg = lines[a][1].split(',')
                    reg2 = reg[1].split('(')
                    try:
                        output.append(ff(instruction, reg[0], reg2[1][:-1], int(reg2[0]) , line_no = a+1))
                    except:
                        output.append(ff(instruction, reg[0], reg2[1][:-1], 'InvalidImmediateVal' , line_no = a+1))
                
                elif lines[a][1].count(',') == 1:                                                            #it executes when there is only one comma in the string
                    reg = lines[a][1].split(',')
                    try:
                        output.append(ff(instruction, reg[0], int(reg[1]) , line_no = a+1))                  #it executes when one is reg and second is imm
                    except:    
                        if reg[1] in register:
                            output.append(ff(instruction, reg[0], reg[1] , line_no = a+1))                   #it executes when both are registers
                        elif reg[1] in labels:
                            minn = LabelToImm(labels, a, reg[1])
                            
                            output.append(ff(instruction, reg[0], 4*(minn-a) , line_no = a+1))               #it executes when one is reg and second is a label
                        
                        else:
                            output.append(ff(instruction, reg[0], 'invalid' , line_no = a+1))
        
        except:
            print('Error in line', a+1)
    return output
            
output = main(lines, register)
errors = []

for a in output:
    if len(a) != 32 and a.isdigit() == False:
        print(a)
        errors.append(a)

print()
if output == []:
    print('No instruction')
    with open(args.output, 'w') as file:
        file.write('')
    exit()

elif output[-1] != '00000000000000000000000001100011' and '00000000000000000000000001100011' not in output:        #it checks if the virtual halt is present in output or not
    print('No VirtualHalt instruction found')
    print()
    print('Errors in the code')
    print()

    with open(args.output, 'w') as file:
        file.write('')
    exit()
    
elif output[-1] != '00000000000000000000000001100011':              #it checks if virtual halt is present in last line or not
    print('VirtualHalt instruction not at code end')
    print()
    print('Errors in the code')
    print()

        
if len(errors) > 0:
    
    print('Errors in the code')
    print()
    
else:
    
    with open(args.output, 'w') as file:
        for a in output[:-1]:
            if len(a) == 32:
                file.write(a+'\n')
        if len(output[-1]) == 32:
            file.write(output[-1])
    print(f"Pogram ran Successfully and output is stored in {args.output} file")            #it executes when the programs executes without any error and the output is stored successfully in the txt file
