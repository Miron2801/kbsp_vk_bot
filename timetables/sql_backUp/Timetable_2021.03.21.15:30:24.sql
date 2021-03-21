-- MySQL dump 10.17  Distrib 10.3.25-MariaDB, for debian-linux-gnueabihf (armv7l)
--
-- Host: localhost    Database: timetable
-- ------------------------------------------------------
-- Server version	10.3.25-MariaDB-0+deb10u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `frases`
--

DROP TABLE IF EXISTS `frases`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `frases` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `frase` text COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `frases`
--

LOCK TABLES `frases` WRITE;
/*!40000 ALTER TABLE `frases` DISABLE KEYS */;
INSERT INTO `frases` VALUES (1,' ');
/*!40000 ALTER TABLE `frases` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ids`
--

DROP TABLE IF EXISTS `ids`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ids` (
  `id` int(11) DEFAULT NULL,
  `groups` text COLLATE utf8_unicode_ci NOT NULL,
  `vkid` text COLLATE utf8_unicode_ci NOT NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ids`
--

LOCK TABLES `ids` WRITE;
/*!40000 ALTER TABLE `ids` DISABLE KEYS */;
INSERT INTO `ids` VALUES (NULL,'ББСО-02-20','195266454'),(NULL,'ББСО-04-20','181257112'),(NULL,'ББСО-04-20','175178550'),(NULL,'ББСО-04-20','200487679'),(NULL,'ББСО-04-20','173203022'),(NULL,'ББСО-04-20','144698793'),(NULL,'ББСО-04-20','284455862'),(NULL,'БББО-07-20','298423546'),(NULL,'БСБО-18-20','137616768'),(NULL,'ББСО-02-20','140512311'),(NULL,'ББСО-03-20','460658372'),(NULL,'БПБО-02-20','354781331'),(NULL,'БИСО-01-20','316972306'),(NULL,'БСБО-14-20','520732083'),(NULL,'БСБО-01-20','145379412'),(NULL,'БАСО-05-20','214556671'),(NULL,'БСБО-08-20','467357090'),(NULL,'БАСО-05-20','289666409'),(NULL,'БСБО-01-20','471130764'),(NULL,'БАСО-05-20','358969355'),(NULL,'БАСО-05-20','315953793'),(NULL,'БСБО-01-20','151413977'),(NULL,'БСБО-18-20','352680694'),(NULL,'БСБО-18-20','150774879'),(NULL,'БСБО-18-20','264514006'),(NULL,'БСБО-18-20','168009412'),(NULL,'БСБО-01-20','305503046'),(NULL,'БСБО-18-20','235756185'),(NULL,'БСБО-04-20','306078605'),(NULL,'БСБО-18-20','262479155'),(NULL,'БСБО-10-20','637593527'),(NULL,'БСБО-10-20','429825127'),(NULL,'БСБО-18-20','481669099'),(NULL,'БСБО-10-20','227184764'),(NULL,'БСБО-10-20','150576010'),(NULL,'БСБО-10-20','384174279'),(NULL,'БАСО-05-20','226604486'),(NULL,'БСБО-18-20','237689591'),(NULL,'БСБО-18-20','197010408'),(NULL,'БАСО-05-20','197213194'),(NULL,'БББО-07-20','210505492'),(NULL,'ББСО-03-20','443274616'),(NULL,'БСБО-17-20','261932199'),(NULL,'БББО-04-20','303364101'),(NULL,'БОСО-02-20','203223324'),(NULL,'БСБО-10-20','70121061'),(NULL,'БАСО-05-20','170815917'),(NULL,'БОСО-02-20','509438711'),(NULL,'БОСО-02-20','332254345'),(NULL,'БОСО-02-20','199830431'),(NULL,'БОСО-02-20','343375218'),(NULL,'БОСО-02-20','341249748'),(NULL,'БОСО-02-20','159645565'),(NULL,'БОСО-01-20','636577956'),(NULL,'БОСО-02-20','287666324'),(NULL,'БЭСО-03-20','226418495'),(NULL,'БИСО-03-20','285705433'),(NULL,'БИСО-03-20','100212567'),(NULL,'БИСО-03-20','145513335'),(NULL,'БИСО-03-20','223970810'),(NULL,'БСБО-03-20','238749516'),(NULL,'БББО-05-20','178376068'),(NULL,'БПСО-01-20','246921673'),(NULL,'БПСО-01-20','280068258'),(NULL,'БИСО-03-20','235546330'),(NULL,'БСБО-03-20','220020101'),(NULL,'БББО-06-20','456137315'),(NULL,'БОСО-02-20','216957700'),(NULL,'БПСО-01-20','547044437'),(NULL,'ББСО-03-20','270813249'),(NULL,'БОСО-02-20','300388817'),(NULL,'БЭСО-03-20','207907853'),(NULL,'БЭСО-03-20','142943815'),(NULL,'БЭСО-03-20','151106478'),(NULL,'БЭСО-03-20','313977659'),(NULL,'БЭСО-03-20','155295337'),(NULL,'БОСО-02-20','184311978'),(NULL,'БОСО-02-20','395928523'),(NULL,'БЭСО-03-20','496952506'),(NULL,'ББСО-03-20','309822445'),(NULL,'БЭСО-03-20','485353386'),(NULL,'БИСО-03-20','264060736'),(NULL,'ББСО-04-20','252034845'),(NULL,'БСБО-03-20','138248141'),(NULL,'БЭСО-03-20','174399047'),(NULL,'ББСО-04-20','274718907'),(NULL,'ББСО-02-20','92813414'),(NULL,'БЭСО-03-20','284062262'),(NULL,'ББСО-03-20','228387299'),(NULL,'БЭСО-03-20','382018822'),(NULL,'БОСО-02-20','176183358'),(NULL,'БЭСО-03-20','44833659'),(NULL,'БЭСО-03-20','424351466'),(NULL,'ББСО-01-20','331970828'),(NULL,'БСБО-03-20','106449503'),(NULL,'БАСО-02-20','182379196'),(NULL,'БПСО-01-20','123510429'),(NULL,'БПСО-01-20','386755209'),(NULL,'БББО-09-20','168578431'),(NULL,'БИСО-03-20','241361839'),(NULL,'БЭСО-01-20','212011352'),(NULL,'БЭСО-03-20','256575792'),(NULL,'ББСО-04-20','88706899'),(NULL,'БАСО-02-20','131707141'),(NULL,'БББО-09-20','135229867'),(NULL,'БББО-09-20','187126431'),(NULL,'БББО-07-20','517201222'),(NULL,'БПСО-01-20','247851627'),(NULL,'БББО-09-20','216308670'),(NULL,'ББСО-04-20','243599077'),(NULL,'БСБО-10-20','612319770'),(NULL,'ББСО-03-20','599904582'),(NULL,'ББСО-04-20','620682424'),(NULL,'БББО-06-20','512498731'),(NULL,'БББО-06-20','368541022'),(NULL,'БББО-06-20','234649545'),(NULL,'БОСО-02-20','441010953'),(NULL,'БСБО-03-20','141369909'),(NULL,'БСБО-03-20','194121831'),(NULL,'БПСО-01-20','324520388'),(NULL,'БББО-07-20','161946374'),(NULL,'БОСО-02-20','383779399'),(NULL,'БББО-09-20','167008363'),(NULL,'БОСО-02-20','268973687'),(NULL,'БПСО-01-20','250573253'),(NULL,'ББСО-04-20','448898033'),(NULL,'БСБО-04-20','212530911'),(NULL,'БЭСО-03-20','152119972'),(NULL,'БББО-09-20','350330748'),(NULL,'БББО-09-20','251721968');
/*!40000 ALTER TABLE `ids` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notification`
--

DROP TABLE IF EXISTS `notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `notification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vk_id` int(11) NOT NULL,
  `is_notifications_assepted` int(11) NOT NULL,
  `study_group` text COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notification`
--

LOCK TABLES `notification` WRITE;
/*!40000 ALTER TABLE `notification` DISABLE KEYS */;
INSERT INTO `notification` VALUES (46,274718907,1,'ББСО-04-20'),(47,350330748,1,'БББО-09-20'),(50,448898033,1,'ББСО-04-20'),(52,144698793,1,'ББСО-04-20'),(53,151413977,1,'БСБО-01-20'),(54,123510429,1,'БПСО-01-20'),(55,131707141,1,'БАСО-02-20'),(57,200487679,1,'ББСО-04-20'),(58,210505492,1,'БББО-07-20'),(59,517201222,1,'БББО-07-20'),(60,300388817,1,'БОСО-02-20'),(61,243599077,1,'ББСО-04-20'),(63,145379412,1,'БСБО-01-20'),(64,620682424,1,''),(66,309822445,1,'ББСО-03-20'),(67,161946374,1,'БББО-07-20'),(68,268973687,1,'БОСО-02-20'),(74,251721968,1,'ББСО-04-20');
/*!40000 ALTER TABLE `notification` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-21 15:30:24
