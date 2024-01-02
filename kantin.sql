-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 12 Des 2023 pada 11.19
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kantin`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `login`
--

CREATE TABLE `login` (
  `username` varchar(20) NOT NULL,
  `password` varchar(10) NOT NULL,
  `level` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `login`
--

INSERT INTO `login` (`username`, `password`, `level`) VALUES
('dapur', '123', 'dapur'),
('kasir', '123', 'kasir'),
('user', '123', 'user');

-- --------------------------------------------------------

--
-- Struktur dari tabel `menu`
--

CREATE TABLE `menu` (
  `id` int(10) NOT NULL,
  `nama_menu` varchar(50) NOT NULL,
  `deskripsi` varchar(100) NOT NULL,
  `harga2` varchar(10) NOT NULL,
  `kategori` enum('makanan','minuman') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `menu`
--

INSERT INTO `menu` (`id`, `nama_menu`, `deskripsi`, `harga2`, `kategori`) VALUES
(1, 'Nasi Goreng Jawa', 'Nasi Goreng dengan bumbu khas tradisional Jawa', '15.000', 'makanan'),
(2, 'Nasi Rames', 'Nasi dengan campuran berbagai macam sayur + mie goreng', '10.000', 'makanan'),
(3, 'Magelangan', 'Nasi Goreng biasa dengan campuran mie ', '20.000', 'makanan'),
(4, 'Soto Lamongan', 'Soto khas bumbu Lamongan ', '8.000', 'makanan'),
(5, 'Nasi Chicken Katsu', 'Nasi ditambah dengan chicken katsu ala jepang dengan saus khas ', '25.000', 'makanan'),
(6, 'Es Teh', 'Es teh dengan menggunakan teh pilihan yang harum', '4.000', 'minuman'),
(7, 'Es Jeruk', 'Es Jeruk dengan menggunakan jeruk orange Demak yang terkenal manis', '5.000', 'minuman'),
(8, 'Wedhang Uwuh', 'Minuman seduhan dari berbagai macam rempah-rempah', '8.000', 'minuman'),
(9, 'Kopi Hitam', 'Seduhan dari biji kopi pilihan', '10.000', 'minuman'),
(10, 'Es Degan', 'Kelapa muda yang diambil langsung dari sumbernya', '15.000', 'minuman');

-- --------------------------------------------------------

--
-- Struktur dari tabel `payment`
--

CREATE TABLE `payment` (
  `id` int(10) NOT NULL,
  `kasir` varchar(50) NOT NULL,
  `hari` date NOT NULL,
  `income` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `payment`
--

INSERT INTO `payment` (`id`, `kasir`, `hari`, `income`) VALUES
(1, 'Fiki', '2023-12-11', '550.000'),
(2, 'Saiful', '2023-12-12', '322.000'),
(3, 'Ridho', '2023-12-13', '425.000'),
(4, 'Putri', '2023-12-14', '297.000'),
(5, 'Alfian', '2023-12-15', '571.000');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pesanan`
--

CREATE TABLE `pesanan` (
  `id` int(10) NOT NULL,
  `nama` varchar(25) NOT NULL,
  `meja` int(10) NOT NULL,
  `nama_menu` varchar(50) NOT NULL,
  `harga2` varchar(10) NOT NULL,
  `catatan` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `pesanan`
--

INSERT INTO `pesanan` (`id`, `nama`, `meja`, `nama_menu`, `harga2`, `catatan`) VALUES
(1, 'Fiki', 8, 'Nasi Goreng Jawa', '15.000', 'Ekstra Pedas'),
(2, 'Ipul', 3, 'Magelangan', '20.000', 'Ekstra Mie + pedas'),
(3, 'Alfian', 1, 'Nasi Chicken Katsu, Es jeruk', '30.000', 'es jeruk sedikit es'),
(4, 'Ridho', 4, 'Nasi Rames, Soto Lamongan, Es Degan', '33.000', ''),
(5, 'Putri', 5, 'Soto Lamongan, Es teh', '12.000', 'Es teh tanpa gula');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`username`);

--
-- Indeks untuk tabel `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `pesanan`
--
ALTER TABLE `pesanan`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `menu`
--
ALTER TABLE `menu`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT untuk tabel `payment`
--
ALTER TABLE `payment`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT untuk tabel `pesanan`
--
ALTER TABLE `pesanan`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
