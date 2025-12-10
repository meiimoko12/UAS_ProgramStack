from collections import deque

stack = deque()

while True:
    print("\n=== PROGRAM STACK ===")
    print("1. Append")
    print("2. AppendLeft")
    print("3. Pop")
    print("4. PopLeft")
    print("5. Clear")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == '1':
        data = input("Masukkan data: ")
        stack.append(data)
        print("Data ditambahkan:", stack)

    elif pilihan == '2':
        data = input("Masukkan data: ")
        stack.appendleft(data)
        print("Data ditambahkan di depan:", stack)

    elif pilihan == '3':
        if stack:
            print("Data yang di-pop:", stack.pop())
        else:
            print("Stack kosong!")

    elif pilihan == '4':
        if stack:
            print("Data yang di-pop left:", stack.popleft())
        else:
            print("Stack kosong!")

    elif pilihan == '5':
        stack.clear()
        print("Stack telah dibersihkan.")

    elif pilihan == '6':
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")