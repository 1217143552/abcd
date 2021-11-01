/*
SQLyog Ultimate v12.5.0 (64 bit)
MySQL - 5.6.24 : Database - 学生数据库
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`学生数据库` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `学生数据库`;

/*Table structure for table `choose` */

DROP TABLE IF EXISTS `choose`;

CREATE TABLE `choose` (
  `sno` char(4) NOT NULL,
  `cno` char(4) NOT NULL,
  `grade` int(11) DEFAULT NULL,
  PRIMARY KEY (`sno`,`cno`),
  KEY `FK_class_choose` (`cno`),
  CONSTRAINT `FK_class_choose` FOREIGN KEY (`cno`) REFERENCES `class` (`cno`),
  CONSTRAINT `FK_student_choose` FOREIGN KEY (`sno`) REFERENCES `student` (`sno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `choose` */

insert  into `choose`(`sno`,`cno`,`grade`) values 
('S1','C1',80),
('S1','C2',85),
('S1','C4',56),
('S1','C5',90),
('S1','C6',75),
('S2','C1',47),
('S2','C3',80),
('S2','C4',75),
('S2','C5',70),
('S3','C1',76),
('S3','C2',70),
('S3','C3',85),
('S3','C4',86),
('S3','C5',90),
('S3','C6',99),
('S4','C1',83),
('S4','C2',85),
('S4','C3',83),
('S5','C2',99),
('S6','C1',96),
('S6','C2',80),
('S6','C3',87);

/*Table structure for table `class` */

DROP TABLE IF EXISTS `class`;

CREATE TABLE `class` (
  `cno` char(4) NOT NULL,
  `cn` char(19) NOT NULL,
  PRIMARY KEY (`cno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `class` */

insert  into `class`(`cno`,`cn`) values 
('C1','数学'),
('C2','英语'),
('C3','Fortran77'),
('C4','Pascal'),
('C5','政治'),
('C6','物理'),
('C7','逻辑');

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `sno` char(4) NOT NULL,
  `sn` char(8) NOT NULL,
  `sex` char(2) NOT NULL,
  `age` int(2) DEFAULT NULL,
  `dept` int(11) NOT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `student` */

insert  into `student`(`sno`,`sn`,`sex`,`age`,`dept`) values 
('S1','徐啸','女',17,2),
('S2','辛国华','男',18,6),
('S3','徐祎','女',20,1),
('S4','邓一偶','男',23,6),
('S5','张季扬','男',19,6),
('S6','张辉','女',22,3),
('S7','王刻画','男',18,6),
('S8','王仁','男',19,3);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
