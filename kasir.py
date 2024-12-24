# perulangan kode
while True :
    
    # cek input variable
    try :

        # deklarasi input dan variable
        jml = float(input("\nmasukkan jumlah belanja : "))
        mem = input("apakah anda punya member? (Y/N) : ")
        disk = 0
        
        # pengecekan member
        if mem == "y" :
            diskmem = 5
        elif mem == "n":
            diskmem = 0
        else :
            print("invalid")

        # perkondisian jumlah belanja
        if jml > 200000 :
            disk = 10
        elif jml > 100000 :
            disk = 5
        elif jml <= 100000 :
            disk = 0
        else :
            print("invalid")

        # perhitungan diskon tan total belanja
        disk = disk + diskmem
        ttldisk = jml * (disk/100)
        ttl = jml - ttldisk

        # print buat total diskon dan belanja
        print("\nDiskon yang di dapat : ", disk, "%")
        print("Total yang harus dibayar : ", ttl)

        # deklarasi input dan variable nominal dan kembalian
        nom = float(input("Masukkan nominal pembayaran : "))
        kem = nom - ttl

        # perkondisian kembalian
        if kem >= 0 :
            print("\nKembalian : ", kem)
        elif kem < 0 :
            print("uang anda kurang:(")
        else :
            print("invalid")

    #disini dia pesan value errornya        
    except ValueError:
          print("Invalid input. masukkan input berupa angka.\n")
