-- MySQL dump 10.13  Distrib 8.0.30, for Linux (x86_64)
--
-- Host: localhost    Database: LojaSuplementos
-- ------------------------------------------------------
-- Server version	8.0.30-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `suplementos`
--

DROP TABLE IF EXISTS `suplementos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suplementos` (
  `id_sup` int NOT NULL AUTO_INCREMENT,
  `descricao` varchar(50) NOT NULL,
  `estoque` int NOT NULL,
  `valor` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id_sup`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suplementos`
--

LOCK TABLES `suplementos` WRITE;
/*!40000 ALTER TABLE `suplementos` DISABLE KEYS */;
INSERT INTO `suplementos` VALUES (1,'BCAA em pó, 500g sabor tangerina',20,50.66),(2,'Whey Protein 1kg, sabor baunilha',30,108.99),(3,'Multivitaminico, 120 cápsulas',40,60.89),(4,'Creatina 300g',30,79.99),(5,'Albumina em pó, 1kg',30,70.00),(6,'Glutamina 500g, sabor limão',40,69.99),(7,'Whey Protein 2kg, sabor limão',30,189.99),(8,'Whey Protein 1kg, sabor morango',35,108.99),(12,'L-Carnitina, 100 cápsulas',50,49.90),(13,'Barrinha de proteína sabor chocolate',50,8.99),(14,'Barrinha de proteína sabor baunilha',50,8.99),(17,'Barrinha de proteína sabor café',50,8.99),(26,'Termogênico - 420mg de cafeína, 60 cápsulas',35,52.99);
/*!40000 ALTER TABLE `suplementos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-29 13:17:57
