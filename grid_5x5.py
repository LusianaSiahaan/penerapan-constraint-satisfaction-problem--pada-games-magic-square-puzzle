#grid 5 * 5

print("Susunan Kotak ")
print("[(1,1) ; (1,2) ; (1,3); (1,4) ; (1,5)]")
print("[(2,1) ; (2,2) ; (2,3); (2,4) ; (2,5)]")
print("[(3,1) ; (3,2) ; (3,3); (3,4) ; (3,5)]")
print("[(4,1) ; (4,2) ; (4,3); (4,4) ; (4,5)]")
print("[(5,1) ; (5,2) ; (5,3); (5,4) ; (5,5)]")


satusatu = input("Masukkan Angka Kotak 1,1 = ")
print(type(satusatu))
a = int(satusatu)
satudua = input("Masukkan Angka Kotak 1,2 = ")
print(type(satudua))
b = int(satudua)
satutiga = input("Masukkan Angka Kotak 1,3 = ")
print(type(satutiga))
c = int(satutiga)
satuempat = input("Masukkan Angka Kotak 1,4 = ")
print(type(satuempat))
d = int(satuempat)
satulima = input("Masukkan Angka Kotak 1,5 = ")
print(type(satulima))
e = int(satulima)

duasatu = input("Masukkan Angka Kotak 2,1 = ")
print(type(duasatu))
f = int(duasatu)
duadua = input("Masukkan Angka Kotak 2,2 = ")
print(type(duadua))
g = int(duadua)
duatiga = input("Masukkan Angka Kotak 2,3 = ")
print(type(duatiga))
h = int(duatiga)
duaempat = input("Masukkan Angka Kotak 2,4 = ")
print(type(duaempat))
i = int(duaempat)
dualima = input("Masukkan Angka Kotak 2,5 = ")
print(type(dualima))
j = int(dualima)

tigasatu = input("Masukkan Angka Kotak 3,1 = ")
print(type(tigasatu))
k = int(tigasatu)
tigadua = input("Masukkan Angka Kotak 3,2 = ")
print(type(tigadua))
l = int(tigadua)
tigatiga = input("Masukkan Angka Kotak 3,3 = ")
print(type(tigatiga))
m = int(tigatiga)
tigaempat = input("Masukkan Angka Kotak 3,4 = ")
print(type(tigaempat))
n = int(tigaempat)
tigalima = input("Masukkan Angka Kotak 3,5 = ")
print(type(tigalima))
o = int(tigalima)

empatsatu = input("Masukkan Angka Kotak 4,1 = ")
print(type(empatsatu))
p = int(empatsatu)
empatdua = input("Masukkan Angka Kotak 4,2 = ")
print(type(empatdua))
q = int(empatdua)
empattiga = input("Masukkan Angka Kotak 4,3 = ")
print(type(empattiga))
r = int(empattiga)
empatempat = input("Masukkan Angka Kotak 4,4 = ")
print(type(empatempat))
s = int(empatempat)
empatlima = input("Masukkan Angka Kotak 4,5 = ")
print(type(empatlima))
t = int(empatlima)

limasatu = input("Masukkan Angka Kotak 5,1 = ")
print(type(limasatu))
u = int(limasatu)
limadua = input("Masukkan Angka Kotak 5,2 = ")
print(type(limadua))
v = int(limadua)
limatiga = input("Masukkan Angka Kotak 5,3 = ")
print(type(limatiga))
w = int(limatiga)
limaempat = input("Masukkan Angka Kotak 5,4 = ")
print(type(limaempat))
x = int(limaempat)
limalima = input("Masukkan Angka Kotak 5,5 = ")
print(type(limalima))
y = int(limalima)

total = input("Masukkan Total yang diinginkan : ")
print(type(total))
totalnilai = int(total)

kotakmsp = []
kotakmsp.append([a,b,c,d,e])
kotakmsp.append([f,g,h,i,j])
kotakmsp.append([k,l,m,n,o])
kotakmsp.append([p,q,r,s,t])
kotakmsp.append([u,v,w,x,y])

def checkingMSP(kotakmsp):
    global totalnilai
    for row in range(0,5):
        for col in range(0,5):
            if kotakmsp[row][col]==0:
                return False
    for row in range(0,5):
        if (kotakmsp[row][0]+kotakmsp[row][1]+kotakmsp[row][2]+kotakmsp[row][3]+kotakmsp[row][4])!=totalnilai:
            return False
    for col in range(0,4):
        if (kotakmsp[0][col]+kotakmsp[1][col]+kotakmsp[2][col]+kotakmsp[3][col]+kotakmsp[4][col])!=totalnilai:
            return False
    if (kotakmsp[0][0]+kotakmsp[1][1]+kotakmsp[2][2]+kotakmsp[3][3]+kotakmsp[4][4])!=totalnilai:
        return False
    if (kotakmsp[0][4]+kotakmsp[1][3]+kotakmsp[2][2]+kotakmsp[3][1]+kotakmsp[4][0])!=totalnilai:
        return False
    return True


def penyelesaiantkt(kotakmsp):
    for i in range(0,25):
        row=i//5
        col=i%5
        if kotakmsp[row][col]==0:
            print("Nilai pada kotak-kotak sedang diperiksa")
            for value in range (1,26):
                if not(value in kotakmsp[0] or value in kotakmsp[1] or value in kotakmsp[2] or value in kotakmsp[3]or value in kotakmsp[4]):
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
    print ("[ {} ]    [ {} ]    [ {} ]  [ {} ]    [ {} ]".format(kotakmsp[0][0], kotakmsp[0][1], kotakmsp[0][2], kotakmsp[0][3], kotakmsp[0][4]))
    print ("[ {} ]    [ {} ]    [ {} ]  [ {} ]    [ {} ]".format(kotakmsp[1][0], kotakmsp[1][1], kotakmsp[1][2], kotakmsp[1][3], kotakmsp[1][4]))
    print ("[ {} ]    [ {} ]    [ {} ]  [ {} ]    [ {} ]".format(kotakmsp[2][0], kotakmsp[2][1], kotakmsp[2][2], kotakmsp[2][3], kotakmsp[2][4]))
    print ("[ {} ]    [ {} ]    [ {} ]  [ {} ]    [ {} ]".format(kotakmsp[3][0], kotakmsp[3][1], kotakmsp[3][2], kotakmsp[3][3], kotakmsp[3][4]))
    print ("[ {} ]    [ {} ]    [ {} ]  [ {} ]    [ {} ]".format(kotakmsp[4][0], kotakmsp[4][1], kotakmsp[4][2], kotakmsp[4][3], kotakmsp[4][4]))
else:
    print("TTidak dapat diselesaikan!")




