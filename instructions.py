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


# def Sub2Complement(rd, rs, register):
#     try:
#         return '0100000'+register['zero']+register[rs]+'000'+register[rd]+'0110011'
#     except:
#         return 'RegisterNotFound'

def Add(rd, rs1, rs2, register):
    try:
        return '0000000'+register[rs2]+register[rs1]+'000'+register[rd]+'0110011'
    except:
        return 'SyntaxError'

def Sub(rd, rs1, rs2, register):
    try:
        return('0100000'+register[rs2]+register[rs1]+'000'+register[rd]+'0110011')
    except:
        return('SyntaxError')

def Slt(rd, rs1, rs2, register):
    try:
        return ('0000000' + register[rs2] + register[rs1] + '010' + register[rd] + '0110011')
    except:
        if rd or rs1 or rs2 not in register:
            return ('RegisterNotFound')
        return ('Error, Somewhere')

def Sltu(rd, rs1, rs2, register):
    try:
        return '0000000'+register[rs2]+register[rs1]+'011'+register[rd]+'0110011'
    except:
         return 'SyntaxError'

def Xor(rd, rs1, rs2, register):
    try:
        return('0000000'+register[rs2]+register[rs1]+'100'+register[rd]+'0110011')
    except:
        return('SyntaxError')

def Sll(rd, rs1, rs2, register):
    try:
        return '0000000'+register[rs2]+register[rs1]+'001'+register[rd]+'0110011'
    except:
        return 'RegisterNotFound'
    
def Srl(rd, rs1, rs2, register):
    try:
        return ('0000000' + register[rs2] + register[rs1] + '101' + register[rd] + '0110011')
    except:
        if rd or rs1 or rs2 not in register:
            return ('RegisterNotFound')
        return ('Error, Somewhere')

def Or(rd, rs1, rs2, register):
    try:
        return '0000000'+register[rs2]+register[rs1]+'110'+register[rd]+'0110011'
    except:
        return 'SyntaxError'

def And(rd, rs1, rs2, register):
    try:
        return('0000000'+register[rs2]+register[rs1]+'111'+register[rd]+'0110011')
    except:
        return('SyntaxError')

def Lw(rd, rs1, imm, register):
    if imm >= 2**11 or imm < -2**11:
        return 'NoBitsToStoreImmediate'
    try:
        return ImmToBin(imm)[-12:]+register[rs1]+'010'+register[rd]+'0000011'
    except:
        return 'RegisterNotFound'

def Addi(rd, rs1, imm, register):
    if imm >= 2**11 or imm < -2**11:
        return ('NoBitsToStoreImmediate')
    try:
        return (ImmToBin(imm)[-12:] + register[rs1] + '000' + register[rd] + '0010011')  #using only the last 12 LSBs
    except:
        if rd or rs1 not in register:
            return ('RegisterNotFound')
        return ('Error, Somewhere')

def Sltiu(rd, rs, imm, register):
    if imm >= 2**11 or imm < -2**11:
        return 'ImmediateOutOfRange'
    try:
        return ImmToBin(imm)[-12:]+register[rs]+'011'+register[rd]+'0010011'
    except:
        return 'SyntaxError'

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

def Sw(rs2, rs1, imm, register):
    if imm >= 2**11 or imm < -2**11:
        return 'NoBitsToStoreImmediate'
    try:
        return ImmToBin(imm)[-12:-5]+register[rs2]+register[rs1]+'010'+ImmToBin(imm)[-5:]+'0100011'
    except:
        return 'SyntaxError'


def Beq(rs1, rs2, imm, register):
    if imm >= 2**11 or imm < -2**11:
        return 'NoBitsToStoreImmediate'
    try:
        return ImmToBin(imm)[-12:-10]+register[rs2]+register[rs1]+'000'+ImmToBin(imm)[-5:]+ImmToBin(imm)[-1]+'1100011'
    except:
        return 'SyntaxError'

