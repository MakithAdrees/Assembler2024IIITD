import os
import argparse
from instructions import Instruction_Check as ff
#Format $python3 Assembler.py input_assembly_code_file_path output_machine_code_file_path
register = {'zero':'00000','ra':'00001','sp':'00010','gp':'00011','tp':'00100','t0':'00101','t1':'00110','t2':'00111','s0':'01000','fp':'01000','s1':'01001','a0':'01010','a1':'01011','a2':'01100','a3':'01101','a4':'01110','a5':'01111','a6':'10000','a7':'10001','s2':'10010','s3':'10011','s4':'10100','s5':'10101','s6':'10110','s7':'10111','s8':'11000','s9':'11001','s10':'11010','s11':'11011','t3':'11100','t4':'11101','t5':'11110','t6':'11111'}
output = []


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

def export_file(file_path, lines):
    with open(file_path, 'w') as file:
        for a in lines:
            file.write(a+'\n')

parser = argparse.ArgumentParser(description='Assembler for RISC-V')
parser.add_argument('input', type=str, help='Input file path')
parser.add_argument('output', type=str, help='Output file path')
args = parser.parse_args()

lines = import_file(args.input)

# function for splitting the instruction and rest of the part
for a in range(len(lines)):
    lines[a] = lines[a].split(' ')

def LabelToImm(labels, a, label):
    lst = labels[label]
    minn = lst[0]
    for i in lst:
        if abs(i-a) < abs(minn-a):
            minn = i
    return  (minn)


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



def main(lines, register):
    for a in range(len(lines)):
        if len(lines[a]) == 1 :
            continue
        if len(lines[a]) > 3:
            print('InvalidInstruction in line', a+1)
        try:
            if len(lines[a]) == 2 and lines[a][0][-1] == ':':
                print('InvalidInstruction in line', a+1)
        except:
            continue


        if len(lines[a]) == 1:
            print('InvalidInstruction in line', a+1)

    
    labels = label(lines)
    
    for a in range(len(lines)):
        if lines[a] == [''] :
            continue
        # if len(lines[a]) > 2:
        #     print('InvalidInstruction in line', a+1)

        # try:
        if lines[a][0][-1] != ':':
            instruction = lines[a][0]
            if lines[a][1].count(',') >2:
                output.append(f'InvalidInstruction in line {a+1}')
            if lines[a][1].count(',') == 0:
                output.append(f'InvalidArguments in line {a+1}')
            if lines[a][1].count(',') == 2:
                reg = lines[a][1].split(',')
                try:
                    output.append(ff(instruction, reg[0], reg[1], int(eval(reg[2])) , line_no = a+1))
                except:   
                    if reg[2] in register:
                        output.append(ff(instruction, reg[0], reg[1], reg[2] , line_no = a+1))
                    elif reg[2] in labels:
                        minn = LabelToImm(labels, a, reg[2])
                        output.append(ff(instruction, reg[0], reg[1], 4*(minn-a) , line_no = a+1))
                    else:
                        output.append(ff(instruction, reg[0], reg[1], 'invalid' , line_no = a+1))

            
            elif '(' in lines[a][1] and ')' in lines[a][1]:
                reg = lines[a][1].split(',')
                reg2 = reg[1].split('(')
                try:
                    output.append(ff(instruction, reg[0], reg2[1][:-1], int(eval(reg2[0])) , line_no = a+1))
                except:
                    output.append(ff(instruction, reg[0], reg2[1][:-1], 'InvalidImmediateVal' , line_no = a+1))
            
            elif lines[a][1].count(',') == 1:
                reg = lines[a][1].split(',')
                try:
                    output.append(ff(instruction, reg[0], int(eval(reg[1])) , line_no = a+1))
                except:    
                    if reg[1] in register:
                        output.append(ff(instruction, reg[0], reg[1] , line_no = a+1))
                    elif reg[1] in labels:
                        minn = LabelToImm(labels, a, reg[1])
                        
                        output.append(ff(instruction, reg[0], 4*(minn-a) , line_no = a+1))
                    
                    else:
                        output.append(ff(instruction, reg[0], 'invalid' , line_no = a+1))
        
        # except:
        #     print('Error in line', a+1)
    return output
            
output = main(lines, register)
errors = []

for a in output:
    if len(a) != 32 and a.isdigit() == False:
        print(a)
        errors.append(a)

print()
if output[-1] != '00000000000000000000000001100011' and '00000000000000000000000001100011' not in output:
    errors.append('No VirtualHalt instruction found')
    print('No VirtualHalt instruction found')
    print()
    print('Errors in the code')
    print()

    with open(args.output, 'w') as file:
        file.write('')
    exit()
    
elif output[-1] != '00000000000000000000000001100011':
    errors.append('VirtualHalt instruction not at code end')
    print('VirtualHalt instruction not at code end')
    print()
    print('Errors in the code')
    print()
    with open(args.output, 'w') as file:
        file.write('')
    exit()
        
if len(errors) > 0:
    
    print('Errors in the code')
    print()
    with open(args.output, 'w') as file:
        file.write('')
    exit()
    
else:
    
    with open(args.output, 'w') as file:
        for a in output:
            if len(a) == 32:
                file.write(a+'\n')
    print(f"Pogram ran Successfully and output is stored in {args.output} file") 
