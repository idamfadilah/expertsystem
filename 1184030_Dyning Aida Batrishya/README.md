variabel :
 nomor ketiga 1 = a
 nomor ketiga 2 = b
 nomor ketiga 3 = c
 nomor ketiga 5 = d
 nomor ketiga 7 = e
 nomor ketiga 8 = ee
 nomor ketiga 9 = f
 nomor keempat 1 = g
 nomor keempat 2 = h
 nomor keempat 3 = i
 nomor keempat 4 = j
 nomor keempat 5 = k
 nomor keempat 6 = l
 nomor keempat 7 = m
 nomor keempat 8 = n
 nomor keempat 9 = o
 nomor indonesia = p
 62 = y
 08 = z
 telkomsel = tl
 kartu halo = q
 simpati = r
 kartu as = s
 indosat = in
 indosat m2 broadband = t
 matrix dan mentari = u
 matrix = v
 im3 = w
 mentari = aa
 xl = ab
 axis = ac
 3 = ad
 smartfren = ae
 ceria = af
 bb = provider

rules :
1 if y then p
2 if p&a&g then q
3 if p&a&h then r
4 if p&a&i then r
5 if p&b&g then r
6 if p&b&h then r
7 if p&d&h then s
8 if p&d&i then s
9 if p&b&i then s
10 if p&d&g then s
11 if p&a&j then t
12 if p&a&k then u
13 if p&a&l then u
14 if p&d&k then v
15 if p&d&l then w
16 if p&d&m then w
17 if p&d&n then aa
18 if p&c&n then ac
19 if p&c&g then ac
20 if p&c&h then ac
21 if p&c&h then ac
21 if p&ee&g then ae
22 if p&ee&h then ae
23 if p&ee&i then ae
24 if p&ee&j then ae
25 if p&ee&k then ae
26 if p&ee&l then ae
27 if p&ee&m then ae
28 if p&ee&n then ae
29 if p&ee&o then ae
30 if p&ee&p then ae
31 if p&b&n then af
32 if z = y
33 if w then in
34 if t then in
35 if u then in
36 if v then in
37 if q then tl
38 if r then tl
39 if s then tl
40 if bb = ?


diketahui : nomor telepon 085713477482, sehingga
didapat y = True dan p&d&m = True. Provider apakah yang digunakan oleh nomor tersebut?

cara kerja dari program tersebut ialah dengan menggunakan 2 metode
- pada forward chaining
untuk mendapatkan hasil akhir (misalkan bb)
forward chaining dimulai dengan mencocokkan fakta yang telah ada, yaitu jika 
y = True, maka p = True dan p&d&m = True, sehingga w True dan in = True
sehingga hasilnya bb = in.
(urutan rule 1 - 16 - 33)
- pada backward chaining
pada backward chaining, hasil akhir (misalnya bb) mempunyai nilai yang sama dengan in yang belum diketahui nilainya, dengan in = True apabila w = True (sehingga bisa saja rule ke 15 atau 16). namun nilai w akan bernilai True jika diketahui bahwa nilai p&d&m = True (maka yang digunakan line 16), jadi nilai p = True dan y = True.
urutan rulenya yaitu 33 - 16 - 1