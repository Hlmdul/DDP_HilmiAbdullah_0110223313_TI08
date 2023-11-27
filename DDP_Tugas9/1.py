# 1. Buatlah fungsi untuk menampilkan data diri:
# contoh pemanggilan : profil(nama,alamat,gender,umur,hoby)

def profil(nama,alamat,gender,umur,hoby):
    print('''
Halo nama saya adalah {}, saya tinggal di {}, saya seorang {} berumur {} tahun. hoby saya adalah {}.'''.format(nama,alamat,gender,umur,hoby))
   

profil("Hilmi Abdullah","Komplek Timah","Laki-laki","23","Membaca")