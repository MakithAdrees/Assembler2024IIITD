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


# all instructions....
    
# R type instructions_______________________________________________________________________________________

def Add(rd, rs1, rs2, register , line_no):
    try:
        return '0000000'+register[rs2]+register[rs1]+'000'+register[rd]+'0110011'
    except:
        if rs1 or rs2 or rd not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)
    
def Sub(rd, rs1, rs2, register , line_no):
    try:
        if rs1=='x0':
            return('0100000'+register[rs2]+register['zero']+'000'+register[rd]+'0110011')
        else:
            return('0100000'+register[rs2]+register[rs1]+'000'+register[rd]+'0110011')
    except:
        if rs1 or rs2 or rd not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

def Slt(rd, rs1, rs2, register , line_no):
    try:
        return ('0000000' + register[rs2] + register[rs1] + '010' + register[rd] + '0110011')
    except:
        if rd or rs1 or rs2 not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

def Sltu(rd, rs1, rs2, register , line_no):
    try:
        return '0000000'+register[rs2]+register[rs1]+'011'+register[rd]+'0110011'
    except:
        if rs1 or rs2 or rd not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

def Xor(rd, rs1, rs2, register , line_no):
    try:
        return('0000000'+register[rs2]+register[rs1]+'100'+register[rd]+'0110011')
    except:
        if rs1 or rs2 or rd not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

def Sll(rd, rs1, rs2, register , line_no):
    try:
        return '0000000'+register[rs2]+register[rs1]+'001'+register[rd]+'0110011'
    except:
        if rs1 or rs2 or rd not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)
    
def Srl(rd, rs1, rs2, register , line_no):
    try:
        return ('0000000' + register[rs2] + register[rs1] + '101' + register[rd] + '0110011')
    except:
        if rd or rs1 or rs2 not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

def Or(rd, rs1, rs2, register , line_no):
    try:
        return '0000000'+register[rs2]+register[rs1]+'110'+register[rd]+'0110011'
    except:
        if rs1 or rs2 or rd not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

def And(rd, rs1, rs2, register , line_no):
    try:
        return('0000000'+register[rs2]+register[rs1]+'111'+register[rd]+'0110011')
    except:
        if rs1 or rs2 or rd not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

# I type instructions______________________________________________________________________________________

