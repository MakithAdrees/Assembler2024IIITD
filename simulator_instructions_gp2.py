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
    
def sltiu(code, registers):
    reg = BinToDec(code[-20:-15])        #finding registers
    imm = code[:12]
    if imm > reg:
        registers[code[-12:-7]] = 1
    return registers
    # print("sltiu")
    
def jalr(code, registers):
    reg = registers["00101"]
    pc = registers["PC"]
    imm = BinToDec(code[:12])
    registers[code[-12:-7]] = pc+4
    registers["PC"] = reg + imm
    return registers
    # print("jalr")
    
def I_Type(code, registers):
    iType = ["000","010","011","addi(code, registers)","jalr(code, registers)","lw(code, registers)","sltiu(code, registers)"]
    s = iType.index(code[-15:-12])
    iterate = 4
    if code[-7:] == "0010011":
        iterate = 3
    eval(iType[s+iterate])

# B type instructions_______________________________________________________________

def Beq(code, registers):
    rs1 = BinToDec(code[:7])
    rs2 = BinToDec(code[-12:-7])
    imm = BinToDec(code[0] + code[-8] + code[1:7] + code[-12:-8] + '0')
    if rs1 == rs2:
        registers["PC"] = registers["PC"] + imm

# def Bne(code, registers):
#     # code

# def Bge(code, registers):
#     # code

# def Bgeu(code, registers):
#     # code

# def Blt(code, registers):
#     # code

# def Bltu(code, registers):
#     # code

def B_Type(code, registers):
    iType = ["000","001","100","101","110","111"]
    iInst = ['Beq(code, registers)','Bne(code, registers)','Blt(code, registers)','Bge(code, registers)','Bltu(code, registers)','Bgeu(code, registers)']
    s = iType.index(code[-15:-12])
    eval(iInst[s])

# U type instructions_______________________________________________________________



# J type instructions_______________________________________________________________


I_Type('1111111110010111 000 000 1100111',{})
B_Type('1111111110010111 000 000 1100111',{})
