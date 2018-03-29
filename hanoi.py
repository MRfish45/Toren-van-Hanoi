NR_OF_DISCS = 8

stokje = [[],[],[],[]]

i = 1
while i <= NR_OF_DISCS:
    stokje[1].append(i)
    stokje[2].append(0)
    stokje[3].append(0)
    i = i + 1
    
##        
##stokje[1] = [1,2,3,4,5,6,7,8]
##stokje[2] = [0,0,0,0,0,0,0,0]
##stokje[3] = [0,0,0,0,0,0,0,0]

def getSchijf (s):
    if s == 0:
        schijf = '|'
    else:
        schijf = '_' * (s+s-1)

    return schijf


def draw():
    i = 0
    while i < NR_OF_DISCS:
        schijf1 = getSchijf(stokje[1][i])
        schijf2 = getSchijf(stokje[2][i])
        schijf3 = getSchijf(stokje[3][i])
        print("{0:^16} {1:^16} {2:^16}".format(schijf1, schijf2, schijf3))
        i = i + 1

def isLegalInput(van, naar):
    if van in ('1','2','3') and naar in ('1','2','3'):
        return True
    return False

def isLegalFromMove(v):
    for schijf in stokje[v]:
        if schijf > 0:
            return True
    return False        

def getFromSchijf(f):
    for schijf in stokje[f]:
        if schijf > 0:
            return schijf
    return 0

def isLegalToMove(f,t):
    for schijf in stokje[t]:
        if schijf > 0:
            if schijf > getFromSchijf(f):
                return True
            return False
    return True


error = ""
while True:
    draw()
    if (error != ""):
        print(error)
    van = input("VAN: ")
    naar = input("NAAR: ")
    if not isLegalInput(van, naar):
        error = "Illegal input!"

    else:
        v=int(van)
        n=int(naar)
        if not isLegalFromMove(v):
            error = "Geen schijf gevonden!"
        elif not isLegalToMove (v,n):
            error = "Illegal move!"
        else:
            
            from_schijf = -1
            i = 0
            while from_schijf == -1 and i < NR_OF_DISCS:
                if stokje[v][i] != 0:
                    from_schijf = i
                i = i + 1

            to_schijf = -1
            i = NR_OF_DISCS - 1
            while to_schijf == -1 and i >= 0:
                if stokje[n][i] == 0:
                    to_schijf = i
                i = i -1
            stokje[n][to_schijf] = stokje[v][from_schijf]
            stokje[v][from_schijf] = 0

            error = ""
            

