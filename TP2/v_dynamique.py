# Q4

dico = dict()
currentConfig=(0,0,0,0)

def acceleration(m,n,i,j):
    if((m,n,i,j) in dico):
        res = dico[m,n,i,j]
    elif ((m,n,i,n-j-1) in dico):
        res = dico[m,n,i,n-j-1]
    elif ((m,n,m-i-1,j) in dico):
        res = dico[m,n,m-i-1,j]
    elif ((m,n,m-i-1,n-j-1) in dico):
        res = dico[m,n,m-i-1,n-j-1]
    elif ((n,m,j,i) in dico):
        res = dico[n,m,j,i]
    elif ((n,m,n-j-1,i) in dico):
        res = dico[n,m,n-j-1,i]
    elif ((n,m,j,m-i-1) in dico):
        res = dico[n,m,j,m-i-1]
    elif ((n,m,n-j-1,m-i-1) in dico):
        res = dico[n,m,n-j-1,m-i-1]
    else:
        res = v_dynamique(m,n,i,j)
##        resTuple = v_dynamique(m,n,i,j)
##        if(resTuple):
##            res = dico[resTuple[0],resTuple[1],resTuple[2],resTuple[3]]
##        else:
##            res = 0

    return res
        

def v_dynamique(m,n,i,j):
    global dico
##    global currentConfig
##    print('currentConfig ' , currentConfig)
    
    lplus = []
    lmoins = []
    if(m==1 and n==1):
        return 0
##        return ()
    #On coupe verticalement
    for k in range(1,m):
        if (k <= i):
            res = acceleration(m-k,n,i-k,j)
            if res > 0 :
                lplus.append(res)
            else:
                lmoins.append(res)
        else:
            res = acceleration(k,n,i,j)
            if res > 0 :    
                lplus.append(res)
            else:
                lmoins.append(res)
    #On coupe horizontalement
    for k in range(1,n):
        if(k<=j):
            res = acceleration(m,n-k,i,j-k)
            if res > 0 :    
                lplus.append(res)
            else:
                lmoins.append(res)
        else:
            res = acceleration(m,k,i,j)
            if res > 0 :    
                lplus.append(res)
            else:
                lmoins.append(res)
    if (len(lmoins) > 0):
        dico[m,n,i,j] = -(max(lmoins) - 1)
##        currentConfig=(m,n,i,j)
        # Il faut pouvoir retourner la configuration
        return dico[m,n,i,j]
##        return (m,n,i,j)
    else :
        dico[m,n,i,j] = -(max(lplus) + 1) 
##        currentConfig=(m,n,i,j)
        # Il faut pouvoir retourner la configuration
        return dico[m,n,i,j] 
##        dico[m,n,i,j] = -(max(lplus) + 1)
##        return (m,n,i,j)

print(v_dynamique(2,3,1,0))


def getvalue(val):
    l = []
    for cle in dico:
        if dico[cle] == val:
          l.append(cle)  
    return l
