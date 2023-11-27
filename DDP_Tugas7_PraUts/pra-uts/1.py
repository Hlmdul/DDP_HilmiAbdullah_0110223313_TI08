JenisKendaraan = input('''
Jenis Kendaraan
1. Motor
2. Mobil
Pilih Jenis Kendaraan:
>>> ''')
match JenisKendaraan.lower():
    case '1'|'motor':
        JenisKendaraan = 'Motor'
    case '2'|'mobil':
        JenisKendaraan = 'Mobil'

JenisBensin = input(''' 
    Jenis Bensin
1. Pertalite
2. Pertamax
3. Pertamax Turbo
Pilih Jenis Bensin:
>>>''')
match JenisBensin.lower():
    case '1'|'pertalite':
        JenisBensin = 'Pertalite'
    case '2'|'pertamax':
        JenisBensin = 'Pertamax'
    case '3'|'pertamax turbo':
        JenisBensin = 'Pertamax Turbo'

KotaTujuan = input('''
Kota Tujuan
1. Jakarta
2. Bekasi
3. Depok
4. Tangerang
5. Bogor
Pilih Kota Tujuan:
>>> ''')
match KotaTujuan.lower():
    case '1'|'jakarta':
        KotaTujuan = 'Jakarta'
    case '2'|'bekasi':
        KotaTujuan = 'Bekasi'
    case '3'|'depok':
        KotaTujuan = 'Depok'
    case '4'|'tangerang':
        KotaTujuan = 'Tangerang'
    case '5'|'bogor':
        KotaTujuan = 'Bogor'
        

if JenisBensin.lower() == 'pertalite':
    Harga = 10000
    JarakTempuh = 12
elif JenisBensin.lower() == 'pertamax':
    Harga = 14000
    JarakTempuh = 13
elif JenisBensin.lower() == 'pertamax turbo':
    Harga = 17000
    JarakTempuh = 13.5

if KotaTujuan.lower() == 'jakarta':
    JarakKota = 20
elif KotaTujuan.lower() == 'bekasi':
    JarakKota = 37.5
elif KotaTujuan.lower() == 'depok':
    JarakKota = 5
elif KotaTujuan.lower() == 'tangerang':
    JarakKota = 99
elif KotaTujuan.lower() == 'bogor':
    JarakKota = 120.6


print(
'''
    Detail Perjalanan:
Jenis Kendaraan: {}
Jenis Bensin: {}
Kota Tujuan: {}
Pemakaian Bensin: {:.2f} Liter
Total Harga: Rp. {:.2f}
'''.format(JenisKendaraan.title(),
            JenisBensin.title(),
            KotaTujuan.title(),
            JarakKota / JarakTempuh,
            (JarakKota / JarakTempuh) * Harga
                )
)
