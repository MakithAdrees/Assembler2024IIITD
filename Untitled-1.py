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


def Sub2Complement(rd, rs, register):
    try:
        return '0100000'+register['zero']+register[rs]+'000'+register[rd]+'0110011'
    except:
        return 'RegisterNotFound'


def Sll(rd, rs1, rs2, register):
    try:
        return '0000000'+register[rs2]+register[rs1]+'001'+register[rd]+'0110011'
    except:
        return 'RegisterNotFound'
    

def Lw(rd, rs1, imm, register):
    if imm >= 2**11 or imm < -2**11:
        return 'NoBitsToStoreImmediate'
    try:
        return ImmToBin(imm)[-12:]+register[rs1]+'010'+register[rd]+'0000011'
    except:
        return 'RegisterNotFound'
    

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


def Bge(rs1, rs2, imm, register):
    if imm >= 2**11 or imm < -2**11:
        return 'NoBitsToStoreImmediate'
    try:
        return ImmToBin(imm)[-12:-10]+register[rs2]+register[rs1]+'101'+ImmToBin(imm)[-5:]+ImmToBin(imm)[-1]+'1100011'
    except:
        return 'SyntaxError'
    
