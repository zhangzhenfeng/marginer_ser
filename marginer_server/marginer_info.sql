/*
Navicat MySQL Data Transfer

Source Server         : 192.168.1.107
Source Server Version : 50544
Source Host           : 192.168.1.105:3306
Source Database       : marginer

Target Server Type    : MYSQL
Target Server Version : 50544
File Encoding         : 65001

Date: 2016-02-15 21:55:43
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for marginer_info
-- ----------------------------
DROP TABLE IF EXISTS `marginer_info`;
CREATE TABLE `marginer_info` (
  `id` varchar(32) NOT NULL,
  `temperature` varchar(10) DEFAULT NULL,
  `humidity` varchar(10) DEFAULT NULL,
  `cpu_temperature` varchar(10) DEFAULT NULL,
  `gpu_temperature` varchar(10) DEFAULT NULL,
  `cpu_rate` varchar(10) DEFAULT NULL,
  `ram` varchar(20) DEFAULT NULL,
  `disk` varchar(20) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
