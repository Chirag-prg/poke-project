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
-- Table structure for table `poke`
--

DROP TABLE IF EXISTS `poke`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `poke` (
  `NAME` varchar(20) NOT NULL,
  `TYPE` varchar(20) NOT NULL,
  `HP` int NOT NULL,
  `ATTK` int NOT NULL,
  `DEF` int NOT NULL,
  `SPA` int NOT NULL,
  `SPD` int NOT NULL,
  `SPE` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `poke`
--

LOCK TABLES `poke` WRITE;
/*!40000 ALTER TABLE `poke` DISABLE KEYS */;
INSERT INTO `poke` VALUES ('Rillaboom','Grass',100,125,90,60,70,85),('Cinderace','Fire',80,116,75,65,75,119),('Ineteleon','Water',70,85,65,125,65,120),('Corviknight','Flying,Steel',98,87,105,53,85,67),('Orbeetle','Bug,Psychic',60,45,119,80,120,90),('Thievul','Dark',70,58,58,87,92,90),('Eldegoss','Grass',60,50,90,80,120,60),('Drednaw','Water,Rock',90,115,90,48,68,74),('Boltund','Electric',69,90,60,90,60,121),('Coalassal','Rock,Fire',110,80,120,80,90,30),('Appletun','Grass,Dragon',110,85,80,100,80,30),('Sandaconda','Ground',72,107,125,65,70,71),('Cramorant','Flying,Water',70,85,55,85,95,85),('Barraskewda','Water',61,123,60,60,50,136),('Toxtricity','Electric,Poison',75,98,70,114,70,75),('Centiskorch','Fire,Bug',100,115,65,90,90,65),('Grapploct','Fighting',80,118,90,70,80,42),('Polterageist','Ghost',60,65,65,134,114,70),('Hatterene','Psychic,Fairy',57,90,95,136,103,29),('Obstagoon','Dark,Normal',93,90,101,60,81,95),('Mr. Rime','Ice,Psychic',80,85,75,110,100,70),('Falinks','Fighting',65,100,100,70,60,75),('Pinchurchin','Electric',48,101,95,91,85,15),('Frosmoth','Ice,Bug',70,65,60,125,90,65),('Stonjourner','Rock',100,125,135,20,20,70),('Eiscue','Ice',75,80,110,65,90,50),('Indeedee','Psychic,Normal',60,65,55,105,95,95),('Morpeko','Electric,Dark',58,95,58,70,58,97),('Copperajah','Steel',122,130,69,80,69,30),('Dracovish','Water,Dragon',90,90,100,70,80,75),('Duraludon','Steel,Dragon',70,95,115,120,50,85),('Zacian','Fairy',92,130,115,80,115,138),('Eternatus','Poison,Dragon',140,85,95,145,95,130),('Urshifu','Fighting,Dark',100,130,100,63,60,97),('Zarude','Dark,Grass',105,120,105,70,95,105),('Regieleki','Electric',80,100,50,100,50,200),('Regidrago','Dragon',200,100,50,100,50,80),('Calyrex','Psychic,Grass',100,80,80,80,80,80),('Spectrier','Ghost',100,65,60,145,80,130);
/*!40000 ALTER TABLE `poke` ENABLE KEYS */;
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
