
def UnsignedToDecimal(binary):
    dec = 0
    pow = len(binary)-1
    for i in binary:
        if i == '1':
            dec += 2**pow
        pow -= 1
    return dec


def SignedToDecimal(binary):
    pow = len(binary)-2
    dec = -int(binary[0]) * 2**(pow+1)
    for i in binary[1:]:
        if i == '1':
            dec += 2**pow
        pow -= 1
    return dec
    

def DecimalTo2sComplement32bit(decimal):
    binary = ''
    if (decimal) < 0:
        decimal = 2**32 + decimal
    while decimal != 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    while len(binary) < 32:
        binary = '0' + binary
    return binary

registers = {"PC":0}
for i in range(32):
    registers[DecimalTo2sComplement32bit(i)[-5:]] = 0

def B_Type(code, registers):
    bType = ["000","001","100","101","110","111"]
    bInst = ['Beq(code, registers)','Bne(code, registers)','Blt(code, registers)','Bge(code, registers)','Bltu(code, registers)','Bgeu(code, registers)']
    s = bType.index(code[-15:-12])
    print(bInst[s])
    return eval(bInst[s])

def Beq(code, registers):
    rs1 = code[-20:-15]
    rs2 = code[-25:-20]
    imm = code[-32] + code[-8] + code[-31:-25] + code[-12:-8] + '0'
    
    if registers[rs1] == registers[rs2]:
        registers["PC"] = registers["PC"] + int(SignedToDecimal(imm)/4)
    else:
        registers["PC"] = registers["PC"] + 1
    return registers

def Bne(code, registers):
    rs1 = code[-20:-15]
    rs2 = code[-25:-20]
    imm = code[-32] + code[-8] + code[-31:-25] + code[-12:-8] + '0'
    if registers[rs1] != registers[rs2]:
        print(registers[rs1], registers[rs2])
        registers["PC"] = registers["PC"] + int(SignedToDecimal(imm)/4)
    else:
        registers["PC"] = registers["PC"] + 1
    return registers

def Bge(code, registers):
    rs1 = code[-20:-15]
    rs2 = code[-25:-20]
    imm = code[-32] + code[-8] + code[-31:-25] + code[-12:-8] + '0'
    if registers[rs1] >= registers[rs2]:
        registers["PC"] = registers["PC"] + int(SignedToDecimal(imm)/4)
    else:
        registers["PC"] = registers["PC"] + 1
    return registers

def Bgeu(code, registers):
    rs1 = code[-20:-15]
    rs2 = code[-25:-20]
    imm = code[-32] + code[-8] + code[-31:-25] + code[-12:-8] + '0'
    if UnsignedToDecimal(DecimalTo2sComplement32bit(registers[rs1])) >= UnsignedToDecimal(DecimalTo2sComplement32bit(registers[rs2])):
        registers["PC"] = registers["PC"] + int(SignedToDecimal(imm)/4)
    else:
        registers["PC"] = registers["PC"] + 1
    return registers

def Blt(code, registers):
    rs1 = code[-20:-15]
    rs2 = code[-25:-20]
    imm = code[-32] + code[-8] + code[-31:-25] + code[-12:-8] + '0'
    if registers[rs1] < registers[rs2]:
        registers["PC"] = registers["PC"] + int(SignedToDecimal(imm)/4)
    else:
        registers["PC"] = registers["PC"] + 1
    return registers

def Bltu(code, registers):
    rs1 = code[-20:-15]
    rs2 = code[-25:-20]
    imm = code[-32] + code[-8] + code[-31:-25] + code[-12:-8] + '0'
    if UnsignedToDecimal(DecimalTo2sComplement32bit(registers[rs1])) < UnsignedToDecimal(DecimalTo2sComplement32bit(registers[rs2])):
        registers["PC"] = registers["PC"] + int(SignedToDecimal(imm)/4)
    else:
        registers["PC"] = registers["PC"] + 1
    return registers

#================================================================================================
#U-Type Instructions

def U_Type(code, registers):
    if code[-7:] == "0110111":
        return Lui(code, registers)
    if code[-7:] == "0010111":
        return Auipc(code, registers)

    return registers
    
def Lui(code, registers):
    imm = SignedToDecimal(code[-32:-12] + 12*'0')
    rd = code[-12:-7]
    registers[rd] = imm
    registers["PC"] = registers["PC"] + 1  

    return registers

def Auipc(code, registers):
    imm = SignedToDecimal(code[-32:-12] + 12*'0')
    rd = code[-12:-7]
    registers[rd] = registers["PC"]*4 + imm
    registers["PC"] = registers["PC"] + 1  

    return registers


