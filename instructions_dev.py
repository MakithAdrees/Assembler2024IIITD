def Sub(rd, rs1, rs2):
    try:
        return('0100000'+register[rs2]+register[rs1]+'000'+register[rd]+'0110011')
    except:
        print('SyntaxError')
        if rs1 or rs2 or rd not in Sub:
            return('Error, Register out of range')
        return('error, somewhere')
def Xor(rd, rs1, rs2):
    try:
        return('0000000'+register[rs2]+register[rs1]+'100'+register[rd]+'0110011')
    except:
        return('SyntaxError')
def And(rd, rs1, rs2):
    try:
        return('0000000'+register[rs2]+register[rs1]+'111'+register[rd]+'0110011')
    except:
        return('SyntaxError')
def Jalr(ImmtoBin, rd, rs2):
    try:
        return(ImmtoBin+register[rs2]+'000'+register[rd]+'1100111')
    except:
        return('SyntaxError')
def Blt(ImmtoBin, rs1, rs2):
    try:
        return(ImmtoBin+register[rs2]+register[rs1]+'100'+ImmtoBin+'1100011')
    except:
        return('SyntaxError')
def Lui(ImmtoBin, rd):
    try:
        return(ImmtoBin+register[rd]+'0110111')
    except:
        return('SyntaxError')
register = {'zero':'00000','ra':'00001','sp':'00010','gp':'00011','tp':'00100','t0':'00101','t1':'00110','t2':'00111','s0':'01000','fp':'01000','s1':'01001','a0':'01010','a1':'01011','a2':'01100','a3':'01101','a4':'01110','a5':'01111','a6':'10000','a7':'10001','s2':'10010','s3':'10011','s4':'10100','s5':'10101','s6':'10110','s7':'10111','s8':'11000','s9':'11001','s10':'11010','s11':'11011','t3':'11100','t4':'11101','t5':'11110','t6':'11111'}