# 3. buatlah fungsi untuk mencetak nilai bilangan ganjil dari parameter yang dimasukkan

def ganjilnya(x):
    for i in range(x):
        if i % 2 != 0:
            print(i, end=" ")

ganjilnya(80)