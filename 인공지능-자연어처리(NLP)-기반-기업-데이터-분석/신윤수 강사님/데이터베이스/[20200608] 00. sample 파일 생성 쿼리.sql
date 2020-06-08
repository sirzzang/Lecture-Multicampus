-- MySQL dump 10.13  Distrib 5.6.23, for Win32 (x86)
--
-- Host: localhost    Database: sample
-- ------------------------------------------------------
-- Server version	5.6.23-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `sample`
--

DROP DATABASE IF EXISTS `sample`;

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `sample` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `sample`;

--
-- Table structure for table `메이커`
--

DROP TABLE IF EXISTS `메이커`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `메이커` (
  `메이커코드` char(4) NOT NULL,
  `메이커명` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`메이커코드`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `메이커`
--

LOCK TABLES `메이커` WRITE;
/*!40000 ALTER TABLE `메이커` DISABLE KEYS */;
INSERT INTO `메이커` VALUES ('M001','메이커1'),('M002','메이커2');
/*!40000 ALTER TABLE `메이커` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `상품`
--

DROP TABLE IF EXISTS `상품`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `상품` (
  `상품코드` char(4) NOT NULL,
  `상품명` varchar(30) DEFAULT NULL,
  `메이커명` varchar(30) DEFAULT NULL,
  `가격` int(11) DEFAULT NULL,
  `상품분류` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`상품코드`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `상품`
--

LOCK TABLES `상품` WRITE;
/*!40000 ALTER TABLE `상품` DISABLE KEYS */;
INSERT INTO `상품` VALUES ('0001','상품1','메이커1',100,'식료품'),('0002','상품2','메이커2',200,'식료품'),('0003','상품3','메이커3',1980,'생활용품');
/*!40000 ALTER TABLE `상품` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `상품2`
--

DROP TABLE IF EXISTS `상품2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `상품2` (
  `상품코드` char(4) NOT NULL,
  `상품명` varchar(30) DEFAULT NULL,
  `메이커코드` char(4) DEFAULT NULL,
  `가격` int(11) DEFAULT NULL,
  `상품분류` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`상품코드`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `상품2`
--

LOCK TABLES `상품2` WRITE;
/*!40000 ALTER TABLE `상품2` DISABLE KEYS */;
INSERT INTO `상품2` VALUES ('0001','상품1','M001',100,'식료품'),('0002','상품2','M001',200,'식료품'),('0003','상품3','M002',1980,'생활용품');
/*!40000 ALTER TABLE `상품2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `상품3`
--

DROP TABLE IF EXISTS `상품3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `상품3` (
  `상품코드` char(4) NOT NULL,
  `상품명` varchar(30) DEFAULT NULL,
  `메이커코드` char(4) DEFAULT NULL,
  `가격` int(11) DEFAULT NULL,
  `상품분류` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`상품코드`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `상품3`
--

LOCK TABLES `상품3` WRITE;
/*!40000 ALTER TABLE `상품3` DISABLE KEYS */;
INSERT INTO `상품3` VALUES ('0001','상품1','M001',100,'식료품'),('0002','상품2','M001',200,'식료품'),('0003','상품3','M002',1980,'생활용품'),('0009','추가상품','M001',300,'식료품');
/*!40000 ALTER TABLE `상품3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `재고수`
--

DROP TABLE IF EXISTS `재고수`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `재고수` (
  `상품코드` char(4) DEFAULT NULL,
  `입고일` date DEFAULT NULL,
  `재고수` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `재고수`
--

LOCK TABLES `재고수` WRITE;
/*!40000 ALTER TABLE `재고수` DISABLE KEYS */;
INSERT INTO `재고수` VALUES ('0001','2014-01-03',200),('0002','2014-02-10',500),('0003','2014-02-14',10);
/*!40000 ALTER TABLE `재고수` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample21`
--

DROP TABLE IF EXISTS `sample21`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample21` (
  `no` int(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `address` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample21`
--

LOCK TABLES `sample21` WRITE;
/*!40000 ALTER TABLE `sample21` DISABLE KEYS */;
INSERT INTO `sample21` VALUES (1,'박준용','1976-10-18','대구광역시 수성구'),(2,'김재진',NULL,'대구광역시 동구'),(3,'홍길동',NULL,'서울특별시 마포구');
/*!40000 ALTER TABLE `sample21` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample24`
--

DROP TABLE IF EXISTS `sample24`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample24` (
  `no` int(11) DEFAULT NULL,
  `a` int(11) DEFAULT NULL,
  `b` int(11) DEFAULT NULL,
  `c` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample24`
--

LOCK TABLES `sample24` WRITE;
/*!40000 ALTER TABLE `sample24` DISABLE KEYS */;
INSERT INTO `sample24` VALUES (1,1,0,0),(2,0,1,0),(3,0,0,1),(4,2,2,0),(5,0,2,2);
/*!40000 ALTER TABLE `sample24` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample25`
--

DROP TABLE IF EXISTS `sample25`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample25` (
  `no` int(11) DEFAULT NULL,
  `text` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample25`
--

LOCK TABLES `sample25` WRITE;
/*!40000 ALTER TABLE `sample25` DISABLE KEYS */;
INSERT INTO `sample25` VALUES (1,'SQL은 RDBMS를 조작하기 위한 언어이다.'),(2,'LIKE에서는 메타문자 %와 _를 사용할 수 있다.'),(3,'LIKE는 SQL에서 사용할 수 있는 술어 중 하나이다.');
/*!40000 ALTER TABLE `sample25` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample31`
--

DROP TABLE IF EXISTS `sample31`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample31` (
  `name` varchar(20) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `address` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample31`
--

LOCK TABLES `sample31` WRITE;
/*!40000 ALTER TABLE `sample31` DISABLE KEYS */;
INSERT INTO `sample31` VALUES ('A씨',36,'대구광역시 중구'),('B씨',18,'부산광역시 연제구'),('C씨',25,'서울특별시 중구');
/*!40000 ALTER TABLE `sample31` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample311`
--

DROP TABLE IF EXISTS `sample311`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample311` (
  `a` varchar(2) DEFAULT NULL,
  `b` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample311`
--

LOCK TABLES `sample311` WRITE;
/*!40000 ALTER TABLE `sample311` DISABLE KEYS */;
INSERT INTO `sample311` VALUES ('1',1),('2',2),('10',10),('11',11);
/*!40000 ALTER TABLE `sample311` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample32`
--

DROP TABLE IF EXISTS `sample32`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample32` (
  `a` int(11) DEFAULT NULL,
  `b` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample32`
--

LOCK TABLES `sample32` WRITE;
/*!40000 ALTER TABLE `sample32` DISABLE KEYS */;
INSERT INTO `sample32` VALUES (1,1),(2,1),(2,2),(1,3),(1,2);
/*!40000 ALTER TABLE `sample32` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample33`
--

DROP TABLE IF EXISTS `sample33`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample33` (
  `no` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample33`
--

LOCK TABLES `sample33` WRITE;
/*!40000 ALTER TABLE `sample33` DISABLE KEYS */;
INSERT INTO `sample33` VALUES (1),(2),(3),(4),(5),(6),(7);
/*!40000 ALTER TABLE `sample33` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample34`
--

DROP TABLE IF EXISTS `sample34`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample34` (
  `no` int(11) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample34`
--

LOCK TABLES `sample34` WRITE;
/*!40000 ALTER TABLE `sample34` DISABLE KEYS */;
INSERT INTO `sample34` VALUES (1,100,10),(2,230,24),(3,1980,1);
/*!40000 ALTER TABLE `sample34` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample341`
--

DROP TABLE IF EXISTS `sample341`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample341` (
  `amount` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample341`
--

LOCK TABLES `sample341` WRITE;
/*!40000 ALTER TABLE `sample341` DISABLE KEYS */;
INSERT INTO `sample341` VALUES (5961.60),(2138.40),(1080.00);
/*!40000 ALTER TABLE `sample341` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample35`
--

DROP TABLE IF EXISTS `sample35`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample35` (
  `no` int(11) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `unit` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample35`
--

LOCK TABLES `sample35` WRITE;
/*!40000 ALTER TABLE `sample35` DISABLE KEYS */;
INSERT INTO `sample35` VALUES (1,100,10,'개'),(2,230,24,'통'),(3,1980,1,'장');
/*!40000 ALTER TABLE `sample35` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample37`
--

DROP TABLE IF EXISTS `sample37`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample37` (
  `a` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample37`
--

LOCK TABLES `sample37` WRITE;
/*!40000 ALTER TABLE `sample37` DISABLE KEYS */;
INSERT INTO `sample37` VALUES (1),(2),(NULL);
/*!40000 ALTER TABLE `sample37` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample41`
--

DROP TABLE IF EXISTS `sample41`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample41` (
  `no` int(11) NOT NULL,
  `a` varchar(30) DEFAULT NULL,
  `b` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample41`
--

LOCK TABLES `sample41` WRITE;
/*!40000 ALTER TABLE `sample41` DISABLE KEYS */;
/*!40000 ALTER TABLE `sample41` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample411`
--

DROP TABLE IF EXISTS `sample411`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample411` (
  `no` int(11) NOT NULL,
  `d` int(11) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample411`
--

LOCK TABLES `sample411` WRITE;
/*!40000 ALTER TABLE `sample411` DISABLE KEYS */;
/*!40000 ALTER TABLE `sample411` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample51`
--

DROP TABLE IF EXISTS `sample51`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample51` (
  `no` int(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample51`
--

LOCK TABLES `sample51` WRITE;
/*!40000 ALTER TABLE `sample51` DISABLE KEYS */;
INSERT INTO `sample51` VALUES (1,'A',1),(2,'A',2),(3,'B',10),(4,'C',3),(5,NULL,NULL);
/*!40000 ALTER TABLE `sample51` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample54`
--

DROP TABLE IF EXISTS `sample54`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample54` (
  `no` int(11) DEFAULT NULL,
  `a` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample54`
--

LOCK TABLES `sample54` WRITE;
/*!40000 ALTER TABLE `sample54` DISABLE KEYS */;
INSERT INTO `sample54` VALUES (1,100),(2,900),(3,20),(4,80);
/*!40000 ALTER TABLE `sample54` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample541`
--

DROP TABLE IF EXISTS `sample541`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample541` (
  `a` int(11) DEFAULT NULL,
  `b` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample541`
--

LOCK TABLES `sample541` WRITE;
/*!40000 ALTER TABLE `sample541` DISABLE KEYS */;
/*!40000 ALTER TABLE `sample541` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample551`
--

DROP TABLE IF EXISTS `sample551`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample551` (
  `no` int(11) DEFAULT NULL,
  `a` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample551`
--

LOCK TABLES `sample551` WRITE;
/*!40000 ALTER TABLE `sample551` DISABLE KEYS */;
INSERT INTO `sample551` VALUES (1,NULL),(2,NULL),(3,NULL),(4,NULL),(5,NULL);
/*!40000 ALTER TABLE `sample551` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample552`
--

DROP TABLE IF EXISTS `sample552`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample552` (
  `no2` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample552`
--

LOCK TABLES `sample552` WRITE;
/*!40000 ALTER TABLE `sample552` DISABLE KEYS */;
INSERT INTO `sample552` VALUES (3),(5);
/*!40000 ALTER TABLE `sample552` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample635`
--

DROP TABLE IF EXISTS `sample635`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample635` (
  `a` int(11) NOT NULL,
  `b` int(11) NOT NULL,
  PRIMARY KEY (`a`,`b`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample635`
--

LOCK TABLES `sample635` WRITE;
/*!40000 ALTER TABLE `sample635` DISABLE KEYS */;
INSERT INTO `sample635` VALUES (1,1),(1,2),(1,3),(2,1),(2,2);
/*!40000 ALTER TABLE `sample635` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample71_a`
--

DROP TABLE IF EXISTS `sample71_a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample71_a` (
  `a` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample71_a`
--

LOCK TABLES `sample71_a` WRITE;
/*!40000 ALTER TABLE `sample71_a` DISABLE KEYS */;
INSERT INTO `sample71_a` VALUES (1),(2),(3);
/*!40000 ALTER TABLE `sample71_a` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample71_b`
--

DROP TABLE IF EXISTS `sample71_b`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample71_b` (
  `b` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample71_b`
--

LOCK TABLES `sample71_b` WRITE;
/*!40000 ALTER TABLE `sample71_b` DISABLE KEYS */;
INSERT INTO `sample71_b` VALUES (2),(10),(11);
/*!40000 ALTER TABLE `sample71_b` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample72_x`
--

DROP TABLE IF EXISTS `sample72_x`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample72_x` (
  `x` varchar(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample72_x`
--

LOCK TABLES `sample72_x` WRITE;
/*!40000 ALTER TABLE `sample72_x` DISABLE KEYS */;
INSERT INTO `sample72_x` VALUES ('A'),('B'),('C');
/*!40000 ALTER TABLE `sample72_x` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample72_y`
--

DROP TABLE IF EXISTS `sample72_y`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample72_y` (
  `y` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample72_y`
--

LOCK TABLES `sample72_y` WRITE;
/*!40000 ALTER TABLE `sample72_y` DISABLE KEYS */;
INSERT INTO `sample72_y` VALUES (1),(2),(3);
/*!40000 ALTER TABLE `sample72_y` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-02-21 11:46:34
