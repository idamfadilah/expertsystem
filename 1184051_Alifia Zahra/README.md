# Forward-Chaining

Ini merupakan program sistem pakar yang menggunakan forward chaining untuk memilih satu dari empat hewan dengan menyeleksi opsi/pilihannya.
Untuk logika kerja yang dapat disimpulkan dari program tersebut akan dijabarkan sebagai berikut : 
Dalam satu variabel yang bernama animal, terdapat beberapa klasifikasi dari 4 hewan yaitu jerapah, harimau, zebra, dan cheetah. Klasifikasi ini memiliki truth yaitu true/false.
Kemudian ada variabel bernama new_facts yang value nya adalah true ini akan digunakan sebagai (kondisi) pada perulangan while. Berdasarkan beberapa sumber yang saya baca, ini termasuk ke dalam Drools. Disebut juga dengan hukum fundamental dalam banyak Sistem Berbasis Aturan - terutama yang mengikuti Rete atau algoritme serupa - bahwa evaluasi kondisi ("t saat", "sisi kiri") terjadi setiap kali ada perubahan dalam Memori Kerja: sisipan, pembaruan, atau menghapus. Sebaliknya, aturan yang diaktifkan atau eksekusi konsekuensi ("kemudian", "sisi kanan") terjadi setelah fireAllRules atau fireUntilHalt dipanggil. Contoh :

while new_fact == True:
    new_fact = False

Terdapat 9 rules dengan kualifikasi yang telah ditentukan dan akan diseleksi sehingga menemukan kecocokan dengan ketentuan satu dari 4 hewan yang ada. Program akan memilih satu hewan setelah menyeleksi opsi, kemudian menyebutkan rules yang diaktifkan / sesuai dengan ketentuan dari klasifikasi pada variabel animal.  

Instruksi menjalankan program : 
1. Program berbasiskan bahasa python
2. Buka file.py melalui tools spyder/lainnya
3. Kemudian running program
4. Klasifikasi dapat dimodifikasi dengan mengubah truth yang memiliki 2 opsi yaitu (true/false)

