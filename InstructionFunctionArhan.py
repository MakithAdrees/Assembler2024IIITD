register = {'x0':'00000','x1':'00001','x2':'00010','x3':'00011','x4':'00100','x5':'00101','x6':'00110','x7':'00111','x8':'01000','x9':'01001','x10':'01010','x11':'01011','x12':'01100','x13':'01101','x14':'01110','x15':'01111','x16':'10000','x17':'10001','x18':'10010','x19':'10011','x20':'10100','x21':'10101','x22':'10110','x23':'10111','x24':'11000','x25':'11001','x26':'11010','x27':'11011','x28':'11100','x29':'11101','x30':'11110','x31':'11111'}

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
    try:
        return ImmToBin(imm)+register[rs]+'011'+register[rd]+'0010011'
    except:
        return 'SyntaxError'

def Bne(rs1, rs2, imm, register):
    try:
        return ImmToBin(imm)+register[rs2]+register[rs1]+'001'+ImmToBin(imm)+'1100011'
    except:
        return 'SyntaxError'
    
def Bltu(rs1, rs2, imm, register):
    try:
        return ImmToBin(imm)+register[rs2]+register[rs1]+'111'+ImmToBin(imm)+'1100011'
    except:
        return 'SyntaxError'
    