def Lw(rd, rs1, imm, register , line_no):
    try:
        if imm >= 2**11 or imm < -2**11:
            return ('ImmediateOutOfRange in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        return ImmToBin(imm)[-12:]+register[rs1]+'010'+register[rd]+'0000011'
    except:
        if rs1 or rd not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

def Addi(rd, rs1, imm, register , line_no):
    try:
        if imm >= 2**11 or imm < -2**11:
            return ('ImmediateOutOfRange in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    
    try:
        return (ImmToBin(imm)[-12:] + register[rs1] + '000' + register[rd] + '0010011')  #using only the last 12 LSBs
    except:
        if rd or rs1 not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

def Sltiu(rd, rs1, imm, register , line_no):
    try:
        if imm >= 2**11 or imm < -2**11:
            return ('ImmediateOutOfRange in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        return ImmToBin(imm)[-12:]+register[rs1]+'011'+register[rd]+'0010011'
    except:
        if rs1 or rd not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

def Jalr(rd, rs1, imm, register , line_no):
    try:
        if imm >= 2**31 or imm < -2**31:
            return ('ImmediateOutOfRange in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        if rs1=='x6':
            return(ImmToBin(imm)[-12:]+register['t1']+'000'+register[rd]+'1100111')
        else:
            return(ImmToBin(imm)[-12:]+register[rs1]+'000'+register[rd]+'1100111')
    except:
        if rs1 or rd not in register:
            return('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

# S type instructions______________________________________________________________________________________

def Sw(rs2, rs1, imm, register , line_no):
    try:
        if imm >= 2**11 or imm < -2**11:
            return ('ImmediateOutOfRange in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        return ImmToBin(imm)[-12:-5]+register[rs2]+register[rs1]+'010'+ImmToBin(imm)[-5:]+'0100011'
    except:
        return 'SyntaxError in line ' + str(line_no)

# B type instructions______________________________________________________________________________________

def Beq(rs1, rs2, imm, register , line_no):
    try:
        if imm >= 2**12 or imm < -2**12:
            return ('ImmediateOutOfRange in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        s = ImmToBin(imm)
        return s[-13]+s[-11:-5]+register[rs2]+register[rs1]+'000'+s[-5:-1]+s[-12]+'1100011'
    except:
        return 'SyntaxError in line ' + str(line_no)

def Bne(rs1, rs2, imm, register , line_no):
    try:
        if imm >= 2**12 or imm < -2**12:
            return ('InvalideImmediate in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        s = ImmToBin(imm)
        return s[-13]+s[-11:-5]+register[rs2]+register[rs1]+'001'+s[-5:-1]+s[-12]+'1100011'
    except:
        return 'SyntaxError in line ' + str(line_no)

def Bge(rs1, rs2, imm, register , line_no):
    try:
        if imm >= 2**12 or imm < -2**12:
            return ('InvalideImmediate in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        s = ImmToBin(imm)
        return s[-13]+s[-11:-5]+register[rs2]+register[rs1]+'101'+s[-5:-1]+s[-12]+'1100011'
    except:
        return 'SyntaxError in line ' + str(line_no)

def Bgeu(rs1, rs2, imm, register , line_no):
    try:
        if imm >= 2**12 or imm < -2**12:
            return ('InvalideImmediate in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        return (ImmToBin(imm)[-13] + ImmToBin(imm)[-11:-5] + register[rs2] + register[rs1] + '111' + ImmToBin(imm)[-4:0] + ImmToBin(imm)[-11] + '1100011')
    except:
        if rs1 or rs2 not in register:
            return ('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

def Blt(rs1, rs2, imm, register , line_no):
    try:
        if imm >= 2**12 or imm < -2**12:
            return ('InvalideImmediate in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        return(ImmToBin(imm)[-13]+ImmToBin(imm)[-11:-5]+register[rs2]+register[rs1]+'100'+ImmToBin(imm)[-5:-1]+ImmToBin(imm)[-12]+'1100011')
    except:
        return 'SyntaxError in line ' + str(line_no)

def Bltu(rs1, rs2, imm, register , line_no):
    try:
        if imm >= 2**12 or imm < -2**12:
            return ('InvalideImmediate in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        s = ImmToBin(imm)
        return s[-13]+s[-11:-5]+register[rs2]+register[rs1]+'110'+s[-5:-1]+s[-12]+'1100011'
    except:
        return 'SyntaxError in line ' + str(line_no)

# U type instructions______________________________________________________________________________________

def Auipc(rd, imm, register , line_no):
    try:
        if imm >= 2**31 or imm < -2**31:
            return ('ImmediateOutOfRange in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        return (ImmToBin(imm)[-32:-12] + register[rd] + '0010111')
    except:
        if rd not in register:
            return ('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

def Lui(rd, imm, register , line_no):
    try:
        if imm >= 2**31 or imm < -2**31:
            return ('ImmediateOutOfRange in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        return(ImmToBin(imm)[-32:-12]+register[rd]+'0110111')
    except:
        return 'SyntaxError in line ' + str(line_no)

# J type instructions______________________________________________________________________________________

def Jal(rd, imm, register , line_no):
    try:
        if imm >= 2**20 or imm < -2**20:
            return ('ImmediateOutOfRange in line ' + str(line_no))
    except:
        return 'Label not found in line ' + str(line_no)
    try:
        return (ImmToBin(imm)[-21]+ImmToBin(imm)[-11:-1]+ImmToBin(imm)[-12]+ImmToBin(imm)[-20:-12]+register[rd]+'1101111')
    except:
        if rd not in register:
            return ('RegisterNotFound in line ' + str(line_no))
        return 'SyntaxError in line ' + str(line_no)

# Function that checks which instruction is called and then calls that function

def Instruction_Check(inst, rd=None, rs1 = None, rs2 = None , line_no = None):
    register = {'zero':'00000','ra':'00001','sp':'00010','gp':'00011','tp':'00100','t0':'00101','t1':'00110','t2':'00111','s0':'01000','fp':'01000','s1':'01001','a0':'01010','a1':'01011','a2':'01100','a3':'01101','a4':'01110','a5':'01111','a6':'10000','a7':'10001','s2':'10010','s3':'10011','s4':'10100','s5':'10101','s6':'10110','s7':'10111','s8':'11000','s9':'11001','s10':'11010','s11':'11011','t3':'11100','t4':'11101','t5':'11110','t6':'11111'}
    # if rs1 or rs2 or rd not in register:
    #         return('Error, Register Index out of range')
    if inst=="add":
        return Add(rd, rs1, rs2, register , line_no)
    elif inst=="sub":
        return Sub(rd, rs1, rs2, register , line_no)
    elif inst=="slt":
        return Slt(rd, rs1, rs2, register , line_no)
    elif inst=="sltu":
        return Sltu(rd, rs1, rs2, register , line_no)
    elif inst=="xor":
        return Xor(rd, rs1, rs2, register , line_no)
    elif inst=="sll":
        return Sll(rd, rs1, rs2, register , line_no)
    elif inst=="srl":
        return Srl(rd, rs1, rs2, register , line_no)
    elif inst=="or":
        return Or(rd, rs1, rs2, register , line_no)
    elif inst=="and":
        return And(rd, rs1, rs2, register , line_no)
    elif inst=="lw":
        return Lw(rd, rs1, rs2, register , line_no)
    elif inst=="addi":
        return Addi(rd, rs1, rs2, register , line_no)
    elif inst=="sltiu":
        return Sltiu(rd, rs1, rs2, register , line_no)
    elif inst=="jalr":
        return Jalr(rd, rs1, rs2, register , line_no)
    elif inst =="sw":
        return Sw(rd,rs1,rs2,register , line_no)
    elif inst =="beq":
        return Beq(rd,rs1,rs2,register , line_no)
    elif inst =="bne":
        return Bne(rd,rs1,rs2,register , line_no)
    elif inst =="blt":
        return Blt(rd,rs1,rs2,register , line_no)
    elif inst =="bge":
        return Bge(rd,rs1,rs2,register ,line_no)
    elif inst =="bltu":
        return Bltu(rd,rs1,rs2,register,line_no)
    elif inst =="bgeu":
        return Bgeu(rd,rs1,rs2,register,line_no)
    elif inst =="lui":
        return Lui(rd,rs1,register,line_no)
    elif inst =="auipc":
        return Auipc(rd,rs1,register,line_no)
    elif inst =="jal":
        return Jal(rd,rs1,register,line_no)
    return('IncorrectInstruction in line ' + str(line_no))
