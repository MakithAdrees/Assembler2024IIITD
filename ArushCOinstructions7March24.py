#Arush Instructions CO, March 7 2024
def slt(rd, rs1, rs2, register):
    try:
        return ('0000000' + register[rs2] + register[rs1] + '010' + register[rd] + '0110011')
    except:
        if rd or rs1 or rs2 not in register:
            return ('RegisterNotFound')
        return ('Error, Somewhere')

def srl(rd, rs1, rs2, register):
    try:
        return ('0000000' + register[rs2] + register[rs1] + '101' + register[rd] + '0110011')
    except:
        if rd or rs1 or rs2 not in register:
            return ('RegisterNotFound')
        return ('Error, Somewhere')

def addi(rd, rs1, imm, register):
    if imm >= 2**11 or imm < -2**11:
        return ('NoBitsToStoreImmediate')
    try:
        return (ImmToBin(imm)[-12:] + register[rs1] + '000' + register[rd] + '0010011')  #using only the last 12 LSBs
    except:
        if rd or rs1 not in register:
            return ('RegisterNotFound')
        return ('Error, Somewhere')

def bgeu(rs1, rs2, imm, register):
    if imm >= 2**11 or imm < -2**11:
        return ('NoBitsToStoreImmediate')
    try:
        return (ImmToBin(imm)[-13] + ImmToBin(imm)[-11:-5] + register[rs2] + register[rs1] + '111' + ImmToBin(imm)[-4:0] + ImmToBin(imm)[-11] + '1100011')
    except:
        if rs1 or rs2 not in register:
            return ('RegisterNotFound')
        return ('Error, Somewhere')

def auipc(rd, imm, register):
    if imm >= 2**19 or imm < -2**19:
        return ('NoBitsToStoreImmediate')
    try:
        return (ImmToBin(imm)[-32:-12] + register[rd] + '0010111')
    except:
        if rd not in register:
            return ('RegisterNotFound')
        return ('Error, Somewhere')

def jal(rd, imm, register):
    if imm >= 2**11 or imm < -2**11:
        return ('NoBitsToStoreImmediate')
    try:
        return (ImmToBin(imm)[-21]+ImmToBin(imm)[-11:-1]+ImmToBin(imm)[-12]+ImmToBin(imm)[-20:-12])
    except:
        if rd not in register:
            return ('RegisterNotFound')
        return ('Error, Somewhere')

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