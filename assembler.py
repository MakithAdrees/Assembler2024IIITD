import os
import argparse

#Format $python3 Assembler.py input_assembly_code_file_path output_machine_code_file_path

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

for a in range(len(lines)):
    lines[a] = lines[a].split(' ')


register = {}

def label(lines):
    labels = {}
    for a in range(len(lines)):
        if lines[a][0][-1] == ':':
            if lines[a][0][:-1] not in labels:
                labels[lines[a][0][:-1]] = [a]
            else:
                labels[lines[a][0][:-1]] += [a]
            lines[a] = lines[a][1:]
    return labels


def main(lines, register):

    for a in range(len(lines)):
        if len(lines[a]) > 3:
            print('InvalidInstruction at line', a+1)

        if len(lines[a]) == 2 and lines[a][0][-1] == ':':
            print('InvalidInstruction at line', a+1)

        if len(lines[a]) == 1:
            print('InvalidInstruction at line', a+1)

    
    labels = label(lines)
    
    for a in range(len(lines)):
        if len(lines[a]) > 2:
            print('InvalidInstruction at line', a+1)

        if lines[a][0][-1] != ':':
            instruction = lines[a][0]
            if lines[a][1].count(',') == 2:
                reg = lines[a][1].split(',')
                try:
                    ff(instruction, reg[0], reg[1], int(reg[2]))
                except:    
                    if reg[2] in register:
                        ff(instruction, reg[0], reg[1], reg[2])
                    elif reg[2] in labels:
                        min = labels[reg[2]][0]
                    
                        for b in labels[reg[2]]:
                            if abs(b-a) < abs(min-a):
                                min = b
                        
                        ff(instruction, reg[0], reg[1], 4*(a-min))
                    
                    else:
                        ff(instruction, reg[0], reg[1], 'invalid')
            
            elif '(' in lines[a][1] and ')' in lines[a][1]:
                reg = lines[a][1].split(',')
                reg2 = reg[1].split('(')
                try:
                    ff(instruction, reg[0], reg2[1][:-1], int(reg2[0]))
                except:
                    ff(instruction, reg[0], reg2[1][:-1], 'InvalidImmediateVal')
            
            elif lines[a][1].count(',') == 1:
                reg = lines[a][1].split(',')
                try:
                    ff(instruction, reg[0], int(reg[1]))
                except:    
                    if reg[1] in register:
                        ff(instruction, reg[0], reg[1])
                    elif reg[1] in labels:
                        min = labels[reg[1]][0]
                    
                        for b in labels[reg[1]]:
                            if abs(b-a) < abs(min-a):
                                min = b
                        
                        ff(instruction, reg[0], 4*(a-min))
                    
                    else:
                        ff(instruction, reg[0], 'invalid')
            
            
                
                
            
            
            
# add rd, rs1, rs2
# lw rd, imm[11:0](rs1)
# jal rd, imm[20:1]
