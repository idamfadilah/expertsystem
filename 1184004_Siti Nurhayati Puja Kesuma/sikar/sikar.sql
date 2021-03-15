-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 14, 2021 at 08:54 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.4.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sikar`
--

-- --------------------------------------------------------

--
-- Table structure for table `tb_admin`
--

CREATE TABLE `tb_admin` (
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_admin`
--

INSERT INTO `tb_admin` (`username`, `password`) VALUES
('admin', '21232f297a57a5a743894a0e4a801fc3');

-- --------------------------------------------------------

--
-- Table structure for table `tb_kesimpulan`
--

CREATE TABLE `tb_kesimpulan` (
  `kode_kesimpulan` int(11) NOT NULL,
  `solusi` varchar(50) NOT NULL,
  `fakta` varchar(100) NOT NULL,
  `oleh` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_kesimpulan`
--

INSERT INTO `tb_kesimpulan` (`kode_kesimpulan`, `solusi`, `fakta`, `oleh`, `status`) VALUES
(1, 'Apartement', 'Menempati hunian sendiri', 'pakar', 'setuju'),
(2, 'Apartement', 'Tidak Memiliki Binatang peliharaan ', 'pakar', 'setuju'),
(3, 'rumah', 'Memiliki banyak furnitur', 'pakar', 'setuju'),
(4, 'rumah', 'Bekerja sebagai pegawai tetap', 'pakar', 'setuju'),
(5, 'rumah', 'Memiliki kendaraan lebih dari 2 ', 'pakar', 'setuju'),
(6, 'Apartement', 'Budget kurang dari 500 jt', 'pakar', 'setuju'),
(7, 'rumah', 'Bersedia tinggal dipinggiran kota', 'pakar', 'setuju'),
(8, 'Apartement', 'Bersedia tinggal di tengah kota', 'pakar', 'setuju'),
(9, 'rumah', 'menetap lebih dari 10tahun', 'pakar', 'setuju'),
(10, 'Apartement', 'suka berpergian keluar kota', 'pakar', 'setuju'),
(11, 'Apartement', 'Jarang bersosialisasi', 'pakar', 'setuju'),
(12, 'rumah', 'suka bercocok tanam', 'pakar', 'setuju');

-- --------------------------------------------------------

--
-- Table structure for table `tb_pertanyaan`
--

CREATE TABLE `tb_pertanyaan` (
  `kode_pertanyaan` varchar(50) NOT NULL,
  `isi_pertanyaan` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_pertanyaan`
--

INSERT INTO `tb_pertanyaan` (`kode_pertanyaan`, `isi_pertanyaan`) VALUES
('m1', 'Apakah anda akan tinggal sendiri?'),
('m10-a', 'Apakah anda membawa binatang peliharaan?'),
('m10-b', 'Apakah anda sudah memiliki furnitur yang banyak?'),
('m11-a', 'Apakah anda memiliki perkerjaan tetap?'),
('m11-b', 'Apakah anda mimiliki kendaraan lebih dari 2?'),
('m12-a', 'Apakah anda memiliki budget kurang dari 500 jt?'),
('m12-b', 'Apakah anda bersedia tinggal dipinggiran kota?'),
('m13-a', 'Apakah anda bersedia tinggal ditengah kota?'),
('m13-b', 'Apakah anda akan tinggal menetap lebih dari 10tahun?'),
('m14', 'Apakah anda suka berpergian keluar kota?'),
('m15', 'Apakah anda seorang yang jarang bersosialisasi?'),
('m16', 'Apakah anda suka becocok tanam?');

-- --------------------------------------------------------

--
-- Table structure for table `tb_solusi`
--

CREATE TABLE `tb_solusi` (
  `kode_solusi` varchar(50) NOT NULL,
  `isi_solusi` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_solusi`
--

INSERT INTO `tb_solusi` (`kode_solusi`, `isi_solusi`) VALUES
('S1', 'Apartement'),
('S10', 'Rumah'),
('S11', 'x-1'),
('S12', 'x-2'),
('S23', 'x-3'),
('S24', 'x-4'),
('S31', 'x-5');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_kesimpulan`
--
ALTER TABLE `tb_kesimpulan`
  ADD PRIMARY KEY (`kode_kesimpulan`);

--
-- Indexes for table `tb_pertanyaan`
--
ALTER TABLE `tb_pertanyaan`
  ADD PRIMARY KEY (`kode_pertanyaan`);

--
-- Indexes for table `tb_solusi`
--
ALTER TABLE `tb_solusi`
  ADD PRIMARY KEY (`kode_solusi`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_kesimpulan`
--
ALTER TABLE `tb_kesimpulan`
  MODIFY `kode_kesimpulan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=151;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
