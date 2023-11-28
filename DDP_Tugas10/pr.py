hasil_akhir = [
{'nama':'Reza', 'nilai':70},
{'nama':'Ciut', 'nilai':63},
{'nama':'Dian', 'nilai':80},
{'nama':'Badu', 'nilai':40}
]

def lulus_saja(hasil_akhir):
   list_nama = []
   for nilai in hasil_akhir:
      if nilai['nilai'] > 65:
         list_nama.append(nilai['nama'])
   return list_nama

print(lulus_saja(hasil_akhir))

tes = [
{'nama':'Bryan', 'nilai':70},
{'nama':'Ijab', 'nilai':53},
{'nama':'Dul', 'nilai':90},
{'nama':'Miko', 'nilai':80}
]

print(lulus_saja(tes))