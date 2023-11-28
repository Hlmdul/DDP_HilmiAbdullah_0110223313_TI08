buah_buahan = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

def duplikasi(buah_buahan):
   duplikat = []
   for buah in buah_buahan:
      duplikat.append(buah)
      duplikat.append(buah)
   return duplikat

print(duplikasi(buah_buahan))


tes = [1,2,3,4,5,6]
print(duplikasi(tes))





