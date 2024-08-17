CREATE DATABASE compraClick;
USE ecommerce;
-- Tabela de Usuários
CREATE TABLE usuario (
 usu_id INT AUTO_INCREMENT PRIMARY KEY,
 usu_username VARCHAR(100) NOT NULL ,
 usu_password VARCHAR(100) NOT NULL,
 usu_email VARCHAR(100) NOT NULL
);
-- Tabela de Categorias
CREATE TABLE categoria (
 cat_id INT AUTO_INCREMENT PRIMARY KEY,
 cat_name VARCHAR(100) NOT NULL
);
-- Tabela de Anúncios
CREATE TABLE ads (
 ads_id INT AUTO_INCREMENT PRIMARY KEY,
 ads_titulo VARCHAR(100) NOT NULL,
 ads_descricao TEXT NOT NULL,
 ads_preco DECIMAL(10, 2) NOT NULL,
 ads_qtd INT NOT NULL,
 ads_cat_id INT NOT NULL,
 ads_usu_id INT NOT NULL,
 FOREIGN KEY (ads_cat_id) REFERENCES categoria(cat_id),
 FOREIGN KEY (ads_usu_id) REFERENCES usuario(usu_id)
);
-- Tabela de Perguntas
CREATE TABLE Perguntas (
 per_id INT AUTO_INCREMENT PRIMARY KEY,
 per_conteudo TEXT NOT NULL,
 per_ad_id INT NOT NULL,
 per_user_id INT NOT NULL,
 per_response TEXT,
 per_horario DATETIME,
 FOREIGN KEY (ad_id) REFERENCES ads(ads_id),
 FOREIGN KEY (per_user_id) REFERENCES usuario(usu_id)
);
-- Tabela de Compras
CREATE TABLE compra (
 com_id INT AUTO_INCREMENT PRIMARY KEY,
 com_ad_id INT NOT NULL,
FRAMEWORKS PARA DESENVOLVIMENTO
DE SOFTWARE
| 4º termo
 com_user_id INT NOT NULL,
 com_horario DATETIME ,
 FOREIGN KEY (ad_id) REFERENCES ads(ads_id),
 FOREIGN KEY (com_ad_id) REFERENCES usuario(usu_id)
);
-- Tabela de Favoritos
CREATE TABLE favoritos (
 fav_id INT AUTO_INCREMENT PRIMARY KEY,
 fav_user_id INT NOT NULL,
 fav_ad_id INT NOT NULL,
 FOREIGN KEY (fav_user_id) REFERENCES usuario(usu_id),
 FOREIGN KEY (fav_ad_id) REFERENCES ads(ads_id),
);
