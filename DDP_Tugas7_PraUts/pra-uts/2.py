NamaPembeli = input(''' 
Selamat datang di Warkop Barokah.
Untuk melakukan pemesanan makanan/minuman,
silakan isi form di bawah ini

Nama Anda:
>>> ''')
NoHpPembeli = input('''
No HP Anda:
>>> ''')
Pesanan = []
Harga = []
Jumlah = []
TotalHarga = []

tanya = 'y'
while tanya == 'y':
    MakanMinum = input('''
Ingin pesan makanan atau minuman?
                       
ketik 1 untuk pesan makanan
ketik 2 untuk pesan minuman
>>>''')
    if MakanMinum.lower() == 'makanan' or MakanMinum == '1':
        Makanan = input('''
Menu Makanan:
1.Nasi Goreng | Rp15.000
2.Mie Goreng | Rp12.000
3.Ayam Geprek | Rp18.000
                        
Pilih Makanan(1/2/3):
>>>''')
        match Makanan.lower():
            case '1'|'nasi goreng':
                Makanan = 'Nasi Goreng'
                Harga.append('15000')
            case '2'|'mie goreng':
                Makanan = 'Mie Goreng'
                Harga.append('12000')
            case '3'|'ayam geprek':
                Makanan = 'Ayam Geprek'
                Harga.append('18000')
        JumlahPesanan = input('Masukkan jumlah pesanan >>> ')
        Pesanan.append(Makanan)
        Jumlah.append(JumlahPesanan)

    elif MakanMinum.lower() == 'minuman' or MakanMinum == '2':
        Minuman = input('''
Menu Minuman:
1.Aneka Jus | Rp5.000
2.Soft Drink | Rp7.000
3.Sweet Ice Tea | Rp10.000 
Pilih Minuman(1/2/3):
>>>''')
        match Minuman.lower():
            case '1'|'aneka jus':
                Minuman = 'Aneka Jus'
                Harga.append('5000')
            case '2'|'soft drink':
                Minuman = 'Soft Drink'
                Harga.append('7000')
            case '3'|'sweet ice tea':
                Minuman = 'Sweet Ice Tea'
                Harga.append('10000')
        JumlahPesanan = input('Masukkan jumlah pesanan >>> ')
        Pesanan.append(Minuman)
        Jumlah.append(JumlahPesanan)
    tanya = input('''
Apakah ada pesanan lain?
ketik 'y' jika Iya
ketik 'n' jika Tidak
>>>''')
    if tanya == 'n':
        break
print('''
    Detail Pesanan 
    Nama: {}
    No HP: {}
'''.format(NamaPembeli,NoHpPembeli))
print('''
    Pesanan anda adalah''')
for i in range(len(Pesanan)):
    print('''
    {} {} dengan harga Rp{} x {} = Rp{}'''.format(Jumlah[i],Pesanan[i],Harga[i],Jumlah[i],int(Harga[i])*int(Jumlah[i])))
    TotalHarga.append(int(Harga[i])*int(Jumlah[i]))
print('''
      Total Harga: Rp''',sum(TotalHarga))
