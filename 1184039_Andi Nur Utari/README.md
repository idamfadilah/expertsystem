
Sistem Pakar untuk Aplikasi Forward Chaining Covid-19 Test

A.	Pengertian Forward Chaining
	Forward chaining merupakan salah satu metode dari sistem pakar yang mencari atau menelusuri solusi melalui masalah. Dengan kata lain metode ini melakukan pertimbangan dari fakta-fakta yang kemudian berujung pada sebuah kesimpulan yang berdasarkan pada fakta-fakta. Metode ini merupakan kebalikan dari metode backward chaining yang melakukan pencarian yang berawal dari hipotesis menuju ke fakta-fakta untuk mendukung hipotesis tersebut.
	Pada metode forward chaining, penjelasan tidak terlalu terfalisitasi karena subgolas tidak diketahui secara ekspilisit sebelum kesimpulannya ditemukan. Forward chaining disebut juga bottom-up reasoning atau pertimbangan dari bawah ke atas, karena metode ini mempertimbangkan dari bukti-bukti pada level bawah, fakta-fakta, menuju ke kesimpulan pada level atas yang berdasarkan pada fakta-fakta.
B.	Analisis Aplikasi 
COVID-19 KNOWLEDGE BASE
A?PDP
B?Fever >= 38 Celcius
C?Cough
D?Flu
E?Sore Throat
F?Pneumonia mild or heavy according to clinical and/or image of radiology
G?Immunocompromised #(Kelainan Imun)
H?Having historical trip to China or region or country where the disease spread within 14 days before the first symptom.
I?Medical officer who get sick with same symptom after nursing patient with acute respiratory infection with unknown caused, without bothered by historical trip or live.
J?Patient with acute respiratory infection from mild to heavy.
K?Contacted with patient confirmed or probable Covid-19 within 14 days before symptom.
L?Having historical contact with infected animal (if it has been identified) within 14 days before symptom.
M?Working or visiting public health service which has cases of confirmed or probable COVID-19 in China or region or country that has been infected within 14 days before symptom.
N?ODP

#RULE_1 PDP  B&(C|D|E)&F
B C D E F A
B C D E - A
B C D - F A
B C - E F A
B C - - F A
B - D E F A
B - D - F A
B - - E F A

#RULE_2 PDP  B&(C|D|E)&G&(H|I)
B C D E G H I A
B C D E G H - A
B C D E G - I A
B C D E G - - A
B C D - G H I A
B C D - G H - A
B C D - G - I A
B C D - G - - A
B C - E G H I A
B C - E G H - A
B C - E G - I A
B C - E G - - A
B C - - G H I A
B C - - G H - A
B C - - G - I A
B C - - G - - A
B - D E G H I A
B - D E G H - A
B - D E G - I A
B - D E G - - A
B - D - G H I A
B - D - G H - A
B - D - G - - A
B - - E G H I A
B - - E G H - A
B - - E G - I A
B - - E G - - A

#RULE_3 PDP  J&(K|L|M|(H&B))
J K L M H B A
J K L M H - A
J K L M - B A
J K L M - - A
J K L - H B A
J K L - H - A
J K L - - B A
J K L - - - A
J K - M H B A
J K - M H - A
J K - M - B A
J K - M - - A
J K - - H B A
J K - - H - A
J K - - - B A
J K - - - - A
J - L M H B A
J - L M H - A
J - L M - B A
J - L M - - A
J - L - H B A
J - L - H - A
J - L - - B A
J - L - - - A
J - - M H B A
J - - M H - A
J - - M - B A
J - - M - - A
J - - - H B A


