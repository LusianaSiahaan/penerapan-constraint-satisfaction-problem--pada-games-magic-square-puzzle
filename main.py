# Function utama aplikasi

print("Kotak 3x3 = 3")
print("Kotak 4x4 = 4")
print("Kotak 5x5 = 5")
grid = input("Masukkan jumlah kotak yang diinginkan= ")
print(type(grid))
jlh_kotak = int(grid)

if n == 3:
    import grid_3x3
if n == 4:
    import grid_4x4
if n == 5:
    import grid_5x5
else:
   print("Grid tidak ditemukan!")