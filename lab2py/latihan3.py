# input nilai variable
a=input("Masukan nilai a=")
b=input("Masukan nilai b=")

# cetak nilai variable
print ("variable a=",a)
print ("variable b=",b)

# cetak kedua variable dengan format string
format_string = f" hasil penggabungan a dan b adalah {a}{b}"

print(format_string)

# konversi variable
a=int(a)
b=int(b)

format_jumlah = f" hasil penjumlahan a dan b adalah ={a+b}"

print(format_jumlah)

format_pembagian = f" hasil pembagian a dan b adalah ={a/b}"

print(format_pembagian)
