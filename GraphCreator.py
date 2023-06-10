# !!
import glob
import os
from mdutils.mdutils import MdUtils
import numpy as np


ALPH=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] #|26|
#ALPH=["α","β","γ","δ","ε","ζ","η","θ","ι","κ","λ","μ","ν","ξ","π","ρ","σ","τ","υ","φ","χ","ψ","ω"]  #|23|


def removeFiles():
    files = glob.glob('./Graph/*')
    for f in files:
        os.remove(f)

def makeVert(id, related):
    mdFile = MdUtils("./Graph/"+str(id)+".md")
    for r in related:
        mdFile.write("[["+str(r)+"]]")
    mdFile.create_md_file()

def MatrixToMD(seq):
    for i in range(seq.__len__()):
        conn = []
        for j in range(seq.__len__()):
            if seq[i][j] == 1:
                conn.append(ALPH[j])
        makeVert (ALPH[i], conn)  


def MakeKValue(val):
    seq = np.zeros((val,val))

    for i in range(val):
        for j in range(val):
            if i!=j:
                seq[i][j]=1
            else:
                seq[i][j]=0
    return seq                

def MakeChain(val):
    seq = np.zeros((val,val))

    for i in range(val):
        for j in range(val):
            if j==(i+1):
                seq[i][j]=1
            if j==(i-1):
                seq[i][j]=1
    return seq   
   
def MakeCicle(val):
    seq = np.zeros((val,val))

    seq[0][val-1]=1
    seq[val-1][0]=1
    for i in range(val):
        for j in range(val):
            if j==(i+1):
                seq[i][j]=1
            if j==(i-1):
                seq[i][j]=1
    return seq  

def MakeBiPart(val):
    seq = np.zeros((val,val))

    for i in range(val):
        for j in range(val):
            if (i+j)%2!=0:
                seq[i][j]=1
    return seq           


m = [
    [0,1,1,0,0,0,0],
    [1,0,1,0,0,0,0],
    [1,1,0,1,0,1,0],
    [0,0,1,0,1,1,1],
    [0,0,0,1,0,1,1],
    [0,0,1,1,1,0,1],
    [0,0,0,1,1,1,0],
    ]

m2 = [
    [0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0],
    [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],


    ]
removeFiles()

#m
#MakeKValue(n)
#MakeCicle(n)
#MakeChain(n)
#MakeBiPart(n)

Matrix = m2


print(Matrix)
MatrixToMD(Matrix)
