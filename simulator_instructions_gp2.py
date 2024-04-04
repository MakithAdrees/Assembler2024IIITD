def binary_to_decimal(bin):
    dec=0
    power=len(bin)-1
    for digit in bin:
        if digit=='1':
            dec+=2**power
        power-=1
    return dec

# I type instructions_______________________________________________________________

def addi(code, registers): #unchecked
    rs1 = registers[code[-20:-15]]                  #finding registers
    imm = code[:12]                       #finding immediate
    sum = BinSum(sext(imm, len(rs1))+rs1)                                   #finding new rd
    registers[code[-12:-7]] = sum                   #rd updated
    return registers
    # print("addi")

def lw(code, registers, memory):   #unchecked
    rs1 = registers[code[-20:-15]]
    imm = code[:12]
    registers[code[-12:-7]] = memory[BinSum(rs1 + sext(imm, len(rs1)))]
    return registers
    # print("lw")
    
def sltiu(code, registers):
    rs1 = registers[code[-20:-15]]
    imm = code[:12]
    if UBinToDec(imm) > UBinToDec(rs1):
        registers[code[-12:-7]] = '1'
    return registers
    # print("sltiu")
    
    
def jalr(code, registers):
    rs1 = registers["00101"]
    pc = registers["PC"]
    imm = Bin2ToDec(code[:12])
    registers[code[-12:-7]] = DecToBin(pc+4)
    registers["PC"] = Bin2ToDec(rs1) + imm
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
    imm = Bin2ToDec(code[0] + code[-8] + code[1:7] + code[-12:-8] + '0')
    if sext(rs1) == sext(rs2):
        registers["PC"] = registers["PC"] + imm
    return registers


def Bne(code, registers): #unchecked
    rs1 = registers[code[:7]]
    rs2 = registers[code[-12:-7]]
    imm = Bin2ToDec(code[0] + code[-8] + code[1:7] + code[-12:-8] + '0')
    if sext(rs1) != sext(rs2):
        registers["PC"] = registers["PC"] + imm
        return registers

def Bge(code, registers): #unchecked
    rs1 = registers[code[:7]]
    rs2 = registers[code[-12:-7]]
    imm = Bin2ToDec(code[0] + code[-8] + code[1:7] + code[-12:-8] + '0')
    if Bin2ToDec(rs1) > Bin2ToDec(rs2):
        registers["PC"] = registers["PC"] + imm
        return registers

def Bgeu(code, registers):
    rs1 = registers[code[-20:-15]]
    rs2 = registers[code[-25:-20]]
    imm = Bin2ToDec(code[-32] + code[-8] + code[-31:-25] + code[-12:-8] + '0')
    if UBinToDec(rs1) > UBinToDec(rs2):
        registers["PC"] = registers["PC"] + imm
    return registers

def Blt(code, registers):
    rs1 = registers[code[-20:-15]]
    rs2 = registers[code[-25:-20]]
    imm = Bin2ToDec(code[-32] + code[-8] + code[-31:-25] + code[-12:-8] + '0')
    if Bin2ToDec(rs1) < Bin2ToDec(rs2):
        registers["PC"] = registers["PC"] + imm
    return registers

def Bltu(code, registers):
    rs1 = registers[code[-20:-15]]
    rs2 = registers[code[-25:-20]]
    imm = Bin2ToDec(code[-32] + code[-8] + code[-31:-25] + code[-12:-8] + '0')
    if Bin2ToDec(rs1) < Bin2ToDec(rs2):
        registers["PC"] = registers["PC"] + imm
    return registers

def B_Type(code, registers):
    bType = ["000","001","100","101","110","111"]
    bInst = ['Beq(code, registers)','Bne(code, registers)','Blt(code, registers)','Bge(code, registers)','Bltu(code, registers)','Bgeu(code, registers)']
    s = bType.index(code[-15:-12])
    return eval(bInst[s])


# S type instructions_______________________________________________________________
def sw(code, registers, memory):  #unchecked
    rs1 = registers[code[-20:-15]]
    rs2 = registers[code[-25:-20]]
    imm = Bin2ToDec(code[-32:-25] + code[-12:-7])
    offset = Bin2ToDec(rs1) + imm
    memory[offset] = sext(rs2, 32)
    return registers

    
def S_Type(code, registers):
    sType = ["010"]
    sInst = ['sw(code, registers)']
    s = sType.index(code[-15:-12])
    return eval(sInst[s])


# J type instructions_______________________________________________________________
    
def Jal(code, registers): #unchecked
    rd = code[-12:-7]
    imm = Bin2ToDec(code[0] + code[12:21] + code[11] + code[1:11] + '0')
    registers[rd] = registers["PC"] + 4
    registers["PC"] = registers["PC"] + imm
    return registers

def J_Type(code, registers):
    Jal(code, registers)



J_Type('1111111110010111 000 000 1100111',{})
B_Type('1111111110010111 000 000 1100111',{})
# U_Type('1111111110010111 000 000 1100111',{})
J_Type('1111111110010111 000 000 1100111',{})
