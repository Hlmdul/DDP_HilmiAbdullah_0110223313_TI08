Stop = ''
while Stop != 'stop':
    LuasKeliling = input('''
program ini dapat menghitung luas dan keliling dari bangun datar layang-layang.
apakah anda ingin menghitung luas atau keliling? (1.luas/2.keliling) >> ''')

    match LuasKeliling.lower():
        case '1'|'luas':
            diagonal1 = int(input('Masukkan Diagonald 1 (dalam satuan meter) >> '))
            diagonal2 = int(input('Masukkan Diagonal 2 (dalam satuan meter) >> '))
            luasLayang = (diagonal1 * diagonal2) / 2
            print(f'''
Layang-layang dengan panjang diagonal 1 {diagonal1}m
dan panjang diagonal 2 {diagonal2}m memiliki luas {luasLayang}m**2''')
            Stop = 'stop'
        case '2'|'keliling':
            sisiPendek = int(input('Masukkan Sisi Pendek (dalam satuan meter) >> '))
            sisiPanjang = int(input('Masukkan Sisi Panjang (dalam satuan meter) >> '))
            kelilingLayang = (sisiPendek*2) + (sisiPanjang*2)
            print(f'''
Layang-layang dengan panjang sisi pendek {sisiPendek}m
dan panjang sisi panjang {sisiPanjang}m memiliki keliling {kelilingLayang}m''')
            Stop = 'stop'
        case _:
            print('Input Salah, Silahkan Coba Lagi')
            Stop = 'loop'

