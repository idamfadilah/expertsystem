# sistem_pakar

forward chaining
untuk mendapatkan hasil akhir (misalkan G), forward chaining dimulai dengan mencocokkan fakta yang telah diketahui.
jika diketahui A dan B bernilai True maka nilai C True dan C = F, sehingga G bernilai True.

backward chaining
pada backward chaining, hasil akhir (misalkan G) memiliki nilai yang sama dengan C yang belum diketahui nilainya (None)
sedangkan C bernilai True apabila A dan B True, dan nilai A, B sudah diketahui yaitu True, maka C true dan G True.

contoh:
misalkan situasi:
1. R1: if A and C then E
2. R2: if D and C then F
3. R3: if B and E then F
4. R4: if B then C
5. R5: if F then G

fakta A dan B bernilai True.
forward chaining (R4-R1-R3-R5)
1. R4 bernilai True, disimpulkan C bernilai True
2. R1 bernilai True, karena A True dan C bernilai True maka E bernilai True
3. R3 bernilai True, karena B bernilai True dan E bernilai True, maka F true
4. R5 bernilai True, karena F bernilai True

backward chaining (R5-R2-R3-R1-R4)
1. R5 nilai G akan sama dengan nilai F yang belum diketahui (None)
2. R2 nilai F sama dengan nilai D dan C yang belum diketahui (None)
3. R3 nilai F sama dengan nilai B dan E, dimana nilai B telah di ketahui yaitu True dan F None
4. R1 nilai E sama dengan nilai A dan C, dimana A diketahui bernilai True dan E None
5. R4 bernilai True karena B bernilai True maka C bernilai True, sehingga didapat kesimpulan bahwa nilai E True kemudian diketahui F True dan akhirnya didapat nilai G yaitu True.
