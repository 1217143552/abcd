/*
SQLyog Ultimate v12.5.0 (64 bit)
MySQL - 5.6.24 : Database - 销售数据库
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`销售数据库` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `销售数据库`;

/*Table structure for table `article` */

DROP TABLE IF EXISTS `article`;

CREATE TABLE `article` (
  `商品号` char(10) NOT NULL,
  `商品名` char(10) DEFAULT NULL,
  `单价` float DEFAULT NULL,
  `库存量` int(11) DEFAULT NULL,
  PRIMARY KEY (`商品号`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `article` */

insert  into `article`(`商品号`,`商品名`,`单价`,`库存量`) values 
('S001','计算机',5000,10),
('S002','打印机',1000,12),
('S003','洗衣机',800,10),
('S004','电冰箱',1100,20);

/*Table structure for table `customer` */

DROP TABLE IF EXISTS `customer`;

CREATE TABLE `customer` (
  `顾客号` char(10) NOT NULL,
  `顾客名` char(10) DEFAULT NULL,
  `性别` char(2) DEFAULT NULL,
  `年龄` int(11) DEFAULT NULL,
  PRIMARY KEY (`顾客号`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `customer` */

insert  into `customer`(`顾客号`,`顾客名`,`性别`,`年龄`) values 
('G001','张三','男',29),
('G002','李四','女',25),
('G003','王五','女',31),
('G004','赵六','男',25);

/*Table structure for table `orderitem` */

DROP TABLE IF EXISTS `orderitem`;

CREATE TABLE `orderitem` (
  `顾客号` char(10) NOT NULL DEFAULT '',
  `商品号` char(10) NOT NULL DEFAULT '',
  `数量` int(11) DEFAULT NULL,
  `购买价` float DEFAULT NULL,
  `购买日期` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`顾客号`,`商品号`,`购买日期`),
  KEY `FK_article_orderitem` (`商品号`),
  CONSTRAINT `FK_article_orderitem` FOREIGN KEY (`商品号`) REFERENCES `article` (`商品号`),
  CONSTRAINT `FK_customer_orderitem` FOREIGN KEY (`顾客号`) REFERENCES `customer` (`顾客号`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `orderitem` */

insert  into `orderitem`(`顾客号`,`商品号`,`数量`,`购买价`,`购买日期`) values 
('G001','S001',2,4000,'2015-08-16 00:00:00'),
('G001','S002',1,800,'2008-01-25 00:00:00'),
('G001','S003',3,600,'2008-01-25 00:00:00'),
('G001','S004',1,880,'2008-01-25 00:00:00'),
('G002','S001',3,4500,'2008-01-01 00:00:00'),
('G003','S001',1,5000,'2008-01-00 00:00:00'),
('G003','S002',1,1000,'2008-01-00 00:00:00');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
