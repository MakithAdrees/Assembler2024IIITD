def LabelToImm(labels, a, label):
    lst = labels[label]
    minn = lst[0]
    for i in lst:
        if abs(i-a) < abs(minn-a):
            minn = i
    return minn
