buah_buahan = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

def balik_list(buah_buahan):
   buah_balik = []
   for i in range(len(buah_buahan)):
      buah_balik.append(buah_buahan[-1-i])

   return buah_balik

print(balik_list(buah_buahan))


tes = [1,2,3,4,5,6,7,8]
print(balik_list(tes))