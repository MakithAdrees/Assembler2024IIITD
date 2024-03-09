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


def Add(rd, rs1, rs2, register):
    try:
        return '0000000'+register[rs2]+register[rs1]+'000'+register[rd]+'0110011'
    except:
        return 'SyntaxError'
    
def Stlu(rd, rs1, rs2, register):
    try:
        return '0000000'+register[rs2]+register[rs1]+'011'+register[rd]+'0110011'
    except:
         return 'SyntaxError'
     
def Or(rd, rs1, rs2, register):
    try:
        return '0000000'+register[rs2]+register[rs1]+'110'+register[rd]+'0110011'
    except:
        return 'SyntaxError'

def Sltiu(rd, rs, imm, register):
    if imm >= 2**11 or imm < -2**11:
        return 'ImmediateOutOfRange'
    try:
        return ImmToBin(imm)[-12:]+register[rs]+'011'+register[rd]+'0010011'
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
    
def Bltu(rs1, rs2, imm, register):
    if imm >= 2**12 or imm < -2**12:
        return 'ImmediateOutOfRange'
    try:
        s = ImmToBin(imm)
        return s[-13]+s[-11:-5]+register[rs2]+register[rs1]+'110'+s[-5:-1]+s[-12]+'1100011'
    except:
        return 'SyntaxError'
    
