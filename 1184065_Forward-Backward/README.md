
The setting is as follows; a man sits in a bunker, unable to observe the outsiden world. He is curious as to whether or not it is raining outside.
His only information about the world is seeing his boss, who is fortunate enough to not live in  the bunker, carry or not carry an umbrella.

If it is raining, there is a 90% chance his boss has an umbrella with him, if it is not raining there is a 20% chance he is carrying an umbrella. There is also a 70% chance of the weather being identical as the day before.

Given 50-50 odds the first day.


Part a):
The unobservable variable is the weather, or to be more precise, whether or not it is raining.

The observable variable is whether or not the protagonist's boss has an umbrella.

The dynamic/transitional model is presented as matrices in the code.


The assumptions in this model are for that both rain and not rain are equally likely at the initial state, which is not necessarily true. Further one could argue that this is very simplified view of how weather operates in the real world. The model assumes constant transitional matrices as well as a very predictable boss.

*************************************************************************************ANALISIS******************************************************************************
Pada program forward dan backward ini menggunakan library numpy. library numpy biasa digunakan untuk membuat sebuah Aljabar linear, terutama pada vector dan Matrik.
Forward disini digunakan untuk menghitung secara rekursif probabilitas gabungan sedangkan Backward digunakan untuk menghitung probabilitas untuk lebih akurat.

Param Vector merupakan nilai yang akan dinormalisasikan, misalnnya jumlah nilai yang ditetapkan dalam nilai tertentu.
Param endsum merupakan nilai default yaitu satu. Karena metode ini akan digunakan untuk membuat vektor stokastik. 

Point 1
Pada point 1 Forward dan Backward Algoritma.
Model transaksi menggunakan kasus matrik 2x2,
Model obs menggunakan kasus matrik 2x2 yang berisi probabilitas untuk observasi yang diberikan.
Previous Forward message digunakan untuk meneruskan pesan forward sebelumnya. 
Previoud Backward message digunkan untuk meneruskan pesan backward sebalumnya.

Point 2
Pada point 2 Gabungan Forward-Backward
Param model transtional adalah matrik likelyhood
Param prior, hasilnya pada nilai awal menjadi [0.5, 05]
Param evidence_list, Fakta yang ditemukan [True, True, False, True, True]
Return, mengembalikan daftar yang berisi vektor yang sesuai.
