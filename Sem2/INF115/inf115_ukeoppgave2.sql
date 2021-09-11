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
-- Database: `inf115_ukeoppgave2`
--

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `game_info`
--

CREATE TABLE `game_info` (
  `Publisher` varchar(255) NOT NULL,
  `Boardgame` varchar(255) NOT NULL,
  `Designer` varchar(255) NOT NULL,
  `Year_published` int(4) NOT NULL,
  `Game_type` varchar(255) NOT NULL,
  `Language` varchar(255) NOT NULL
) ;

--
-- Dataark for tabell `game_info`
--

INSERT INTO `game_info` (`Publisher`, `Boardgame`, `Designer`, `Year_published`, `Game_type`, `Language`) VALUES
('Czech Games Edition', 'Codenames', 'Vlaada Chvátil', 2015, 'Party', 'English'),
('Days of Wonder', 'Five Tribes', 'Bruno Cathala', 2014, 'Strategy', 'English'),
('Lookout Games', 'Agricola', 'Uwe Rosenberg', 2007, 'Strategy', 'German'),
('Z-Man Games', 'Pandemic', 'Matt Leacock', 2008, 'Cooperative', 'Norwegian');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `game_store`
--

CREATE TABLE `game_store` (
  `Store_number` int(32) NOT NULL,
  `Store_name` varchar(255) NOT NULL,
  `City` varchar(255) NOT NULL
) ;

--
-- Dataark for tabell `game_store`
--

INSERT INTO `game_store` (`Store_number`, `Store_name`, `City`) VALUES
(1, 'Outland', 'Bergen'),
(2, 'Tromsø Brukt bokhandel', 'Tromsø');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `sales`
--

CREATE TABLE `sales` (
  `Publisher` varchar(255) DEFAULT NULL,
  `Boardgame` varchar(255) DEFAULT NULL,
  `Store_number` int(32) DEFAULT NULL,
  `Year` int(32) DEFAULT NULL,
  `Month` int(32) DEFAULT NULL,
  `Quantity` int(11) NOT NULL
) ;

--
-- Dataark for tabell `sales`
--

INSERT INTO `sales` (`Publisher`, `Boardgame`, `Store_number`, `Year`, `Month`, `Quantity`) VALUES
('Lookout Games', 'Agricola', 1, 2014, 8, 2),
('Lookout Games', 'Agricola', 2, 2014, 3, 1),
('Czech Games Edition', 'Codenames', 1, 2015, 2, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `game_info`
--
ALTER TABLE `game_info`
  ADD PRIMARY KEY (`Publisher`,`Boardgame`);

--
-- Indexes for table `game_store`
--
ALTER TABLE `game_store`
  ADD PRIMARY KEY (`Store_number`);

--
-- Indexes for table `sales`
--
ALTER TABLE `sales`
  ADD KEY `Publisher` (`Publisher`,`Boardgame`),
  ADD KEY `Store_number` (`Store_number`);

--
-- Begrensninger for dumpede tabeller
--

--
-- Begrensninger for tabell `sales`
--
ALTER TABLE `sales`
  ADD CONSTRAINT `sales_ibfk_1` FOREIGN KEY (`Publisher`,`Boardgame`) REFERENCES `game_info` (`Publisher`, `Boardgame`),
  ADD CONSTRAINT `sales_ibfk_2` FOREIGN KEY (`Store_number`) REFERENCES `game_store` (`Store_number`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
