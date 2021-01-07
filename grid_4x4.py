#Grid 4x4
#Kelompok_twopercent
print("Susunan Kotak ")
print("[(1,1) ; (1,2) ; (1,3) ; (1,4)]")
print("[(2,1) ; (2,2) ; (2,3) ; (2,4)]")
print("[(3,1) ; (3,2) ; (3,3) ; (3,4)]")
print("[(4,1) ; (4,2) ; (4,3) ; (4,4)]")

satuA = input("Masukkan Angka Kotak 1,1 = ")
print(type(satuA))
a = int(satuA)
satuB = input("Masukkan Angka Kotak 1,2 = ")
print(type(satuB))
b = int(satuB)
atuC = input("Masukkan Angka Kotak 1,3 = ")
print(type(satuC))
c = int(satuC)
satuD = input("Masukkan Angka Kotak 1,4 = ")
print(type(satuD))
d = int(satuD)

duaA = input("Masukkan Angka Kotak 2,1 = ")
print(type(duaA))
e = int(duaA)
duaB = input("Masukkan Angka Kotak 2,2 = ")
print(type(duaB))
f = int(duaB)
duaC = input("Masukkan Angka Kotak 2,3 = ")
print(type(duaC))
g = int(duaC)
duaD = input("Masukkan Angka Kotak 2,4 = ")
print(type(duaD))
h = int(duaD)

tigaA = input("Masukkan Angka Kotak 3,1 = ")
print(type(tigaA))
i = int(tigaA)
tigaB = input("Masukkan Angka Kotak 3,2 = ")
print(type(tigaB))
j = int(tigaB)
tigaC = input("Masukkan Angka Kotak 3,3 = ")
print(type(tigaC))
k = int(tigaC)
tigaD = input("Masukkan Angka Kotak 3,4 = ")
print(type(tigaD))
l = int(tigaD)

empatA = input("Masukkan Angka Kotak 4,1 = ")
print(type(empatA))
m = int(empatA)
empatB = input("Masukkan Angka Kotak 4,2 = ")
print(type(empatB))
n = int(empatB)
empatC = input("Masukkan Angka Kotak 4,3 = ")
print(type(empatC))
o = int(empatC)
empatD = input("Masukkan Angka Kotak 4,4 = ")
print(type(empatD))
p = int(empatD)
total = input("Masukkan Total yang diinginkan : ")
print(type(total))
totalnilai = int(total)

kotakmsp = []
kotakmsp.append([a,b,c,d])
kotakmsp.append([e,f,g,h])
kotakmsp.append([i,j,k,l])
kotakmsp.append([m,n,o,p])


def checkingMSP(kotakmsp):
    global totalnilai
    for row in range(0,4):
        for col in range(0,4):
            if kotakmsp[row][col]==0:
                return False
    for row in range(0,4):
        if (kotakmsp[row][0]+kotakmsp[row][1]+kotakmsp[row][2]+kotakmsp[row][3])!=totalnilai:
            return False
    for col in range(0,4):
        if (kotakmsp[0][col]+kotakmsp[1][col]+kotakmsp[2][col]+kotakmsp[3][col])!=totalnilai:
            return False
    if (kotakmsp[0][0]+kotakmsp[1][1]+kotakmsp[2][2]+kotakmsp[3][3])!=totalnilai:
        return False
    if (kotakmsp[0][3]+kotakmsp[1][2]+kotakmsp[2][1]+kotakmsp[3][0])!=totalnilai:
        return False
    return True


    # In[36]:


def penyelesaiantkt(kotakmsp):
    for i in range(0,16):
        row=i//4
        col=i%4
        if kotakmsp[row][col]==0:
            print("Nilai pada kotak-kotak sedang diperiksa")
            for value in range (1,17):
                if not(value in kotakmsp[0] or value in kotakmsp[1] or value in kotakmsp[2] or value in kotakmsp[3]):
                    kotakmsp[row][col]= value
                    if checkingMSP(kotakmsp):
                        print("Nilai pada kotak-kotak sudah selesai diperiksa.")
                        return True
                    else:
                        if penyelesaiantkt(kotakmsp):
                            return True
            break
    print(kotakmsp)
    kotakmsp[row][col] = 0

    # In[37]:


solved = penyelesaiantkt(kotakmsp)
if solved:
    print("Hasil Penyelesaian:")
    print (" [ {} ]    [ {} ]    [ {} ]    [ {} ]".format(kotakmsp[0][0], kotakmsp[0][1], kotakmsp[0][2], kotakmsp[0][3]))
    print (" [ {} ]    [ {} ]    [ {} ]    [ {} ]".format(kotakmsp[1][0], kotakmsp[1][1], kotakmsp[1][2], kotakmsp[1][3]))
    print (" [ {} ]    [ {} ]    [ {} ]    [ {} ]".format(kotakmsp[2][0], kotakmsp[2][1], kotakmsp[2][2], kotakmsp[2][3]))
    print (" [ {} ]    [ {} ]    [ {} ]    [ {} ]".format(kotakmsp[3][0], kotakmsp[3][1], kotakmsp[3][2], kotakmsp[3][3]))
else:
    print("Magic Square Puzzle sudah selesai")