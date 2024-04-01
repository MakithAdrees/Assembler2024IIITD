def binary_to_decimal(bin):
    dec=0
    power=len(bin)-1
    for digit in bin:
        if digit=='1':
            dec+=2**power
        power-=1
    return dec

def DecToBin(decimal):
    binary = bin(decimal)[2:]
    return binary
def BinToDec(binary):
    decimal = "0000"
    return decimal

# I type instructions_______________________________________________________________

def addi(code, registers):
    reg = registers[code[-20:-15]]        #finding registers
    imm = BinToDec(code[:12])                       #finding immediate
    sum = imm+reg         #finding new rd
    registers[code[-12:-7]] = sum         #rd updated
    return registers
    # print("addi")

def lw(code, registers):
    #arnesh will do it
    #will do it on 3 april
    print("lw")
    return registers

    
def sltiu(code, registers):
    rs1 = registers[code[-20:-15]]
    imm = code[:12]
    if imm > rs1:
        registers[code[-12:-7]] = 1
    return registers
    # print("sltiu")
    
    
def jalr(code, registers):
    rs1 = registers["00101"]
    pc = registers["PC"]
    imm = BinToDec(code[:12])
    registers[code[-12:-7]] = pc+4
    registers["PC"] = rs1 + imm
    return registers
    # print("jalr")
    
    
def I_Type(code, registers):
    iType = ["000","010","011","addi(code, registers)","jalr(code, registers)","lw(code, registers)","sltiu(code, registers)"]
    s = iType.index(code[-15:-12])
    iterate = 4
    if code[-7:] == "0010011":
        iterate = 3
    return eval(iType[s+iterate])

# B type instructions_______________________________________________________________

def Beq(code, registers):
    rs1 = registers[code[:7]]
    rs2 = registers[code[-12:-7]]
    imm = BinToDec(code[0] + code[-8] + code[1:7] + code[-12:-8] + '0')
    if rs1 == rs2:
        registers["PC"] = registers["PC"] + imm
    return registers


# def Bne(code, registers):
#     # code

# def Bge(code, registers):
#     # code


def Bgeu(code, registers):
    rs1 = registers[code[-20:-15]]
    rs2 = registers[code[-25:-20]]
    imm = BinToDec(code[-32] + code[-8] + code[-31:-25] + code[-12:-8] + '0')
    if rs1 > rs2:
        registers["PC"] = registers["PC"] + imm
    return registers


def Blt(code, registers):
    rs1 = registers[code[-20:-15]]
    rs2 = registers[code[-25:-20]]
    imm = BinToDec(code[-32] + code[-8] + code[-31:-25] + code[-12:-8] + '0')
    if rs1 < rs2:
        registers["PC"] = registers["PC"] + imm
    return registers


def Bltu(code, registers):
    rs1 = registers[code[-20:-15]]
    rs2 = registers[code[-25:-20]]
    imm = BinToDec(code[-32] + code[-8] + code[-31:-25] + code[-12:-8] + '0')
    if rs1 < rs2:
        registers["PC"] = registers["PC"] + imm
    return registers


def B_Type(code, registers):
    bType = ["000","001","100","101","110","111"]
    bInst = ['Beq(code, registers)','Bne(code, registers)','Blt(code, registers)','Bge(code, registers)','Bltu(code, registers)','Bgeu(code, registers)']
    s = bType.index(code[-15:-12])
    return eval(bInst[s])


# S type instructions_______________________________________________________________
def sw(code, registers):
    rs1 = registers[-20:-15]
    rs2 = registers[-25:-20]
    imm = BinToDec(code[-32:-25] + code[-12:-7])
    #incomplete
    return registers

    
def S_Type(code, registers):
    sType = ["010"]
    sInst = ['sw(code, registers)']
    s = sType.index(code[-15:-12])
    return eval(sInst[s])


# J type instructions_______________________________________________________________


I_Type('1111111110010111 000 000 1100111',{})
B_Type('1111111110010111 000 000 1100111',{})
