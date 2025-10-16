CREATE DATABASE property_manager CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'pm_user'@'localhost' IDENTIFIED BY 'strong_password_here';
GRANT ALL PRIVILEGES ON property_manager.* TO 'pm_user'@'localhost';
FLUSH PRIVILEGES;