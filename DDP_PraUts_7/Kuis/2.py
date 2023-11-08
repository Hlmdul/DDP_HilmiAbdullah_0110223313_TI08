Pesanan = []
JumlahPesanan = []
Harga = []

NamaPembeli = input('''
Selamat Datang di Warkop Barokah.
Untuk pemesanan makanan atau minuman silakan isi form di bawah:

Nama Anda:
Jawab Disini >>> ''')

NoHp = input('''
No. HP Anda:
Jawab Disini >>> ''')

YaTidak = '1'

while YaTidak == '1':
    MakananMinuman = input('''
Pesan makanan atau minuman?
1. Makanan
2. Minuman
Jawab Disini >>> ''')
    
    if MakananMinuman == '1' or MakananMinuman.lower() == 'makanan':
        Makanan = input('''
Makanan yang Tersedia:
1. Nasi Goreng | Rp. 15.000
2. Mie Goreng | Rp. 12.000
3. Ayam Geprek | Rp. 18.000

Pilih Makanan (1/2/3):
Jawab Disini >>> ''')
        match Makanan.lower():
            case '1' | 'nasi goreng':
                Pesanan.append('Nasi Goreng') 
                Harga.append(15000)
            case '2' | 'mie goreng':
                Pesanan.append('Mie Goreng')
                Harga.append(12000)
            case '3' | 'ayam geprek':
                Pesanan.append('Ayam Geprek')
                Harga.append(18000)
        JumlahMakanan = int(input('Masukkan jumlah pesanan >>> '))
        JumlahPesanan.append(JumlahMakanan)


    elif MakananMinuman == '2' or MakananMinuman.lower() == 'minuman':
        Minuman = input('''
Minuman yang Tersedia:
1. Aneka Jus | Rp. 15.000
2. Soft Drink | Rp. 10.000
3. Sweet Ice Tea | Rp. 5.000

Pilih Minuman (1/2/3):
Jawab Disini >>> ''')
        match Minuman.lower():
            case '1' | 'aneka jus':
                Pesanan.append('Aneka Jus')
                Harga.append(15000)
            case '2' | 'soft drink':
                Pesanan.append('Soft Drink')
                Harga.append(10000)
            case '3' | 'sweet ice tea':
                Pesanan.append('Sweet Ice Tea')
                Harga.append(5000)
        JumlahMinuman = int(input('Masukkan jumlah pesanan >>> '))
        JumlahPesanan.append(JumlahMinuman)
    
    tanya = input('''
Apakan anda ingin memesan lagi?
ketik '1' jika ya
ketik '2' jika tidak
Jawab Disini >>> ''')
    YaTidak = tanya

print('''
Terima kasih telah memesan di Warkop Barokah.
Berikut rincian pemesanan anda:
    Nama: {}
    No. HP: {}
    
Pesanan Anda:''')

TotalBayar = []
for i in range(len(Pesanan)):
    TotalHarga = Harga[i] * JumlahPesanan[i]
    print('    {}. {} x {} | Rp. {}'.format(i+1, Pesanan[i], JumlahPesanan[i], TotalHarga))
    TotalBayar.append(TotalHarga)

print('''
Total Bayar: Rp. {:.2f}
'''.format(sum(TotalBayar)))     