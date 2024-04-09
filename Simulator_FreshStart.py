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
    if decimal < 0:
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
    return eval(bInst[s])

def Beq(code, registers):
    rs1 = code[-20:-15]
    rs2 = code[-25:-20]
    imm = code[-32] + code[-8] + code[-31:-25] + code[-12:-8] + '0'
    if registers[rs1] == registers[rs2]:
        registers["PC"] = registers["PC"] + SignedToDecimal(imm)
    return registers

def Bne(code, registers):
    rs1 = code[-20:-15]
    rs2 = code[-25:-20]
    imm = code[-32] + code[-8] + code[-31:-25] + code[-12:-8] + '0'
    if registers[rs1] != registers[rs2]:
        registers["PC"] = registers["PC"] + SignedToDecimal(imm)
    return registers

def Bge(code, registers):
    rs1 = code[-20:-15]
    rs2 = code[-25:-20]
    imm = code[-32] + code[-8] + code[-31:-25] + code[-12:-8] + '0'
    if registers[rs1] >= registers[rs2]:
        registers["PC"] = registers["PC"] + SignedToDecimal(imm)
    return registers

def Bgeu(code, registers):
    rs1 = code[-20:-15]
    rs2 = code[-25:-20]
    imm = code[-32] + code[-8] + code[-31:-25] + code[-12:-8] + '0'
    if UnsignedToDecimal(DecimalTo2sComplement32bit(registers[rs1])) >= UnsignedToDecimal(DecimalTo2sComplement32bit(registers[rs2])):
        registers["PC"] = registers["PC"] + SignedToDecimal(imm)
    return registers

def Blt(code, registers):
    rs1 = code[-20:-15]
    rs2 = code[-25:-20]
    imm = code[-32] + code[-8] + code[-31:-25] + code[-12:-8] + '0'
    if registers[rs1] < registers[rs2]:
        registers["PC"] = registers["PC"] + SignedToDecimal(imm)
    return registers

def Bltu(code, registers):
    rs1 = code[-20:-15]
    rs2 = code[-25:-20]
    imm = code[-32] + code[-8] + code[-31:-25] + code[-12:-8] + '0'
    if UnsignedToDecimal(DecimalTo2sComplement32bit(registers[rs1])) < UnsignedToDecimal(DecimalTo2sComplement32bit(registers[rs2])):
        registers["PC"] = registers["PC"] + SignedToDecimal(imm)
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
    return registers

def Auipc(code, registers):
    imm = SignedToDecimal(code[-32:-12] + 12*'0')
    rd = code[-12:-7]
    registers[rd] = registers["PC"] + imm
    return registers


#================================================================================================
#I-Type Instructions

def I_Type(code, registers):
    iType = ["000","010","011","Addi(code, registers)","Jalr(code, registers)","Lw(code, registers)","Sltiu(code, registers)"]
    s = iType.index(code[-15:-12])
    iterate = 4
    if code[-7:] == "0010011":
        iterate = 3
    return eval(iType[s+iterate])

def Addi(code, registers):
    imm = SignedToDecimal(code[-32:-20])
    rd = code[-12:-7]
    rs1 = code[-20:-15]
    registers[rd] = registers[rs1] + imm
    return registers

def Jalr(code, registers):   #rs1 could be x6
    imm = SignedToDecimal(code[-32:-20])
    rd = code[-12:-7]
    rs1 = code[-20:-15]
    registers[rd] = registers["PC"] + 1
    registers["PC"] = registers[rs1] + imm
    return registers

def lw(code, registers, memory):
    imm = SignedToDecimal(code[-32:-20])
    rd = code[-12:-7]
    rs1 = code[-20:-15]
    offset = registers[rs1] + imm
    registers[rd] = memory[offset]
    return registers

def Sltiu(code, registers):
    rd = code[-12:-7]
    rs1 = UnsignedToDecimal(DecimalTo2sComplement32bit(registers[code[-20:-15]]))
    imm = UnsignedToDecimal(code[-32:-20])
    if rs1 < imm:
        registers[rd] = 1
    return registers

#================================================================================================
#S-Type Instructions

def S_Type(code, registers, memory):
    sInst = ["Sw(code, registers, memory)"]
    return eval(sInst[0])

def sw(code, registers, memory):
    imm = SignedToDecimal(code[-32:-25] + code[-12:-7])
    rs1 = code[-20:-15]
    rs2 = code[-25:-20]
    offset = registers[rs1] + imm
    memory[offset] = registers[rs2]
    return memory

#================================================================================================