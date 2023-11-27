# 1. Buatkan list dengan nilai [kodeKendaraan, namaKendaraan, ccKendaraan, warnaKendaraan]
myList = [1, 'Rx King', 150, 'Hitam']
# 2. Dari list pada nomor 1 silakan ditambahkan : 
#    di akhir tambahkan [hargaKendaraan, jumlahRoda]
#    sisipkan setelah nama kendaraan [merkKendaraan, jenisKendaraan]
print('pada list myList terdapat data :', myList)
myList.append('Rp15.000.000')
myList.append(2)
myList.insert(2, 'Yamaha')
myList.insert(3, 'Motor')
print('setelah dilakukan function append dan insert pada list myList, data yang terdapat pada myList menjadi :', myList)

# 3. Buatlah program python menggunakan operator match dan case untuk menghitung luas bangun datar:
#    pilihan 1 menghitung luas Persegi
#    pilihan 2 menghitung luas lingkaran
#    pilihan 3 menghitung luas segitiga
#    selain itu beri keterangan salah memasukkan pilihan

luas = input('Masukkan pilihan bangun datar yang ingin dihitung luasnya (1. Persegi, 2. Lingkaran, 3. Segitiga): ')
match luas:
    case '1'|'persegi'|'Persegi':
        panjangSisi = int(input('Masukkan panjang sisi persegi: '))
        luasPersegi = panjangSisi * panjangSisi
        print('Luas persegi adalah', luasPersegi)
    case '2'|'lingkaran'|'Lingkaran':
        jariJari = int(input('Masukkan jari-jari lingkaran: '))
        luasLingkaran = 3.14 * jariJari * jariJari
        print('Luas lingkaran adalah', luasLingkaran)
    case '3'|'segitiga'|'Segitiga':
        panjangAlas = int(input('Masukkan panjang alas segitiga: '))
        tinggiSegitiga = int(input('Masukkan tinggi segitiga: '))
        luasSegitiga = 0.5 * panjangAlas * tinggiSegitiga
        print('Luas segitiga adalah', luasSegitiga)
    case _:
        print('tidak dapat menghitung bangun datar tersebut, silakan masukkan pilihan yang benar.')




