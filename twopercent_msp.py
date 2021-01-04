#!/usr/bin/env python
# coding: utf-8

# In[51]:


#PROYEK MAGICSQUARE TWOPERCENT


# In[14]:


#3 X 3
print("Susunan Kotak ")
print("[(1,1) ; (1,2) ; (1,3)]")
print("[(2,1) ; (2,2) ; (2,3)]")
print("[(3,1) ; (3,2) ; (3,3)]")

satusatu = input("Masukkan Angka Kotak 1,1 = ")
print(type(satusatu))
a = int(satusatu)
satudua = input("Masukkan Angka Kotak 1,2 = ")
print(type(satudua))
b = int(satudua)
satutiga = input("Masukkan Angka Kotak 1,3 = ")
print(type(satutiga))
c = int(satutiga)

duasatu = input("Masukkan Angka Kotak 2,1 = ")
print(type(duasatu))
d = int(duasatu)
duadua = input("Masukkan Angka Kotak 2,2 = ")
print(type(duadua))
e = int(duadua)
duatiga = input("Masukkan Angka Kotak 2,3 = ")
print(type(duatiga))
f = int(duatiga)

tigasatu = input("Masukkan Angka Kotak 3,1 = ")
print(type(tigasatu))
g = int(tigasatu)
tigadua = input("Masukkan Angka Kotak 3,2 = ")
print(type(tigadua))
h = int(tigadua)
tigatiga = input("Masukkan Angka Kotak 3,3 = ")
print(type(tigatiga))
i = int(tigatiga)

total = input("Masukkan Total yang diinginkan : ")
print(type(total))
totalnilai = int(total)


# In[34]:


#tkt = tiga kali tiga
kotakmsp_tkt = []
kotakmsp_tkt.append([a,b,c])
kotakmsp_tkt.append([d,e,f])
kotakmsp_tkt.append([g,h,i])


# In[35]:


def checkingMSP(kotakmsp_tkt):
    global totalnilai
    for row in range(0,3):
        for col in range(0,3):
            if kotakmsp_tkt[row][col]==0:
                return False
    for row in range(0,3):
        if (kotakmsp_tkt[row][0]+kotakmsp_tkt[row][1]+kotakmsp_tkt[row][2])!=totalnilai:
            return False
    for col in range(0,3):
        if (kotakmsp_tkt[0][col]+kotakmsp_tkt[1][col]+kotakmsp_tkt[2][col])!=totalnilai:
            return False
    if (kotakmsp_tkt[0][0]+kotakmsp_tkt[1][1]+kotakmsp_tkt[2][2])!=totalnilai:
        return False
    if (kotakmsp_tkt[0][2]+kotakmsp_tkt[1][1]+kotakmsp_tkt[2][0])!=totalnilai:
        return False
    return True


# In[36]:


def penyelesaiantkt(kotakmsp_tkt):
    for i in range(0,9):
        row=i//3
        col=i%3
        if kotakmsp_tkt[row][col]==0:
            print("Nilai pada kotak-kotak sedang diperiksa")
            for value in range (1,10):
                if not(value in kotakmsp_tkt[0] or value in kotakmsp_tkt[1] or value in kotakmsp_tkt[2]):
                    kotakmsp_tkt[row][col]= value
                    if checkingMSP(kotakmsp_tkt):
                        print("Nilai pada kotak-kotak sudah selesai diperiksa.")
                        return True
                    else:
                        if penyelesaiantkt(kotakmsp_tkt):
                            return True
            break
    print(kotakmsp_tkt)
    kotakmsp_tkt[row][col] = 0


# In[37]:


solved = penyelesaiantkt(kotakmsp_tkt)
if solved:
    print("Hasil Penyelesaian:")
    print (" [ {} ]    [ {} ]    [ {} ]".format(kotakmsp_tkt[0][0], kotakmsp_tkt[0][1], kotakmsp_tkt[0][2]))
    print (" [ {} ]    [ {} ]    [ {} ]".format(kotakmsp_tkt[1][0], kotakmsp_tkt[1][1], kotakmsp_tkt[1][2]))
    print (" [ {} ]    [ {} ]    [ {} ]".format(kotakmsp_tkt[2][0], kotakmsp_tkt[2][1], kotakmsp_tkt[2][2]))
else:
    print("Magic Square Puzzle sudah selesai")


# In[ ]:




