# 1. Print semua bilangan ganjil dari list berikut, hentikan perulangan ketika sudah melewati bilangan 553.
# Pakai perulangan while.

numbers = [
 951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725,
547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390,
984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236,
375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219,
918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815,
67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440,
380, 126, 721, 328, 753, 470, 743, 527
]

#ver1
i=0
while i<=numbers.index(553):
    if numbers[i]%2 != 0:
        print(numbers[i], end=', ')
    i+=1

#ver2
i=0
bilangan = int(input('''Program ini akan mem-print semua bilangan ganjil dari list "numbers",
dan akan berhenti ketika bertemu bilangan yang anda input.

sebutkan bilangan yang anda inginkan: '''))
if bilangan in numbers:
    print('bilangan yang anda input adalah {}, maka hasil proses print adalah: '.format(bilangan))
    while i<=numbers.index(bilangan):
        if numbers[i]%2!=0:
            print(numbers[i], end=", ")
        i+=1
else:
    print('bilangan {} tidak ada dalam list, silakan input bilangan lain.'.format(bilangan))


# 2. Buat lah output dari menggunakan bahasa pemprograman python dengan : 
# 1 + 3 + 5 + 7 +9 +11 +13 + 15 +17 +19 = ...

#ver1
for i in range(1,20,2):
    if i<19:
        print(i, end=' + ')
    else:
        print(i, end=" ")

print('=',sum(range(1,20,2)))

#ver2
batas = int(input('''
program ini akan menjumlahkan bilangan ganjil dari 1 sampai batas bilangan yang anda input.
Masukkan batas bilangan: '''))
print('Anda menentukan {} sebagai batas, maka dihasilkan penjumlahan: ')
for i in range(1,batas,2):
    if i<(batas-1):
        print(i, end=' + ')
    else:
        print(i, end=" ")

print('=',sum(range(1,batas,2)))



# 3. Buat program untuk minta input jumlah baris dan buat
# rangkaian berikut ini
# *
# **
# ***
# ****
# Dan seterusnya sejumlah baris yang diinputkan
# Gunakan for loop dengan range

bintang = '*'
x=1
pertanyaan=int(input('''program ini berfungsi untuk mencetak tanda bintang(*) sebanyak jumlah baris yang anda inginkan
jumlah bintang menyesuaikan barisnya,
misal: jumlah bintang pada baris ke-1 adalah 1 bintang, jumlah bintang pada baris ke-2 adalah 2 bintang, dan seterusnya.

masukkan jumlah barisan bintang yang ingin anda cetak: '''))
print('mencetak {} baris bintang...'.format(pertanyaan))
for i in range(pertanyaan):
    print(bintang*x)
    x+=1