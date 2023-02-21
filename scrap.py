import os
import requests

r = requests.get("https://youtube.com", cookies={'CONSENT': 'YES+1'})
print (r.text)
f = open("c:/Users/Pablo/Desktop/pagina.txt", "w", encoding="utf-8")
f.write(r.text)
f.close()
#Cambios
#Cambios
#Cambios
#Cambios
#Cambios
#Cambios
