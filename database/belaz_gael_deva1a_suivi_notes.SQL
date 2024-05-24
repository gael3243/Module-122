-- OM 2021.02.17
-- FICHIER MYSQL POUR FAIRE FONCTIONNER LES EXEMPLES
-- DE REQUETES MYSQL
-- Database: MACCAUD_OLIVIER_INFO1X_FILMS_164_2023

-- Destruction de la BD si elle existe.
-- Pour être certain d'avoir la dernière version des données

DROP DATABASE IF EXISTS belaz_gael_deva1a_suivi_notes;

-- Création d'un nouvelle base de donnée

CREATE DATABASE IF NOT EXISTS belaz_gael_deva1a_suivi_notes;

-- Utilisation de cette base de donnée

USE belaz_gael_deva1a_suivi_notes;
-- --------------------------------------------------------
-- Hôte:                         127.0.0.1
-- Version du serveur:           8.0.30 - MySQL Community Server - GPL
-- SE du serveur:                Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Listage de la structure de la base pour belaz_gael_deva1a_suivi_notes
CREATE DATABASE IF NOT EXISTS `belaz_gael_deva1a_suivi_notes` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `belaz_gael_deva1a_suivi_notes`;

-- Listage de la structure de table belaz_gael_deva1a_suivi_notes. t_apprenti
CREATE TABLE IF NOT EXISTS `t_apprenti` (
  `id_apprennti` int NOT NULL AUTO_INCREMENT,
  `nom_apprenti` char(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `prenom_apprenti` char(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `filiere_apprenti` char(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `ordonance_apprenti` int DEFAULT NULL,
  PRIMARY KEY (`id_apprennti`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table belaz_gael_deva1a_suivi_notes.t_apprenti : ~5 rows (environ)
INSERT INTO `t_apprenti` (`id_apprennti`, `nom_apprenti`, `prenom_apprenti`, `filiere_apprenti`, `ordonance_apprenti`) VALUES
	(3, 'Belaz', 'Gael', 'Developpement', 2021),
	(4, 'Nava', 'Justin', 'Operateur', 2018),
	(5, 'Moore', 'William', 'Exploitation', 2021),
	(6, 'Angelo', 'Mary', 'Developpement', 2017),
	(7, 'Freed', 'Diane', 'Operateur', 2017);

-- Listage de la structure de table belaz_gael_deva1a_suivi_notes. t_matiere
CREATE TABLE IF NOT EXISTS `t_matiere` (
  `id_matiere` int NOT NULL AUTO_INCREMENT,
  `nom_matiere` char(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `fk_type_matiere` int DEFAULT NULL,
  PRIMARY KEY (`id_matiere`),
  KEY `FK_matiere_type_matiere` (`fk_type_matiere`),
  CONSTRAINT `FK_matiere_type_matiere` FOREIGN KEY (`fk_type_matiere`) REFERENCES `t_type_matiere` (`id_type_matiere`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table belaz_gael_deva1a_suivi_notes.t_matiere : ~6 rows (environ)
INSERT INTO `t_matiere` (`id_matiere`, `nom_matiere`, `fk_type_matiere`) VALUES
	(1, 'Math', 3),
	(2, 'Anglais', 3),
	(3, 'CultureGeneral', 3),
	(4, 'i164', 1),
	(5, 'i319', 1),
	(6, 'i117', 2);

-- Listage de la structure de table belaz_gael_deva1a_suivi_notes. t_notes
CREATE TABLE IF NOT EXISTS `t_notes` (
  `id_notes` int NOT NULL AUTO_INCREMENT,
  `notes` decimal(20,6) DEFAULT NULL,
  `fk_matiere` int DEFAULT NULL,
  `fk_typeNotes` int DEFAULT NULL,
  `fk_apprenti` int DEFAULT NULL,
  PRIMARY KEY (`id_notes`) USING BTREE,
  KEY `FK_notes_matiere` (`fk_matiere`),
  KEY `FK_notes_type_notes` (`fk_typeNotes`),
  KEY `FK_notes_apprenti` (`fk_apprenti`),
  CONSTRAINT `FK_notes_apprenti` FOREIGN KEY (`fk_apprenti`) REFERENCES `t_apprenti` (`id_apprennti`),
  CONSTRAINT `FK_notes_matiere` FOREIGN KEY (`fk_matiere`) REFERENCES `t_matiere` (`id_matiere`),
  CONSTRAINT `FK_notes_type_notes` FOREIGN KEY (`fk_typeNotes`) REFERENCES `t_type_notes` (`id_type_notes`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table belaz_gael_deva1a_suivi_notes.t_notes : ~7 rows (environ)
INSERT INTO `t_notes` (`id_notes`, `notes`, `fk_matiere`, `fk_typeNotes`, `fk_apprenti`) VALUES
	(1, 5.000000, 4, 1, 5),
	(2, 4.000000, 1, 4, 6),
	(3, 3.500000, 3, 3, 5),
	(4, 6.000000, 4, 2, 3),
	(5, 5.500000, 1, 4, 4),
	(6, 2.000000, 2, 2, 5),
	(7, 4.500000, 5, 1, 7);

-- Listage de la structure de table belaz_gael_deva1a_suivi_notes. t_suivi
CREATE TABLE IF NOT EXISTS `t_suivi` (
  `id_suivi` int NOT NULL AUTO_INCREMENT,
  `fk_apprenti` int DEFAULT NULL,
  `fk_matiere` int DEFAULT NULL,
  `annee` char(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id_suivi`) USING BTREE,
  KEY `FK__apprenti` (`fk_apprenti`),
  KEY `FK_t_apprenti_matiere_matiere` (`fk_matiere`),
  CONSTRAINT `FK__apprenti` FOREIGN KEY (`fk_apprenti`) REFERENCES `t_apprenti` (`id_apprennti`),
  CONSTRAINT `FK_t_apprenti_matiere_matiere` FOREIGN KEY (`fk_matiere`) REFERENCES `t_matiere` (`id_matiere`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table belaz_gael_deva1a_suivi_notes.t_suivi : ~7 rows (environ)
INSERT INTO `t_suivi` (`id_suivi`, `fk_apprenti`, `fk_matiere`, `annee`) VALUES
	(1, 7, 4, 'Premiere'),
	(2, 6, 5, 'Quatrieme'),
	(3, 4, 2, 'Deuxieme'),
	(4, 4, 4, 'Premiere'),
	(5, 3, 1, 'Troisieme'),
	(6, 7, 5, 'Quatrieme'),
	(7, 5, 2, 'Troisieme');

-- Listage de la structure de table belaz_gael_deva1a_suivi_notes. t_type_matiere
CREATE TABLE IF NOT EXISTS `t_type_matiere` (
  `id_type_matiere` int NOT NULL AUTO_INCREMENT,
  `type_matiere` char(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id_type_matiere`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table belaz_gael_deva1a_suivi_notes.t_type_matiere : ~3 rows (environ)
INSERT INTO `t_type_matiere` (`id_type_matiere`, `type_matiere`) VALUES
	(1, 'ModuleEpsic'),
	(2, 'ModuleCie'),
	(3, 'BrancheGeneral');

-- Listage de la structure de table belaz_gael_deva1a_suivi_notes. t_type_notes
CREATE TABLE IF NOT EXISTS `t_type_notes` (
  `id_type_notes` int NOT NULL AUTO_INCREMENT,
  `type_notes` char(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id_type_notes`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Listage des données de la table belaz_gael_deva1a_suivi_notes.t_type_notes : ~4 rows (environ)
INSERT INTO `t_type_notes` (`id_type_notes`, `type_notes`) VALUES
	(1, 'Normal'),
	(2, 'MoyenneSemestrielle'),
	(3, 'MoyenneAnnuel'),
	(4, 'MoyenneFinale');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
