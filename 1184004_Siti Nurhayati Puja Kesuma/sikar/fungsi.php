<?php

function answer($kode){
    if($kode=='m1'){
        echo "<a class='btn col-sm-1 mrg btn-lg btn-outline-light' href='question.php?kode=m10-a'>Ya</a>";
        echo "<a class='btn col-sm-1 mrg btn-lg btn-outline-light' href='question.php?kode=m10-b'>Tidak</a>";
    }
    if($kode=='m10-a'){
        echo "<a class='btn col-sm-1 mrg btn-lg btn-outline-light' href='question.php?kode=m12-a'>Ya</a>";
        echo "<a class='btn col-sm-1 mrg btn-lg btn-outline-light' href='question.php?kode=m11-a'>Tidak</a>";

    }

    if($kode=='m10-b'){
        echo "<a class='btn col-sm-1 mrg btn-lg btn-outline-light' href='question.php?kode=m11-a'>Ya</a>";
        echo "<a class='btn col-sm-1 mrg btn-lg btn-outline-light' href='question.php?kode=m11-b'>Tidak</a>";
    }

    if($kode=='m11-b'){
        echo "<a class='btn col-sm-1 mrg btn-lg btn-outline-light' href='question.php?kode=m12-b'>Ya</a>";
        echo "<a class='btn col-sm-1 mrg btn-lg btn-outline-light' href='question.php?kode=m12-a'>Tidak</a>";
    }

    if($kode=='m12-a'){
        echo "<a class='btn col-sm-1 mrg btn-lg btn-outline-light' href='question.php?kode=m13-a'>Ya</a>";
        echo "<a class='btn col-sm-1 mrg btn-lg btn-outline-light' href='question.php?kode=m12-b'>Tidak</a>";
    }

    if($kode=='m13-a'){
        echo "<a class='btn col-sm-1 mrg btn-lg btn-outline-light' href='question.php?kode=m14'>Ya</a>";
        echo "<a class='btn col-sm-1 mrg btn-lg btn-outline-light' href='question.php?kode=m13-b'>Tidak</a>";
    }
    if($kode=='m11-a'){
        echo "<a class='btn col-sm-1 mrg btn-lg btn-outline-light' href='question.php?kode=m12-b'>Ya</a>";
        echo "<a class='btn col-sm-1 mrg btn-lg btn-outline-light' href='question.php?kode=m14'>Tidak</a>";
    }
    if($kode=='m12-b'){
        echo "<a class='btn col-sm-1 mrg btn-lg btn-outline-light' href='question.php?kode=m13-b'>Ya</a>";
        echo "<a class='btn col-sm-1 mrg btn-lg btn-outline-light' href='question.php?kode=m13-a'>Tidak</a>";
    }
    if($kode=='m13-b'){
        echo "<a class='btn col-sm-1 mrg btn-lg btn-outline-light' href='question.php?kode=m16'>Ya</a>";
        echo "<a class='btn col-sm-1 mrg btn-lg btn-outline-light' href='question.php?kode=m15'>Tidak</a>";
    }  

    if($kode=='m14'){
        echo "<a class='btn col-sm-1 mrg btn-lg btn-outline-light' href='question.php?kode=m15'>Ya</a>";
        echo "<a class='btn col-sm-1 mrg btn-lg btn-outline-light' href='question.php?kode=m16'>Tidak</a>";
    }   
    if($kode=='m15'){
        echo "<a class='btn col-sm-1 mrg btn-lg btn-outline-light' href='solusi.php?kode=s1'>Ya</a>";
        echo "<a class='btn col-sm-1 mrg btn-lg btn-outline-light' href='solusi.php?kode=s10'>Tidak</a>";
    }   
    if($kode=='m16'){
        echo "<a class='btn col-sm-1 mrg btn-lg btn-outline-light' href='solusi.php?kode=s10'>Ya</a>";
        echo "<a class='btn col-sm-1 mrg btn-lg btn-outline-light' href='solusi.php?kode=s1'>Tidak</a>";
    }   

}

function kesimpulan($hasil){
    include 'koneksi.php';
    $sql = "SELECT * from tb_kesimpulan WHERE solusi='$hasil' AND status='setuju'";
    $data = mysqli_query($connect,$sql);
    while ($row = mysqli_fetch_assoc($data)) {
        echo '<p>-'.$row['fakta'].'</p>';
    }  
}

function solusi($kode){    
    if ($kode=='s1') {
        $hasil = "Apartement";
        kesimpulan($hasil);        
    }
    if ($kode=='s10') {
        $hasil = "Rumah";
        kesimpulan($hasil);
    }
    if ($kode=='s11') {
        $hasil = "x-1";
        kesimpulan($hasil);
    }
     if ($kode=='s12') {
        $hasil = "x-2";
        kesimpulan($hasil);
    }
  
     if ($kode=='s23') {
        $hasil = "x-3";
        kesimpulan($hasil);
    }
     if ($kode=='s24') {
        $hasil = "x-4";
        kesimpulan($hasil);   
    }
     if ($kode=='s31') {
        $hasil = "x-5";
        kesimpulan($hasil);
    }
}


?>