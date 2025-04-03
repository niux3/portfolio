
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL,
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);
INSERT INTO alembic_version VALUES('1ef0ebbef7f9');
CREATE TABLE activities (
	id INTEGER NOT NULL,
	name VARCHAR(64) NOT NULL,
	icon TEXT,
	PRIMARY KEY (id)
);
INSERT INTO activities VALUES(1,'aviation','fa-solid fa-plane');
INSERT INTO activities VALUES(2,'automobile','fa-solid fa-car');
INSERT INTO activities VALUES(3,'sports équestres','fa-solid fa-horse');
INSERT INTO activities VALUES(4,'alimentation','fa-solid fa-utensils');
INSERT INTO activities VALUES(5,'finance','fa-solid fa-piggy-bank');
INSERT INTO activities VALUES(6,'hygiène','fa-solid fa-soap');
INSERT INTO activities VALUES(7,'e-commerce','fa-solid fa-cart-shopping');
INSERT INTO activities VALUES(8,'blog','fa-brands fa-blogger');
INSERT INTO activities VALUES(9,'construction','fa-solid fa-person-digging');
INSERT INTO activities VALUES(10,'livres','fa-solid fa-book');
INSERT INTO activities VALUES(11,'nucléaire','fa-solid fa-radiation');
INSERT INTO activities VALUES(12,'électroménager','fa-solid fa-blender-phone');
INSERT INTO activities VALUES(13,'opticien','fa-solid fa-glasses');
INSERT INTO activities VALUES(14,'santé','fa-solid fa-notes-medical');
INSERT INTO activities VALUES(15,'motocyclette','fa-solid fa-motorcycle');
INSERT INTO activities VALUES(16,'coiffure','fa-solid fa-scissors');
INSERT INTO activities VALUES(17,'grande distibution','fa-solid fa-shirt');
INSERT INTO activities VALUES(18,'bagage','fa-solid fa-suitcase-rolling');
INSERT INTO activities VALUES(19,'réseau social','fa-solid fa-people-arrows');
INSERT INTO activities VALUES(20,'journalisme','fa-solid fa-newspaper');
INSERT INTO activities VALUES(21,'la radio','fa-solid fa-radio');
INSERT INTO activities VALUES(22,'conciergerie','fa-solid fa-bell-concierge');
INSERT INTO activities VALUES(23,'maroquinerie','bla');
INSERT INTO activities VALUES(24,'musique','fa-solid fa-music');
CREATE TABLE categories (
	id INTEGER NOT NULL,
	name VARCHAR(32) NOT NULL,
	PRIMARY KEY (id)
);
INSERT INTO categories VALUES(1,'thumb');
INSERT INTO categories VALUES(2,'normal');
CREATE TABLE functions (
	id INTEGER NOT NULL,
	name VARCHAR(128) NOT NULL,
	PRIMARY KEY (id)
);
INSERT INTO functions VALUES(1,'frontend');
INSERT INTO functions VALUES(2,'backend');
INSERT INTO functions VALUES(3,'backend/frontend');
CREATE TABLE technologies (
	id INTEGER NOT NULL,
	name VARCHAR(32) NOT NULL,
	PRIMARY KEY (id)
);
INSERT INTO technologies VALUES(1,'HTML');
INSERT INTO technologies VALUES(2,'CSS');
INSERT INTO technologies VALUES(3,'Javascript');
INSERT INTO technologies VALUES(4,'PHP');
INSERT INTO technologies VALUES(5,'MySql');
INSERT INTO technologies VALUES(6,'Python 3');
INSERT INTO technologies VALUES(7,'Django');
INSERT INTO technologies VALUES(8,'Flask');
INSERT INTO technologies VALUES(9,'ReactJS');
INSERT INTO technologies VALUES(10,'Svelte/Sveltkit');
INSERT INTO technologies VALUES(11,'SVG');
INSERT INTO technologies VALUES(12,'NodeJS');
INSERT INTO technologies VALUES(13,'ExpressJS');
INSERT INTO technologies VALUES(14,'PostgreSQL');
INSERT INTO technologies VALUES(15,'MJML');
INSERT INTO technologies VALUES(16,'Wordpress');
INSERT INTO technologies VALUES(17,'Joomla');
INSERT INTO technologies VALUES(18,'JQuery');
INSERT INTO technologies VALUES(19,'DRF');
INSERT INTO technologies VALUES(20,'Docker');
CREATE TABLE images (
	id INTEGER NOT NULL,
	name VARCHAR(128) NOT NULL,
	url VARCHAR(128) NOT NULL,
	online SMALLINT,
	description TEXT,
	categories_id INTEGER,
	portfolios_id INTEGER,
	created DATETIME,
	modified DATETIME,
	PRIMARY KEY (id),
	FOREIGN KEY(categories_id) REFERENCES categories (id),
	FOREIGN KEY(portfolios_id) REFERENCES functions (id)
);
INSERT INTO images VALUES(1,'bla','/static/img/leroy-merlin/1--1__fd4f977f-bcdb-4e80-9d47-cbc9fede4eb0.jpg',1,'blabla',1,1,'2022-10-11 00:43:01.065160','2022-10-11 00:43:12.757378');
INSERT INTO images VALUES(2,'bla','/static/img/john-paul/4--1__852ff8e0-2c4d-49f0-948d-be0455af5b0b.jpg',1,'blabla',1,4,'2023-03-20 19:36:46.001663','2023-03-20 19:36:46.001673');
INSERT INTO images VALUES(3,'bla','/static/img/carenity/8--1__712e0e1d-af2b-491e-bcde-67fe868f5670.jpg',1,'blabla',1,8,'2023-03-20 19:37:21.682487','2023-03-20 19:37:21.682501');
INSERT INTO images VALUES(5,'bla','/static/img/mytravelchic/22--1__14c04cdc-f7c9-49b5-a4b8-cb82677db08a.jpg',1,'blabla',1,22,'2023-03-20 19:38:46.032633','2023-03-20 19:38:46.032641');
INSERT INTO images VALUES(6,'bla','/static/img/radio-france/5--1__1ff4e321-35d8-4dc9-b680-f057342b2e80.jpg',1,'blabla',1,5,'2023-03-20 19:56:44.531112','2023-03-20 19:56:44.531117');
INSERT INTO images VALUES(8,'bla','/static/img/palmares-lepoint/7--1__05762776-2c17-4793-af13-fdedf6b05eaf.jpg',1,'blabla',1,7,'2023-03-20 20:08:35.761256','2023-03-20 20:08:35.761262');
INSERT INTO images VALUES(9,'bla','/static/img/rimowa/9--1__b4f117d4-ffd1-48e3-a846-0b5fbbf64efe.jpg',1,'blabla',1,9,'2023-03-20 20:17:57.779069','2023-03-20 20:17:57.779076');
INSERT INTO images VALUES(10,'bla','/static/img/longchamp/10--1__2d6eac2b-2ba3-4ccc-90f5-c568ac1ee746.jpg',1,'blabla',1,10,'2023-03-20 20:20:06.050396','2023-03-20 20:20:06.050406');
INSERT INTO images VALUES(11,'Confbox','/static/img/confbox/44--1__989e67c3-57d3-4335-9d5b-b505631f5df8.jpg',1,'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet laborum illum maxime iusto minima reiciendis praesentium labore ab, sed sapiente officia enim consequuntur atque non rerum nostrum quibusdam rem molestiae!',1,44,'2023-10-18 23:00:53.616942','2023-10-18 23:00:53.616952');
INSERT INTO images VALUES(12,'cevital','/static/img/cevital/11--1__ebcbbc10-7c0e-4460-8693-b0abfc810bab.jpg',1,'ipsum',1,11,'2023-10-18 23:06:45.942784','2023-10-18 23:06:45.942790');
INSERT INTO images VALUES(13,'René Furterer','/static/img/rene-furterer/12--1__b0870a72-a317-4e0b-9e09-dc85f8367b89.jpg',1,'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet laborum illum maxime iusto minima reiciendis praesentium labore ab, sed sapiente officia enim consequuntur atque non rerum nostrum quibusdam rem molestiae!',1,12,'2023-10-18 23:12:40.637620','2023-10-18 23:12:40.637627');
INSERT INTO images VALUES(15,'Dacia','/static/img/dacia/13--1__8625edf7-2f52-4d28-a1af-f37f7190db7c.jpg',1,'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet laborum illum maxime iusto minima reiciendis praesentium labore ab, sed sapiente officia enim consequuntur atque non rerum nostrum quibusdam rem molestiae!',1,13,'2023-10-18 23:19:08.184156','2023-10-18 23:19:08.184162');
INSERT INTO images VALUES(16,'UPSA','/static/img/upsa/14--1__e84648ce-ee8f-4611-abb2-ca5a9af2e091.jpg',1,'blabla',1,14,'2023-10-18 23:22:32.305896','2023-10-18 23:22:32.305900');
INSERT INTO images VALUES(17,'Renault Clio RS','/static/img/clio-rs-melody/15--1__2e0c6de3-394f-405f-af5d-c5155fa51745.jpg',1,'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet laborum illum maxime iusto minima reiciendis praesentium labore ab, sed sapiente officia enim consequuntur atque non rerum nostrum quibusdam rem molestiae!',1,15,'2023-10-18 23:25:40.676051','2023-10-18 23:25:40.676057');
INSERT INTO images VALUES(18,'Renault Kadjar','/static/img/renault-kadjarquest/16--1__6f38182c-8700-481b-ab82-21f258ffeda8.jpg',1,'blabla',1,16,'2023-10-19 00:10:23.139472','2023-10-19 00:10:23.139477');
INSERT INTO images VALUES(19,'Renault le siege','/static/img/le-siege-renault/17--1__9d039491-c003-4bf9-b15c-af0d8ea3bc96.jpg',1,'blabla',1,17,'2023-10-19 00:36:09.384618','2023-10-19 00:36:09.384624');
INSERT INTO images VALUES(20,'Atelier Renault','/static/img/atelier-renault/18--1__f35557a1-69ed-4e4b-a951-120b42c9fd85.jpg',1,'blabla',1,18,'2023-10-19 00:48:47.415396','2023-10-19 00:48:47.415403');
INSERT INTO images VALUES(21,'adp','/static/img/aeroport-de-paris/19--1__39109470-7631-40f7-baac-cf93177501d8.jpg',1,'blabla',1,19,'2023-10-19 00:51:26.181194','2023-10-19 00:51:26.181198');
INSERT INTO images VALUES(22,'afflelou','/static/img/afflelou/20--1__9cc49a33-3f10-4b0f-9595-5ce569494304.jpg',1,'blabla',1,20,'2023-10-19 00:58:59.948430','2023-10-19 00:58:59.948437');
INSERT INTO images VALUES(23,'fullsix','/static/img/fullsix/21--1__e5381e61-7c88-4d28-9d59-d2535ec38c9e.jpg',1,'blabla',1,21,'2023-10-19 01:13:01.263799','2023-10-19 01:13:01.263804');
INSERT INTO images VALUES(24,'bzc','/static/img/bazarchic/23--1__b4d8d647-8286-4dca-bb11-0d9cfe514a35.jpg',1,'blabla',1,23,'2023-10-19 04:49:45.656946','2023-10-19 04:49:45.656953');
INSERT INTO images VALUES(25,'brasserie flo','/static/img/brasserie-flo/24--1__988771eb-629e-44f7-a019-0e4bebdbb0c8.jpg',1,'blabla',1,24,'2023-10-19 04:54:51.608037','2023-10-19 04:54:51.608044');
INSERT INTO images VALUES(26,'Dyson','/static/img/dyson-affaire-airblade/25--1__b0d53bc6-d56e-43fb-8bb9-9b9513c6419b.jpg',1,'blabla',1,25,'2023-10-19 05:01:14.904381','2023-10-19 05:01:14.904385');
INSERT INTO images VALUES(27,'peugeot design lab','/static/img/peugeot-design-lab/26--1__ea5b2e36-74dc-45ad-8563-67b0b093920b.jpg',1,'blabla',1,26,'2023-10-19 05:06:38.670451','2023-10-19 05:06:38.670455');
INSERT INTO images VALUES(28,'Peugeot','/static/img/peugeot/27--1__80093aec-9fcc-4e99-b9fa-b2b3ce9bdfff.jpg',1,'blabla',1,27,'2023-10-19 05:15:34.809073','2023-10-19 05:15:34.809087');
INSERT INTO images VALUES(29,'Peugeot 4008','/static/img/peugeot-4008/28--1__e8f42ca5-6a84-4355-aab2-acbec8c457fe.jpg',1,'blabla',1,28,'2023-10-19 05:25:06.162623','2023-10-19 05:25:06.162628');
INSERT INTO images VALUES(30,'LePoint','/static/img/journal-lepoint/6--1__f2c82cae-38ba-4701-ab12-7a3101a9c5ec.jpg',1,'blabla',1,6,'2023-10-19 05:49:38.362201','2023-10-19 05:49:38.362205');
INSERT INTO images VALUES(31,'Flyopenskies','/static/img/flyopensky-v2/29--1__9b56c29b-f752-4159-90e1-1282655a58d8.jpg',1,'blabla',1,29,'2023-10-19 06:06:15.481947','2023-10-19 06:06:15.481951');
INSERT INTO images VALUES(32,'Honda Moto','/static/img/honda-moto/3--1__cd65e531-84bb-4f56-a631-89bb9f25d46d.jpg',1,'blabla',1,3,'2023-10-19 06:14:56.608680','2023-10-19 06:14:56.608685');
INSERT INTO images VALUES(33,'Europcar','/static/img/europcar/31--1__1430a59f-3db8-4b05-83be-290497d0440d.jpg',1,'blabla',1,31,'2023-10-19 06:27:06.475683','2023-10-19 06:27:06.475688');
INSERT INTO images VALUES(34,'Air Caraïbes','/static/img/air-caraibes/32--1__70b7998c-661c-4e9c-ac33-e4ba58953573.jpg',1,'blabla',1,32,'2023-10-19 06:32:28.291624','2023-10-19 06:32:28.291629');
INSERT INTO images VALUES(35,'air madagascar','/static/img/air-madagascar/33--1__cf77e25e-723b-4f34-a588-1f4f6142437c.jpg',1,'blabla',1,33,'2023-10-19 06:46:41.291956','2023-10-19 06:46:41.291960');
INSERT INTO images VALUES(36,'cfc','/static/img/cfc/34--1__c9263548-615f-4041-bad7-5e4becb51411.jpg',1,'blabla',1,34,'2023-10-19 07:30:05.742855','2023-10-19 07:30:05.742860');
INSERT INTO images VALUES(37,'algeco','/static/img/algeco/35--1__bfd3ce6f-70c3-402e-bcfe-8b5136e4588f.jpg',1,'blabla',1,35,'2023-10-19 07:34:29.276653','2023-10-19 07:34:29.276657');
INSERT INTO images VALUES(38,'fidelity vie','/static/img/fidelity-vie/36--1__9ce37de1-891a-47f4-961f-1f00590da6ac.jpg',1,'blabla',1,36,'2023-10-19 08:07:14.976455','2023-10-19 08:07:14.976460');
INSERT INTO images VALUES(39,'blog mel','/static/img/de-quoi-je-me-mel/37--1__43105f7f-0235-4eb1-b2f7-934eacf3215a.jpg',1,'blabla',1,37,'2023-10-19 08:12:26.816239','2023-10-19 08:12:26.816246');
INSERT INTO images VALUES(40,'leclerc','/static/img/qui-est-le-moins-cher/38--1__1bb25b84-56ef-4c4a-b823-e843202717ba.jpg',1,'blabla',1,38,'2023-10-19 08:25:54.918900','2023-10-19 08:25:54.918907');
INSERT INTO images VALUES(41,'decolor stop','/static/img/decolor-stop/39--1__f822f123-444a-4167-b28e-f5a2b0797610.jpg',1,'blabla',1,39,'2023-10-19 08:31:44.320925','2023-10-19 08:31:44.320933');
INSERT INTO images VALUES(42,'my peugeot','/static/img/my-peugeot/40--1__d58ed398-8083-4e15-9a8e-88b314563ad3.jpg',1,'blabla',1,40,'2023-10-19 08:36:50.571284','2023-10-19 08:36:50.571288');
INSERT INTO images VALUES(43,'flyopenskyies','/static/img/flyopenskies-v3/30--1__00111803-1131-424b-96ba-b1c5c971c375.jpg',1,'blabla',1,30,'2023-10-20 10:15:13.483178','2023-10-20 10:15:13.483187');
INSERT INTO images VALUES(44,'cavadeos','/static/img/leperon/42--1__c932fbb1-95de-4900-979f-db6495e35b86.jpg',1,'blabla',1,42,'2023-10-20 10:36:02.668551','2023-10-20 10:36:02.668558');
INSERT INTO images VALUES(45,'areva','/static/img/areva/2--1__7f910da3-52b3-45e1-8f72-a92c694bd2ef.jpg',1,'blabla',1,2,'2023-10-20 10:42:29.965417','2023-10-20 10:42:29.965421');
INSERT INTO images VALUES(46,'volkwagen up','/static/img/europcar-up/50--1__d703e247-79af-4464-a1dd-f6c49ae84b87.jpg',1,'blabla',1,50,'2023-10-20 10:47:39.208026','2023-10-20 10:47:39.208032');
INSERT INTO images VALUES(47,'sacla','/static/img/sacla/43--1__66fc5e67-ae86-4065-869a-41a14b2bd49d.jpg',1,'blabla',1,43,'2023-10-20 11:01:34.321130','2023-10-20 11:01:34.321135');
INSERT INTO images VALUES(48,'Leroy Merlin','/static/img/leroy-merlin/1--2__0b92bd59-b78a-4aae-8822-9972b7436049.jpg',1,'lorem',2,1,'2023-10-31 14:31:51.356743','2023-10-31 14:31:51.356751');
INSERT INTO images VALUES(49,'Leroy Merlin','/static/img/leroy-merlin/1--2__173343e1-818b-4bbc-9b30-7ee92330f5c6.jpg',1,'lorem',2,1,'2023-10-31 14:32:06.267190','2023-10-31 14:32:06.267197');
INSERT INTO images VALUES(50,'Leroy Merlin','/static/img/leroy-merlin/1--2__6fad9b9c-da0e-4670-aa28-7a01b386e890.jpg',1,'lorem',2,1,'2023-10-31 14:32:19.031663','2023-10-31 14:32:19.031668');
INSERT INTO images VALUES(51,'Leroy Merlin','/static/img/leroy-merlin/1--2__d8ffde2e-9157-45b2-9d90-98e081958a0d.jpg',1,'lorem',2,1,'2023-10-31 14:32:30.054514','2023-10-31 14:32:30.054518');
INSERT INTO images VALUES(52,'Leroy Merlin','/static/img/leroy-merlin/1--2__5dea7052-0d11-4ce2-a09b-7007d908abdc.jpg',1,'lorem',2,1,'2023-10-31 14:33:25.051109','2023-10-31 14:33:25.051113');
INSERT INTO images VALUES(53,'Areva','/static/img/areva/2--2__130e0b7b-c5c3-4306-9b55-4fd46525e072.jpg',1,'lorem',2,2,'2023-10-31 14:45:44.693353','2023-10-31 14:45:44.693358');
INSERT INTO images VALUES(54,'Areva','/static/img/areva/2--2__2c26d60e-320a-4b11-b2b1-4c7df5b8c6e1.jpg',1,'lorem',2,2,'2023-10-31 14:46:02.892722','2023-10-31 14:46:02.892726');
INSERT INTO images VALUES(55,'Areva','/static/img/areva/2--2__7b3215f1-08d7-48b0-9bd5-5fbfabd8f203.jpg',1,'lorem',2,2,'2023-10-31 14:46:15.666614','2023-10-31 14:46:15.666620');
INSERT INTO images VALUES(56,'Areva','/static/img/areva/2--2__5ed6571d-096e-4131-b2e8-81857d4354e7.jpg',1,'lorem',2,2,'2023-10-31 14:46:27.196148','2023-10-31 14:46:27.196154');
INSERT INTO images VALUES(57,'Areva','/static/img/areva/2--2__91aad3fb-aabf-4c7e-9360-ebb199318588.jpg',1,'lorem',2,2,'2023-10-31 14:46:40.169122','2023-10-31 14:46:40.169126');
INSERT INTO images VALUES(58,'Areva','/static/img/areva/2--2__749c9e1d-91e8-4483-b841-9aa3c8d4f770.jpg',1,'lorem',2,2,'2023-10-31 14:46:48.620712','2023-10-31 14:46:48.620716');
INSERT INTO images VALUES(59,'Honda moto','/static/img/honda-moto/3--2__26824672-0f66-4b4b-ba72-8f0b17ae7665.jpg',1,'lorem',2,3,'2023-10-31 17:36:42.282575','2023-10-31 17:36:42.282581');
INSERT INTO images VALUES(60,'Honda moto','/static/img/honda-moto/3--2__22f87dfe-e862-473c-9eea-94c95fec7e6c.jpg',1,'lorem',2,3,'2023-10-31 17:37:00.587959','2023-10-31 17:37:00.587964');
INSERT INTO images VALUES(61,'Honda moto','/static/img/honda-moto/3--2__38880d1e-8243-402a-9ae5-74c6e584dee1.jpg',1,'lorem',2,3,'2023-10-31 17:37:10.569370','2023-10-31 17:37:10.569374');
INSERT INTO images VALUES(62,'Honda moto','/static/img/honda-moto/3--2__f93564d9-0969-48db-941e-81b2ba58c969.jpg',1,'lorem',2,3,'2023-10-31 17:37:23.136446','2023-10-31 17:37:23.136452');
INSERT INTO images VALUES(63,'Radio france','/static/img/radio-france/5--2__96eb2c35-ff36-4a24-a7a5-274423dbca7b.jpg',1,'lorem',2,5,'2023-11-02 15:20:59.540378','2023-11-02 15:20:59.540386');
INSERT INTO images VALUES(64,'Radio france','/static/img/radio-france/5--2__9b7a3dd4-7395-4c96-894c-3ce7cdfd16b0.jpg',1,'lorem',2,5,'2023-11-02 15:21:09.902534','2023-11-02 15:21:09.902540');
INSERT INTO images VALUES(65,'Radio france','/static/img/radio-france/5--2__0908dae0-ec1b-4aa8-8b2f-571b94927ccb.jpg',1,'lorem',2,5,'2023-11-02 15:21:19.025388','2023-11-02 15:21:19.025393');
INSERT INTO images VALUES(66,'Journal LePoint','/static/img/journal-lepoint/6--2__0209fc52-8bf0-4bb3-8bb9-1f909b1632c9.jpg',1,'lorem',2,6,'2023-11-02 15:34:32.173195','2023-11-02 15:34:32.173201');
INSERT INTO images VALUES(67,'Journal LePoint','/static/img/journal-lepoint/6--2__fdef8ae1-6fa6-40b2-9e8b-05c29987336c.jpg',1,'lorem',2,6,'2023-11-02 15:34:41.301294','2023-11-02 15:34:41.301298');
INSERT INTO images VALUES(68,'Journal LePoint','/static/img/journal-lepoint/6--2__b15b0e69-12af-4a94-8495-ac4979b52ff3.jpg',1,'lorem',2,6,'2023-11-02 15:34:49.447894','2023-11-02 15:34:49.447901');
INSERT INTO images VALUES(69,'Palmares journal LePoint','/static/img/palmares-journal-lepoint/7--2__80fb5a8f-1537-4090-b08a-d55cc59f31b3.jpg',1,'lorem',2,7,'2023-11-02 16:38:23.951642','2023-11-02 16:38:23.951648');
INSERT INTO images VALUES(70,'Palmares journal LePoint','/static/img/palmares-journal-lepoint/7--2__e17dd7fe-457a-4979-88b6-bea8e6d5e10a.jpg',1,'lorem',2,7,'2023-11-02 16:38:36.746605','2023-11-02 16:38:36.746610');
INSERT INTO images VALUES(71,'Palmares journal LePoint','/static/img/palmares-journal-lepoint/7--2__c9ee1983-ed61-4fb9-9462-5ad95900afc1.jpg',1,'lorem',2,7,'2023-11-02 16:38:45.683475','2023-11-02 16:38:45.683479');
INSERT INTO images VALUES(72,'Palmares journal LePoint','/static/img/palmares-journal-lepoint/7--2__0d0824b3-2518-4214-9622-78efc4b0c668.jpg',1,'lorem',2,7,'2023-11-02 16:38:55.127868','2023-11-02 16:38:55.127876');
INSERT INTO images VALUES(73,'Palmares journal LePoint','/static/img/palmares-journal-lepoint/7--2__54afaef7-0aec-4eef-b42a-fc6f6e9817d4.jpg',1,'lorem',2,7,'2023-11-02 16:39:35.716041','2023-11-02 16:39:35.716047');
INSERT INTO images VALUES(74,'Palmares journal LePoint','/static/img/palmares-journal-lepoint/7--2__8c30f5c3-7118-4590-8d9a-7a765cb1268d.jpg',1,'lorem',2,7,'2023-11-02 16:39:42.394937','2023-11-02 16:39:42.394943');
INSERT INTO images VALUES(75,'Palmares journal LePoint','/static/img/palmares-journal-lepoint/7--2__99e432c9-d432-4c82-93a8-9c345728955d.jpg',1,'lorem',2,7,'2023-11-02 16:39:50.339086','2023-11-02 16:39:50.339091');
CREATE TABLE portfolios (
	id INTEGER NOT NULL,
	name VARCHAR(128) NOT NULL,
	slug VARCHAR(128),
	description TEXT,
	color VARCHAR(8) NOT NULL,
	created DATETIME,
	modified DATETIME,
	online SMALLINT,
	url VARCHAR(256) NOT NULL,
	functions_id INTEGER,
	sort INTEGER NOT NULL,
	year INTEGER,
	activities_id INTEGER,
	customer VARCHAR(128) NOT NULL,
	location VARCHAR(128) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(activities_id) REFERENCES activities (id),
	FOREIGN KEY(functions_id) REFERENCES functions (id)
);
INSERT INTO portfolios VALUES(1,'Leroy Merlin','leroy-merlin','Avoir la chance d''accompagner une refonte si ambitieuse est sans aucun doute un projet unique dans une carrière. La richesse incroyable de la marque et les enjeux e-commerce du projet ont largement contribué à animer mon quotidien pendant 2 ans et demie.  Ce fût une vraie la passion que j''ai pour cette enseigne. À noter que le projet a été récompensé. Aussi, leroymerlin.fr est dans le top 50 des sites préférés des Français. ','#379a2a','2021-11-16 00:26:14.261733','2025-03-20 17:32:44.917730',1,'https://www.leroymerlin.fr/',1,44,'2010 - 2012',7,'Business Lab','Nanterre');
INSERT INTO portfolios VALUES(2,'Areva','areva','Dans le monde en constante évolution de l''industrie de l''énergie, la collaboration et la communication internes sont essentielles. En tant que lead développeur frontend, j''ai participé à la création du réseau social en interne d''Areva, une plateforme qui favorise la connectivité, l''innovation et la collaboration au sein de cette entreprise leader du secteur nucléaire. Le projet fût récompensé et acclamé. ','#e83232','2021-11-16 00:26:46.458804','2025-03-20 17:32:44.909592',1,'http://areva.com',1,43,'2012 - 2013',11,'Business Lab - Areva','La Garenne Colombe');
INSERT INTO portfolios VALUES(3,'Honda moto','honda-moto','La refonte intégrale des sites web Honda Moto et Honda Moto Occasion a été un projet phare de ma carrière de développeur full-stack. Cette initiative a représenté une opportunité  pour mettre en valeur mon expertise en matière de développement web, couvrant à la fois le front-end et le back-end.','#000000','2021-11-16 00:27:37.201240','2025-03-20 17:32:44.742213',1,'https://moto.honda.fr/',1,12,'2016-2017',15,'Publicis - Prodigious','Paris 8');
INSERT INTO portfolios VALUES(4,'John Paul','john-paul','Au sein de l''équipe John Paul, j''ai eu le privilège de travailler en tant que développeur backend, une expérience passionnante qui m''a permis de contribuer de manière significative au succès continu de l''entreprise. Mon rôle principal consistait à assurer la maintenance et à apporter des améliorations essentielles aux projets.','#000000','2022-10-11 00:57:48.881997','2025-03-20 17:32:44.708550',1,'https://www.johnpaul.com/fr',2,2,'2021-2022',22,'John Paul','Paris');
INSERT INTO portfolios VALUES(5,'Radio france','radio-france','J''ai eu l''opportunité exceptionnelle de collaborer en tant que développeur fullstack sur le projet Radio France.fr. Cette expérience de coréalisation a été enrichissante à bien des égards. Elle m''a permis de contribuer de manière significative à la création d''une plateforme web de premier plan pour l''une des institutions culturelles les plus emblématiques de France.','#000000','2022-10-11 00:58:39.929821','2025-03-20 17:32:44.712537',1,'https://www.radiofrance.fr/',3,3,'2022-2023',21,'La Maison de la Radio','Paris 16');
INSERT INTO portfolios VALUES(6,'Journal LePoint','journal-lepoint','En qualité d''ingénieur cumulant les compétences front-end et back-end, j''ai eu l''opportunité de jouer un rôle déterminant dans l''évolution des plateformes numériques du journal renommé Le Point. Mon rôle consistait à garantir une expérience utilisateur de qualité tant sur leur site web que sur leur application mobile.','#000000','2022-10-11 01:00:00.252469','2025-03-20 17:32:44.715723',1,'https://www.lepoint.fr/',3,4,'2019-2021',20,'SEBDO','Paris 15');
INSERT INTO portfolios VALUES(7,'Palmares journal LePoint','palmares-journal-lepoint','L''une de mes réalisations les plus marquantes en tant qu''ingénieur a été la conception et la mise en place d''un système de palmarès complet pour le prestigieux journal Le Point. Mon rôle englobait à la fois le développement front-end et back-end, et incluait même la création d''applications spécifiques pour certains palmarès.','#000000','2022-10-11 01:00:38.134005','2025-03-20 17:32:44.719047',1,'https://www.lepoint.fr/',3,5,'2019-2021',20,'SEBDO','Paris 15');
INSERT INTO portfolios VALUES(8,'Carenity','carenity','L''une de mes réalisations notables en tant que développeur a été la refonte complète du backoffice et l''amélioration substantielle du système de questionnaire pour Carenity. Dans ce projet, j''ai été responsable du développement complet du front-end et du back-end, ce qui a été une expérience particulièrement enrichissante.','#000000','2022-10-11 01:02:00.841336','2025-03-20 17:32:44.722838',1,'https://www.carenity.com/',3,6,2019,14,'Carenity','Paris 9');
INSERT INTO portfolios VALUES(9,'Rimowa','rimowa','L''un de mes projets les plus gratifiants en tant que développeur a été la refonte totale du site e-commerce de la marque emblématique Rimowa. Dans cette entreprise, j''ai été co-responsable du développement complet, en prenant en charge à la fois le front-end et le back-end du site.','#000000','2022-10-11 01:03:00.947694','2025-03-20 17:32:44.726524',1,'https://www.rimowa.com/',3,7,2018,18,'Viseo','Boulogne');
INSERT INTO portfolios VALUES(10,'Longchamp','longchamp','La refonte du site e-commerce Longchamp était un défi passionnant, car elle visait à créer une plateforme en ligne à la hauteur de la renommée de cette marque maroquinerie de luxe. Ma mission consistait à m''assurer que le site alliait non seulement une esthétique attrayante, mais aussi des performances optimales, ainsi que la gestion efficace d''une large gamme de produits et d''options de personnalisation.','#000000','2022-10-11 01:04:18.637109','2025-03-20 17:32:44.729784',1,'https://www.longchamp.com',3,8,2018,23,'Creativ - Viseo','Paris 2');
INSERT INTO portfolios VALUES(11,'Cevital','cevital','J''ai eu l''occasion de mettre en œuvre ma passion et mon expertise en tant que développeur full-stack dans la réalisation du site vitrine du prestigieux groupe nord-africain Cevital. Cette expérience a été marquante, car elle m''a permis de contribuer de manière significative à la représentation en ligne de l''une des entreprises les plus influentes et diversifiées du Maghreb.','#000000','2022-10-11 01:05:22.502715','2025-03-20 17:32:44.736180',1,'https://www.cevital.com/',3,10,'2016-2017',17,'Publicis/Prodigious','Paris 8');
INSERT INTO portfolios VALUES(12,'Rene Furterer','rene-furterer','La refonte complète du projet René Furterer a représenté une étape significative dans mon parcours en tant que développeur full-stack. Ce projet a permis de mettre en avant mon expertise dans la création d''expériences numériques complètes, couvrant à la fois le développement front-end et back-end.','#000000','2022-10-11 01:06:18.358424','2025-03-20 17:32:44.739394',1,'https://www.renefurterer.com/fr-fr',3,11,'2016-2017',6,'Publicis - Razorfish','Paris 8');
INSERT INTO portfolios VALUES(13,'Dacia','dacia','J''ai joué un rôle essentiel dans la maintenance et l''évolution continue du projet Dacia Automobile, une tâche qui a demandé un engagement constant envers l''amélioration de l''expérience en ligne de cette marque automobile renommée.','#000000','2022-10-11 01:09:03.895334','2025-03-20 17:32:44.745111',1,'https://www.dacia.fr/',1,13,'2017-2018',2,'Publicis - Prodigious','Paris 8');
INSERT INTO portfolios VALUES(14,'UPSA','upsa','La refonte du site vitrine de l''UPSA a représenté une étape dans mon parcours en tant que développeur, où j''ai contribué à la modernisation de la présence en ligne de cette organisation pharmaceutique de renommée mondiale.','#000000','2022-10-11 01:11:01.320719','2025-03-20 17:32:44.748395',1,'https://www.upsa.com/',3,14,2017,14,'Publicis - Prodigious','Paris 8');
INSERT INTO portfolios VALUES(15,'Clio RS Melody','clio-rs-melody','La création de l''application web de Renault Clio RS melody fût une belle expérience qui plus fût récompensée par la profession et les médias. L''application événementielle Renault Clio RS Melody représente une innovation passionnante dans l''univers automobile, démontrant la capacité de Renault à combiner la technologie et la musique pour créer une expérience unique. Le spot publicitaire de l''application est ici https://www.dailymotion.com/video/x4xy0br','#000000','2022-10-11 01:11:38.295178','2025-03-20 17:32:44.751392',1,'http://clio-rs.renault.com',3,15,2016,2,'Publicis - Prodigious','Paris 8');
INSERT INTO portfolios VALUES(16,'Renault Kadjarquest','renault-kadjarquest','La création de l''application événementielle Renault Kadjarquest a été une initiative novatrice, marquant une étape significative dans la stratégie de Renault pour célébrer le lancement de son modèle emblématique, le Renault Kadjar. Cette application a été le fruit d''une collaboration étroite entre Renault et des experts en développement d''applications, visant à offrir une expérience unique aux passionnés de voitures.','#000000','2022-10-11 01:12:30.008611','2025-03-20 17:32:44.754779',1,'https://kadjarquest.renault.fr/',3,16,2017,2,'Publicis - Prodigious','Paris 8');
INSERT INTO portfolios VALUES(17,'Le Siège Renault','le-siege-renault','La refonte de l''application événementielle de Renault en tant que partenaire officiel du Festival de Deauville a été une initiative exceptionnelle, démontrant l''engagement de Renault envers l''innovation et la création d''expériences uniques pour les amateurs de cinéma et de voitures.','#000000','2022-10-11 01:13:04.615107','2025-03-20 17:32:44.757946',1,'http://lesiege.renault.fr',3,17,'2016-2017',2,'Publicis - Prodigious','Paris 8');
INSERT INTO portfolios VALUES(18,'Atelier Renault','atelier-renault','La maintenance en continu et les évolutions de l''application web de la boutique des Champs-Élysées Atelier Renault ont été une mission essentielle pour garantir une expérience en ligne exceptionnelle aux visiteurs de ce lieu emblématique dédié à l''automobile et à l''art de vivre à la française.','#000000','2022-10-11 01:14:03.558177','2025-03-20 17:32:44.761185',1,'https://atelier.renault.com/',3,18,2017,2,'Publicis - Prodigious','Paris 8');
INSERT INTO portfolios VALUES(19,'Aéroport de Paris','aeroport-de-paris','L''aéroport de Paris, en tant que plaque tournante majeure du voyage en Europe, est le théâtre de mouvements incessants, accueillant des millions de voyageurs du monde entier chaque année. Au cœur de cette mécanique complexe se trouve l''application web de l''aéroport de Paris, une ressource numérique cruciale pour les passagers et un outil de gestion essentiel pour l''aéroport lui-même.','#000000','2022-10-11 01:14:55.054868','2025-03-20 17:32:44.764495',1,'https://www.parisaeroport.fr/',1,19,'2015 - 2016',1,'Fullsix - ADP','Levallois Perret');
INSERT INTO portfolios VALUES(20,'Afflelou','afflelou','L''opticien Afflelou est une marque bien connue dans le monde de l''optique, offrant une large gamme de produits et de services pour la santé visuelle. Au cœur de leur engagement envers la satisfaction des clients se trouve leur application web, un outil numérique essentiel qui facilite la vie de ceux qui cherchent des solutions visuelles de qualité.','#000000','2022-10-11 01:15:43.892729','2025-03-20 17:32:44.767529',1,'https://www.afflelou.com/',1,20,'2015 - 2016',13,'Fullsix','Levallois Perret');
INSERT INTO portfolios VALUES(21,'Fullsix','fullsix','L''agence web FullSIX, reconnue pour son expertise dans le domaine du marketing digital et de la conception web, a entrepris une transformation significative en refondant son propre site web. Cette initiative démontre l''engagement continu de FullSIX à rester à la pointe de l''innovation dans un secteur en constante évolution.','#000000','2022-10-11 01:16:34.425394','2025-03-20 17:32:44.771069',1,'https://betcfullsix.com/',3,21,'2015 - 2016',19,'Fullsix','Levallois Perret');
INSERT INTO portfolios VALUES(22,'MyTravelChic','mytravelchic','La maintenance et l''évolution d''un site web de voyage en ligne sont essentielles pour garantir une bonne expérience utilisateur, tout en restant à la pointe de l''industrie du tourisme. Dans ce contexte, mes travaux sur le site de voyage en ligne MyTravelchic ont été un exemple remarquable d''engagement envers la qualité et l''innovation dans le secteur du voyage.','#000000','2022-10-11 01:18:18.346086','2025-03-20 17:32:44.777478',1,'https://www.idiliz.com/',1,22,2022,7,'groupe Bazarchic','Gennevillier');
INSERT INTO portfolios VALUES(23,'Bazarchic','bazarchic','Les sites de ventes privées ont révolutionné le monde du commerce en ligne en offrant aux consommateurs des offres exclusives sur des produits de qualité. Parmi ces plateformes, Bazarchic s''est distingué en tant que destination privilégiée pour les chasseurs de bonnes affaires. Cependant, pour rester à la pointe de l''industrie, j''ai effectué la refonte partielle, la maintenance et l''évolution de cette plateforme.','#000000','2022-10-11 01:18:53.155737','2025-03-20 17:32:44.784917',1,'https://fr.bazarchic.com/',1,23,2015,7,'groupe Bazarchic','Gennevillier');
INSERT INTO portfolios VALUES(24,'Brasserie Flo','brasserie-flo','La Brasserie Flo est une icône de la gastronomie française, offrant une expérience culinaire authentique et raffinée depuis des décennies. Pour assurer une présence en ligne à la hauteur de cette renommée, une série de sites web a été conçue et développée. En tant que concepteur, J''ai joué un rôle essentiel dans la création de ces plateformes numériques, visant à refléter l''excellence de la Brasserie Flo et à offrir aux visiteurs une excellente expérience en ligne.','#000000','2022-10-11 01:20:13.834067','2025-03-20 17:32:44.793131',1,'https://www.groupeflo.com/',3,24,2011,4,'Groupe Flo','Nanterre');
INSERT INTO portfolios VALUES(25,'Dyson affaire airblade','dyson-affaire-airblade','L''intranet commercial Dyson Airblade est un outil vital pour une entreprise qui a révolutionné le domaine de la technologie de séchage des mains. Pour assurer une interface intuitive, efficace et conviviale pour les équipes commerciales et les partenaires, une conception exceptionnelle était cruciale. En tant que concepteur, j''ai joué un rôle central dans la création de cet intranet, apportant une expertise en design.','#000000','2022-10-11 01:21:00.474761','2025-03-20 17:32:44.801130',1,'https://www.youtube.com/watch?v=jU0WojRkd30',3,25,2012,12,'Business Lab','Nanterre');
INSERT INTO portfolios VALUES(26,'Peugeot Design Lab','peugeot-design-lab','Peugeot Design Lab, une division de la célèbre marque automobile Peugeot, est synonyme d''innovation, de design novateur et d''excellence créative. En tant que concepteur, j''ai eu l''opportunité de participer à la refonte de cette entité de renom. Mes travaux ont contribué à redéfinir et à moderniser l''image du Peugeot Design Lab, un laboratoire de design réputé pour son expertise en conception industrielle, son sens du détail et sa passion pour l''innovation.','#000000','2022-10-11 01:21:46.168850','2025-03-20 17:32:44.809597',1,'http://www.peugeotdesignlab.com/fr',1,26,2012,2,'Business Lab','Nanterre');
INSERT INTO portfolios VALUES(27,'Peugeot','peugeot','La refonte d''une marque emblématique telle que Peugeot est une tâche colossale qui nécessite une expertise technique de haut niveau. Il est à noter que le projet fût récompensé par un topcom or','#000000','2022-10-11 01:22:22.839410','2025-03-20 17:32:44.817410',1,'https://www.peugeot.fr/',1,27,2012,2,'Business Lab','Nanterre');
INSERT INTO portfolios VALUES(28,'Peugeot 4008','peugeot-4008',replace(replace('Peugeot lance en avril 2012 un nouveau SUV, Peugeot 4008, sur un marché très dynamique et fortement concurrentiel, donc avec une problématique majeure d’émergence sur sa catégorie. Peugeot a souhaité une campagne originale dans sa forme et dans son contenu, et proposant une expérience interactive innovante avec le modèle.  Une opération 100% YouTube (custom channel + relais display) combinant une logique d’engagement via un parcours vidéo ludique de « quête » du véhicule et une mécanique d’acquisition performante via un jeu concours. Un lancement full digital inédit, réalisé en seulement 4 semaines et en étroite collaboration avec les équipes Google. Top Com d''Or (catégorie site événementiel)\r\n','\r',char(13)),'\n',char(10)),'#000000','2022-10-11 01:22:58.225405','2025-03-20 17:32:44.825894',1,'https://www.youtube.com/watch?v=p9SJQjioTb0',1,28,2012,2,'Business Lab','Nanterre');
INSERT INTO portfolios VALUES(29,'Flyopenskies v2','flyopenskies-v2','L''aviation a toujours été un symbole de liberté, de découverte et de connexion. Dans un monde en constante évolution, les compagnies aériennes jouent un rôle clé dans la réalisation de ces aspirations. C''est avec une profonde passion pour l''aviation et un dévouement envers l''innovation que nous avons entrepris la refonte des sites web de FlyOpenSky.','#000000','2022-10-11 01:23:42.488045','2025-03-20 17:32:44.832478',1,'http://www.flyopenskies.com/',1,29,2010,1,'Business Lab - Amadeus','Nanterre');
INSERT INTO portfolios VALUES(30,'Flyopenskies v3','flyopenskies-v3','L''aviation a toujours été un symbole de liberté, de découverte et de connexion. Dans un monde en constante évolution, les compagnies aériennes jouent un rôle clé dans la réalisation de ces aspirations. C''est avec une profonde passion pour l''aviation et un dévouement envers l''innovation que nous avons entrepris la refonte des sites web de FlyOpenSky.','#000000','2022-10-11 01:24:03.610475','2025-03-20 17:32:44.838232',1,'http://www.flyopenskies.com/',1,30,2011,1,'Business Lab - Amadeus','Nanterre');
INSERT INTO portfolios VALUES(31,'Europcar','europcar','La refonte du site web Europcar représente bien plus qu''un simple rafraîchissement visuel. C''est le fruit d''un engagement à innover et à améliorer l''expérience des clients. Nous avons recréé une plateforme en ligne qui reflète la passion pour la mobilité, et à offrir des services de location de voitures de premier ordre.','#000000','2022-10-11 01:24:50.015014','2025-03-20 17:32:44.842875',1,'https://www.europcar.fr',1,31,2011,2,'Business Lab','Nanterre');
INSERT INTO portfolios VALUES(32,'Air Caraïbes','air-caraibes','Le voyage aérien a le pouvoir de créer des souvenirs inoubliables, de connecter des cultures et d''inspirer l''exploration. Air Caraïbes, une icône du ciel caribéen, a toujours compris cette magie du voyage. J''ai été ravi de présenter la refonte complète du site d''Air Caraïbes, une transformation qui redéfinissait la manière dont les clients planifiaient et réservaient leurs voyages vers les Caraïbes.','#000000','2022-10-11 01:25:35.064979','2025-03-20 17:32:44.846910',1,'https://www.aircaraibes.com/',1,32,'2011 - 2012',1,'Business Lab - Amadeus','Nanterre');
INSERT INTO portfolios VALUES(33,'Air Madagascar','air-madagascar','Le voyage aérien, c''est bien plus que le simple déplacement d''un point A à un point B. C''est l''opportunité de créer des souvenirs inoubliables, de découvrir de nouvelles cultures et de vivre des aventures qui marquent une vie. En tant que développeur frontend, j''ai eu le privilège de jouer un rôle essentiel dans la refonte du site web d''Air Madagascar, une compagnie aérienne nationale qui symbolise la porte d''entrée vers la magnifique île de Madagascar.','#000000','2022-10-11 01:26:24.544751','2025-03-20 17:32:44.850785',1,'https://madagascarairlines.com',1,33,'2011 - 2012',1,'Business Lab - Amadeus','Nanterre');
INSERT INTO portfolios VALUES(34,'CFC','cfc','La préservation et la promotion de la propriété intellectuelle sont au cœur de la diffusion du savoir, de la culture et de l''innovation. En tant que développeur frontend et backend, j''ai joué un rôle primordial dans la refonte du site du Centre Français d''Exploitation du Droit de Copie (CFC), une institution majeure dans la gestion des droits d''auteur pour les copies papier et numériques de publications en France.','#000000','2022-10-11 01:27:15.632311','2025-03-20 17:32:44.855426',1,'https://www.cfcopies.com/',3,34,'2012 - 2013',10,'Business Lab','Nanterre');
INSERT INTO portfolios VALUES(35,'Algeco','algeco','En tant que développeur frontend et backend, j''ai eu l''opportunité de participer à la refonte du site Ageco.fr, une référence en matière de bâtiments modulaires pour une économie locale et durable. Que ce soit des bureaux modulaires, des bungalows de chantier ou des écoles modulaires, ma mission était de rendre accessible à tous les avantages de la construction modulaire.','#000000','2022-10-11 01:28:11.110968','2025-03-20 17:32:44.859929',1,'https://www.algeco.fr/',3,35,'2011-2012',9,'Business Lab','Nanterre');
INSERT INTO portfolios VALUES(36,'Fidelity Vie','fidelity-vie','L''assurance vie est bien plus qu''un simple contrat financier. C''est une garantie de sécurité pour l''avenir, une assurance pour vos proches et un moyen de bâtir un patrimoine durable. En tant que développeur frontend et backend, j''ai eu le privilège de jouer un rôle central dans la refonte du site fidelityvie.fr, une plateforme dédiée au contrat d''assurance vie qui incarne la confiance et la prévoyance financière.','#000000','2022-10-11 01:28:48.948470','2025-03-20 17:32:44.863857',1,'https://www.fidelityvie.fr',3,36,2012,5,'Business Lab','Nanterre');
INSERT INTO portfolios VALUES(37,'De quoi je me M.E.L','de-quoi-je-me-mel','La communication numérique est devenue le reflet de la connaissance et de l''expertise, un moyen d''échanger des idées et de partager des visions. En tant que développeur frontend, nous avons refait à la demande Michel-Édouard Leclerc son blog. Une plateforme qui incarne la voix d''un expert renommé en économie et en commerce.','#000000','2022-10-11 01:29:51.169233','2025-03-20 17:32:44.867903',1,'https://www.michel-edouard-leclerc.com/',1,37,2011,8,'Business Lab','Nanterre');
INSERT INTO portfolios VALUES(38,'Qui est le moins cher','qui-est-le-moins-cher','Dans un monde où l''efficacité et l''accessibilité sont des atouts majeurs, le site "Qui Est le Moins Cher" se distingue par son engagement à offrir des offres inégalables. En tant que développeur frontend, j''ai eu l''opportunité de contribuer à la refonte de cette plateforme, qui incarne la recherche des meilleures affaires et des prix les plus compétitifs.','#000000','2022-10-11 01:30:37.402401','2025-03-20 17:32:44.872012',1,'https://www.quiestlemoinscher.leclerc/',1,38,2012,4,'Business Lab','Nanterre');
INSERT INTO portfolios VALUES(39,'Decolor Stop','decolor-stop','La préservation de la qualité et de la longévité des vêtements et du linge de maison est une préoccupation majeure de la vie quotidienne. En tant que développeur frontend, j''ai contribué à la maintenance et à l''amélioration en continu du site Decolor Stop','#000000','2022-10-11 01:31:22.707267','2025-03-20 17:32:44.875886',1,'https://www.decolorstop.com/',1,39,'2010 - 2013',6,'Business Lab','Nanterre');
INSERT INTO portfolios VALUES(40,'My Peugeot','my-peugeot','L''automobile, c''est bien plus qu''un simple moyen de transport. C''est une expérience de mobilité, de confort et de fiabilité. En tant que lead développeur frontend, j''ai participé à la refonte du site My Peugeot, l''espace client de Peugeot, un espace en ligne qui incarne l''engagement envers l''excellence du service client.','#000000','2022-10-11 01:32:03.504933','2025-03-20 17:32:44.883215',1,'https://mypeugeot.peugeot.fr/',1,40,'2011 - 2012',2,'Business Lab - Argonautes','Nanterre');
INSERT INTO portfolios VALUES(41,'banque casino','banque-casino','L''efficacité de la communication numérique est cruciale, en particulier dans le secteur financier où la confiance et la transparence sont essentielles. En tant que lead développeur frontend, j''ai participé à la création de templates email pour Banque Casino, une institution financière de renom qui place ses clients au cœur de son engagement.','#000000','2022-10-11 01:32:45.499031','2025-03-20 17:32:44.892298',1,'https://client.floabank.fr/',1,41,2013,5,'Business Lab','Nanterre');
INSERT INTO portfolios VALUES(42,'leperon','leperon','L''univers du sport équestre est en constante évolution, et l''accès à l''information à jour est crucial pour les passionnés. En tant que lead développeur frontend, j''ai maintenu et fait évoluer le site Cavadeos (leperon.fr), la référence en matière d''actualité cheval et d''informations équestres.','#000000','2022-10-11 01:33:35.138960','2025-03-20 17:32:44.901113',1,'https://www.leperon.fr/',1,42,'2011 - 2013',3,'Business Lab','Nanterre');
INSERT INTO portfolios VALUES(43,'Sacla','sacla','La cuisine, c''est bien plus qu''une simple préparation de repas, c''est une expérience sensorielle et une exploration de saveurs. En tant que lead développeur frontend, j''ai coréalisé le site de Sacla, une entreprise renommée pour ses produits alimentaires de qualité et ses délices culinaires.','#000000','2022-10-11 01:34:04.558689','2025-03-20 17:32:44.926170',1,'https://sacla.fr/',1,45,2010,4,'Business Lab','Nanterre');
INSERT INTO portfolios VALUES(44,'Confbox','confbox','La refonte du projet Confbox, un système de conférence en ligne, a été une expérience de conception exceptionnelle à laquelle j''ai eu le privilège d''être concepteur et architecte. Cette refonte a été l''occasion de mettre en avant ma passion pour l''innovation en matière de communication virtuelle et ma capacité à créer des solutions technologiques de pointe.','#000000','2023-10-16 13:22:35.476962','2025-03-20 17:32:44.732860',1,'http://confbox.com',3,9,2018,19,'Creativ','Paris');
INSERT INTO portfolios VALUES(45,'sfr','sfr','SFR, un acteur de premier plan dans le secteur des télécommunications en France. En tant que développeur frontend et backend, j''ai eu l''opportunité de coréaliser des modules personnalisés sur le site de SFR.  ','#000000','2023-10-16 14:03:30.403380','2025-03-20 17:32:44.932823',1,'https://sfr.fr',3,46,2017,17,'Publicis - Prodigious','Paris 8');
INSERT INTO portfolios VALUES(46,'Se soigner moins cher','se-soigner-moins-cher','Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet laborum illum maxime iusto minima reiciendis praesentium labore ab, sed sapiente officia enim consequuntur atque non rerum nostrum quibusdam rem molestiae!','#000000','2023-10-18 17:09:02.706181','2025-03-20 17:32:44.939665',1,'https://www.e.leclerc/cat/parapharmacie',1,47,2013,7,'Business Lab','Nanterre');
INSERT INTO portfolios VALUES(47,'histoire et archives leclerc','histoire-et-archives-leclerc','Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet laborum illum maxime iusto minima reiciendis praesentium labore ab, sed sapiente officia enim consequuntur atque non rerum nostrum quibusdam rem molestiae!','#000000','2023-10-18 17:48:17.243438','2025-03-20 17:32:44.946118',1,'https://www.histoireetarchives.leclerc/',1,48,2012,7,'Business Lab','Nanterre');
INSERT INTO portfolios VALUES(48,'le mouvement leclerc','le-mouvement-leclerc','Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet laborum illum maxime iusto minima reiciendis praesentium labore ab, sed sapiente officia enim consequuntur atque non rerum nostrum quibusdam rem molestiae!','#000000','2023-10-18 17:49:26.231134','2025-03-20 17:32:44.952645',1,'https://www.mouvement.leclerc/',1,49,2011,7,'Business Lab','Nanterre');
INSERT INTO portfolios VALUES(49,'emag sfr','emag-sfr','Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet laborum illum maxime iusto minima reiciendis praesentium labore ab, sed sapiente officia enim consequuntur atque non rerum nostrum quibusdam rem molestiae!','#000000','2023-10-18 19:03:09.387037','2025-03-20 17:32:44.958604',1,'https://sfr.fr',3,50,2017,20,'Publicis - Prodigious','Paris 8');
INSERT INTO portfolios VALUES(50,'Europcar-up','europcar-up','Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet laborum illum maxime iusto minima reiciendis praesentium labore ab, sed sapiente officia enim consequuntur atque non rerum nostrum quibusdam rem molestiae!','#000000','2023-10-18 19:11:37.702563','2025-03-20 17:32:44.963469',1,'http://europcar.com',3,51,2011,2,'Business Lab','Nanterre');
INSERT INTO portfolios VALUES(51,'Believe','believe',replace(replace('J''ai récemment eu l''opportunité de participer à la refonte de l''application musicale Smart Entry. Mon rôle principal a été de moderniser et d''améliorer l''interface utilisateur pour offrir une expérience plus fluide et intuitive aux utilisateurs. En outre, j''ai développé un système de traduction intégré, permettant à Smart Entry de devenir accessible à un public international en 17 langues. Cette expérience enrichissante m''a permis de combiner mes compétences techniques et créatives pour apporter des solutions innovantes et améliorer l''accessibilité de l''application.\r\n','\r',char(13)),'\n',char(10)),'#000000','2024-07-23 10:49:28.336918','2025-03-20 17:32:44.703909',1,'https://www.believe.com/',3,1,2024,24,'Believe','St Ouen');
CREATE TABLE portfolios_technologies (
	id INTEGER NOT NULL,
	technologies_id INTEGER,
	portfolios_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(portfolios_id) REFERENCES portfolios (id),
	FOREIGN KEY(technologies_id) REFERENCES technologies (id)
);
INSERT INTO portfolios_technologies VALUES(433,6,4);
INSERT INTO portfolios_technologies VALUES(434,7,4);
INSERT INTO portfolios_technologies VALUES(435,14,4);
INSERT INTO portfolios_technologies VALUES(436,19,4);
INSERT INTO portfolios_technologies VALUES(492,1,5);
INSERT INTO portfolios_technologies VALUES(493,2,5);
INSERT INTO portfolios_technologies VALUES(494,3,5);
INSERT INTO portfolios_technologies VALUES(495,10,5);
INSERT INTO portfolios_technologies VALUES(496,12,5);
INSERT INTO portfolios_technologies VALUES(509,1,8);
INSERT INTO portfolios_technologies VALUES(510,2,8);
INSERT INTO portfolios_technologies VALUES(511,3,8);
INSERT INTO portfolios_technologies VALUES(512,4,8);
INSERT INTO portfolios_technologies VALUES(513,5,8);
INSERT INTO portfolios_technologies VALUES(514,6,8);
INSERT INTO portfolios_technologies VALUES(515,9,8);
INSERT INTO portfolios_technologies VALUES(516,1,9);
INSERT INTO portfolios_technologies VALUES(517,2,9);
INSERT INTO portfolios_technologies VALUES(518,3,9);
INSERT INTO portfolios_technologies VALUES(519,9,9);
INSERT INTO portfolios_technologies VALUES(520,1,10);
INSERT INTO portfolios_technologies VALUES(521,2,10);
INSERT INTO portfolios_technologies VALUES(522,3,10);
INSERT INTO portfolios_technologies VALUES(523,9,10);
INSERT INTO portfolios_technologies VALUES(536,1,11);
INSERT INTO portfolios_technologies VALUES(537,2,11);
INSERT INTO portfolios_technologies VALUES(538,3,11);
INSERT INTO portfolios_technologies VALUES(539,4,11);
INSERT INTO portfolios_technologies VALUES(540,5,11);
INSERT INTO portfolios_technologies VALUES(541,18,11);
INSERT INTO portfolios_technologies VALUES(548,1,7);
INSERT INTO portfolios_technologies VALUES(549,2,7);
INSERT INTO portfolios_technologies VALUES(550,3,7);
INSERT INTO portfolios_technologies VALUES(551,6,7);
INSERT INTO portfolios_technologies VALUES(552,7,7);
INSERT INTO portfolios_technologies VALUES(553,14,7);
INSERT INTO portfolios_technologies VALUES(554,1,44);
INSERT INTO portfolios_technologies VALUES(555,2,44);
INSERT INTO portfolios_technologies VALUES(556,3,44);
INSERT INTO portfolios_technologies VALUES(557,6,44);
INSERT INTO portfolios_technologies VALUES(558,7,44);
INSERT INTO portfolios_technologies VALUES(559,12,44);
INSERT INTO portfolios_technologies VALUES(600,1,12);
INSERT INTO portfolios_technologies VALUES(601,2,12);
INSERT INTO portfolios_technologies VALUES(602,3,12);
INSERT INTO portfolios_technologies VALUES(603,6,12);
INSERT INTO portfolios_technologies VALUES(604,7,12);
INSERT INTO portfolios_technologies VALUES(605,14,12);
INSERT INTO portfolios_technologies VALUES(606,1,3);
INSERT INTO portfolios_technologies VALUES(607,2,3);
INSERT INTO portfolios_technologies VALUES(608,3,3);
INSERT INTO portfolios_technologies VALUES(609,6,3);
INSERT INTO portfolios_technologies VALUES(610,7,3);
INSERT INTO portfolios_technologies VALUES(611,1,13);
INSERT INTO portfolios_technologies VALUES(612,2,13);
INSERT INTO portfolios_technologies VALUES(613,3,13);
INSERT INTO portfolios_technologies VALUES(614,4,13);
INSERT INTO portfolios_technologies VALUES(615,5,13);
INSERT INTO portfolios_technologies VALUES(616,1,14);
INSERT INTO portfolios_technologies VALUES(617,2,14);
INSERT INTO portfolios_technologies VALUES(618,3,14);
INSERT INTO portfolios_technologies VALUES(619,6,14);
INSERT INTO portfolios_technologies VALUES(620,7,14);
INSERT INTO portfolios_technologies VALUES(653,1,22);
INSERT INTO portfolios_technologies VALUES(654,2,22);
INSERT INTO portfolios_technologies VALUES(655,3,22);
INSERT INTO portfolios_technologies VALUES(656,18,22);
INSERT INTO portfolios_technologies VALUES(657,1,23);
INSERT INTO portfolios_technologies VALUES(658,2,23);
INSERT INTO portfolios_technologies VALUES(659,3,23);
INSERT INTO portfolios_technologies VALUES(660,12,23);
INSERT INTO portfolios_technologies VALUES(677,1,26);
INSERT INTO portfolios_technologies VALUES(678,2,26);
INSERT INTO portfolios_technologies VALUES(679,3,26);
INSERT INTO portfolios_technologies VALUES(680,18,26);
INSERT INTO portfolios_technologies VALUES(760,1,41);
INSERT INTO portfolios_technologies VALUES(761,2,41);
INSERT INTO portfolios_technologies VALUES(762,3,41);
INSERT INTO portfolios_technologies VALUES(763,12,41);
INSERT INTO portfolios_technologies VALUES(764,15,41);
INSERT INTO portfolios_technologies VALUES(765,1,42);
INSERT INTO portfolios_technologies VALUES(766,2,42);
INSERT INTO portfolios_technologies VALUES(767,3,42);
INSERT INTO portfolios_technologies VALUES(768,18,42);
INSERT INTO portfolios_technologies VALUES(769,1,2);
INSERT INTO portfolios_technologies VALUES(770,2,2);
INSERT INTO portfolios_technologies VALUES(771,3,2);
INSERT INTO portfolios_technologies VALUES(772,12,2);
INSERT INTO portfolios_technologies VALUES(773,18,2);
INSERT INTO portfolios_technologies VALUES(774,1,1);
INSERT INTO portfolios_technologies VALUES(775,2,1);
INSERT INTO portfolios_technologies VALUES(776,3,1);
INSERT INTO portfolios_technologies VALUES(777,4,1);
INSERT INTO portfolios_technologies VALUES(778,18,1);
INSERT INTO portfolios_technologies VALUES(783,1,45);
INSERT INTO portfolios_technologies VALUES(784,2,45);
INSERT INTO portfolios_technologies VALUES(785,3,45);
INSERT INTO portfolios_technologies VALUES(786,6,45);
INSERT INTO portfolios_technologies VALUES(787,7,45);
INSERT INTO portfolios_technologies VALUES(788,14,45);
INSERT INTO portfolios_technologies VALUES(789,1,46);
INSERT INTO portfolios_technologies VALUES(790,2,46);
INSERT INTO portfolios_technologies VALUES(791,3,46);
INSERT INTO portfolios_technologies VALUES(792,18,46);
INSERT INTO portfolios_technologies VALUES(797,1,48);
INSERT INTO portfolios_technologies VALUES(798,2,48);
INSERT INTO portfolios_technologies VALUES(799,3,48);
INSERT INTO portfolios_technologies VALUES(800,18,48);
INSERT INTO portfolios_technologies VALUES(801,1,47);
INSERT INTO portfolios_technologies VALUES(802,2,47);
INSERT INTO portfolios_technologies VALUES(803,3,47);
INSERT INTO portfolios_technologies VALUES(804,18,47);
INSERT INTO portfolios_technologies VALUES(805,1,24);
INSERT INTO portfolios_technologies VALUES(806,2,24);
INSERT INTO portfolios_technologies VALUES(807,3,24);
INSERT INTO portfolios_technologies VALUES(808,4,24);
INSERT INTO portfolios_technologies VALUES(809,5,24);
INSERT INTO portfolios_technologies VALUES(810,18,24);
INSERT INTO portfolios_technologies VALUES(811,1,49);
INSERT INTO portfolios_technologies VALUES(812,2,49);
INSERT INTO portfolios_technologies VALUES(813,3,49);
INSERT INTO portfolios_technologies VALUES(814,6,49);
INSERT INTO portfolios_technologies VALUES(815,7,49);
INSERT INTO portfolios_technologies VALUES(816,9,49);
INSERT INTO portfolios_technologies VALUES(817,12,49);
INSERT INTO portfolios_technologies VALUES(818,14,49);
INSERT INTO portfolios_technologies VALUES(819,1,50);
INSERT INTO portfolios_technologies VALUES(820,2,50);
INSERT INTO portfolios_technologies VALUES(821,3,50);
INSERT INTO portfolios_technologies VALUES(822,4,50);
INSERT INTO portfolios_technologies VALUES(823,5,50);
INSERT INTO portfolios_technologies VALUES(824,18,50);
INSERT INTO portfolios_technologies VALUES(825,1,25);
INSERT INTO portfolios_technologies VALUES(826,2,25);
INSERT INTO portfolios_technologies VALUES(827,3,25);
INSERT INTO portfolios_technologies VALUES(828,4,25);
INSERT INTO portfolios_technologies VALUES(829,5,25);
INSERT INTO portfolios_technologies VALUES(830,18,25);
INSERT INTO portfolios_technologies VALUES(831,1,15);
INSERT INTO portfolios_technologies VALUES(832,2,15);
INSERT INTO portfolios_technologies VALUES(833,3,15);
INSERT INTO portfolios_technologies VALUES(834,9,15);
INSERT INTO portfolios_technologies VALUES(835,12,15);
INSERT INTO portfolios_technologies VALUES(836,13,15);
INSERT INTO portfolios_technologies VALUES(837,1,16);
INSERT INTO portfolios_technologies VALUES(838,2,16);
INSERT INTO portfolios_technologies VALUES(839,3,16);
INSERT INTO portfolios_technologies VALUES(840,6,16);
INSERT INTO portfolios_technologies VALUES(841,7,16);
INSERT INTO portfolios_technologies VALUES(842,1,17);
INSERT INTO portfolios_technologies VALUES(843,2,17);
INSERT INTO portfolios_technologies VALUES(844,3,17);
INSERT INTO portfolios_technologies VALUES(845,6,17);
INSERT INTO portfolios_technologies VALUES(846,7,17);
INSERT INTO portfolios_technologies VALUES(847,1,18);
INSERT INTO portfolios_technologies VALUES(848,2,18);
INSERT INTO portfolios_technologies VALUES(849,3,18);
INSERT INTO portfolios_technologies VALUES(850,6,18);
INSERT INTO portfolios_technologies VALUES(851,7,18);
INSERT INTO portfolios_technologies VALUES(852,9,18);
INSERT INTO portfolios_technologies VALUES(853,19,18);
INSERT INTO portfolios_technologies VALUES(854,1,19);
INSERT INTO portfolios_technologies VALUES(855,2,19);
INSERT INTO portfolios_technologies VALUES(856,3,19);
INSERT INTO portfolios_technologies VALUES(857,12,19);
INSERT INTO portfolios_technologies VALUES(858,1,20);
INSERT INTO portfolios_technologies VALUES(859,2,20);
INSERT INTO portfolios_technologies VALUES(860,3,20);
INSERT INTO portfolios_technologies VALUES(861,9,20);
INSERT INTO portfolios_technologies VALUES(862,12,20);
INSERT INTO portfolios_technologies VALUES(863,1,21);
INSERT INTO portfolios_technologies VALUES(864,2,21);
INSERT INTO portfolios_technologies VALUES(865,3,21);
INSERT INTO portfolios_technologies VALUES(866,12,21);
INSERT INTO portfolios_technologies VALUES(867,1,27);
INSERT INTO portfolios_technologies VALUES(868,2,27);
INSERT INTO portfolios_technologies VALUES(869,3,27);
INSERT INTO portfolios_technologies VALUES(870,18,27);
INSERT INTO portfolios_technologies VALUES(871,1,28);
INSERT INTO portfolios_technologies VALUES(872,2,28);
INSERT INTO portfolios_technologies VALUES(873,3,28);
INSERT INTO portfolios_technologies VALUES(874,4,28);
INSERT INTO portfolios_technologies VALUES(875,5,28);
INSERT INTO portfolios_technologies VALUES(876,18,28);
INSERT INTO portfolios_technologies VALUES(877,1,6);
INSERT INTO portfolios_technologies VALUES(878,2,6);
INSERT INTO portfolios_technologies VALUES(879,3,6);
INSERT INTO portfolios_technologies VALUES(880,4,6);
INSERT INTO portfolios_technologies VALUES(881,9,6);
INSERT INTO portfolios_technologies VALUES(882,1,29);
INSERT INTO portfolios_technologies VALUES(883,2,29);
INSERT INTO portfolios_technologies VALUES(884,3,29);
INSERT INTO portfolios_technologies VALUES(885,18,29);
INSERT INTO portfolios_technologies VALUES(886,1,30);
INSERT INTO portfolios_technologies VALUES(887,2,30);
INSERT INTO portfolios_technologies VALUES(888,3,30);
INSERT INTO portfolios_technologies VALUES(889,18,30);
INSERT INTO portfolios_technologies VALUES(890,1,31);
INSERT INTO portfolios_technologies VALUES(891,2,31);
INSERT INTO portfolios_technologies VALUES(892,3,31);
INSERT INTO portfolios_technologies VALUES(893,18,31);
INSERT INTO portfolios_technologies VALUES(894,1,32);
INSERT INTO portfolios_technologies VALUES(895,2,32);
INSERT INTO portfolios_technologies VALUES(896,3,32);
INSERT INTO portfolios_technologies VALUES(897,18,32);
INSERT INTO portfolios_technologies VALUES(898,1,33);
INSERT INTO portfolios_technologies VALUES(899,2,33);
INSERT INTO portfolios_technologies VALUES(900,3,33);
INSERT INTO portfolios_technologies VALUES(901,18,33);
INSERT INTO portfolios_technologies VALUES(902,1,34);
INSERT INTO portfolios_technologies VALUES(903,2,34);
INSERT INTO portfolios_technologies VALUES(904,3,34);
INSERT INTO portfolios_technologies VALUES(905,4,34);
INSERT INTO portfolios_technologies VALUES(906,5,34);
INSERT INTO portfolios_technologies VALUES(907,18,34);
INSERT INTO portfolios_technologies VALUES(908,1,35);
INSERT INTO portfolios_technologies VALUES(909,2,35);
INSERT INTO portfolios_technologies VALUES(910,3,35);
INSERT INTO portfolios_technologies VALUES(911,4,35);
INSERT INTO portfolios_technologies VALUES(912,5,35);
INSERT INTO portfolios_technologies VALUES(913,18,35);
INSERT INTO portfolios_technologies VALUES(914,1,36);
INSERT INTO portfolios_technologies VALUES(915,2,36);
INSERT INTO portfolios_technologies VALUES(916,3,36);
INSERT INTO portfolios_technologies VALUES(917,4,36);
INSERT INTO portfolios_technologies VALUES(918,5,36);
INSERT INTO portfolios_technologies VALUES(919,18,36);
INSERT INTO portfolios_technologies VALUES(920,1,37);
INSERT INTO portfolios_technologies VALUES(921,2,37);
INSERT INTO portfolios_technologies VALUES(922,3,37);
INSERT INTO portfolios_technologies VALUES(923,4,37);
INSERT INTO portfolios_technologies VALUES(924,5,37);
INSERT INTO portfolios_technologies VALUES(925,1,38);
INSERT INTO portfolios_technologies VALUES(926,2,38);
INSERT INTO portfolios_technologies VALUES(927,3,38);
INSERT INTO portfolios_technologies VALUES(928,1,39);
INSERT INTO portfolios_technologies VALUES(929,2,39);
INSERT INTO portfolios_technologies VALUES(930,3,39);
INSERT INTO portfolios_technologies VALUES(931,18,39);
INSERT INTO portfolios_technologies VALUES(932,1,40);
INSERT INTO portfolios_technologies VALUES(933,2,40);
INSERT INTO portfolios_technologies VALUES(934,3,40);
INSERT INTO portfolios_technologies VALUES(935,18,40);
INSERT INTO portfolios_technologies VALUES(936,1,43);
INSERT INTO portfolios_technologies VALUES(937,2,43);
INSERT INTO portfolios_technologies VALUES(938,3,43);
INSERT INTO portfolios_technologies VALUES(939,18,43);
INSERT INTO portfolios_technologies VALUES(940,1,51);
INSERT INTO portfolios_technologies VALUES(941,2,51);
INSERT INTO portfolios_technologies VALUES(942,3,51);
INSERT INTO portfolios_technologies VALUES(943,6,51);
INSERT INTO portfolios_technologies VALUES(944,10,51);
INSERT INTO portfolios_technologies VALUES(945,12,51);
INSERT INTO portfolios_technologies VALUES(946,20,51);
COMMIT;
