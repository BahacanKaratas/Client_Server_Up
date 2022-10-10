#Önce bir soket bağlantısı kurmak için başladım
import socket

import http.client

#import requests okulun kendi adresini kullanarak indirdiğim PYCHARM da hata verdi ve bir çok yönteme başvurmama rağmen
# hata vermeye devam etti. Bu yüzden http.client import ederek API call yapmam gerekti.
#BURADAKİ http.client importunun TCP HTTP ile hiçbir ilgisi yoktur. Tamamiyle POSTMAN yardımı ile belirleyip
#GET yapmak için kullancağım kodu yazabilmem için kullandığım bir kütüphane. Bu yüzden ödevin kuralları dışında bir
#harekette bulunmamış oluyorum.


#Aşağıdaki şekilde server soketi oluşturdum ve bu TCP bağlantısı kurmamı sağladı.
#! SOKET İLE TCP BAĞLANTISI KURUP BASİT BİR HTTP SUNUCUSU KURARKEN (a şıkkı) HERHANGİ BİR HAZIR KÜTÜPHANE KULLANILMADI !

c=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect(('localhost',9999));

#B şıkkında istenen API bağlantısı postman yardımı ile bu şekilde elde edildi

conn = http.client.HTTPSConnection("catfact.ninja")
payload = ''
headers = {}
conn.request("GET", "/fact", payload, headers)
res = conn.getresponse()
data = res.read()

data2=(""+str(data))

# Gelen veri daha anlaşılır ve güzel bir şekilde servera gönderildi (c şıkkı)
dataModified=data2[11:data2.find(".")+1]


#Server ve client arası TCP Socket bağlantısı
c.send(bytes(dataModified,"utf-8"))

print(c.recv(1024).decode())
print(c.recv(1024).decode())
print(c.recv(1024).decode())

c.close()


