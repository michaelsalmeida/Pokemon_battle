drop database gamepoke;

create database gamepoke;
use gamepoke;

CREATE TABLE login (
pk_login int(2) PRIMARY KEY auto_increment,
nick VARCHAR(30),
senha VARCHAR(50)
);

CREATE TABLE treinador (
pk_treinador int(2) PRIMARY KEY auto_increment,
fk_login int(2),
potion int(2),
superpotion int(2),
hyperpotion int(2),	
maxpotion int(2),
pokedolar int(5),
foreign key (fk_login) references login (pk_login)
);

CREATE TABLE pokemon (
pk_pokemon int(2) PRIMARY KEY auto_increment,
fk_treinador int(2),
nome_pokemon VARCHAR(20),
nivel int(3),
vida int(4),
atk int(3),
def int(3),
velocidade int(3),
vida_original int(3),
foreign key (fk_treinador) references treinador (pk_treinador)
);
