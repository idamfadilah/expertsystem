# Tugas Forward dan Backward Chaining

Forward Chaining adalah metode untuk mengetahui fakta-fakta atau informasi yang baru melalui aturan dan fakta yang ada.

mammal(A) ==> vertebrate(A)

vertebrate(A) ==> animal(A)

vertebrate(A),flying(A) ==> bird(A)

vertebrate("duck")

flying("duck")

mammal("cat")


Aturan
1. Jika fakta sama dengan mamalia maka hewan itu adalah vertebrata
2. Jika fakta sama dengan vertebrata maka hewan itu adalah kingdom animal
3. JIka fakta sama dengan vertebrata dan terbang maka hewan itu adalah burung

```

```

1. global facts yaitu variabel fakta
2. global is_changed yaitu variabel looping
3. is_changed = True berarti pada saat looping menyimpan kondisi true
4. facts = [["vertebrate","duck"],["flying","duck"],["mammal","cat"]] merupakan fakta yg ada
5. def assert_fact(fact): yaitu fungsi buat ngisi fakta/array
6. if not fact in facts: berarti jika tidak ada fakta di fakta lama
7. facts += [fact] perintah ini digunakan untuk menambahkan fakta baru
8. while is_changed: berarti pada saat kondisi looping nya true
9. is_changed = False berarti pada kondisi loopingnya diganti false biar ga looping di while doang
10. for A1 in facts: perintah ini digunakan untuk A1 di variabel fakta
11. if A1[0] == "mammal": perintah ini berarti A1[0] adalah mammal
12. assert_fact(["vertebrate",A1[1]]) diperintah ini menambahkan fakta baru yaitu vertebrata, A1[1]
13. if A1[0] == "vertebrate":
       assert_fact(["animal",A1[1]])
    Diperintah ini berarti jika A1[0] adalah vertebrata, maka menambahkan fakta baru yaitu animal, A1[1]
14. if A1[0] == "vertebrate" and ["flying",A1[1]] in facts:
      assert_fact(["bird",A1[1]])
    Diperintah ini berarti jika A1[0] adalah vertebrata dan terbang, A1[1], maka menambahkan fakta baru yaitu bird, A1[1]
