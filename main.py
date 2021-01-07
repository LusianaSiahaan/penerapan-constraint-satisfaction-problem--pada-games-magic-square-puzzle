# Function utama aplikasi

import subprocess

while True:
    try:
        choice = int(input("Please enter your choice: "))
    except ValueError:
        print("Insert another value!")
        continue
    else:
        break
if choice == 3: 
    subprocess.call(['python', 'grid_3x3.py'])
elif choice == 4: 
    subprocess.call(['python', 'grid_4x4.py'])
elif choice == 5: 
    subprocess.call(['python', 'grid_5x5.py'])
else:
    print("Grid tidak ditemukan!")