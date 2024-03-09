lines = [['add','rd,rs1,rs2'],]  #stores all lines from the input file

def label(lines):
    labels = {}
    for a in range(len(lines)):
        if lines[a][0][-1] == ':':
            if lines[a][0][:-1] not in labels:
                labels[lines[a][0][:-1]] = [a+1]
            else:
                labels[lines[a][0][:-1]] += [a+1]
    return labels


def main(lines):
    labels = label(lines)
    
    for a in range(len(lines)):
        if lines[a][0][-1] != ':':
            instruction = lines[a][0]
            reg = lines[a][1].split(',')
            if len(reg) == 3:
                ff(instruction, reg[0],reg[1],reg[2])
            

main(lines)