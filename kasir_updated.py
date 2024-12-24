def member(mem):
    
    if mem == "y":
        return 5  
    elif mem == "n":
        return 0  
    else:
        print("Input tidak valid!")
        return None  

def diskon(jml):
 
    if jml > 200000 :
        return 10
    elif jml > 100000 :
        return 5
    elif jml <= 100000 :
        return 0
    else :
        print("invalid")
        return None

def proses_pembayaran(jml, diskon, member):
    disk = diskon + member
    ttldisk = jml * (disk/100)
    ttl = jml - ttldisk
    
    return ttl, disk

# perulangan kode
while True :
    
    # cek input variable
    try :
        # deklarasi input dan variable
        jml = float(input("\nmasukkan jumlah belanja : "))
        mem_in = input("Apakah Anda punya member? (Y/N): ").strip().lower()
        diskmem = member(mem_in)

        # cek input member selain y/n
        if diskmem is None:
            continue
        
        dis = diskon(jml)
        ttl, disk = proses_pembayaran(jml, dis, diskmem)
        
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
