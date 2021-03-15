print("")
print("+-------------------------------------------+")
print("")

print("Halo silahkan masukan nama anda. ")
nama = input("Nama : ")
print("")
print("+-------------------------------------------+")
print("")
print("Halo "+nama+" selamat datang di system pakar covid-19")
print("")
print("+-------------------------------------------+")

#pemeriksaan
pemeriksaan = input ("Apakah kamu ingin aku periksa ? (y/n) : ")
#cek gejala umum
if pemeriksaan == "y" :
    print("Okee.... tolong jawab pertanyaanku yah :)")
    print("")

    print("1. Demam")
    print("2. Batuk Kering")
    print("1. Kelelahan")
    cek1 = input("Apakah kamu merasakan gejala tersebut ? (y/n) : ")
    print("")
    
    #cek gejala yang sedikit tidak umum
    if cek1 == "y" :
        print("1. Rasa tidak nyaman dan nyeri")
        print("2. Nyeri tenggorokan")
        print("3. Diare")
        print("4. Konjungtivitis (mata merah)")
        print("5. Sakit kepala")
        print("6. Hilang indra perasa atau penciuman")
        print("7. Ruam pada kulit, atau perubahan warna pada jari tangan atau jari kaki")
        cek2 = input("Selanjutnya apakah kamu merasakan gejala ini ? (y/n) : ")
        print("")

        #cek gejala serius
        if cek2 == "y" :
            print("1. Kesulitan bernapas atau sesak napas")
            print("2. Nyeri dada atau rasa tertekan pada dada")
            print("3. hilangnya kemampuan berbicara atau bergerak")
            cek3 = input("Apakah kamu merasakan gejala ini ? (y/n) : ")
            print("")

            if cek3 == "y" :
                print("Waduh segera cari bantuan medis jika kamu mengalami gejala ini...!")
                print("mungkin saja kamu terinfeksi virus covid-19,")
                print("tapi jangan kahwatir sekarang sudah ada vaksinnya")
                print("silahkan menuju kerumah sakit terdekat")

            elif cek3 == "n" :
                print("Jika kamu tidak merasakan adanya gejala ini, kamu harus tetap kerumah sakit yah.!")
                print("Jangan lupa untuk selalu memakai masker "+ nama)
                print("Stay Safe")
        
        elif cek2 == "n" :
            print("Jika kamu tidak merasakan gejala ini siahkan beristerahat secukupnya "+nama+", jangan lupa untuk meminum obat menurun demam :)")
            print("Semoga cepat sebuh dan bisa beraktifiktas kembali dan jangan lupa untuk memakai masker")
            print("Silahkan datang kembali....!")
            print("Stay Safe")

    
    elif cek1 == "n" :
        print("Yaudah deh nanti kamu datang kembali yah..!")
        print("Stay Safe")

elif pemeriksaan == "n" :
    print("Silahkan datang kembali yah "+nama+" dan jangan lupa pakai masker, Stay Safe..!")

