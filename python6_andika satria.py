print("1, persegi\n")

sisi = int(input("masukan nilai sisi: "))
luas_p = sisi * sisi
print("luas persegi adalah", luas_p)

print("2, persegi panjanag")

panjang = int(input("masukan nilai panjang")) 
lebar = int(input("masukan nilai lebar"))
luas_pp = panjang = lebar 
print("luas persegi panjang adalah: ", luas_pp)

print("3, segitig")

alas = int(input("masukan nilai alas"))
tinggi = int(input("masukan nilai tinggi"))
luas_s = alas * tinggi 
print("luas segitiga adalah: ", luas_s)

print("4, jajar genjang")

alas = int(input("masukan nilai alas"))
tinggi = int(input("masukan nilai tinggi"))
luas_j = alas * tinggi
print("luas jajar genjang adalah: ",  luas_j) 

print("5, lingkaran")

phi = 3.14
r = int(input("masukan nilai panjang jari-jari lingkaran: "))
luas_l = phi * r * r
print("luas lingkaran adalah:", luas_l)