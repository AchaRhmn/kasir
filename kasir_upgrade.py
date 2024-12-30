#pendefinisian functions
def produk():
    dafpro = {
        "1": {"nama": "Pensil", "harga": 2000},
        "2": {"nama": "Buku", "harga": 5000},
        "3": {"nama": "Samsung Galaxy Z Fold6 RAM 12GB ROM 1TB", "harga": 27400000},
        "4": {"nama": "Modul lengkap berbahasa binatang", "harga": 110000}
    }
    return dafpro

# fungsi perkondisian member
def member(mem):
    
    if mem == "y":
        return 5  
    elif mem == "n":
        return 0  
    else:
        print("Input tidak valid!")
        return None  

# fungsi pengkondisian diskon
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

# fungsi proses pembayaran
def proses_pembayaran(jml, diskon, member):
    disk = diskon + member
    ttldisk = jml * (disk/100)
    ttl = jml - ttldisk
    
    return ttl, disk

jml = 0
total_barang = []

# perulangan kode
while True :
    
    # cek input variable
    try :

        dafpro = produk()
        
        # perulangan buat nampilin produk
        print("\nlist produk :")
        for k, v in dafpro.items():
            print(f"{k}. {v['nama']} - {v['harga']}")
        
        print("\n==============================================\n")
        print("opsi : 00 - input barang")
        print("       99 - cetak struk")
        print("       111 - keluar")
        pilih = int(input("\npilih opsi : "))
        
        if pilih == 00 : #input barang
             
             while True:
                barang = input("\nInput kode produk ('e' - untuk exit): ")
                

                if barang in dafpro:
                    print(f"Produk : {dafpro[barang]['nama']} - {dafpro[barang]['harga']}")
                    qty = int(input("Masukkan jumlah produk : "))

                    if qty <= 0 :
                        print('jumlah produk harus lebih dari 0')
                        continue

                    # jika barang sudah diinput
                    adaproduk = False
                    for i in total_barang :
                        if i['nama'] == dafpro[barang]['nama'] :
                            i['jumlah'] += qty
                            i['subtotal'] = i['harga']*i['jumlah']
                            jml += dafpro[barang]['harga']*qty
                            
                            adaproduk = True
                            print(f"terinput : {i['jumlah']} x {dafpro[barang]['nama']}. Subtotal: {i['subtotal']}\n")   

                                   
                    if not adaproduk :
                        subtotal = dafpro[barang]['harga'] * qty
                        total_barang.append({"nama" :dafpro[barang]['nama'], "harga":dafpro[barang]['harga'], "jumlah" : qty, "subtotal":subtotal})
                        jml += subtotal

                        print(f"terinput : {qty} x {dafpro[barang]['nama']}. Subtotal: {subtotal}\n")

                elif barang.lower() == "e": 
                    break

                else:
                    print("Produk tidak tersedia")
        
        elif pilih == 99:  # Cetak struk
            
            if not total_barang:
                print("\nproduk kosong. Tidak ada yang bisa dicetak.\n")
                continue
            
            print("\n","="*50,"\n")
            print(f"{'Nama':<20}{'Harga':<10}{'Jumlah':<10}{'Subtotal':<10}")
            print("-" * 50)
            print("Struk Belanja:")
            for i in total_barang:
                print(f"- {i['nama']:<20}: {i['harga']:<10} X {i['jumlah']:<10} = {i['subtotal']:10}")

            print(f"\nTotal harga: {jml}")
            
            # perhitungan diskon
            mem = input("\nApakah Anda member? (y/n): ").lower().strip()
            diskmem= member(mem)
            dis = diskon(jml)
            ttl, disk = proses_pembayaran(jml, dis, diskmem)
            
            print(f"Diskon yang didapat: {disk}%")
            print(f"Total yang harus dibayar: {ttl}")

            # deklarasi input dan variable nominal dan kembalian
            nom = float(input("\nMasukkan nominal pembayaran : "))
            kem = nom - ttl

            # perkondisian kembalian
            if kem >= 0 :
                print("\nKembalian : ", kem)
            elif kem < 0 :
                print("uang anda kurang:(")
            else :
                print("invalid")
            print("\n==============================================\n")
        
        elif pilih == 111 :
            print("\nTerimakasih sudah belanja :D\n")       
            break

        else:
            print("Opsi tidak valid.")

    #disini dia pesan value errornya        
    except ValueError:
          print("Invalid input. masukkan input berupa angka.\n")
