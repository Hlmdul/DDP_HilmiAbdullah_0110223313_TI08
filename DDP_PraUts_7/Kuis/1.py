NamaKendaraan = input('''
Jenis Kendaraan:
1. Mobil
2. Motor

Pilih Jenis Kendaraan (1/2):
Jawab Disini >>> ''')

JenisBensin = input('''
Jenis Bensin:
1. Pertalite
2. Pertamax
3. Pertamax Turbo

Pilih Jenis Bensin (1/2/3):
Jawab Disini >>> ''')

KotaTujuan = input('''
Kota Tujuan:
1. Jakarta
2. Bekasi
3. Depok
4. Tangerang
5. Bogor

Pilih Kota Tujuan (1/2/3/4/5):
Jawab Disini >>> ''')

match JenisBensin.lower():
    case '1' | 'pertalite':
        JenisBensin = 'Pertalite'
        HargaBensin = 10000
        JarakTempuh = 12
    case '2' | 'pertamax':
        JenisBensin = 'Pertamax'
        HargaBensin = 14000
        JarakTempuh = 13
    case '3' | 'pertamax turbo':
        JenisBensin = 'Pertamax Turbo'
        HargaBensin = 17000
        JarakTempuh = 13.5

match KotaTujuan.lower():
    case '1' | 'jakarta':
        KotaTujuan = 'Jakarta'
        JarakKota = 20
    case '2' | 'bekasi':
        KotaTujuan = 'Bekasi'
        JarakKota = 35.7
    case '3' | 'depok':
        KotaTujuan = 'Depok'
        JarakKota = 5
    case '4' | 'tangerang':
        KotaTujuan = 'Tangerang'
        JarakKota = 99
    case '5' | 'bogor':
        KotaTujuan = 'Bogor'
        JarakKota = 120.6

print ('''
Detail Perjalanan Anda:
Jenis Kendaraan: {}
Jenis Bensin: {}
Kota Tujuan: {}
Pemakaian Bensin: {:.2f} Liter
Total Harga Bensin:
    Rp. {:.2f} x {:.2f} = Rp. {:.2f}
'''.format(NamaKendaraan, JenisBensin, KotaTujuan, JarakKota / JarakTempuh, HargaBensin, (JarakKota / JarakTempuh), HargaBensin * (JarakKota / JarakTempuh)))