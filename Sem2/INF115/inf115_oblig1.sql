-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 11. Sep, 2021 15:44 PM
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
-- Database: `inf115_oblig1`
--

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `amino_acid_nomenclature`
--

CREATE TABLE `amino_acid_nomenclature` (
  `Amino_id` varchar(20) NOT NULL,
  `Symbol` char(1) DEFAULT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `Code` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dataark for tabell `amino_acid_nomenclature`
--

INSERT INTO `amino_acid_nomenclature` (`Amino_id`, `Symbol`, `Name`, `Code`) VALUES
('a1', 'A', 'Alanine', 'Ala'),
('a10', 'L', 'Leucine', 'Leu'),
('a11', 'M', 'Methionine', 'Met'),
('a12', 'N', 'Asparagine', 'Asn'),
('a13', 'P', 'Proline', 'Pro'),
('a14', 'Q', 'Glutamine', 'Gln'),
('a15', 'R', 'Arginine', 'Arg'),
('a16', 'S', 'Serine', 'Ser'),
('a17', 'T', 'Threonine', 'Thr'),
('a18', 'V', 'Valine', 'Val'),
('a19', 'W', 'Tryptophan', 'Trp'),
('a2', 'C', 'Cysteine', 'Cys'),
('a20', 'Y', 'Tyrosine', 'Tyr'),
('a21', NULL, NULL, 'Stop'),
('a22', NULL, NULL, 'Stop'),
('a23', NULL, NULL, 'Stop'),
('a3', 'D', 'Aspartic acid', 'Asp'),
('a4', 'E', 'Glutamic acid', 'Glu'),
('a5', 'F', 'Phenylalanine', 'Phe'),
('a6', 'G', 'Glycine', 'Gly'),
('a7', 'H', 'Histidine', 'His'),
('a8', 'I', 'Isoleucine', 'Ile'),
('a9', 'K', 'Lysine', 'Lys');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `amino_acid_properties`
--

CREATE TABLE `amino_acid_properties` (
  `Name` varchar(20) NOT NULL,
  `Molecular_mass` smallint(6) DEFAULT NULL,
  `Polarity` varchar(20) DEFAULT NULL,
  `Charge` varchar(20) DEFAULT NULL
) ;

--
-- Dataark for tabell `amino_acid_properties`
--

INSERT INTO `amino_acid_properties` (`Name`, `Molecular_mass`, `Polarity`, `Charge`) VALUES
('Alanine', 89, 'non polar', 'uncharged'),
('Arginine', 175, 'polar', 'positive'),
('Asparagine', 132, 'polar', 'uncharged'),
('Aspartic acid', 132, 'polar', 'negative'),
('Cysteine', 121, 'polar', 'uncharged'),
('Glutamic acid', 146, 'polar', 'negative'),
('Glutamine', 146, 'polar', 'uncharged'),
('Glycine', 75, 'non polar', 'uncharged'),
('Histidine', 155, 'polar', 'positive'),
('Isoleucine', 131, 'non polar', 'uncharged'),
('Leucine', 131, 'non polar', 'uncharged'),
('Lysine', 147, 'polar', 'positive'),
('Methionine', 149, 'non polar', 'uncharged'),
('Phenylalanine', 165, 'non polar', 'uncharged'),
('Proline', 115, 'non polar', 'uncharged'),
('Serine', 105, 'polar', 'uncharged'),
('Threonine', 119, 'polar', 'uncharged'),
('Tryptophan', 204, 'non polar', 'uncharged'),
('Tyrosine', 181, 'polar', 'uncharged'),
('Valine', 117, 'non polar', 'uncharged');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `codons`
--

CREATE TABLE `codons` (
  `Codon_id` varchar(3) NOT NULL,
  `Codon_sequence` char(3) DEFAULT NULL,
  `Position1` char(1) DEFAULT NULL,
  `Position2` char(1) DEFAULT NULL,
  `Position3` char(1) DEFAULT NULL,
  `Amino_acid_id` varchar(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dataark for tabell `codons`
--

INSERT INTO `codons` (`Codon_id`, `Codon_sequence`, `Position1`, `Position2`, `Position3`, `Amino_acid_id`) VALUES
('c1', 'TTT', 'T', 'T', 'T', 'a5'),
('c10', 'ATC', 'A', 'T', 'C', 'a8'),
('c11', 'ATA', 'A', 'T', 'A', 'a8'),
('c12', 'ATG', 'A', 'T', 'G', 'a11'),
('c13', 'GTT', 'G', 'T', 'T', 'a18'),
('c14', 'GTC', 'G', 'T', 'C', 'a18'),
('c15', 'GTA', 'G', 'T', 'A', 'a18'),
('c16', 'GTG', 'G', 'T', 'G', 'a18'),
('c17', 'TCT', 'T', 'C', 'T', 'a16'),
('c18', 'TCC', 'T', 'C', 'C', 'a16'),
('c19', 'TCA', 'T', 'C', 'A', 'a16'),
('c2', 'TTC', 'T', 'T', 'C', 'a5'),
('c20', 'TCG', 'T', 'C', 'G', 'a16'),
('c21', 'CCT', 'C', 'C', 'T', 'a13'),
('c22', 'CCC', 'C', 'C', 'C', 'a13'),
('c23', 'CCA', 'C', 'C', 'A', 'a13'),
('c24', 'CCG', 'C', 'C', 'G', 'a13'),
('c25', 'ACT', 'A', 'C', 'T', 'a17'),
('c26', 'ACC', 'A', 'C', 'C', 'a17'),
('c27', 'ACA', 'A', 'C', 'A', 'a17'),
('c28', 'ACG', 'A', 'C', 'G', 'a17'),
('c29', 'GCT', 'G', 'C', 'T', 'a1'),
('c3', 'TTA', 'T', 'T', 'A', 'a10'),
('c30', 'GCC', 'G', 'C', 'C', 'a1'),
('c31', 'GCA', 'G', 'C', 'A', 'a1'),
('c32', 'GCG', 'G', 'C', 'G', 'a1'),
('c33', 'TAT', 'T', 'A', 'T', 'a20'),
('c34', 'TAC', 'T', 'A', 'C', 'a20'),
('c35', 'TAA', 'T', 'A', 'A', 'a21'),
('c36', 'TAG', 'T', 'A', 'G', 'a22'),
('c37', 'CAT', 'C', 'A', 'T', 'a7'),
('c38', 'CAC', 'C', 'A', 'C', 'a7'),
('c39', 'CAA', 'C', 'A', 'A', 'a14'),
('c4', 'TTG', 'T', 'T', 'G', 'a10'),
('c40', 'CAG', 'C', 'A', 'G', 'a14'),
('c41', 'AAT', 'A', 'A', 'T', 'a12'),
('c42', 'AAC', 'A', 'A', 'C', 'a12'),
('c43', 'AAA', 'A', 'A', 'A', 'a9'),
('c44', 'AAG', 'A', 'A', 'G', 'a9'),
('c45', 'GAT', 'G', 'A', 'T', 'a3'),
('c46', 'GAC', 'G', 'A', 'C', 'a3'),
('c47', 'GAA', 'G', 'A', 'A', 'a4'),
('c48', 'GAG', 'G', 'A', 'G', 'a4'),
('c49', 'TGT', 'T', 'G', 'T', 'a2'),
('c5', 'CTT', 'C', 'T', 'T', 'a10'),
('c50', 'TGC', 'T', 'G', 'C', 'a2'),
('c51', 'TGA', 'T', 'G', 'A', 'a23'),
('c52', 'TGG', 'T', 'G', 'G', 'a19'),
('c53', 'CGT', 'C', 'G', 'T', 'a15'),
('c54', 'CGC', 'C', 'G', 'C', 'a15'),
('c55', 'CGA', 'C', 'G', 'A', 'a15'),
('c56', 'CGG', 'C', 'G', 'G', 'a15'),
('c57', 'AGT', 'A', 'G', 'T', 'a16'),
('c58', 'AGC', 'A', 'G', 'C', 'a16'),
('c59', 'AGA', 'A', 'G', 'A', 'a15'),
('c6', 'CTC', 'C', 'T', 'C', 'a10'),
('c60', 'AGG', 'A', 'G', 'G', 'a15'),
('c61', 'GGT', 'G', 'G', 'T', 'a6'),
('c62', 'GGC', 'G', 'G', 'C', 'a6'),
('c63', 'GGA', 'G', 'G', 'A', 'a6'),
('c64', 'GGG', 'G', 'G', 'G', 'a6'),
('c7', 'CTA', 'C', 'T', 'A', 'a10'),
('c8', 'CTG', 'C', 'T', 'G', 'a10'),
('c9', 'ATT', 'A', 'T', 'T', 'a8');

-- --------------------------------------------------------

--
-- Tabellstruktur for tabell `nucleotides`
--

CREATE TABLE `nucleotides` (
  `Symbol` char(1) NOT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `Type` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dataark for tabell `nucleotides`
--

INSERT INTO `nucleotides` (`Symbol`, `Name`, `Type`) VALUES
('A', 'Adenine', 'Purine'),
('C', 'Cytosine', 'Pyrimidine'),
('G', 'Guanine', 'Purine'),
('T', 'Thymine', 'Pyrimidine');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `amino_acid_nomenclature`
--
ALTER TABLE `amino_acid_nomenclature`
  ADD PRIMARY KEY (`Amino_id`),
  ADD UNIQUE KEY `Amino_id` (`Amino_id`),
  ADD KEY `Name_fk` (`Name`);

--
-- Indexes for table `amino_acid_properties`
--
ALTER TABLE `amino_acid_properties`
  ADD PRIMARY KEY (`Name`);

--
-- Indexes for table `codons`
--
ALTER TABLE `codons`
  ADD PRIMARY KEY (`Codon_id`),
  ADD KEY `Position1_fk` (`Position1`),
  ADD KEY `Position2_fk` (`Position2`),
  ADD KEY `Position3_fk` (`Position3`),
  ADD KEY `Amino_acid_fk` (`Amino_acid_id`);

--
-- Indexes for table `nucleotides`
--
ALTER TABLE `nucleotides`
  ADD PRIMARY KEY (`Symbol`);

--
-- Begrensninger for dumpede tabeller
--

--
-- Begrensninger for tabell `amino_acid_nomenclature`
--
ALTER TABLE `amino_acid_nomenclature`
  ADD CONSTRAINT `Name_fk` FOREIGN KEY (`Name`) REFERENCES `amino_acid_properties` (`Name`);

--
-- Begrensninger for tabell `codons`
--
ALTER TABLE `codons`
  ADD CONSTRAINT `Amino_acid_fk` FOREIGN KEY (`Amino_acid_id`) REFERENCES `amino_acid_nomenclature` (`Amino_id`),
  ADD CONSTRAINT `Position1_fk` FOREIGN KEY (`Position1`) REFERENCES `nucleotides` (`Symbol`),
  ADD CONSTRAINT `Position2_fk` FOREIGN KEY (`Position2`) REFERENCES `nucleotides` (`Symbol`),
  ADD CONSTRAINT `Position3_fk` FOREIGN KEY (`Position3`) REFERENCES `nucleotides` (`Symbol`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
