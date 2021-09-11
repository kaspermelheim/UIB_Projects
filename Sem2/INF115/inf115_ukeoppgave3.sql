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
-- Database: `inf115_ukeoppgave3`
--

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `airport`
--

CREATE TABLE `airport` (
  `Airport_No` int(11) NOT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `City_name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dataark for tabell `airport`
--

INSERT INTO `airport` (`Airport_No`, `Name`, `City_name`) VALUES
(1, 'Gardermoen', 'Oslo'),
(2, 'Heathrow', 'London'),
(3, 'Charles de Gaulle', 'Paris');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `border`
--

CREATE TABLE `border` (
  `Country1` varchar(20) NOT NULL,
  `Country2` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dataark for tabell `border`
--

INSERT INTO `border` (`Country1`, `Country2`) VALUES
('Finland', 'Norway'),
('Finland', 'Russia'),
('Finland', 'Sweden'),
('Norway', 'Finland'),
('Norway', 'Russia'),
('Norway', 'Sweden'),
('Russia', 'Finland'),
('Russia', 'Norway'),
('Sweden', 'Finland'),
('Sweden', 'Norway');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `cities`
--

CREATE TABLE `cities` (
  `Name` varchar(20) NOT NULL,
  `Area` int(11) DEFAULT NULL,
  `Country` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dataark for tabell `cities`
--

INSERT INTO `cities` (`Name`, `Area`, `Country`) VALUES
('Helsinki', 715, 'Finland'),
('Moscow', 2511, 'Russia'),
('Oslo', 480, 'Norway'),
('ReykjavÃk', 273, 'Iceland'),
('Stockholm', 188, 'Sweden');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `company`
--

CREATE TABLE `company` (
  `Airline_code` char(2) NOT NULL,
  `Name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dataark for tabell `company`
--

INSERT INTO `company` (`Airline_code`, `Name`) VALUES
('DY', 'Norwegian'),
('LH', 'Lufthansa'),
('SK', 'SAS');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `countries`
--

CREATE TABLE `countries` (
  `Name` varchar(20) NOT NULL,
  `Area` int(11) DEFAULT NULL,
  `Capital_city` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dataark for tabell `countries`
--

INSERT INTO `countries` (`Name`, `Area`, `Capital_city`) VALUES
('Finland', 338424, 'Helsinki'),
('Iceland', 102775, 'ReykjavÃk'),
('Norway', 385178, 'Oslo'),
('Russia', 17098242, 'Moscow'),
('Sweden', 450295, 'Stockholm');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `flights`
--

CREATE TABLE `flights` (
  `Company_code` char(2) NOT NULL,
  `Serial_number` int(11) NOT NULL,
  `Departure_location` int(11) DEFAULT NULL,
  `Departure_time` time DEFAULT NULL,
  `Arrival_location` int(11) DEFAULT NULL,
  `Arrival_time` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dataark for tabell `flights`
--

INSERT INTO `flights` (`Company_code`, `Serial_number`, `Departure_location`, `Departure_time`, `Arrival_location`, `Arrival_time`) VALUES
('DY', 510, 3, '16:30:00', 1, '18:15:00'),
('DY', 740, 3, '06:45:00', 2, '08:30:00'),
('LH', 310, 1, '10:15:00', 2, '12:15:00'),
('LH', 565, 3, '16:30:00', 1, '18:15:00'),
('SK', 430, 2, '13:55:00', 1, '15:20:00'),
('SK', 835, 1, '15:25:00', 3, '15:30:00'),
('SK', 890, 1, '10:30:00', 2, '12:05:00');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `population`
--

CREATE TABLE `population` (
  `Name` varchar(20) NOT NULL,
  `Year` smallint(6) NOT NULL,
  `Number` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dataark for tabell `population`
--

INSERT INTO `population` (`Name`, `Year`, `Number`) VALUES
('Finland', 1980, 4771000),
('Finland', 2000, 5171000),
('Finland', 2015, 5486000),
('Iceland', 1980, 254000),
('Iceland', 2000, 318000),
('Iceland', 2015, 329000),
('Norway', 1980, 4091000),
('Norway', 2000, 4478000),
('Norway', 2015, 5166000),
('Russia', 1980, 138483000),
('Russia', 2000, 146597000),
('Russia', 2015, 143976000),
('Sweden', 1980, 8318000),
('Sweden', 2000, 8861000),
('Sweden', 2015, 9802000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `airport`
--
ALTER TABLE `airport`
  ADD PRIMARY KEY (`Airport_No`);

--
-- Indexes for table `border`
--
ALTER TABLE `border`
  ADD PRIMARY KEY (`Country1`,`Country2`),
  ADD KEY `Border_FK2` (`Country2`);

--
-- Indexes for table `cities`
--
ALTER TABLE `cities`
  ADD PRIMARY KEY (`Name`),
  ADD KEY `Cities_FK` (`Country`);

--
-- Indexes for table `company`
--
ALTER TABLE `company`
  ADD PRIMARY KEY (`Airline_code`);

--
-- Indexes for table `countries`
--
ALTER TABLE `countries`
  ADD PRIMARY KEY (`Name`);

--
-- Indexes for table `flights`
--
ALTER TABLE `flights`
  ADD PRIMARY KEY (`Company_code`,`Serial_number`),
  ADD KEY `Flights_Airport_FK1` (`Departure_location`),
  ADD KEY `Flights_Airport_FK2` (`Arrival_location`);

--
-- Indexes for table `population`
--
ALTER TABLE `population`
  ADD PRIMARY KEY (`Name`,`Year`);

--
-- Begrensninger for dumpede tabeller
--

--
-- Begrensninger for tabell `border`
--
ALTER TABLE `border`
  ADD CONSTRAINT `Border_FK1` FOREIGN KEY (`Country1`) REFERENCES `countries` (`Name`),
  ADD CONSTRAINT `Border_FK2` FOREIGN KEY (`Country2`) REFERENCES `countries` (`Name`);

--
-- Begrensninger for tabell `cities`
--
ALTER TABLE `cities`
  ADD CONSTRAINT `Cities_FK` FOREIGN KEY (`Country`) REFERENCES `countries` (`Name`);

--
-- Begrensninger for tabell `flights`
--
ALTER TABLE `flights`
  ADD CONSTRAINT `Flights_Airline_FK` FOREIGN KEY (`Company_code`) REFERENCES `company` (`Airline_code`),
  ADD CONSTRAINT `Flights_Airport_FK1` FOREIGN KEY (`Departure_location`) REFERENCES `airport` (`Airport_No`),
  ADD CONSTRAINT `Flights_Airport_FK2` FOREIGN KEY (`Arrival_location`) REFERENCES `airport` (`Airport_No`);

--
-- Begrensninger for tabell `population`
--
ALTER TABLE `population`
  ADD CONSTRAINT `population_FK1` FOREIGN KEY (`Name`) REFERENCES `countries` (`Name`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
