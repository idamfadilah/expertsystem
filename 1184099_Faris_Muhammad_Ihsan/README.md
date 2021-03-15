# Tugas-Sistem-Pakar

Forward Chaining merupakan sebuah metode pengambilan keputusan untuk mendapatka solusi melalui Kemungkinan yang ada hingga menjadi sebuah fakta. 

Aturan yang digunakan 

1. D dan E merupakan kondisi true
2. Jika X adalah A dan B maka C
3. Jika X adalah D dan E maka F
4. Jika X adalah C maka G 
5. Jika X adalah F maka H


```
X = "Buaya"
D = "Buas"
E = "Bertaring"
A = "Melompat"
B = "Memakan Serangga"
C = "Ayam"
F = "Hidup di dua alam"
G = "Halal"
H = "Haram"
```
Kode diatas adalah variabel untuk menyimpan data kemungkinan


```
is_changed = True
facts = [[D,X],[E,X]]
```
Blok Kode ini digunakan untuk menyimpan Variabel 

```
def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True
 ```
Blok kode ini merupakan method yang digunakan untuk menyimpan fakta baru pada saat looping


```
while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == A and [B,A1[1]] in facts:
            assert_fact([C,A1[1]])
        if A1[0] == D and [E,A1[1]] in facts:
            assert_fact([F,A1[1]])
        if A1[0] == C:
            assert_fact([G,A1[1]])
        if A1[0] == F:
            assert_fact([H,A1[1]])
```
Blok Kode ini digunakan sebagai Looping Aturan yang sudah ditetapkan untuk menemukan fakta baru.
