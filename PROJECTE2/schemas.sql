DROP DATABASE IF EXISTS `odisea`;
CREATE DATABASE IF NOT EXISTS `odisea` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `odisea`;

CREATE TABLE IF NOT EXISTS `socios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `hoteles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `ubicacion` text DEFAULT NULL,
  `disponibilidad` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `habitaciones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hotel_id` int(11) DEFAULT NULL,
  `tipo` varchar(50) DEFAULT NULL,
  `disponibilidad` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`),
  KEY `hotel_id` (`hotel_id`),
  CONSTRAINT `habitaciones_ibfk_1` FOREIGN KEY (`hotel_id`) REFERENCES `hoteles` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `pistas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `tipo` varchar(50) DEFAULT NULL,
  `disponibilidad` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `restaurantes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `ubicacion` text DEFAULT NULL,
  `valoracion` decimal(3,1) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `disponibilidad` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `servicio_restaurante` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `restaurante_id` INT(11) NOT NULL,
  `tipo_menu` VARCHAR(50) DEFAULT NULL,
  `tipo_cocina` VARCHAR(100) DEFAULT NULL,
  `ambiente` VARCHAR(100) DEFAULT NULL,
  `terraza` TINYINT(1) DEFAULT 0,
  PRIMARY KEY (`id`),
  KEY `restaurante_id` (`restaurante_id`),
  CONSTRAINT `servicio_restaurante_ibfk_1` FOREIGN KEY (`restaurante_id`) REFERENCES `restaurantes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `spa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `disponibilidad` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `servicio_spa` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `spa_id` INT(11) NOT NULL,
  `tipo_servicio` VARCHAR(100) DEFAULT NULL,
  `duracion` INT DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `spa_id` (`spa_id`),
  CONSTRAINT `servicio_spa_ibfk_1` FOREIGN KEY (`spa_id`) REFERENCES `spa` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `servicio_pistas` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `pista_id` INT(11) NOT NULL,
  `tipo_pista` VARCHAR(50) DEFAULT NULL,
  `numero_personas` INT DEFAULT NULL,
  `material` VARCHAR(100) DEFAULT NULL,
  `tiempo_disponible` VARCHAR(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `pista_id` (`pista_id`),
  CONSTRAINT `servicio_pistas_ibfk_1` FOREIGN KEY (`pista_id`) REFERENCES `pistas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `reservas_hotel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `socio_id` int(11) DEFAULT NULL,
  `habitacion_id` int(11) DEFAULT NULL,
  `fecha_entrada` date DEFAULT NULL,
  `fecha_salida` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `socio_id` (`socio_id`),
  KEY `habitacion_id` (`habitacion_id`),
  CONSTRAINT `reservas_hotel_ibfk_1` FOREIGN KEY (`socio_id`) REFERENCES `socios` (`id`),
  CONSTRAINT `reservas_hotel_ibfk_2` FOREIGN KEY (`habitacion_id`) REFERENCES `habitaciones` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `reservas_pistas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `socio_id` int(11) DEFAULT NULL,
  `pista_id` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `socio_id` (`socio_id`),
  KEY `pista_id` (`pista_id`),
  CONSTRAINT `reservas_pistas_ibfk_1` FOREIGN KEY (`socio_id`) REFERENCES `socios` (`id`),
  CONSTRAINT `reservas_pistas_ibfk_2` FOREIGN KEY (`pista_id`) REFERENCES `pistas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `reservas_restaurante` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `socio_id` int(11) DEFAULT NULL,
  `restaurante_id` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `socio_id` (`socio_id`),
  KEY `restaurante_id` (`restaurante_id`),
  CONSTRAINT `reservas_restaurante_ibfk_1` FOREIGN KEY (`socio_id`) REFERENCES `socios` (`id`),
  CONSTRAINT `reservas_restaurante_ibfk_2` FOREIGN KEY (`restaurante_id`) REFERENCES `restaurantes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `reservas_spa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `socio_id` int(11) DEFAULT NULL,
  `spa_id` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `socio_id` (`socio_id`),
  KEY `spa_id` (`spa_id`),
  CONSTRAINT `reservas_spa_ibfk_1` FOREIGN KEY (`socio_id`) REFERENCES `socios` (`id`),
  CONSTRAINT `reservas_spa_ibfk_2` FOREIGN KEY (`spa_id`) REFERENCES `spa` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `favoritos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `socio_id` int(11) DEFAULT NULL,
  `tipo` varchar(50) DEFAULT NULL,
  `referencia_id` int(11) DEFAULT NULL,
  `fecha_agregado` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `socio_id` (`socio_id`),
  CONSTRAINT `favoritos_ibfk_1` FOREIGN KEY (`socio_id`) REFERENCES `socios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
