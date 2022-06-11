-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 10, 2022 at 05:13 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pbo_akhir`
--

-- --------------------------------------------------------

--
-- Table structure for table `lapangan`
--

CREATE TABLE `lapangan` (
  `id_lapangan` int(11) NOT NULL,
  `jenis_lapangan` varchar(10) NOT NULL,
  `tarif_lapangan` int(11) NOT NULL,
  `status_lapangan` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `lapangan`
--

INSERT INTO `lapangan` (`id_lapangan`, `jenis_lapangan`, `tarif_lapangan`, `status_lapangan`) VALUES
(1, 'Vinyl', 70000, 'Tersedia'),
(2, 'Sintetis', 65000, 'Disewa'),
(3, 'Sintetis', 75000, 'Disewa'),
(4, 'Vinyl', 70000, 'Disewa'),
(5, 'Sintetis', 80000, 'Disewa');

-- --------------------------------------------------------

--
-- Table structure for table `pemesanan_lapangan`
--

CREATE TABLE `pemesanan_lapangan` (
  `id_pemesanan` int(11) NOT NULL,
  `id_lapangan` int(11) NOT NULL,
  `tanggal_pemesanan` varchar(25) NOT NULL,
  `tanggal_sewa` varchar(25) NOT NULL,
  `jam_sewa` varchar(20) NOT NULL,
  `durasi_sewa` int(11) NOT NULL,
  `harga_sewa` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pemesanan_lapangan`
--

INSERT INTO `pemesanan_lapangan` (`id_pemesanan`, `id_lapangan`, `tanggal_pemesanan`, `tanggal_sewa`, `jam_sewa`, `durasi_sewa`, `harga_sewa`) VALUES
(1, 4, 'Fri Jun  3 19:20:15 2022', '9 Juni 2022', '8.30', 3, 210000),
(2, 2, 'Fri Jun  3 19:47:43 2022', '8 Desember 2022', '15.00', 1, 65000);

-- --------------------------------------------------------

--
-- Table structure for table `pemesanan_rompi`
--

CREATE TABLE `pemesanan_rompi` (
  `id_pemesanan` int(11) NOT NULL,
  `id_rompi` int(11) NOT NULL,
  `tanggal_pemesanan` varchar(25) NOT NULL,
  `tanggal_sewa` varchar(25) NOT NULL,
  `jam_sewa` varchar(20) NOT NULL,
  `durasi_sewa` int(10) NOT NULL,
  `harga_sewa` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pemesanan_rompi`
--

INSERT INTO `pemesanan_rompi` (`id_pemesanan`, `id_rompi`, `tanggal_pemesanan`, `tanggal_sewa`, `jam_sewa`, `durasi_sewa`, `harga_sewa`) VALUES
(1, 2, 'Fri Jun  3 19:24:00 2022', '7 Juli 2022', '13.00', 1, 30000),
(2, 5, 'Sat Jun  4 16:23:45 2022', '5 April 2023', '8.30', 2, 50000);

-- --------------------------------------------------------

--
-- Table structure for table `rompi`
--

CREATE TABLE `rompi` (
  `id_rompi` int(11) NOT NULL,
  `merk_rompi` varchar(10) NOT NULL,
  `warna_rompi` varchar(10) NOT NULL,
  `tarif_rompi` int(11) NOT NULL,
  `status_rompi` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rompi`
--

INSERT INTO `rompi` (`id_rompi`, `merk_rompi`, `warna_rompi`, `tarif_rompi`, `status_rompi`) VALUES
(1, 'Specs', 'Gelap', 20000, 'Disewa'),
(2, 'Specs', 'Terang', 20000, 'Tersedia'),
(3, 'Puma', 'Terang', 15000, 'Tersedia'),
(4, 'Puma', 'Gelap', 15000, 'Tersedia'),
(5, 'Nike', 'Terang', 25000, 'Disewa'),
(6, 'Nike', 'Gelap', 25000, 'Tersedia');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `lapangan`
--
ALTER TABLE `lapangan`
  ADD PRIMARY KEY (`id_lapangan`);

--
-- Indexes for table `pemesanan_lapangan`
--
ALTER TABLE `pemesanan_lapangan`
  ADD PRIMARY KEY (`id_pemesanan`);

--
-- Indexes for table `pemesanan_rompi`
--
ALTER TABLE `pemesanan_rompi`
  ADD PRIMARY KEY (`id_pemesanan`);

--
-- Indexes for table `rompi`
--
ALTER TABLE `rompi`
  ADD PRIMARY KEY (`id_rompi`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `lapangan`
--
ALTER TABLE `lapangan`
  MODIFY `id_lapangan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `pemesanan_lapangan`
--
ALTER TABLE `pemesanan_lapangan`
  MODIFY `id_pemesanan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `pemesanan_rompi`
--
ALTER TABLE `pemesanan_rompi`
  MODIFY `id_pemesanan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `rompi`
--
ALTER TABLE `rompi`
  MODIFY `id_rompi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
