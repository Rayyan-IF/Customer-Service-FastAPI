-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.4.28-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             12.4.0.6659
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for store
CREATE DATABASE IF NOT EXISTS `store` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `store`;

-- Dumping structure for table store.address_store
CREATE TABLE IF NOT EXISTS `address_store` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `address` varchar(30) DEFAULT NULL,
  `district` varchar(20) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `province` varchar(20) DEFAULT NULL,
  `postal_code` varchar(10) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `fk_address_customer_id` (`customer_id`),
  CONSTRAINT `fk_address_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customer_store` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table store.address_store: ~5 rows (approximately)
INSERT IGNORE INTO `address_store` (`id`, `customer_id`, `address`, `district`, `city`, `province`, `postal_code`, `created_at`, `updated_at`) VALUES
	(1, 1, 'Kopo Sayati', 'Kab. Bandung', 'Bandung', 'Jawa barat', '40228', '2023-08-07 20:31:58', '2023-08-07 20:31:58'),
	(2, 2, 'Bidara Cina', 'Jakarta Timur', 'Jakarta', 'DKI jakarta', '12345', '2023-08-07 20:31:58', '2023-08-07 20:31:58'),
	(3, 3, 'Margahayu', 'Kab. Bandung', 'Bandung', 'Jawa Barat', '40225', '2023-08-07 20:31:58', '2023-08-07 20:31:58'),
	(4, 4, 'Blok M', 'Jakarta Selatan', 'Jakarta', 'DKI jakarta', '12344', '2023-08-07 20:31:58', '2023-08-07 20:31:58'),
	(5, 5, 'Ancol', 'Jakarta Utara', 'Jakarta', 'DKI jakarta', '12347', '2023-08-07 20:31:58', '2023-08-07 20:31:58');

-- Dumping structure for table store.customer_store
CREATE TABLE IF NOT EXISTS `customer_store` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(30) DEFAULT NULL,
  `name` varchar(30) NOT NULL,
  `gender` varchar(3) DEFAULT NULL,
  `phone_number` varchar(15) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `email` varchar(30) NOT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table store.customer_store: ~5 rows (approximately)
INSERT IGNORE INTO `customer_store` (`id`, `title`, `name`, `gender`, `phone_number`, `image`, `email`, `created_at`, `updated_at`) VALUES
	(1, 'SPD', 'Sobandi', 'Pri', '0812345678', 'https://www.simplilearn.com/ice9/free_resources_article_thumb/what_is_image_Processing.jpg', 'sobandi@gmail.com', '2023-08-07 20:25:45', '2023-08-07 20:25:45'),
	(2, 'HJ', 'Mansur', 'Pri', '08123456789', 'https://dfstudio-d420.kxcdn.com/wordpress/wp-content/uploads/2019/06/digital_camera_photo-1080x675.j', 'mansur@gmail.com', '2023-08-07 20:25:45', '2023-08-07 20:25:45'),
	(3, 'MEng', 'Yayan', 'Pri', '08123456780', 'https://media.istockphoto.com/id/1322277517/photo/wild-grass-in-the-mountains-at-sunset.jpg?s=612x61', 'yayan@gmail.com', '2023-08-07 20:25:45', '2023-08-07 20:25:45'),
	(4, 'Dr', 'Lisna', 'Wan', '08123456781', 'https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWF', 'lisna@gmail.com', '2023-08-07 20:25:45', '2023-08-07 20:25:45'),
	(5, 'Phd', 'Rahmat', 'Pri', '08123456782', 'https://img.freepik.com/premium-photo/image-colorful-galaxy-sky-generative-ai_791316-9864.jpg?w=2000', 'rahmat@gmail.com', '2023-08-07 20:25:45', '2023-08-07 20:25:45');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
