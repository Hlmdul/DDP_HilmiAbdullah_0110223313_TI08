# 1. buat program python untuk menentukan apakah seseorang tergolong sebagai
# anak-anak (usia di bawah 18),
# dewasa (usia antara 18 dan 63),
# atau lansia (di atas 65)

nama = 'dul'
umur = 100

if (umur < 18):
    kategori = 'anak-anak'
    print('{} umur kamu {} jadi kamu tergolong sebagai {} ya'.format(nama,umur,kategori))
elif (umur >= 18 and umur < 63):
    kategori = 'dewasa'
    print('bapak {} umur anda {} jadi anda tergolong sebagai {} ya'.format(nama,umur,kategori))
else:
    kategori = 'lansia'
    print('bapak {} umur anda {} jadi anda tergolong sebagai {} ya'.format(nama,umur,kategori))
    

# 2. buat program python untuk menentukan angka mana yang lebih besar dan menampilkan pesan yang sesuai

bil_1 = 2
bil_2 = 10

if (bil_1 > bil_2):
    print('bilangan 1 yang memiliki nilai {}, adalah bilangan yang lebih besar dari bilangan 2 yang memiliki nilai {}'.format(bil_1,bil_2))
elif (bil_2 > bil_1):
    print('bilangan 2 yang memiliki nilai {}, adalah bilangan yang lebih besar dari bilangan 1 yang memiliki nilai {}'.format(bil_2,bil_1))
else:
    print('kedua bilangan tersebut memiliki nilai yang sama')
    





