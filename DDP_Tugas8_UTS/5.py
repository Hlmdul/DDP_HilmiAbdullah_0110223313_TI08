AngkaPertama = int(input('Masukkan Angka Pertama >> '))
AngkaKedua = int(input('Masukkan Angka Kedua >> '))

loop = True
while loop == True:
    Operator = input('''Pilih Operator:
                 1. Tambah(+)
                 2. Kurang(-)
                 3. Bagi(/)
                 4. Kali(*)
                 5. Pangkat(**)
                 >> ''')
    match Operator.lower():
        case '1'|'tambah'|'+':
            Operator = '+'
            Hasil = AngkaPertama + AngkaKedua
        case '2'|'kurang'|'-':
            Operator = '-'
            Hasil = AngkaPertama - AngkaKedua
        case '3'|'bagi'|'/':
            Operator = '/'
            Hasil = AngkaPertama / AngkaKedua
        case '4'|'kali'|'*':
            Operator = '*'
            Hasil = AngkaPertama * AngkaKedua
        case '5'|'pangkat'|'**':
            Operator = '**'
            Hasil = AngkaPertama ** AngkaKedua
        case _:
            Operator = 'Tidak Ditemukan'

    if Operator == 'Tidak Ditemukan':
        print('Operator Tidak Ditemukan, Pilih Operator yang Tersedia')
        loop = True
        
    else:
        loop = False
        print(f'''
    angka pertama: {AngkaPertama}
    angka kedua: {AngkaKedua}
    operator: {Operator}
    hasil operasi : {AngkaPertama} {Operator} {AngkaKedua} = {Hasil}
    ''')
        
        