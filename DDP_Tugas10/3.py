string = 'Nurul Fikri'

def konsonan(string):
   string_konsonan = string
   vokal = ['a', 'i', 'u', 'e', 'o', ' ']
   for i in range(len(string)):
      if string[i].lower() in vokal:
         string_konsonan = string_konsonan.replace(string[i],'')
      
   return string_konsonan

print(konsonan(string))


tes = 'hai nama saya dul!'
print(konsonan(tes))










