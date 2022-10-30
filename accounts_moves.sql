-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: accounts
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `moves`
--

DROP TABLE IF EXISTS `moves`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `moves` (
  `NAME` varchar(20) NOT NULL,
  `TYPE` varchar(20) NOT NULL,
  `POWER` int NOT NULL,
  `ACCURACY` int NOT NULL,
  `NOU` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `moves`
--

LOCK TABLES `moves` WRITE;
/*!40000 ALTER TABLE `moves` DISABLE KEYS */;
INSERT INTO `moves` VALUES ('Apple Acid','Grass',80,100,10),('Astal Barrage','Ghost',120,100,5),('Aura Wheel','Electric',110,100,10),('Behemoth Bash','Steel',100,100,5),('Behemoth Blade ','Steel',100,100,5),('Bitter Malice','Ghost',60,100,15),('Bleadwind Storm ','Flying',95,80,5),('Body Press','Fighting',80,100,10),('Bolt Beak','Electric',85,100,10),('Branch Poke','Grass',40,100,40),('Breaking Swipe','Dragon',60,100,15),('Burning Jealousy','Fire',70,100,5),('Ceaseless Edge','Dark',65,90,15),('Choloroblast','Grass',120,95,5),('Dragon Darts','Dragon',50,100,10),('Drum Beating','Grass',80,100,10),('Dual Wingbeat','Flying',40,90,10),('Esper Wing','Psychic',75,90,10),('Erie Spell','Psychic',80,100,5),('Eternabeam','Dragon',160,90,5),('Expanding Force','Psychic',80,100,10),('False Surrender','Dark',80,100,10),('Fiery Wrath','Dark',90,100,10),('Fishious Rend','Water',85,100,10),('Flip Turn','Water',60,100,20),('Freezing Glare','Psychic',90,100,10),('Glacial Lance','Ice',130,100,5),('Grassy Glide','Grass',70,100,20),('Grav Apple','Grass',80,100,10),('Headlong Rush','Ground',100,100,5),('Infernal Parade','Ghost',60,100,15),('Jaw Lock','Dark',80,100,10),('Lash Out','Dark',75,100,5),('Meteor Assault','Fighting',150,100,5),('Meteor Beam','Rock',120,90,10),('Misty Explosion','Fairy',100,100,5),('Mountain Gale','Ice',100,85,5),('Mystical Power ','Psychic',70,90,10),('Overdrive','Electric',80,100,10),('Poltergeist','Ghost',110,90,5),('Psyshield Bash','Psychic',70,90,10),('Pyro Ball','Fire',120,90,5),('Raging Fury','Fire',90,85,10),('Rising Voltage','Electric',70,100,20),('Sandsear Storm','Ground',95,80,5),('Scale Shot ','Dragon',25,90,20),('Scorching Sands','Ground',70,100,10),('Skitter Smack','Bug',70,90,10),('Snap Trap','Grass',35,100,15),('Snipe Shot','Water',80,100,15),('Spirit Break','Fairy',75,100,15),('Springtide Storm','Fairy',95,80,5),('Steel Beam','Steel',140,95,5),('Steel Roller','Steel',130,100,5),('Stone Axe','Rock',65,90,15),('Strange Steam','Fairy',90,95,10),('Thunder Cage','Electric',80,90,15),('Triple Arrows ','Fighting',50,100,15),('Thunderous Kick','Fighting',90,100,10),('Triple Axel','Ice',20,90,10),('Wave Crash','Water',75,100,10),('Victory Dance ','Fighting',0,0,10),('Wicked Blow','Dark',80,100,5),('Wildbolt Storm','Electric',95,80,5),('Shelter','Steel',0,0,10),('Decorate','Fairy',0,0,10),('Accelerock','Rock',40,100,20),('Burn Up','Fire',130,100,5),('Fleur Cannon','Fairy',130,90,5),('Nature\'s Madness','Fairy',0,90,10),('Diamond Storm','Rock',100,95,5),('Freeze-Dry','Ice',70,100,20);
/*!40000 ALTER TABLE `moves` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-30 18:22:58