def Bne(rs1, rs2, imm, register):
    if imm >= 2**12 or imm < -2**12:
        return 'ImmediateOutOfRange'
    try:
        s = ImmToBin(imm)
        return s[-13]+s[-11:-5]+register[rs2]+register[rs1]+'001'+s[-5:-1]+s[-12]+'1100011'
    except:
        return 'SyntaxError'

def Bge(rs1, rs2, imm, register):
    if imm >= 2**11 or imm < -2**11:
        return 'NoBitsToStoreImmediate'
    try:
        return ImmToBin(imm)[-12:-10]+register[rs2]+register[rs1]+'101'+ImmToBin(imm)[-5:]+ImmToBin(imm)[-1]+'1100011'
    except:
        return 'SyntaxError'

def Bgeu(rs1, rs2, imm, register):
    if imm >= 2**11 or imm < -2**11:
        return ('NoBitsToStoreImmediate')
    try:
        return (ImmToBin(imm)[-13] + ImmToBin(imm)[-11:-5] + register[rs2] + register[rs1] + '111' + ImmToBin(imm)[-4:0] + ImmToBin(imm)[-11] + '1100011')
    except:
        if rs1 or rs2 not in register:
            return ('RegisterNotFound')
        return ('Error, Somewhere')

def Blt(rs1, rs2, imm, register):
    if imm >= 2**31 or imm < -2**31:
        return 'NoBitsToStoreImmediate'
    try:
        return(ImmtoBin(imm)[-13]+ImmtoBin(imm)[-11:-5]+register[rs2]+register[rs1]+'100'+ImmtoBin(imm)[-5:-1]+ImmtoBin(imm)[-12]+'1100011')
    except:
        return('SyntaxError')

def Bltu(rs1, rs2, imm, register):
    if imm >= 2**12 or imm < -2**12:
        return 'ImmediateOutOfRange'
    try:
        s = ImmToBin(imm)
        return s[-13]+s[-11:-5]+register[rs2]+register[rs1]+'110'+s[-5:-1]+s[-12]+'1100011'
    except:
        return 'SyntaxError'

def Auipc(rd, imm, register):
    if imm >= 2**19 or imm < -2**19:
        return ('NoBitsToStoreImmediate')
    try:
        return (ImmToBin(imm)[-32:-12] + register[rd] + '0010111')
    except:
        if rd not in register:
            return ('RegisterNotFound')
        return ('Error, Somewhere')

def Lui(rd, imm, register):
    if imm >= 2**31 or imm < -2**31:
        return 'NoBitsToStoreImmediate'
    try:
        return(ImmtoBin(imm)[-32:-12]+register[rd]+'0110111')
    except:
        return('SyntaxError')

def Jal(rd, imm, register):
    if imm >= 2**11 or imm < -2**11:
        return ('NoBitsToStoreImmediate')
    try:
        return (ImmToBin(imm)[-21]+ImmToBin(imm)[-11:-1]+ImmToBin(imm)[-12]+ImmToBin(imm)[-20:-12])
    except:
        if rd not in register:
            return ('RegisterNotFound')
        return ('Error, Somewhere')


def Instruction_Check(register, inst, rs1, rs2, rd=None):
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
    elif inst =="sw":
        return Sw(rs1,rs2,imm,register)
    elif inst =="beq":
        return Beq(rs1,rs2,imm,register)
    elif inst =="bne":
        return Bne(rs1,rs2,imm,register)
    elif inst =="blt":
        return Blt(rs1,rs2,imm,register)
    elif inst =="bge":
        return Bge(rs1,rs2,imm,register)
    elif inst =="bltu":
        return Bltu(rs1,rs2,imm,register)
    elif inst =="bgeu":
        return Bgeu(rs1,rs2,imm,register)
    elif inst =="lui":
        return Lui(rd,imm,register)
    elif inst =="auipc":
        return Auipc(rd,imm,register)
    elif inst =="jal":
        return Jal(rd,imm,register)
    return('IncorrectInstruction')
