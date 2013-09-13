USE tomnz_kapai

-- MySQL dump 10.13  Distrib 5.1.33, for Win32 (ia32)
--
-- Host: localhost    Database: tomnz_kapaidj
-- ------------------------------------------------------
-- Server version	5.1.33-community

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `permission_id_refs_id_5886d21f` (`permission_id`),
  CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_5886d21f` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_message`
--

DROP TABLE IF EXISTS `auth_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `auth_message_user_id` (`user_id`),
  CONSTRAINT `user_id_refs_id_650f49a6` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_message`
--

LOCK TABLES `auth_message` WRITE;
/*!40000 ALTER TABLE `auth_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add message',4,'add_message'),(11,'Can change message',4,'change_message'),(12,'Can delete message',4,'delete_message'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add site',6,'add_site'),(17,'Can change site',6,'change_site'),(18,'Can delete site',6,'delete_site'),(19,'Can add log entry',7,'add_logentry'),(20,'Can change log entry',7,'change_logentry'),(21,'Can delete log entry',7,'delete_logentry'),(22,'Can add news item',8,'add_newsitem'),(23,'Can change news item',8,'change_newsitem'),(24,'Can delete news item',8,'delete_newsitem'),(25,'Can add instance',9,'add_instance'),(26,'Can change instance',9,'change_instance'),(27,'Can delete instance',9,'delete_instance'),(28,'Can add boss',10,'add_boss'),(29,'Can change boss',10,'change_boss'),(30,'Can delete boss',10,'delete_boss'),(31,'Can add boss detail',11,'add_bossdetail'),(32,'Can change boss detail',11,'change_bossdetail'),(33,'Can delete boss detail',11,'delete_bossdetail'),(34,'Can add session',12,'add_session'),(35,'Can change session',12,'change_session'),(36,'Can delete session',12,'delete_session'),(37,'Can add redirect',13,'add_redirect'),(38,'Can change redirect',13,'change_redirect'),(39,'Can delete redirect',13,'delete_redirect'),(40,'Can add recruitment class',14,'add_recruitmentclass'),(41,'Can change recruitment class',14,'change_recruitmentclass'),(42,'Can delete recruitment class',14,'delete_recruitmentclass'),(43,'Can add gallery',15,'add_gallery'),(44,'Can change gallery',15,'change_gallery'),(45,'Can delete gallery',15,'delete_gallery'),(46,'Can add gallery item',16,'add_galleryitem'),(47,'Can change gallery item',16,'change_galleryitem'),(48,'Can delete gallery item',16,'delete_galleryitem'),(49,'Can add migration history',17,'add_migrationhistory'),(50,'Can change migration history',17,'change_migrationhistory'),(51,'Can delete migration history',17,'delete_migrationhistory'),(52,'Can add phpbb user',18,'add_phpbbuser'),(53,'Can change phpbb user',18,'change_phpbbuser'),(54,'Can delete phpbb user',18,'delete_phpbbuser'),(55,'Can add django phpbb user mapping',19,'add_djangophpbbusermapping'),(56,'Can change django phpbb user mapping',19,'change_djangophpbbusermapping'),(57,'Can delete django phpbb user mapping',19,'delete_djangophpbbusermapping'),(58,'Can add phpbb forum',20,'add_phpbbforum'),(59,'Can change phpbb forum',20,'change_phpbbforum'),(60,'Can delete phpbb forum',20,'delete_phpbbforum'),(61,'Can add phpbb topic',21,'add_phpbbtopic'),(62,'Can change phpbb topic',21,'change_phpbbtopic'),(63,'Can delete phpbb topic',21,'delete_phpbbtopic'),(64,'Can add phpbb post',22,'add_phpbbpost'),(65,'Can change phpbb post',22,'change_phpbbpost'),(66,'Can delete phpbb post',22,'delete_phpbbpost'),(67,'Can add phpbb group',23,'add_phpbbgroup'),(68,'Can change phpbb group',23,'change_phpbbgroup'),(69,'Can delete phpbb group',23,'delete_phpbbgroup'),(70,'Can add phpbb acl role',24,'add_phpbbaclrole'),(71,'Can change phpbb acl role',24,'change_phpbbaclrole'),(72,'Can delete phpbb acl role',24,'delete_phpbbaclrole'),(73,'Can add phpbb acl option',25,'add_phpbbacloption'),(74,'Can change phpbb acl option',25,'change_phpbbacloption'),(75,'Can delete phpbb acl option',25,'delete_phpbbacloption'),(76,'Can add Phpbb config entry',26,'add_phpbbconfig'),(77,'Can change Phpbb config entry',26,'change_phpbbconfig'),(78,'Can delete Phpbb config entry',26,'delete_phpbbconfig');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'admin','','','admin@kapaiguild.com','sha1$c1c88$01dfc03d51c03b2a856a5fd1799c5f3669fd0bab',1,1,1,'2009-09-30 16:25:44','2009-07-30 14:01:15');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `group_id_refs_id_f116770` (`group_id`),
  CONSTRAINT `group_id_refs_id_f116770` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_7ceef80f` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `permission_id_refs_id_67e79cb` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_dfbab7d` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_user_id` (`user_id`),
  KEY `django_admin_log_content_type_id` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_288599e6` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c8665aa` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2009-07-30 14:58:47',1,9,'1','Ulduar 25',1,''),(2,'2009-07-30 14:58:57',1,9,'2','Ulduar 10',1,''),(3,'2009-07-30 14:59:09',1,9,'3','Naxx 25',1,''),(4,'2009-07-30 14:59:18',1,9,'4','Naxx 10',1,''),(5,'2009-07-30 15:00:07',1,10,'1','Flame Leviathan',1,''),(6,'2009-07-30 15:00:29',1,10,'2','Razorscale',1,''),(7,'2009-07-30 15:00:47',1,10,'3','Flame Leviathan',1,''),(8,'2009-07-30 15:01:23',1,10,'4','Anub\'rekhan',1,''),(9,'2009-07-30 15:01:44',1,10,'5','Anub\'rekhan',1,''),(10,'2009-07-30 15:02:30',1,11,'1','1 Tower',1,''),(11,'2009-07-30 15:02:46',1,11,'2','2 Towers',1,''),(12,'2009-07-30 15:03:04',1,11,'3','3 Towers',1,''),(13,'2009-07-30 15:04:11',1,11,'4','1 Tower',1,''),(14,'2009-07-30 15:04:27',1,11,'5','2 Towers',1,''),(15,'2009-07-30 15:04:43',1,11,'6','3 Towers',1,''),(16,'2009-07-30 15:58:13',1,8,'1','Test news item',1,''),(17,'2009-07-31 13:57:26',1,10,'2','Razorscale (Ulduar 25)',2,'Changed active.'),(18,'2009-07-31 13:57:47',1,10,'2','Razorscale (Ulduar 25)',2,'Changed ordering and active.'),(19,'2009-08-03 16:26:46',1,14,'1','Death Knight',1,''),(20,'2009-08-03 16:27:00',1,14,'2','Druid',1,''),(21,'2009-08-03 16:27:10',1,14,'3','Hunter',1,''),(22,'2009-08-03 16:27:21',1,14,'4','Mage',1,''),(23,'2009-08-03 16:27:33',1,14,'5','Paladin',1,''),(24,'2009-08-03 16:27:44',1,14,'6','Priest',1,''),(25,'2009-08-03 16:27:56',1,14,'7','Rogue',1,''),(26,'2009-09-30 13:05:54',1,15,'1','Test Gallery',1,'');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'message','auth','message'),(5,'content type','contenttypes','contenttype'),(6,'site','sites','site'),(7,'log entry','admin','logentry'),(8,'news item','index','newsitem'),(9,'instance','progression','instance'),(10,'boss','progression','boss'),(11,'boss detail','progression','bossdetail'),(12,'session','sessions','session'),(13,'redirect','redirects','redirect'),(14,'recruitment class','recruitment','recruitmentclass'),(15,'gallery','gallery','gallery'),(16,'gallery item','gallery','galleryitem'),(17,'migration history','south','migrationhistory'),(18,'phpbb user','phpbb','phpbbuser'),(19,'django phpbb user mapping','phpbb','djangophpbbusermapping'),(20,'phpbb forum','phpbb','phpbbforum'),(21,'phpbb topic','phpbb','phpbbtopic'),(22,'phpbb post','phpbb','phpbbpost'),(23,'phpbb group','phpbb','phpbbgroup'),(24,'phpbb acl role','phpbb','phpbbaclrole'),(25,'phpbb acl option','phpbb','phpbbacloption'),(26,'Phpbb config entry','phpbb','phpbbconfig');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_redirect`
--

DROP TABLE IF EXISTS `django_redirect`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_redirect` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `site_id` int(11) NOT NULL,
  `old_path` varchar(200) NOT NULL,
  `new_path` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `site_id` (`site_id`,`old_path`),
  KEY `django_redirect_site_id` (`site_id`),
  KEY `django_redirect_old_path` (`old_path`),
  CONSTRAINT `site_id_refs_id_4aa27aa6` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_redirect`
--

LOCK TABLES `django_redirect` WRITE;
/*!40000 ALTER TABLE `django_redirect` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_redirect` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('055068ed6cc3be55189fc51cd65d2d45','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS5kNjMyZDhhNGI0MzAzNDQ5YzNh\nNGI3ZmY5NmI3NGI5NA==\n','2009-10-14 16:25:44'),('11f6b0532d242ed78b24c6ea0c43d963','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS5kNjMyZDhhNGI0MzAzNDQ5YzNh\nNGI3ZmY5NmI3NGI5NA==\n','2009-08-13 14:57:25'),('f45df63ac6322e78eae5390473bbc63b','gAJ9cQFVCnRlc3Rjb29raWVxAlUGd29ya2VkcQNzLmNmYjU4MDQ4ODczNzE3NjNhYTJmZDc3ZDRh\nZWNlNGI2\n','2010-07-08 15:19:56');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gallery_gallery`
--

DROP TABLE IF EXISTS `gallery_gallery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gallery_gallery` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `created_date` date DEFAULT NULL,
  `ordering` int(11) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `slug` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gallery_gallery`
--

LOCK TABLES `gallery_gallery` WRITE;
/*!40000 ALTER TABLE `gallery_gallery` DISABLE KEYS */;
INSERT INTO `gallery_gallery` VALUES (1,'Test Gallery','2009-09-30',100,1,'test');
/*!40000 ALTER TABLE `gallery_gallery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gallery_galleryitem`
--

DROP TABLE IF EXISTS `gallery_galleryitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gallery_galleryitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gallery_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `uploaded_date` date DEFAULT NULL,
  `image_url` varchar(200) NOT NULL,
  `thumb_url` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `ordering` int(11) NOT NULL,
  `active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `gallery_galleryitem_gallery_id` (`gallery_id`),
  CONSTRAINT `gallery_id_refs_id_605febb2` FOREIGN KEY (`gallery_id`) REFERENCES `gallery_gallery` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gallery_galleryitem`
--

LOCK TABLES `gallery_galleryitem` WRITE;
/*!40000 ALTER TABLE `gallery_galleryitem` DISABLE KEYS */;
INSERT INTO `gallery_galleryitem` VALUES (1,1,'Test','2009-09-30','img/gallery/aa40af3b_650_600.jpg','img/gallery/aa40af3b_100_80.jpg','Test',100,1),(2,1,'Test2','2009-09-30','img/gallery/93a51f1c_650_600.jpg','img/gallery/93a51f1c_100_80.jpg','This is a cool photo lol',100,1);
/*!40000 ALTER TABLE `gallery_galleryitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_newsitem`
--

DROP TABLE IF EXISTS `index_newsitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `index_newsitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `when_published` datetime NOT NULL,
  `active` tinyint(1) NOT NULL,
  `body` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_newsitem`
--

LOCK TABLES `index_newsitem` WRITE;
/*!40000 ALTER TABLE `index_newsitem` DISABLE KEYS */;
INSERT INTO `index_newsitem` VALUES (1,'Test news item','2009-07-30 15:57:52',1,'<p>Test news item</p>\r\n<p>Ipsum dolor etc</p>');
/*!40000 ALTER TABLE `index_newsitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phpbb3_acl_options`
--

DROP TABLE IF EXISTS `phpbb3_acl_options`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phpbb3_acl_options` (
  `auth_option_id` int(11) NOT NULL,
  `auth_option` varchar(60) NOT NULL,
  `is_global` int(11) NOT NULL,
  `is_local` int(11) NOT NULL,
  `founder_only` int(11) NOT NULL,
  PRIMARY KEY (`auth_option_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phpbb3_acl_options`
--

LOCK TABLES `phpbb3_acl_options` WRITE;
/*!40000 ALTER TABLE `phpbb3_acl_options` DISABLE KEYS */;
/*!40000 ALTER TABLE `phpbb3_acl_options` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phpbb3_acl_roles`
--

DROP TABLE IF EXISTS `phpbb3_acl_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phpbb3_acl_roles` (
  `role_id` int(11) NOT NULL,
  `role_name` varchar(255) NOT NULL,
  `role_description` longtext NOT NULL,
  `role_type` varchar(10) NOT NULL,
  `role_order` int(11) NOT NULL,
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phpbb3_acl_roles`
--

LOCK TABLES `phpbb3_acl_roles` WRITE;
/*!40000 ALTER TABLE `phpbb3_acl_roles` DISABLE KEYS */;
/*!40000 ALTER TABLE `phpbb3_acl_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phpbb3_config`
--

DROP TABLE IF EXISTS `phpbb3_config`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phpbb3_config` (
  `config_name` varchar(255) NOT NULL,
  `config_value` varchar(255) NOT NULL,
  `is_dynamic` int(11) NOT NULL,
  PRIMARY KEY (`config_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phpbb3_config`
--

LOCK TABLES `phpbb3_config` WRITE;
/*!40000 ALTER TABLE `phpbb3_config` DISABLE KEYS */;
/*!40000 ALTER TABLE `phpbb3_config` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phpbb3_forums`
--

DROP TABLE IF EXISTS `phpbb3_forums`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phpbb3_forums` (
  `forum_id` int(11) NOT NULL,
  `forum_name` varchar(60) NOT NULL,
  `forum_topics` int(11) NOT NULL,
  `forum_posts` int(11) NOT NULL,
  `forum_last_post_id` int(11) NOT NULL,
  `forum_desc` longtext NOT NULL,
  `parent_id` int(11) NOT NULL,
  `left_id` int(11) NOT NULL,
  `right_id` int(11) NOT NULL,
  PRIMARY KEY (`forum_id`),
  UNIQUE KEY `forum_last_post_id` (`forum_last_post_id`),
  UNIQUE KEY `left_id` (`left_id`),
  UNIQUE KEY `right_id` (`right_id`),
  KEY `phpbb3_forums_63f17a16` (`parent_id`),
  CONSTRAINT `forum_last_post_id_refs_post_id_6358767` FOREIGN KEY (`forum_last_post_id`) REFERENCES `phpbb3_posts` (`post_id`),
  CONSTRAINT `left_id_refs_forum_id_3b34c033` FOREIGN KEY (`left_id`) REFERENCES `phpbb3_forums` (`forum_id`),
  CONSTRAINT `parent_id_refs_forum_id_3b34c033` FOREIGN KEY (`parent_id`) REFERENCES `phpbb3_forums` (`forum_id`),
  CONSTRAINT `right_id_refs_forum_id_3b34c033` FOREIGN KEY (`right_id`) REFERENCES `phpbb3_forums` (`forum_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phpbb3_forums`
--

LOCK TABLES `phpbb3_forums` WRITE;
/*!40000 ALTER TABLE `phpbb3_forums` DISABLE KEYS */;
/*!40000 ALTER TABLE `phpbb3_forums` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phpbb3_groups`
--

DROP TABLE IF EXISTS `phpbb3_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phpbb3_groups` (
  `group_id` int(11) NOT NULL,
  `group_type` int(11) NOT NULL,
  `group_founder_manage` int(11) NOT NULL,
  `group_name` varchar(255) NOT NULL,
  `group_desc` longtext NOT NULL,
  `group_desc_bitfield` varchar(255) NOT NULL,
  `group_desc_options` int(11) NOT NULL,
  PRIMARY KEY (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phpbb3_groups`
--

LOCK TABLES `phpbb3_groups` WRITE;
/*!40000 ALTER TABLE `phpbb3_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `phpbb3_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phpbb3_posts`
--

DROP TABLE IF EXISTS `phpbb3_posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phpbb3_posts` (
  `post_id` int(11) NOT NULL,
  `topic_id` int(11) NOT NULL,
  `forum_id` int(11) NOT NULL,
  `poster_id` int(11) NOT NULL,
  `post_time` int(11) NOT NULL,
  `post_text` longtext NOT NULL,
  PRIMARY KEY (`post_id`),
  KEY `phpbb3_posts_57732028` (`topic_id`),
  KEY `phpbb3_posts_499a185a` (`forum_id`),
  KEY `phpbb3_posts_4fb13833` (`poster_id`),
  CONSTRAINT `forum_id_refs_forum_id_18e88529` FOREIGN KEY (`forum_id`) REFERENCES `phpbb3_forums` (`forum_id`),
  CONSTRAINT `poster_id_refs_user_id_173369ba` FOREIGN KEY (`poster_id`) REFERENCES `phpbb3_users` (`user_id`),
  CONSTRAINT `topic_id_refs_topic_id_326ef2f5` FOREIGN KEY (`topic_id`) REFERENCES `phpbb3_topics` (`topic_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phpbb3_posts`
--

LOCK TABLES `phpbb3_posts` WRITE;
/*!40000 ALTER TABLE `phpbb3_posts` DISABLE KEYS */;
/*!40000 ALTER TABLE `phpbb3_posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phpbb3_topics`
--

DROP TABLE IF EXISTS `phpbb3_topics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phpbb3_topics` (
  `topic_id` int(11) NOT NULL,
  `topic_title` varchar(60) NOT NULL,
  `topic_replies` int(11) NOT NULL,
  `topic_poster` int(11) NOT NULL,
  `topic_time` int(11) NOT NULL,
  `forum_id` int(11) NOT NULL,
  `topic_last_post_id` int(11) NOT NULL,
  `topic_first_post_id` int(11) NOT NULL,
  `topic_last_post_time` int(11) NOT NULL,
  PRIMARY KEY (`topic_id`),
  UNIQUE KEY `topic_last_post_id` (`topic_last_post_id`),
  UNIQUE KEY `topic_first_post_id` (`topic_first_post_id`),
  KEY `phpbb3_topics_505fb38c` (`topic_poster`),
  KEY `phpbb3_topics_499a185a` (`forum_id`),
  CONSTRAINT `forum_id_refs_forum_id_8dfb981` FOREIGN KEY (`forum_id`) REFERENCES `phpbb3_forums` (`forum_id`),
  CONSTRAINT `topic_first_post_id_refs_post_id_19aa5ee5` FOREIGN KEY (`topic_first_post_id`) REFERENCES `phpbb3_posts` (`post_id`),
  CONSTRAINT `topic_last_post_id_refs_post_id_19aa5ee5` FOREIGN KEY (`topic_last_post_id`) REFERENCES `phpbb3_posts` (`post_id`),
  CONSTRAINT `topic_poster_refs_user_id_62b75e62` FOREIGN KEY (`topic_poster`) REFERENCES `phpbb3_users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phpbb3_topics`
--

LOCK TABLES `phpbb3_topics` WRITE;
/*!40000 ALTER TABLE `phpbb3_topics` DISABLE KEYS */;
/*!40000 ALTER TABLE `phpbb3_topics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phpbb3_users`
--

DROP TABLE IF EXISTS `phpbb3_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phpbb3_users` (
  `user_id` int(11) NOT NULL,
  `username` varchar(25) NOT NULL,
  `user_password` varchar(32) NOT NULL,
  `user_posts` int(11) NOT NULL,
  `user_email` varchar(255) NOT NULL,
  `user_website` varchar(100) NOT NULL,
  `user_avatar_type` int(11) NOT NULL,
  `user_avatar` varchar(250) NOT NULL,
  `user_regdate` int(11) NOT NULL,
  `user_lastvisit` int(11) NOT NULL,
  `user_sig_bbcode_uid` varchar(8) NOT NULL,
  `user_sig_bbcode_bitfield` varchar(255) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phpbb3_users`
--

LOCK TABLES `phpbb3_users` WRITE;
/*!40000 ALTER TABLE `phpbb3_users` DISABLE KEYS */;
/*!40000 ALTER TABLE `phpbb3_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phpbb_djangophpbbusermapping`
--

DROP TABLE IF EXISTS `phpbb_djangophpbbusermapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phpbb_djangophpbbusermapping` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `django_user_id` int(11) NOT NULL,
  `phpbb_user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_user_id` (`django_user_id`),
  UNIQUE KEY `phpbb_user_id` (`phpbb_user_id`),
  CONSTRAINT `phpbb_user_id_refs_user_id_198de5d2` FOREIGN KEY (`phpbb_user_id`) REFERENCES `phpbb3_users` (`user_id`),
  CONSTRAINT `django_user_id_refs_id_6d447643` FOREIGN KEY (`django_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phpbb_djangophpbbusermapping`
--

LOCK TABLES `phpbb_djangophpbbusermapping` WRITE;
/*!40000 ALTER TABLE `phpbb_djangophpbbusermapping` DISABLE KEYS */;
/*!40000 ALTER TABLE `phpbb_djangophpbbusermapping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `progression_boss`
--

DROP TABLE IF EXISTS `progression_boss`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `progression_boss` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `instance_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `cleared_date` date DEFAULT NULL,
  `ordering` int(11) NOT NULL,
  `current` tinyint(1) NOT NULL,
  `active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `progression_boss_instance_id` (`instance_id`),
  CONSTRAINT `instance_id_refs_id_eb050f` FOREIGN KEY (`instance_id`) REFERENCES `progression_instance` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `progression_boss`
--

LOCK TABLES `progression_boss` WRITE;
/*!40000 ALTER TABLE `progression_boss` DISABLE KEYS */;
INSERT INTO `progression_boss` VALUES (1,1,'Flame Leviathan','2009-04-15',1,1,1),(2,1,'Razorscale','2009-04-22',0,1,1),(3,2,'Flame Leviathan','2009-04-17',1,1,1),(4,3,'Anub\'rekhan','2009-01-21',1,1,1),(5,4,'Anub\'rekhan','2008-12-08',1,1,1),(6,5,'TEST BOSS',NULL,100,1,1);
/*!40000 ALTER TABLE `progression_boss` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `progression_bossdetail`
--

DROP TABLE IF EXISTS `progression_bossdetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `progression_bossdetail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `boss_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `cleared_date` date DEFAULT NULL,
  `ordering` int(11) NOT NULL,
  `active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `progression_bossdetail_boss_id` (`boss_id`),
  CONSTRAINT `boss_id_refs_id_827a2f8` FOREIGN KEY (`boss_id`) REFERENCES `progression_boss` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `progression_bossdetail`
--

LOCK TABLES `progression_bossdetail` WRITE;
/*!40000 ALTER TABLE `progression_bossdetail` DISABLE KEYS */;
INSERT INTO `progression_bossdetail` VALUES (1,1,'1 Tower','2009-05-13',1,1),(2,1,'2 Towers','2009-06-17',2,1),(3,1,'3 Towers','2009-07-01',3,1),(4,3,'1 Tower','2009-07-30',1,1),(5,3,'2 Towers','2009-06-19',2,1),(6,3,'3 Towers','2009-06-25',3,1),(7,6,'BOSS DETAIL TEST',NULL,100,1);
/*!40000 ALTER TABLE `progression_bossdetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `progression_instance`
--

DROP TABLE IF EXISTS `progression_instance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `progression_instance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `cleared_date` date DEFAULT NULL,
  `image_url` varchar(200) NOT NULL,
  `ordering` int(11) NOT NULL,
  `current` tinyint(1) NOT NULL,
  `active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `progression_instance`
--

LOCK TABLES `progression_instance` WRITE;
/*!40000 ALTER TABLE `progression_instance` DISABLE KEYS */;
INSERT INTO `progression_instance` VALUES (1,'Ulduar 25',NULL,'',1,1,1),(2,'Ulduar 10',NULL,'',2,1,1),(3,'Naxx 25',NULL,'',90,0,1),(4,'Naxx 10',NULL,'',91,0,1),(5,'TEST INSTANCE',NULL,'',100,1,1);
/*!40000 ALTER TABLE `progression_instance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recruitment_recruitmentclass`
--

DROP TABLE IF EXISTS `recruitment_recruitmentclass`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `recruitment_recruitmentclass` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `image_url` varchar(200) NOT NULL,
  `requirements` varchar(20) NOT NULL,
  `active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recruitment_recruitmentclass`
--

LOCK TABLES `recruitment_recruitmentclass` WRITE;
/*!40000 ALTER TABLE `recruitment_recruitmentclass` DISABLE KEYS */;
INSERT INTO `recruitment_recruitmentclass` VALUES (1,'Death Knight','img/kapai/deathknight.gif','None',1),(2,'Druid','img/kapai/druid.gif','None',1),(3,'Hunter','img/kapai/hunter.gif','None',1),(4,'Mage','img/kapai/mage.gif','None',1),(5,'Paladin','img/kapai/paladin.gif','None',1),(6,'Priest','img/kapai/priest.gif','None',1),(7,'Rogue','img/kapai/priest.gif','None',1);
/*!40000 ALTER TABLE `recruitment_recruitmentclass` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `south_migrationhistory`
--

DROP TABLE IF EXISTS `south_migrationhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `south_migrationhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) NOT NULL,
  `migration` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `south_migrationhistory`
--

LOCK TABLES `south_migrationhistory` WRITE;
/*!40000 ALTER TABLE `south_migrationhistory` DISABLE KEYS */;
INSERT INTO `south_migrationhistory` VALUES (1,'index','0001_initial','2010-06-23 22:25:55'),(2,'progression','0001_initial','2010-06-23 22:26:11'),(3,'recruitment','0001_initial','2010-06-23 22:26:15'),(4,'gallery','0001_initial','2010-06-23 22:26:22');
/*!40000 ALTER TABLE `south_migrationhistory` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2010-06-24  3:26:50
