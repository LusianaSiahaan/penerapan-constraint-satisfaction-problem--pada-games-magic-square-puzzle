# Function utama aplikasi

import subprocess

while True:
    try:
        choice = int(input("List of grid available:\n 1: Grid 3x3 \n 2: Grid 4x4 \n 3: Grid 5x5 \nChoose: "))
    except ValueError:
        print("Insert another value!")
        continue
    else:
        break
if choice == 1: 
    subprocess.call(['python', 'grid_3x3.py'])
elif choice == 2: 
    subprocess.call(['python', 'grid_4x4.py'])
elif choice == 3: 
    subprocess.call(['python', 'grid_5x5.py'])
else:
    print("Grid tidak ditemukan!")