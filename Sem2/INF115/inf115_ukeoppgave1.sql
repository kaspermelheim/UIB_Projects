-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 11. Sep, 2021 15:45 PM
-- Tjener-versjon: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `inf115_ukeoppgave1`
--

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `film`
--

CREATE TABLE `film` (
  `FNr` int(11) NOT NULL,
  `Title` varchar(32) DEFAULT NULL,
  `Year` int(11) DEFAULT NULL,
  `Country` varchar(32) DEFAULT NULL,
  `Director` varchar(32) DEFAULT NULL,
  `Run_time` int(11) DEFAULT NULL,
  `Price` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dataark for tabell `film`
--

INSERT INTO `film` (`FNr`, `Title`, `Year`, `Country`, `Director`, `Run_time`, `Price`) VALUES
(1, '2001: A Space Odyssey', 1968, 'USA', 'Stanley\r\nKubrick', 141, 149),
(2, 'Blade Runner', 1982, 'USA', 'Ridley Scott', 117, NULL),
(3, 'Alien', 1979, 'USA', 'Ridley Scott', 116, 123),
(4, 'Aliens', 1986, 'USA', 'James Cameron', 137, 123),
(5, 'Star wars', 1977, 'USA', 'George Lucas', 121, NULL),
(6, 'Brazil', 1985, 'UK', 'Terry Gilliam', 142, 149),
(7, 'Metropolis', 1927, 'Germany', 'Fritz Lang', 124, 87),
(8, 'The Terminator', 1984, 'USA', 'James Cameron', 107, 149),
(9, 'The Empire Strikes Back', 1980, 'USA', 'George\r\nLucas', 124, 123),
(10, 'ET the Extra-Terrestrial', 1982, 'USA', 'Steven Spielberg', 115, 87),
(11, 'The Thing', 1982, 'USA', 'John Carpenter', 109, 135),
(12, 'Moon', 2009, 'UK', 'Duncan Jones', 97, NULL),
(13, 'Stalker', 1979, 'Soviet Union', 'Andrei\r\nTarkovsky', 161, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `film`
--
ALTER TABLE `film`
  ADD PRIMARY KEY (`FNr`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
