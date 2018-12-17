-- Table: Room
CREATE TABLE Room (
   id int IDENTITY(1,1) PRIMARY KEY, 
   code varchar(20) NOT NULL UNIQUE,
   type varchar(10) CHECK (type IN ('care', 'operations', 'icu')),
    empty BIT NOT NULL
);


-- Table: Doctor
CREATE TABLE Doctor (
   id int IDENTITY(1,1) PRIMARY KEY,
   username varchar(20) UNIQUE NOT NULL,
   name varchar(45) ,
   password varchar(20) NOT NULL,
   department varchar(45) ,   
);

-- Table: Nurses_WardBoys
CREATE TABLE Nurses_WardBoys (
   id int IDENTITY(1,1) PRIMARY KEY,
   username varchar(20) UNIQUE NOT NULL,
   name varchar(45) ,
   password varchar(20) NOT NULL,
   type varchar(10) CHECK (type IN ('nurse', 'ward')),
   room_id int ,
   FOREIGN KEY (room_id) REFERENCES Room(id) ON DELETE SET NULL ON UPDATE CASCADE   
);

-- Table: Patient
CREATE TABLE Patient (
   id int IDENTITY(1,1) PRIMARY KEY,
   username varchar(20) UNIQUE NOT NULL,
   name varchar(45) ,
   password varchar(20) NOT NULL ,
   age int,
   cell varchar(11) ,
   address varchar(45) ,
   disease varchar(45) ,
   treatment varchar(45) ,
   cure_price float ,
   entry_date date default CURRENT_TIMESTAMP,
   exit_date date default '2020-12-12' ,
   bill float ,
   doctor_id int NOT NULL,
   room_id int NOT NULL,
   diagnose varchar(1024) ,
   sidenotes varchar(1024) ,
   FOREIGN KEY (room_id) REFERENCES Room(id) ON DELETE NO ACTION ON UPDATE CASCADE,
   FOREIGN KEY (doctor_id) REFERENCES Doctor(id) ON DELETE NO ACTION ON UPDATE CASCADE
);



insert into Room  (code, type, empty) values ('N0','care',1)
insert into Room  (code, type, empty) values ('N1','care',1)

insert into Doctor (username,password,name,department) values ('joo','123','Kareem','Surgery')
insert into Doctor (username,password,name,department) values ('raid','123','Raid Serag','Tabal')
insert into Doctor (username,password,name,department) values ('r3','123','Raid Serag','Tabal')
insert into Doctor (username,password,name,department) values ('33','123','Raid Serag','Tabal')

insert into Patient (name, password, age, username, cell, address ,disease, treatment, cure_price, bill, doctor_id, room_id, diagnose, sidenotes) values ('Raaed','123',21,'Rr','01000000000','14 ElGomla St.','Lung Cancer','Chemo',500.0,900.0,1,1,'Coughing Blood','Took His medicine')
insert into Patient (name, password, age, username, cell, address ,disease, treatment, cure_price, bill, doctor_id, room_id, diagnose, sidenotes) values ('Kareem Kiro','123',21,'Kiro','01222222222+','14 ElGomla St.','Heart Cancer','Chemo',300.0,400.0,1,2,'Coughing Blood','Took His medicine')
insert into Patient (name, password, age, username, cell, address ,disease, treatment, cure_price, bill, doctor_id, room_id, diagnose, sidenotes) values ('som3a','123',21,'Esmail','01111111111','14  St.','Heart Cancer','Chemo',400.0,400.0,2,1,'Coughing Blood','Took His medicine')

insert into Nurses_WardBoys (name,username,password,type,room_id) values ('Nurse0','nurse0','123','nurse',2)
insert into Nurses_WardBoys (name,username,password,type,room_id) values ('Nurse1','nurse1','123','nurse',1)
insert into Nurses_WardBoys (name,username,password,type,room_id) values ('Ward0','ward0','123','ward',2)

SELECT * FROM Doctor

SELECT * FROM Room

SELECT * FROM Patient

SELECT * FROM Nurses_WardBoys