#RULE_4 ODP B|(~F&H&(~K|M|L)) N
B F H K M L N
B F H K M - N
B F H K - L N
B F H K - - N
B F H - M L N
B F H - M - N
B F H - - L N
B F H - - - N
B F - K M L N
B F - K M - N
B F - K - L N
B F - K - - N
B F - - M L N
B F - - M - N
B F - - - L N
B F - - - - N
B - H K M L N
B - H K M - N
B - H K - L N
B - H K - - N
B - H - M L N
B - H - M - N
B - H - - L N
B - H - - - N
B - - K M L N
B - - K M - N
B - - K - L N
B - - K - - N
B - - - M L N
B - - - M - N
B - - - - L N
B - - - - - N
- - H K M L N
- - H K M - N
- - H K - L N
- - H - M L N
- - H - M - N
- - H - - L N
- - H - - - N

CARA KERJA PROGRAM (SERTA PEMBACAAN RULE):
1.	User harus terlebih dahulu memasukkan gender 
2.	Lalu input nama
3.	Input jawaban dari pertanyaan sesuai dengan gejala yang ditimbulkan 
4.	Setelah input jawaban klik sumbit  
5.	Pengecekan pada rule pertama dahulu 
6.	Apabila tidak terdiagnosa PDP-19, akan dilakukan pengecekan rule kedua. 
7.	Apabila tidak terdiagnosa PDP, maka akan dilakukan pengecekan pada rule ketiga.
8.	Apabila tidak terdiagnosa PDP pada rule ketiga maka akan dilakukan pengecekan pada rule keempat(ODP). 
9.	Apabila tidak terdeteksi ODP maka user dinyatakan tidak terkena covid-19(Negative).


Pembacaan Rule :
1.	'B', 'C', 'D', etc. menyatakan kondisi 'True'
2.	'-' menyatakan kondisi 'False'
3.	'A' atau 'N' adalah result dari semua kondisi premise
File main.py akan mengambilkan input dari 'index.html'
4.	lalu input akan dibandingkan dengan rule secara forward chaining
Misalnya kondisi B pasien menjawab 'Yes'. Value yang diambil
5.	akan menjadi 'B ', jika pasien menjawab 'No' value yang diambil
6.	akan menjadi '- '. Blank space dalam value digunakan untuk
7.	split jawaban menjadi array. Setelah semua pertanyaan dijawab,
8.	lalu kita bandingkan dengan KB 'rule1.txt', dan mencarikan semua
9.	kondisi dimana B itu True. Jika semua questionnaire sudah dijawab,
10.	dan kondisi pertama tidak ada yang sama dengan knowledge base, maka
11.	akan masuk ke rule berikutnya sampai rule ODP (rule 4). Jika tidak
12.	ada kondisi yang memenuhi rule ODP (rule 4), maka pasien dinyatakan negative COVID-19.

if result_rule1:
        return "You are diagnosed with COVID-19.", adviceForPdp
    else:
        result_rule2 = fc_seven_goals(submitAnswers_rule2, knowledge_rule2)
        if result_rule2:
            return "You are diagnosed with COVID-19.", adviceForPdp
        else:
            result_rule3 = fc_six_goals(submitAnswers_rule3, knowledge_rule3)
            if result_rule3:
                return "You are diagnosed with COVID-19.", adviceForPdp
            else:
                result_rule4 = fc_six_goals(submitAnswer_rule4, knowledge_rule4)
                if result_rule4:
                    return "You are labeled to have ODP.", adviceForOdp
                else:
                    return "You are not diagnosed with COVID-19", adviceForNon

CARA MENDAPATKAN RULE:
1.	Membuat logika matematika gejala COVID-19 berdasarkan artikel jurnal.
2.	Membuat truth table dalam 'Google Sheets' untuk mendapatkan semua kemungkinan truth values dari setiap premise.
3.	Menggunakan formula logika matematika (RULES berdasarkan artikel), untuk mendapatkan hasil akhir ('A' atau 'N') dari truth value setiap premise ('B', 'C', 'D', etc).
4.	Masukkan truth value yang bernilai 'True' untuk hasil akhir ('A' atau 'D'), ke file '.txt' (seperti rule1.txt ini) dan akan dibaca oleh python.



