# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 22:20:52 2021

@author: user
"""

#rule 
# nomor ketiga 1 = a
# nomor ketiga 2 = b
# nomor ketiga 3 = c
# nomor ketiga 5 = d
# nomor ketiga 7 = e
# nomor ketiga 8 = ee
# nomor ketiga 9 = f
# nomor keempat 1 = g
# nomor keempat 2 = h
# nomor keempat 3 = i
# nomor keempat 4 = j
# nomor keempat 5 = k
# nomor keempat 6 = l
# nomor keempat 7 = m
# nomor keempat 8 = n
# nomor keempat 9 = o
# nomor indonesia = p
# 62 = y
# 08 = z
# kartu halo = q
# simpati = r
# kartu as = s
# indosat m2 broadband = t
# matrix dan mentari = u
# matrix = v
# im3 = w
# mentari = aa
# xl = ab
# axis = ac
# 3 = ad
# smartfren = ae
# ceria = af

#1 if y then p
#2 if p&a&g then q
#3 if p&a&h then r
#4 if p&a&i then r
#5 if p&b&g then r
#6 if p&b&h then r
#7 if p&d&h then s
#8 if p&d&i then s
#9 if p&b&i then s
#10 if p&d&g then s
#11 if p&a&j then t
#12 if p&a&k then u
#13 if p&a&l then u
#14 if p&d&k then v
#15 if p&d&l then w
#16 if p&d&m then w
#17 if p&d&n then aa
#18 if p&c&n then ac
#19 if p&c&g then ac
#20 if p&c&h then ac
#21 if p&c&h then ac
#21 if p&ee&g then ae
#22 if p&ee&h then ae
#23 if p&ee&i then ae
#24 if p&ee&j then ae
#25 if p&ee&k then ae
#26 if p&ee&l then ae
#27 if p&ee&m then ae
#28 if p&ee&n then ae
#29 if p&ee&o then ae
#30 if p&ee&p then ae
#31 if p&b&n then af
#32 if y=z


#diket : nomor telepon 085713477482, sehingga
#didapat y = True dan d&m = True. Provider apakah yang digunakan oleh nomor tersebut?

#forward chaining
pilihan = input("\nHallo , \nApakah anda ingin mengecek nomor anda ? (y/n) : ")

list = ["Telkomsel", "Indosat", "XL", "AXIS", "3 Three", "Smartfren", "Ceria"]

list_telkomsel = ["Kartu Halo", "Simpati", "Kartu AS"]
list_indosat = ["Indosat M2 Broadband", "Matrix dan Mentari","Matrix","IM3", "Mentari"]
#forward chaining
while pilihan == 'y' :
    print("+-----------------------------------------------+")
    print("|\t\tSelamat Datang di Sistem Pakar Provider\t\t\t|")
    print("|\t\tProvider yang digunakan pada Nomor\t\t|")
    print("+-----------------------------------------------+")
    nomor = "08571347973"
    ask1 = input("apakah nomor sudah sesuai? (y/n) : ")
    data_nomor = nomor[:4]
    if ask1 == 'y' :
        if data_nomor == '0857' or data_nomor == '0857':
            print("provider yang digunakan",list[1])
            print(list_indosat[0])
        elif data_nomor == '0815' or data_nomor == '0816':
            print("provider yang digunakan",list[1])
            print(list_indosat[1])
        elif data_nomor == '0814':
            print("provider yang digunakan",list[1])
            print(list_indosat[0])
        elif data_nomor == '0858':
            print("provider yang digunakan",list[1])
            print(list_indosat[4])
        elif data_nomor == '0811':
            print("provider yang digunakan",list[0])
            print(list_telkomsel[0])
        elif data_nomor == '0812' or data_nomor == '0813':
            print("provider yang digunakan",list[0])
            print(list_telkomsel[1])
        elif data_nomor == '0821' or data_nomor == '0822':
            print("provider yang digunakan",list[0])
            print(list_telkomsel[1])
        elif data_nomor == '0852' or data_nomor == '0853':
            print("provider yang digunakan",list[0])
            print(list_telkomsel[2])
        elif data_nomor == '0823' or data_nomor == '0851':
            print("provider yang digunakan",list[0])
            print(list_telkomsel[2])
        elif data_nomor == '0817' or data_nomor == '0818' or data_nomor == '0819' or data_nomor == '0859' or data_nomor == '0877' or data_nomor == '0878':
            print("provider yang digunakan",list[2])
        elif data_nomor == '0838' or data_nomor == '0831' or data_nomor == '0832' or data_nomor == '0833':
            print("provider yang digunakan",list[3])
        elif data_nomor == '0895' or data_nomor == '0896' or data_nomor == '0897' or data_nomor == '0898' or data_nomor == '0899':
            print("provider yang digunakan",list[4])
        elif data_nomor == '0881' or data_nomor == '0882' or data_nomor == '0883' or data_nomor == '0884' or data_nomor == '0885':
            print("provider yang digunakan",list[5])
        elif data_nomor == '0881' or data_nomor == '0886' or data_nomor == '0887' or data_nomor == '0888' or data_nomor == '0889':
            print("provider yang digunakan",list[5])
        elif data_nomor == '0828':
            print("provider yang digunakan",list[6])
        else :
            print("cek kembali nomor yang anda masukkan")
        print("\n+-----------------------------------------------+") 
        pilihan = input("\nHallo , \nApakah anda ingin mengecek nomor anda kembali ? (y/n) : ")
        
        if pilihan == 'y' :
            print("+-----------------------------------------------+")
            print("|\t\tSelamat Datang di Sistem Pakar Provider\t\t\t|")
            print("|\t\tProvider yang digunakan pada Nomor\t\t|")
            print("+-----------------------------------------------+")
else :
    print("\n")
    print("+-------------Terima Kasih Telah berkunjung--------------+")
    print("+--------------Selalu Jaga Kesehatan---------------------+")
    
#backward chaining
pilihan = input("\nHallo , \nApakah anda ingin mengecek format nomor yang digunakan pada provider tertentu ? (y/n) : ")
list = ["Telkomsel", "Indosat", "XL", "AXIS", "3 Three", "Smartfren", "Ceria"]
list_telkomsel = ["Kartu Halo", "Simpati", "Kartu AS"]
list_indosat = ["Indosat M2 Broadband", "Matrix dan Mentari","Matrix","IM3", "Mentari"]

while pilihan == 'y' :
    print("+-----------------------------------------------+")
    print("|\t\tSelamat Datang di Sistem Pakar Provider\t\t\t|")
    print("|\t\tFormat nomor pada provider tertentu\t\t|")
    print("+-----------------------------------------------+")
    print("silakan pilih provider yang hendak dicek")
    print("1", list[0])
    print("2", list[1])
    print("3", list[2])
    print("4", list[3])
    print("5", list[4])
    print("6", list[5])
    print("7", list[6])
    provider = input("jawab sesuai nomor : ")
    ask1 = input("apakah anda yakin? (y/n) : ")
    if ask1 == 'y' :
        if provider == '1':
            print("0811 for Kartu Halo")
            print("0812 for Simpati")
            print("0813 for Simpati")
            print("0821 for Simpati")
            print("0822 for Simpati")
            print("0852 for Kartu AS")
            print("0853 for Kartu AS")
            print("0823 for Kartu AS")
            print("0851 for Kartu AS")
        elif provider == '2':
            print("0814 for indosat M2 Broadband")
            print("0815 for Matrix dan Mentari")
            print("0816 for Matrix dan Mentari")
            print("0855 for Matrix")
            print("0856 for IM3")
            print("0857 for IM3")
            print("0858 for Mentari")
        elif provider == '3':
            print("0817 for XL")
            print("0817 for XL")
            print("0819 for XL")
            print("0859 for XL")
            print("0877 for XL")
            print("0878 for XL")
        elif provider == '4':
            print("0838 for Axis")
            print("0831 for Axis")
            print("0832 for Axis")
            print("0833 for Axis")
        elif provider == '5':
            print("0895 for 3")
            print("0896 for 3")
            print("0897 for 3")
            print("0898 for 3")
            print("0899 for 3")
        elif provider == '6':
            print("0881 for Smartfren")
            print("0882 for Smartfren")
            print("0883 for Smartfren")
            print("0884 for Smartfren")
            print("0885 for Smartfren")
            print("0886 for Smartfren")
            print("0887 for Smartfren")
            print("0888 for Smartfren")
            print("0889 for Smartfren")
        else:
            print("0828 for Ceria")
        print("\n+-----------------------------------------------+") 
        pilihan = input("\nHallo , \nApakah anda ingin mengecek lagi? (y/n) : ")
        
        if pilihan == 'y' :
            print("+-----------------------------------------------+")
            print("|\t\tSelamat Datang di Sistem Pakar Provider\t\t\t|")
            print("|\t\tProvider yang digunakan pada Nomor\t\t|")
            print("+-----------------------------------------------+")
else :
    print("\n")
    print("+-------------Terima Kasih Telah berkunjung--------------+")
    print("+--------------Selalu Jaga Kesehatan---------------------+")
                
                                   
            