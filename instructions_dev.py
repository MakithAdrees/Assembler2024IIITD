def Sub(rd, rs1, rs2, register):
    try:
        return('0100000'+register[rs2]+register[rs1]+'000'+register[rd]+'0110011')
    except:
        return('SyntaxError')
        
def Xor(rd, rs1, rs2, register):
    try:
        return('0000000'+register[rs2]+register[rs1]+'100'+register[rd]+'0110011')
    except:
        return('SyntaxError')
        
def And(rd, rs1, rs2, register):
    try:
        return('0000000'+register[rs2]+register[rs1]+'111'+register[rd]+'0110011')
    except:
        return('SyntaxError')

def Jalr(rd, rs1, imm, register):
    if imm >= 2**31 or imm < -2**31:
        return 'NoBitsToStoreImmediate'
    try:
        if rs1=='x6';
            return(ImmtoBin(imm)[-12:]+register['t1']+'000'+register[rd]+'1100111')
        else:
            return(ImmtoBin(imm)[-12:]+register[rs1]+'000'+register[rd]+'1100111')
    except:
        return('SyntaxError')
        
def Blt(rs1, rs2, imm, register):
    if imm >= 2**31 or imm < -2**31:
        return 'NoBitsToStoreImmediate'
    try:
        return(ImmtoBin(imm)[-13]+ImmtoBin(imm)[-11:-5]+register[rs2]+register[rs1]+'100'+ImmtoBin(imm)[-5:-1]+ImmtoBin(imm)[-12]+'1100011')
    except:
        return('SyntaxError')
        
def Lui(rd, imm, register):
    if imm >= 2**31 or imm < -2**31:
        return 'NoBitsToStoreImmediate'
    try:
        return(ImmtoBin(imm)[-32:-12]+register[rd]+'0110111')
    except:
        return('SyntaxError')


def Instruction_Check(inst, rd, rs1, rs2, register):
    if rs1 or rs2 or rd not in register:
            return('Error, Register Index out of range')
    elif inst=="add":
        return Add(rd, rs1, rs2, register)
    elif inst=="sub":
        if rs1=="x0":
            return Sub(rd, 'zero', rs2, register)
        else:
            return Sub(rd, rs1, rs2, register)
    elif inst=="slt":
        return Slt(rd, rs1, rs2, register)
    elif inst=="sltu":
        return Sltu(rd, rs1, rs2, register)
    elif inst=="xor":
        return Xor(rd, rs1, rs2, register)
    elif inst=="sll":
        return Sll(rd, rs1, rs2, register)
    elif inst=="srl":
        return Srl(rd, rs1, rs2, register)
    elif inst=="or":
        return Or(rd, rs1, rs2, register)
    elif inst=="and":
        return And(rd, rs1, rs2, register)
    elif inst=="lw":
        return Lw(rd, rs1, rs2, register)
    elif inst=="addi":
        return Addi(rd, rs1, rs2, register)
    elif inst=="sltiu":
        return Sltiu(rd, rs1, rs2, register)
    elif inst=="jalr":
        return Jalr(rd, rs1, rs2, register)
    return('IncorrectInstruction')
register = {'zero':'00000','ra':'00001','sp':'00010','gp':'00011','tp':'00100','t0':'00101','t1':'00110','t2':'00111','s0':'01000','fp':'01000','s1':'01001','a0':'01010','a1':'01011','a2':'01100','a3':'01101','a4':'01110','a5':'01111','a6':'10000','a7':'10001','s2':'10010','s3':'10011','s4':'10100','s5':'10101','s6':'10110','s7':'10111','s8':'11000','s9':'11001','s10':'11010','s11':'11011','t3':'11100','t4':'11101','t5':'11110','t6':'11111'}