#================================================================================================
#I-Type Instructions

def I_Type(code, registers , memory):
    iType = ["000","010","011","Addi(code, registers)","Jalr(code, registers)","Lw(code, registers,memory)","Sltiu(code, registers)"]
    s = iType.index(code[-15:-12])
    iterate = 4
    if code[-7:] == "0010011":
        iterate = 3
    print(iType[s+iterate])
    return eval(iType[s+iterate])

def Addi(code, registers):
    imm = SignedToDecimal(code[-32:-20])
    rd = code[-12:-7]
    rs1 = code[-20:-15]
    registers[rd] = registers[rs1] + imm
    registers["PC"] = registers["PC"] + 1

    return registers

def Jalr(code, registers):   #rs1 could be x6
    imm = SignedToDecimal(code[-32:-20])
    rd = code[-12:-7]
    rs1 = code[-20:-15]
    registers[rd] = registers["PC"]*4 + 4
    registers["PC"] = int(registers[rs1]/4) + int(imm/4)
    return registers

# def Jalr(code, registers):   #rs1 could be x6
#     imm = SignedToDecimal(code[-32:-20])
#     rd = code[-12:-7]
#     rs1 = code[-20:-15]
#     registers[rd] = registers["PC"]*4 + 4
#     #PC = x6 + sext(imm[11:0])
#     registers["PC"] = int(registers["00110"]/4) + int(imm/4)

#     return registers

def Lw(code, registers, memory):
    imm = SignedToDecimal(code[-32:-20])
    rd = code[-12:-7]
    rs1 = code[-20:-15]
    offset = registers[rs1] + imm
    registers[rd] = memory[offset]
    registers["PC"] = registers["PC"] + 1   

    return registers

def Sltiu(code, registers):
    rd = code[-12:-7]
    rs1 = UnsignedToDecimal(DecimalTo2sComplement32bit(registers[code[-20:-15]]))
    imm = UnsignedToDecimal(code[-32:-20])
    registers["PC"] = registers["PC"] + 1 

    if rs1 < imm:
        registers[rd] = 1
    return registers

#================================================================================================
#S-Type Instructions

def S_Type(code, registers, memory):
    sInst = ["Sw(code, registers, memory)"]
    return eval(sInst[0])

def Sw(code, registers, memory):
    imm = SignedToDecimal(code[-32:-25] + code[-12:-7])
    rs1 = code[-20:-15]
    rs2 = code[-25:-20]
    offset = registers[rs1] + imm
    memory[offset] = registers[rs2]
    registers["PC"] = registers["PC"] + 1  

    return memory

#================================================================================================

def Add(code , registers):
    rs2 = code[-25:-20]
    rs1 = code[-20:-15]
    rd = code[-12:-7]

    registers[rd] = registers[rs1] + registers[rs2]
    registers["PC"] = registers["PC"] + 1

    return registers
#sub rd, rs1, rs2 rd = signed(rs1) - signed(rs2)
def Sub(code , registers):
    rs2 = code[-25:-20]
    rs1 = code[-20:-15]
    rd = code[-12:-7]
    registers[rd] = registers[rs1] - registers[rs2]
    registers["PC"] = registers["PC"] + 1

    return registers

#slt rd, rs1, rs2 rd = 1. If sext(rs1) < sext(rs2)
def Slt(code , registers):
    rs2 = code[-25:-20]
    rs1 = code[-20:-15]
    rd = code[-12:-7]
    if registers[rs1] < registers[rs2]:
        registers[rd] = 1
    else:
        registers[rd] = 0
    registers["PC"] = registers["PC"] + 1

    return registers

#sltu rd, rs1, rs2 rd = 1. If unsigned(rs1) < unsigned(rs2)
def Sltu(code , registers):
    rs2 = UnsignedToDecimal(DecimalTo2sComplement32bit(registers(code[-25:-20])))
    rs1 = UnsignedToDecimal(DecimalTo2sComplement32bit(registers(code[-20:-15])))
    rd = code[-12:-7]
    if rs1 < rs2:
        registers[rd] = 1
    else:
        registers[rd] = 0
    registers["PC"] = registers["PC"] + 1

    return registers


#xor rd, rs1, rs2 rd = rs1⊕rs2 (Bitwise Exor)
def Xor(code , registers):
    rs2 = code[-25:-20]
    rs1 = code[-20:-15]
    rd = code[-12:-7]
    registers[rd] = registers[rs1] ^ registers[rs2]
    registers["PC"] = registers["PC"] + 1

    return registers

#sll rd, rs1, rs2 rd = rs1<<unsigned(rs2[4:0])
#Left shift rs1 by the value in lower 5 bits of rs2.

def Sll(code , registers):
    rs2 = code[-25:-20]
    rs1 = code[-20:-15]
    rd = code[-12:-7]
    registers[rd] = registers[rs1] << registers[rs2]
    registers["PC"] = registers["PC"] + 1

    return registers


#srl rd, rs1, rs2 rd = rs1>>unsigned(rs2[4:0])
#Right shift rs1 by the value in lower 5 bits of rs2.

def Srl(code , registers):
    rs2 = code[-25:-20]
    rs2 = UnsignedToDecimal(DecimalTo2sComplement32bit(registers[rs2]) [-6:-1] )
    rs1 = code[-20:-15]
    rd = code[-12:-7]
    print(code)
    registers[rd] = registers[rs1] >> rs2
    registers["PC"] = registers["PC"] + 1

    return registers

#or rd, rs1, rs2 rd = rs1|rs2 (Bitwise logical or.)
def Or(code , registers):
    rs2 = UnsignedToDecimal(DecimalTo2sComplement32bit(registers(code[-25:-20])) [-5])
    rs1 = registers(code[-20:-15])
    rd = code[-12:-7]
    registers[rd] = rs1 | rs2
    registers["PC"] = registers["PC"] + 1

    return registers

#and rd, rs1, rs2 rd = rs1&rs2 (Bitwise logical and.)
def And(code , registers):
    rs2 = code[-25:-20]
    rs1 = code[-20:-15]
    rd = code[-12:-7]

    registers[rd] = registers[rs1] & registers[rs2] 
    registers["PC"] = registers["PC"] + 1

    return registers


def R_Type(code, registers):
    rType = ['000' , '001' , '010' , '011' , '100' , '101' , '110' , '111']
    rInst = ['Add(code, registers)','Sll(code, registers)','Slt(code, registers)','Sltu(code, registers)','Xor( code, registers)','Srl(code, registers)','Or(code, registers)','And(code, registers)']

    s = rType.index(code[-15:-12])
    print(code[0:7])
    if code[0:7] == '0100000' and code[-15:-12] == "000":
        print("Sub")
        return Sub(code, registers)
    else:
        print(rInst[s])
        return eval(rInst[s])

def Jal(code, registers):
    rd = code[-12:-7]
    imm = SignedToDecimal(code[-32] + code[-20:-11] + code[-21] + code[-31:-21] + '0')

    registers[rd] = registers['PC']*4 + 4
    registers['PC'] = registers['PC'] + int(imm/4)
    return registers


def J_type(code, registers):
    if code[-7:] == '1101111':
        return Jal(code, registers)                 


#$python3 Simulator.py input_machine_code_file_path output_trace_file_path

import sys

def main():
    looper = 0
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, 'r') as f:
        lines = f.readlines()
        code = []
        for x in lines:
            code.append(x.strip())

    registers = {"PC":0}
    for i in range(32):
        registers[DecimalTo2sComplement32bit(i)[-5:]] = 0

    registers['00010'] = UnsignedToDecimal("00000000000000000000000100000000")


    registers_out = ""
    memory = {}
    for i in range(32):
        memory[i] = 0
    pc = 0
    while True:
        line = code[pc]

        #R type 0110011
 
        if line[-7:] == "0110011":
            print("R type")
            registers = R_Type(line, registers)

        #I type 0000011 or 0010011 or 1100111
        if line[-7:] == "0000011" or line[-7:] == "0010011" or line[-7:] == "1100111":
            print("I type")
            registers = I_Type(line, registers, memory)

        #S type 0100011
        if line[-7:] == "0100011":
            print("S type")
            memory = S_Type(line, registers, memory)

        #B type 1100011
        if line[-7:] == "1100011":
            print("B type")
            registers = B_Type(line, registers)

        #U type 0010111 or 0110111
        if line[-7:] == "0010111" or line[-7:] == "0110111":
            print("U type")
            registers = U_Type(line, registers)
  
        #J type 1101111
        if line[-7:] == "1101111" :
            print("J type")
            registers = J_type(line, registers)

        print('PC' , +registers['PC'])
        registers['00000'] = 0
        registers_out += "0b"+DecimalTo2sComplement32bit(registers["PC"]*4) + " "
        for i in range(32):
            registers_out += "0b"+DecimalTo2sComplement32bit(registers[DecimalTo2sComplement32bit(i)[-5:]]) + " "
        print('looper ', looper)
        looper += 1
        registers_out += "\n"
        if registers["PC"] == pc:
            break   
        if registers["PC"] >= len(code):
            break
        pc = registers["PC"]


    with open(output_file, 'w') as f:
        f.write(registers_out)




main()