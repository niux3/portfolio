--
-- PostgreSQL database dump
--

-- Dumped from database version 13.21 (Debian 13.21-0+deb11u1)
-- Dumped by pg_dump version 13.21 (Debian 13.21-0+deb11u1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: renaud
--

INSERT INTO alembic_version VALUES ('ca25c63cf85e');


--
-- Data for Name: project_activities; Type: TABLE DATA; Schema: public; Owner: renaud
--

INSERT INTO project_activities VALUES (1, 'aviation', 'fa-solid fa-plane');
INSERT INTO project_activities VALUES (2, 'automobile', 'fa-solid fa-car');
INSERT INTO project_activities VALUES (3, 'sports équestres', 'fa-solid fa-horse');
INSERT INTO project_activities VALUES (4, 'alimentation', 'fa-solid fa-utensils');
INSERT INTO project_activities VALUES (5, 'finance', 'fa-solid fa-piggy-bank');
INSERT INTO project_activities VALUES (6, 'hygiène', 'fa-solid fa-soap');
INSERT INTO project_activities VALUES (7, 'e-commerce', 'fa-solid fa-cart-shopping');
INSERT INTO project_activities VALUES (8, 'blog', 'fa-brands fa-blogger');
INSERT INTO project_activities VALUES (9, 'construction', 'fa-solid fa-person-digging');
INSERT INTO project_activities VALUES (10, 'livres', 'fa-solid fa-book');
INSERT INTO project_activities VALUES (11, 'nucléaire', 'fa-solid fa-radiation');
INSERT INTO project_activities VALUES (12, 'électroménager', 'fa-solid fa-blender-phone');
INSERT INTO project_activities VALUES (13, 'opticien', 'fa-solid fa-glasses');
INSERT INTO project_activities VALUES (14, 'santé', 'fa-solid fa-notes-medical');
INSERT INTO project_activities VALUES (15, 'motocyclette', 'fa-solid fa-motorcycle');
INSERT INTO project_activities VALUES (16, 'coiffure', 'fa-solid fa-scissors');
INSERT INTO project_activities VALUES (17, 'grande distibution', 'fa-solid fa-shirt');
INSERT INTO project_activities VALUES (18, 'bagage', 'fa-solid fa-suitcase-rolling');
INSERT INTO project_activities VALUES (19, 'réseau social', 'fa-solid fa-people-arrows');
INSERT INTO project_activities VALUES (20, 'journalisme', 'fa-solid fa-newspaper');
INSERT INTO project_activities VALUES (21, 'la radio', 'fa-solid fa-radio');
INSERT INTO project_activities VALUES (22, 'conciergerie', 'fa-solid fa-bell-concierge');
INSERT INTO project_activities VALUES (23, 'maroquinerie', 'bla');
INSERT INTO project_activities VALUES (24, 'musique', 'fa-solid fa-music');


--
-- Data for Name: project_functions; Type: TABLE DATA; Schema: public; Owner: renaud
--

INSERT INTO project_functions VALUES (1, 'frontend');
INSERT INTO project_functions VALUES (2, 'backend');
INSERT INTO project_functions VALUES (3, 'backend/frontend');


--
-- Data for Name: project_projects; Type: TABLE DATA; Schema: public; Owner: renaud
--

INSERT INTO project_projects VALUES (2, 'John Paul', 'john-paul', 'Au sein de l''équipe John Paul, j''ai eu le privilège de travailler en tant que développeur backend, une expérience passionnante qui m''a permis de contribuer de manière significative au succès continu de l''entreprise. Mon rôle principal consistait à assurer la maintenance et à apporter des améliorations essentielles aux projets.', '#000000', '2025-04-05 01:05:28.905392', '2025-04-05 01:05:28.905397', 1, 'https://www.johnpaul.com/fr', 2, NULL, 22, 'John Paul', 'Paris', '2021-2022');
INSERT INTO project_projects VALUES (3, 'Radio france', 'radio-france', 'J''ai eu l''opportunité exceptionnelle de collaborer en tant que développeur fullstack sur le projet Radio France.fr. Cette expérience de coréalisation a été enrichissante à bien des égards. Elle m''a permis de contribuer de manière significative à la création d''une plateforme web de premier plan pour l''une des institutions culturelles les plus emblématiques de France.', '#000000', '2025-04-05 01:05:28.929671', '2025-04-05 01:05:28.929677', 1, 'https://www.radiofrance.fr/', 3, NULL, 21, 'La Maison de la Radio', 'Paris 16', '2022-2023');
INSERT INTO project_projects VALUES (4, 'Journal LePoint', 'journal-lepoint', 'En qualité d''ingénieur cumulant les compétences front-end et back-end, j''ai eu l''opportunité de jouer un rôle déterminant dans l''évolution des plateformes numériques du journal renommé Le Point. Mon rôle consistait à garantir une expérience utilisateur de qualité tant sur leur site web que sur leur application mobile.', '#000000', '2025-04-05 01:05:28.959321', '2025-04-05 01:05:28.959326', 1, 'https://www.lepoint.fr/', 3, NULL, 20, 'SEBDO', 'Paris 15', '2019-2021');
INSERT INTO project_projects VALUES (5, 'Palmares journal LePoint', 'palmares-journal-lepoint', 'L''une de mes réalisations les plus marquantes en tant qu''ingénieur a été la conception et la mise en place d''un système de palmarès complet pour le prestigieux journal Le Point. Mon rôle englobait à la fois le développement front-end et back-end, et incluait même la création d''applications spécifiques pour certains palmarès.', '#000000', '2025-04-05 01:05:28.988853', '2025-04-05 01:05:28.988859', 1, 'https://www.lepoint.fr/', 3, NULL, 20, 'SEBDO', 'Paris 15', '2019-2021');
INSERT INTO project_projects VALUES (6, 'Carenity', 'carenity', 'L''une de mes réalisations notables en tant que développeur a été la refonte complète du backoffice et l''amélioration substantielle du système de questionnaire pour Carenity. Dans ce projet, j''ai été responsable du développement complet du front-end et du back-end, ce qui a été une expérience particulièrement enrichissante.', '#000000', '2025-04-05 01:05:29.023821', '2025-04-05 01:05:29.023826', 1, 'https://www.carenity.com/', 3, NULL, 14, 'Carenity', 'Paris 9', '2019');
INSERT INTO project_projects VALUES (7, 'Rimowa', 'rimowa', 'L''un de mes projets les plus gratifiants en tant que développeur a été la refonte totale du site e-commerce de la marque emblématique Rimowa. Dans cette entreprise, j''ai été co-responsable du développement complet, en prenant en charge à la fois le front-end et le back-end du site.', '#000000', '2025-04-05 01:05:29.063103', '2025-04-05 01:05:29.063108', 1, 'https://www.rimowa.com/', 3, NULL, 18, 'Viseo', 'Boulogne', '2018');
INSERT INTO project_projects VALUES (9, 'Confbox', 'confbox', 'La refonte du projet Confbox, un système de conférence en ligne, a été une expérience de conception exceptionnelle à laquelle j''ai eu le privilège d''être concepteur et architecte. Cette refonte a été l''occasion de mettre en avant ma passion pour l''innovation en matière de communication virtuelle et ma capacité à créer des solutions technologiques de pointe.', '#000000', '2025-04-05 01:05:29.178565', '2025-04-05 01:05:29.178575', 1, 'http://confbox.com', 3, NULL, 19, 'Creativ', 'Paris', '2018');
INSERT INTO project_projects VALUES (10, 'Cevital', 'cevital', 'J''ai eu l''occasion de mettre en œuvre ma passion et mon expertise en tant que développeur full-stack dans la réalisation du site vitrine du prestigieux groupe nord-africain Cevital. Cette expérience a été marquante, car elle m''a permis de contribuer de manière significative à la représentation en ligne de l''une des entreprises les plus influentes et diversifiées du Maghreb.', '#000000', '2025-04-05 01:05:29.236726', '2025-04-05 01:05:29.23675', 1, 'https://www.cevital.com/', 3, NULL, 17, 'Publicis/Prodigious', 'Paris 8', '2016-2017');
INSERT INTO project_projects VALUES (11, 'Rene Furterer', 'rene-furterer', 'La refonte complète du projet René Furterer a représenté une étape significative dans mon parcours en tant que développeur full-stack. Ce projet a permis de mettre en avant mon expertise dans la création d''expériences numériques complètes, couvrant à la fois le développement front-end et back-end.', '#000000', '2025-04-05 01:05:29.29791', '2025-04-05 01:05:29.29792', 1, 'https://www.renefurterer.com/fr-fr', 3, NULL, 6, 'Publicis - Razorfish', 'Paris 8', '2016-2017');
INSERT INTO project_projects VALUES (12, 'Honda moto', 'honda-moto', 'La refonte intégrale des sites web Honda Moto et Honda Moto Occasion a été un projet phare de ma carrière de développeur full-stack. Cette initiative a représenté une opportunité  pour mettre en valeur mon expertise en matière de développement web, couvrant à la fois le front-end et le back-end.', '#000000', '2025-04-05 01:05:29.355838', '2025-04-05 01:05:29.355856', 1, 'https://moto.honda.fr/', 1, NULL, 15, 'Publicis - Prodigious', 'Paris 8', '2016-2017');
INSERT INTO project_projects VALUES (13, 'Dacia', 'dacia', 'J''ai joué un rôle essentiel dans la maintenance et l''évolution continue du projet Dacia Automobile, une tâche qui a demandé un engagement constant envers l''amélioration de l''expérience en ligne de cette marque automobile renommée.', '#000000', '2025-04-05 01:05:29.433662', '2025-04-05 01:05:29.433679', 1, 'https://www.dacia.fr/', 1, NULL, 2, 'Publicis - Prodigious', 'Paris 8', '2017-2018');
INSERT INTO project_projects VALUES (14, 'UPSA', 'upsa', 'La refonte du site vitrine de l''UPSA a représenté une étape dans mon parcours en tant que développeur, où j''ai contribué à la modernisation de la présence en ligne de cette organisation pharmaceutique de renommée mondiale.', '#000000', '2025-04-05 01:05:29.482749', '2025-04-05 01:05:29.482757', 1, 'https://www.upsa.com/', 3, NULL, 14, 'Publicis - Prodigious', 'Paris 8', '2017');
INSERT INTO project_projects VALUES (15, 'Clio RS Melody', 'clio-rs-melody', 'La création de l''application web de Renault Clio RS melody fût une belle expérience qui plus fût récompensée par la profession et les médias. L''application événementielle Renault Clio RS Melody représente une innovation passionnante dans l''univers automobile, démontrant la capacité de Renault à combiner la technologie et la musique pour créer une expérience unique. Le spot publicitaire de l''application est ici https://www.dailymotion.com/video/x4xy0br', '#000000', '2025-04-05 01:05:29.536819', '2025-04-05 01:05:29.536827', 1, 'http://clio-rs.renault.com', 3, NULL, 2, 'Publicis - Prodigious', 'Paris 8', '2016');
INSERT INTO project_projects VALUES (1, 'Believe', 'believe', 'J''ai récemment eu l''opportunité de participer à la refonte de l''application musicale Smart Entry. Mon rôle principal a été de moderniser et d''améliorer l''interface utilisateur pour offrir une expérience plus fluide et intuitive aux utilisateurs. En outre, j''ai développé un système de traduction intégré, permettant à Smart Entry de devenir accessible à un public international en 17 langues. Cette expérience enrichissante m''a permis de combiner mes compétences techniques et créatives pour apporter des solutions innovantes et améliorer l''accessibilité de l''application.
', '#000000', '2025-04-05 01:05:28.855128', '2025-04-10 16:53:54.218081', 1, 'https://www.believe.com/', 3, NULL, 24, 'Believe', 'St Ouen', '2024');
INSERT INTO project_projects VALUES (16, 'Renault Kadjarquest', 'renault-kadjarquest', 'La création de l''application événementielle Renault Kadjarquest a été une initiative novatrice, marquant une étape significative dans la stratégie de Renault pour célébrer le lancement de son modèle emblématique, le Renault Kadjar. Cette application a été le fruit d''une collaboration étroite entre Renault et des experts en développement d''applications, visant à offrir une expérience unique aux passionnés de voitures.', '#000000', '2025-04-05 01:05:29.623971', '2025-04-05 01:05:29.623984', 1, 'https://kadjarquest.renault.fr/', 3, NULL, 2, 'Publicis - Prodigious', 'Paris 8', '2017');
INSERT INTO project_projects VALUES (17, 'Le Siège Renault', 'le-siege-renault', 'La refonte de l''application événementielle de Renault en tant que partenaire officiel du Festival de Deauville a été une initiative exceptionnelle, démontrant l''engagement de Renault envers l''innovation et la création d''expériences uniques pour les amateurs de cinéma et de voitures.', '#000000', '2025-04-05 01:05:29.695076', '2025-04-05 01:05:29.695093', 1, 'http://lesiege.renault.fr', 3, NULL, 2, 'Publicis - Prodigious', 'Paris 8', '2016-2017');
INSERT INTO project_projects VALUES (18, 'Atelier Renault', 'atelier-renault', 'La maintenance en continu et les évolutions de l''application web de la boutique des Champs-Élysées Atelier Renault ont été une mission essentielle pour garantir une expérience en ligne exceptionnelle aux visiteurs de ce lieu emblématique dédié à l''automobile et à l''art de vivre à la française.', '#000000', '2025-04-05 01:05:29.772238', '2025-04-05 01:05:29.772255', 1, 'https://atelier.renault.com/', 3, NULL, 2, 'Publicis - Prodigious', 'Paris 8', '2017');
INSERT INTO project_projects VALUES (19, 'Aéroport de Paris', 'aeroport-de-paris', 'L''aéroport de Paris, en tant que plaque tournante majeure du voyage en Europe, est le théâtre de mouvements incessants, accueillant des millions de voyageurs du monde entier chaque année. Au cœur de cette mécanique complexe se trouve l''application web de l''aéroport de Paris, une ressource numérique cruciale pour les passagers et un outil de gestion essentiel pour l''aéroport lui-même.', '#000000', '2025-04-05 01:05:29.845302', '2025-04-05 01:05:29.845314', 1, 'https://www.parisaeroport.fr/', 1, NULL, 1, 'Fullsix - ADP', 'Levallois Perret', '2015 - 2016');
INSERT INTO project_projects VALUES (20, 'Afflelou', 'afflelou', 'L''opticien Afflelou est une marque bien connue dans le monde de l''optique, offrant une large gamme de produits et de services pour la santé visuelle. Au cœur de leur engagement envers la satisfaction des clients se trouve leur application web, un outil numérique essentiel qui facilite la vie de ceux qui cherchent des solutions visuelles de qualité.', '#000000', '2025-04-05 01:05:29.885261', '2025-04-05 01:05:29.885278', 1, 'https://www.afflelou.com/', 1, NULL, 13, 'Fullsix', 'Levallois Perret', '2015 - 2016');
INSERT INTO project_projects VALUES (21, 'Fullsix', 'fullsix', 'L''agence web FullSIX, reconnue pour son expertise dans le domaine du marketing digital et de la conception web, a entrepris une transformation significative en refondant son propre site web. Cette initiative démontre l''engagement continu de FullSIX à rester à la pointe de l''innovation dans un secteur en constante évolution.', '#000000', '2025-04-05 01:05:29.961196', '2025-04-05 01:05:29.961213', 1, 'https://betcfullsix.com/', 3, NULL, 19, 'Fullsix', 'Levallois Perret', '2015 - 2016');
INSERT INTO project_projects VALUES (22, 'MyTravelChic', 'mytravelchic', 'La maintenance et l''évolution d''un site web de voyage en ligne sont essentielles pour garantir une bonne expérience utilisateur, tout en restant à la pointe de l''industrie du tourisme. Dans ce contexte, mes travaux sur le site de voyage en ligne MyTravelchic ont été un exemple remarquable d''engagement envers la qualité et l''innovation dans le secteur du voyage.', '#000000', '2025-04-05 01:05:30.025671', '2025-04-05 01:05:30.025687', 1, 'https://www.idiliz.com/', 1, NULL, 7, 'groupe Bazarchic', 'Gennevillier', '2022');
INSERT INTO project_projects VALUES (23, 'Bazarchic', 'bazarchic', 'Les sites de ventes privées ont révolutionné le monde du commerce en ligne en offrant aux consommateurs des offres exclusives sur des produits de qualité. Parmi ces plateformes, Bazarchic s''est distingué en tant que destination privilégiée pour les chasseurs de bonnes affaires. Cependant, pour rester à la pointe de l''industrie, j''ai effectué la refonte partielle, la maintenance et l''évolution de cette plateforme.', '#000000', '2025-04-05 01:05:30.075799', '2025-04-05 01:05:30.075805', 1, 'https://fr.bazarchic.com/', 1, NULL, 7, 'groupe Bazarchic', 'Gennevillier', '2015');
INSERT INTO project_projects VALUES (24, 'Brasserie Flo', 'brasserie-flo', 'La Brasserie Flo est une icône de la gastronomie française, offrant une expérience culinaire authentique et raffinée depuis des décennies. Pour assurer une présence en ligne à la hauteur de cette renommée, une série de sites web a été conçue et développée. En tant que concepteur, J''ai joué un rôle essentiel dans la création de ces plateformes numériques, visant à refléter l''excellence de la Brasserie Flo et à offrir aux visiteurs une excellente expérience en ligne.', '#000000', '2025-04-05 01:05:30.101797', '2025-04-05 01:05:30.101803', 1, 'https://www.groupeflo.com/', 3, NULL, 4, 'Groupe Flo', 'Nanterre', '2011');
INSERT INTO project_projects VALUES (26, 'Peugeot Design Lab', 'peugeot-design-lab', 'Peugeot Design Lab, une division de la célèbre marque automobile Peugeot, est synonyme d''innovation, de design novateur et d''excellence créative. En tant que concepteur, j''ai eu l''opportunité de participer à la refonte de cette entité de renom. Mes travaux ont contribué à redéfinir et à moderniser l''image du Peugeot Design Lab, un laboratoire de design réputé pour son expertise en conception industrielle, son sens du détail et sa passion pour l''innovation.', '#000000', '2025-04-05 01:05:30.175448', '2025-04-05 01:05:30.175456', 1, 'http://www.peugeotdesignlab.com/fr', 1, NULL, 2, 'Business Lab', 'Nanterre', '2012');
INSERT INTO project_projects VALUES (27, 'Peugeot', 'peugeot', 'La refonte d''une marque emblématique telle que Peugeot est une tâche colossale qui nécessite une expertise technique de haut niveau. Il est à noter que le projet fût récompensé par un topcom or', '#000000', '2025-04-05 01:05:30.222481', '2025-04-05 01:05:30.222489', 1, 'https://www.peugeot.fr/', 1, NULL, 2, 'Business Lab', 'Nanterre', '2012');
INSERT INTO project_projects VALUES (28, 'Peugeot 4008', 'peugeot-4008', 'Peugeot lance en avril 2012 un nouveau SUV, Peugeot 4008, sur un marché très dynamique et fortement concurrentiel, donc avec une problématique majeure d’émergence sur sa catégorie. Peugeot a souhaité une campagne originale dans sa forme et dans son contenu, et proposant une expérience interactive innovante avec le modèle.  Une opération 100% YouTube (custom channel + relais display) combinant une logique d’engagement via un parcours vidéo ludique de « quête » du véhicule et une mécanique d’acquisition performante via un jeu concours. Un lancement full digital inédit, réalisé en seulement 4 semaines et en étroite collaboration avec les équipes Google. Top Com d''Or (catégorie site événementiel)
', '#000000', '2025-04-05 01:05:30.26511', '2025-04-05 01:05:30.265127', 1, 'https://www.youtube.com/watch?v=p9SJQjioTb0', 1, NULL, 2, 'Business Lab', 'Nanterre', '2012');
INSERT INTO project_projects VALUES (29, 'Flyopenskies v2', 'flyopenskies-v2', 'L''aviation a toujours été un symbole de liberté, de découverte et de connexion. Dans un monde en constante évolution, les compagnies aériennes jouent un rôle clé dans la réalisation de ces aspirations. C''est avec une profonde passion pour l''aviation et un dévouement envers l''innovation que nous avons entrepris la refonte des sites web de FlyOpenSky.', '#000000', '2025-04-05 01:05:30.341779', '2025-04-05 01:05:30.34179', 1, 'http://www.flyopenskies.com/', 1, NULL, 1, 'Business Lab - Amadeus', 'Nanterre', '2010');
INSERT INTO project_projects VALUES (30, 'Flyopenskies v3', 'flyopenskies-v3', 'L''aviation a toujours été un symbole de liberté, de découverte et de connexion. Dans un monde en constante évolution, les compagnies aériennes jouent un rôle clé dans la réalisation de ces aspirations. C''est avec une profonde passion pour l''aviation et un dévouement envers l''innovation que nous avons entrepris la refonte des sites web de FlyOpenSky.', '#000000', '2025-04-05 01:05:30.390473', '2025-04-05 01:05:30.390486', 1, 'http://www.flyopenskies.com/', 1, NULL, 1, 'Business Lab - Amadeus', 'Nanterre', '2011');
INSERT INTO project_projects VALUES (31, 'Europcar', 'europcar', 'La refonte du site web Europcar représente bien plus qu''un simple rafraîchissement visuel. C''est le fruit d''un engagement à innover et à améliorer l''expérience des clients. Nous avons recréé une plateforme en ligne qui reflète la passion pour la mobilité, et à offrir des services de location de voitures de premier ordre.', '#000000', '2025-04-05 01:05:30.439538', '2025-04-05 01:05:30.43955', 1, 'https://www.europcar.fr', 1, NULL, 2, 'Business Lab', 'Nanterre', '2011');
INSERT INTO project_projects VALUES (32, 'Air Caraïbes', 'air-caraibes', 'Le voyage aérien a le pouvoir de créer des souvenirs inoubliables, de connecter des cultures et d''inspirer l''exploration. Air Caraïbes, une icône du ciel caribéen, a toujours compris cette magie du voyage. J''ai été ravi de présenter la refonte complète du site d''Air Caraïbes, une transformation qui redéfinissait la manière dont les clients planifiaient et réservaient leurs voyages vers les Caraïbes.', '#000000', '2025-04-05 01:05:30.488609', '2025-04-05 01:05:30.488622', 1, 'https://www.aircaraibes.com/', 1, NULL, 1, 'Business Lab - Amadeus', 'Nanterre', '2011 - 2012');
INSERT INTO project_projects VALUES (33, 'Air Madagascar', 'air-madagascar', 'Le voyage aérien, c''est bien plus que le simple déplacement d''un point A à un point B. C''est l''opportunité de créer des souvenirs inoubliables, de découvrir de nouvelles cultures et de vivre des aventures qui marquent une vie. En tant que développeur frontend, j''ai eu le privilège de jouer un rôle essentiel dans la refonte du site web d''Air Madagascar, une compagnie aérienne nationale qui symbolise la porte d''entrée vers la magnifique île de Madagascar.', '#000000', '2025-04-05 01:05:30.537218', '2025-04-05 01:05:30.53723', 1, 'https://madagascarairlines.com', 1, NULL, 1, 'Business Lab - Amadeus', 'Nanterre', '2011 - 2012');
INSERT INTO project_projects VALUES (34, 'CFC', 'cfc', 'La préservation et la promotion de la propriété intellectuelle sont au cœur de la diffusion du savoir, de la culture et de l''innovation. En tant que développeur frontend et backend, j''ai joué un rôle primordial dans la refonte du site du Centre Français d''Exploitation du Droit de Copie (CFC), une institution majeure dans la gestion des droits d''auteur pour les copies papier et numériques de publications en France.', '#000000', '2025-04-05 01:05:30.586188', '2025-04-05 01:05:30.5862', 1, 'https://www.cfcopies.com/', 3, NULL, 10, 'Business Lab', 'Nanterre', '2012 - 2013');
INSERT INTO project_projects VALUES (35, 'Algeco', 'algeco', 'En tant que développeur frontend et backend, j''ai eu l''opportunité de participer à la refonte du site Ageco.fr, une référence en matière de bâtiments modulaires pour une économie locale et durable. Que ce soit des bureaux modulaires, des bungalows de chantier ou des écoles modulaires, ma mission était de rendre accessible à tous les avantages de la construction modulaire.', '#000000', '2025-04-05 01:05:30.656761', '2025-04-05 01:05:30.656774', 1, 'https://www.algeco.fr/', 3, NULL, 9, 'Business Lab', 'Nanterre', '2011-2012');
INSERT INTO project_projects VALUES (36, 'Fidelity Vie', 'fidelity-vie', 'L''assurance vie est bien plus qu''un simple contrat financier. C''est une garantie de sécurité pour l''avenir, une assurance pour vos proches et un moyen de bâtir un patrimoine durable. En tant que développeur frontend et backend, j''ai eu le privilège de jouer un rôle central dans la refonte du site fidelityvie.fr, une plateforme dédiée au contrat d''assurance vie qui incarne la confiance et la prévoyance financière.', '#000000', '2025-04-05 01:05:30.729322', '2025-04-05 01:05:30.729335', 1, 'https://www.fidelityvie.fr', 3, NULL, 5, 'Business Lab', 'Nanterre', '2012');
INSERT INTO project_projects VALUES (37, 'De quoi je me M.E.L', 'de-quoi-je-me-mel', 'La communication numérique est devenue le reflet de la connaissance et de l''expertise, un moyen d''échanger des idées et de partager des visions. En tant que développeur frontend, nous avons refait à la demande Michel-Édouard Leclerc son blog. Une plateforme qui incarne la voix d''un expert renommé en économie et en commerce.', '#000000', '2025-04-05 01:05:30.799465', '2025-04-05 01:05:30.799483', 1, 'https://www.michel-edouard-leclerc.com/', 1, NULL, 8, 'Business Lab', 'Nanterre', '2011');
INSERT INTO project_projects VALUES (38, 'Qui est le moins cher', 'qui-est-le-moins-cher', 'Dans un monde où l''efficacité et l''accessibilité sont des atouts majeurs, le site "Qui Est le Moins Cher" se distingue par son engagement à offrir des offres inégalables. En tant que développeur frontend, j''ai eu l''opportunité de contribuer à la refonte de cette plateforme, qui incarne la recherche des meilleures affaires et des prix les plus compétitifs.', '#000000', '2025-04-05 01:05:30.860754', '2025-04-05 01:05:30.860767', 1, 'https://www.quiestlemoinscher.leclerc/', 1, NULL, 4, 'Business Lab', 'Nanterre', '2012');
INSERT INTO project_projects VALUES (39, 'Decolor Stop', 'decolor-stop', 'La préservation de la qualité et de la longévité des vêtements et du linge de maison est une préoccupation majeure de la vie quotidienne. En tant que développeur frontend, j''ai contribué à la maintenance et à l''amélioration en continu du site Decolor Stop', '#000000', '2025-04-05 01:05:30.89993', '2025-04-05 01:05:30.899943', 1, 'https://www.decolorstop.com/', 1, NULL, 6, 'Business Lab', 'Nanterre', '2010 - 2013');
INSERT INTO project_projects VALUES (40, 'My Peugeot', 'my-peugeot', 'L''automobile, c''est bien plus qu''un simple moyen de transport. C''est une expérience de mobilité, de confort et de fiabilité. En tant que lead développeur frontend, j''ai participé à la refonte du site My Peugeot, l''espace client de Peugeot, un espace en ligne qui incarne l''engagement envers l''excellence du service client.', '#000000', '2025-04-05 01:05:30.947188', '2025-04-05 01:05:30.947201', 1, 'https://mypeugeot.peugeot.fr/', 1, NULL, 2, 'Business Lab - Argonautes', 'Nanterre', '2011 - 2012');
INSERT INTO project_projects VALUES (41, 'banque casino', 'banque-casino', 'L''efficacité de la communication numérique est cruciale, en particulier dans le secteur financier où la confiance et la transparence sont essentielles. En tant que lead développeur frontend, j''ai participé à la création de templates email pour Banque Casino, une institution financière de renom qui place ses clients au cœur de son engagement.', '#000000', '2025-04-05 01:05:30.995504', '2025-04-05 01:05:30.995516', 1, 'https://client.floabank.fr/', 1, NULL, 5, 'Business Lab', 'Nanterre', '2013');
INSERT INTO project_projects VALUES (42, 'leperon', 'leperon', 'L''univers du sport équestre est en constante évolution, et l''accès à l''information à jour est crucial pour les passionnés. En tant que lead développeur frontend, j''ai maintenu et fait évoluer le site Cavadeos (leperon.fr), la référence en matière d''actualité cheval et d''informations équestres.', '#000000', '2025-04-05 01:05:31.047504', '2025-04-05 01:05:31.047511', 1, 'https://www.leperon.fr/', 1, NULL, 3, 'Business Lab', 'Nanterre', '2011 - 2013');
INSERT INTO project_projects VALUES (43, 'Areva', 'areva', 'Dans le monde en constante évolution de l''industrie de l''énergie, la collaboration et la communication internes sont essentielles. En tant que lead développeur frontend, j''ai participé à la création du réseau social en interne d''Areva, une plateforme qui favorise la connectivité, l''innovation et la collaboration au sein de cette entreprise leader du secteur nucléaire. Le projet fût récompensé et acclamé. ', '#e83232', '2025-04-05 01:05:31.077197', '2025-04-05 01:05:31.077202', 1, 'http://areva.com', 1, NULL, 11, 'Business Lab - Areva', 'La Garenne Colombe', '2012 - 2013');
INSERT INTO project_projects VALUES (44, 'Leroy Merlin', 'leroy-merlin', 'Avoir la chance d''accompagner une refonte si ambitieuse est sans aucun doute un projet unique dans une carrière. La richesse incroyable de la marque et les enjeux e-commerce du projet ont largement contribué à animer mon quotidien pendant 2 ans et demie.  Ce fût une vraie la passion que j''ai pour cette enseigne. À noter que le projet a été récompensé. Aussi, leroymerlin.fr est dans le top 50 des sites préférés des Français. ', '#379a2a', '2025-04-05 01:05:31.134518', '2025-04-05 01:05:31.134535', 1, 'https://www.leroymerlin.fr/', 1, NULL, 7, 'Business Lab', 'Nanterre', '2010 - 2012');
INSERT INTO project_projects VALUES (45, 'Sacla', 'sacla', 'La cuisine, c''est bien plus qu''une simple préparation de repas, c''est une expérience sensorielle et une exploration de saveurs. En tant que lead développeur frontend, j''ai coréalisé le site de Sacla, une entreprise renommée pour ses produits alimentaires de qualité et ses délices culinaires.', '#000000', '2025-04-05 01:05:31.190578', '2025-04-05 01:05:31.190583', 1, 'https://sacla.fr/', 1, NULL, 4, 'Business Lab', 'Nanterre', '2010');
INSERT INTO project_projects VALUES (46, 'sfr', 'sfr', 'SFR, un acteur de premier plan dans le secteur des télécommunications en France. En tant que développeur frontend et backend, j''ai eu l''opportunité de coréaliser des modules personnalisés sur le site de SFR.  ', '#000000', '2025-04-05 01:05:31.214712', '2025-04-05 01:05:31.214717', 1, 'https://sfr.fr', 3, NULL, 17, 'Publicis - Prodigious', 'Paris 8', '2017');
INSERT INTO project_projects VALUES (47, 'Se soigner moins cher', 'se-soigner-moins-cher', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet laborum illum maxime iusto minima reiciendis praesentium labore ab, sed sapiente officia enim consequuntur atque non rerum nostrum quibusdam rem molestiae!', '#000000', '2025-04-05 01:05:31.248222', '2025-04-05 01:05:31.248227', 1, 'https://www.e.leclerc/cat/parapharmacie', 1, NULL, 7, 'Business Lab', 'Nanterre', '2013');
INSERT INTO project_projects VALUES (48, 'histoire et archives leclerc', 'histoire-et-archives-leclerc', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet laborum illum maxime iusto minima reiciendis praesentium labore ab, sed sapiente officia enim consequuntur atque non rerum nostrum quibusdam rem molestiae!', '#000000', '2025-04-05 01:05:31.273298', '2025-04-05 01:05:31.273303', 1, 'https://www.histoireetarchives.leclerc/', 1, NULL, 7, 'Business Lab', 'Nanterre', '2012');
INSERT INTO project_projects VALUES (49, 'le mouvement leclerc', 'le-mouvement-leclerc', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet laborum illum maxime iusto minima reiciendis praesentium labore ab, sed sapiente officia enim consequuntur atque non rerum nostrum quibusdam rem molestiae!', '#000000', '2025-04-05 01:05:31.298584', '2025-04-05 01:05:31.29859', 1, 'https://www.mouvement.leclerc/', 1, NULL, 7, 'Business Lab', 'Nanterre', '2011');
INSERT INTO project_projects VALUES (50, 'emag sfr', 'emag-sfr', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet laborum illum maxime iusto minima reiciendis praesentium labore ab, sed sapiente officia enim consequuntur atque non rerum nostrum quibusdam rem molestiae!', '#000000', '2025-04-05 01:05:31.32171', '2025-04-05 01:05:31.321715', 1, 'https://sfr.fr', 3, NULL, 20, 'Publicis - Prodigious', 'Paris 8', '2017');
INSERT INTO project_projects VALUES (51, 'Europcar-up', 'europcar-up', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet laborum illum maxime iusto minima reiciendis praesentium labore ab, sed sapiente officia enim consequuntur atque non rerum nostrum quibusdam rem molestiae!', '#000000', '2025-04-05 01:05:31.386176', '2025-04-05 01:05:31.386194', 1, 'http://europcar.com', 3, NULL, 2, 'Business Lab', 'Nanterre', '2011');
INSERT INTO project_projects VALUES (8, 'Longchamp', 'longchamp', 'La refonte du site e-commerce Longchamp était un défi passionnant, car elle visait à créer une plateforme en ligne à la hauteur de la renommée de cette marque maroquinerie de luxe. Ma mission consistait à m''assurer que le site alliait non seulement une esthétique attrayante, mais aussi des performances optimales, ainsi que la gestion efficace d''une large gamme de produits et d''options de personnalisation.', '#000000', '2025-04-05 01:05:29.11621', '2025-04-07 15:35:09.543044', 1, 'https://www.longchamp.com', 3, NULL, 7, 'Creativ - Viseo', 'Paris 2', '2018');
INSERT INTO project_projects VALUES (25, 'Dyson affaire airblade V1', 'dyson-affaire-airblade-v1', 'L''intranet commercial Dyson Airblade est un outil vital pour une entreprise qui a révolutionné le domaine de la technologie de séchage des mains. Pour assurer une interface intuitive, efficace et conviviale pour les équipes commerciales et les partenaires, une conception exceptionnelle était cruciale. En tant que concepteur, j''ai joué un rôle central dans la création de cet intranet, apportant une expertise en design.', '#000000', '2025-04-05 01:05:30.135427', '2025-05-19 16:54:00.96868', 1, 'https://www.youtube.com/watch?v=jU0WojRkd30', 3, NULL, 12, 'Business Lab', 'Nanterre', '2012');


--
-- Data for Name: project_technologies; Type: TABLE DATA; Schema: public; Owner: renaud
--

INSERT INTO project_technologies VALUES (21, 'FastAPI', 1);
INSERT INTO project_technologies VALUES (1, 'HTML', 1);
INSERT INTO project_technologies VALUES (2, 'CSS', 1);
INSERT INTO project_technologies VALUES (3, 'Javascript', 1);
INSERT INTO project_technologies VALUES (5, 'MySql', 1);
INSERT INTO project_technologies VALUES (6, 'Python 3', 1);
INSERT INTO project_technologies VALUES (7, 'Django', 1);
INSERT INTO project_technologies VALUES (8, 'Flask', 1);
INSERT INTO project_technologies VALUES (9, 'ReactJS', 1);
INSERT INTO project_technologies VALUES (10, 'Svelte/Sveltkit', 1);
INSERT INTO project_technologies VALUES (11, 'SVG', 1);
INSERT INTO project_technologies VALUES (12, 'NodeJS', 1);
INSERT INTO project_technologies VALUES (13, 'ExpressJS', 1);
INSERT INTO project_technologies VALUES (14, 'PostgreSQL', 1);
INSERT INTO project_technologies VALUES (15, 'MJML', 1);
INSERT INTO project_technologies VALUES (18, 'JQuery', 1);
INSERT INTO project_technologies VALUES (19, 'DRF', 1);
INSERT INTO project_technologies VALUES (20, 'Docker', 1);
INSERT INTO project_technologies VALUES (4, 'PHP', 0);
INSERT INTO project_technologies VALUES (16, 'Wordpress', 0);
INSERT INTO project_technologies VALUES (17, 'Joomla', 0);
INSERT INTO project_technologies VALUES (22, 'VueJS/NuxtJS', 1);
INSERT INTO project_technologies VALUES (23, 'GNU/Linux', 1);


--
-- Data for Name: project_projects_technologies; Type: TABLE DATA; Schema: public; Owner: renaud
--

INSERT INTO project_projects_technologies VALUES (1, 1, 1);
INSERT INTO project_projects_technologies VALUES (2, 2, 1);
INSERT INTO project_projects_technologies VALUES (3, 3, 1);
INSERT INTO project_projects_technologies VALUES (4, 6, 1);
INSERT INTO project_projects_technologies VALUES (5, 10, 1);
INSERT INTO project_projects_technologies VALUES (6, 12, 1);
INSERT INTO project_projects_technologies VALUES (7, 20, 1);
INSERT INTO project_projects_technologies VALUES (8, 6, 2);
INSERT INTO project_projects_technologies VALUES (9, 7, 2);
INSERT INTO project_projects_technologies VALUES (10, 14, 2);
INSERT INTO project_projects_technologies VALUES (11, 19, 2);
INSERT INTO project_projects_technologies VALUES (12, 1, 3);
INSERT INTO project_projects_technologies VALUES (13, 2, 3);
INSERT INTO project_projects_technologies VALUES (14, 3, 3);
INSERT INTO project_projects_technologies VALUES (15, 10, 3);
INSERT INTO project_projects_technologies VALUES (16, 12, 3);
INSERT INTO project_projects_technologies VALUES (17, 1, 4);
INSERT INTO project_projects_technologies VALUES (18, 2, 4);
INSERT INTO project_projects_technologies VALUES (19, 3, 4);
INSERT INTO project_projects_technologies VALUES (20, 4, 4);
INSERT INTO project_projects_technologies VALUES (21, 9, 4);
INSERT INTO project_projects_technologies VALUES (22, 1, 5);
INSERT INTO project_projects_technologies VALUES (23, 2, 5);
INSERT INTO project_projects_technologies VALUES (24, 3, 5);
INSERT INTO project_projects_technologies VALUES (25, 6, 5);
INSERT INTO project_projects_technologies VALUES (26, 7, 5);
INSERT INTO project_projects_technologies VALUES (27, 14, 5);
INSERT INTO project_projects_technologies VALUES (28, 1, 6);
INSERT INTO project_projects_technologies VALUES (29, 2, 6);
INSERT INTO project_projects_technologies VALUES (30, 3, 6);
INSERT INTO project_projects_technologies VALUES (31, 4, 6);
INSERT INTO project_projects_technologies VALUES (32, 5, 6);
INSERT INTO project_projects_technologies VALUES (33, 6, 6);
INSERT INTO project_projects_technologies VALUES (34, 9, 6);
INSERT INTO project_projects_technologies VALUES (35, 1, 7);
INSERT INTO project_projects_technologies VALUES (36, 2, 7);
INSERT INTO project_projects_technologies VALUES (37, 3, 7);
INSERT INTO project_projects_technologies VALUES (38, 9, 7);
INSERT INTO project_projects_technologies VALUES (39, 1, 8);
INSERT INTO project_projects_technologies VALUES (40, 2, 8);
INSERT INTO project_projects_technologies VALUES (41, 3, 8);
INSERT INTO project_projects_technologies VALUES (42, 9, 8);
INSERT INTO project_projects_technologies VALUES (43, 1, 9);
INSERT INTO project_projects_technologies VALUES (44, 2, 9);
INSERT INTO project_projects_technologies VALUES (45, 3, 9);
INSERT INTO project_projects_technologies VALUES (46, 6, 9);
INSERT INTO project_projects_technologies VALUES (47, 7, 9);
INSERT INTO project_projects_technologies VALUES (48, 12, 9);
INSERT INTO project_projects_technologies VALUES (49, 1, 10);
INSERT INTO project_projects_technologies VALUES (50, 2, 10);
INSERT INTO project_projects_technologies VALUES (51, 3, 10);
INSERT INTO project_projects_technologies VALUES (52, 4, 10);
INSERT INTO project_projects_technologies VALUES (53, 5, 10);
INSERT INTO project_projects_technologies VALUES (54, 18, 10);
INSERT INTO project_projects_technologies VALUES (55, 1, 11);
INSERT INTO project_projects_technologies VALUES (56, 2, 11);
INSERT INTO project_projects_technologies VALUES (57, 3, 11);
INSERT INTO project_projects_technologies VALUES (58, 6, 11);
INSERT INTO project_projects_technologies VALUES (59, 7, 11);
INSERT INTO project_projects_technologies VALUES (60, 14, 11);
INSERT INTO project_projects_technologies VALUES (61, 1, 12);
INSERT INTO project_projects_technologies VALUES (62, 2, 12);
INSERT INTO project_projects_technologies VALUES (63, 3, 12);
INSERT INTO project_projects_technologies VALUES (64, 6, 12);
INSERT INTO project_projects_technologies VALUES (65, 7, 12);
INSERT INTO project_projects_technologies VALUES (66, 1, 13);
INSERT INTO project_projects_technologies VALUES (67, 2, 13);
INSERT INTO project_projects_technologies VALUES (68, 3, 13);
INSERT INTO project_projects_technologies VALUES (69, 4, 13);
INSERT INTO project_projects_technologies VALUES (70, 5, 13);
INSERT INTO project_projects_technologies VALUES (71, 1, 14);
INSERT INTO project_projects_technologies VALUES (72, 2, 14);
INSERT INTO project_projects_technologies VALUES (73, 3, 14);
INSERT INTO project_projects_technologies VALUES (74, 6, 14);
INSERT INTO project_projects_technologies VALUES (75, 7, 14);
INSERT INTO project_projects_technologies VALUES (76, 1, 15);
INSERT INTO project_projects_technologies VALUES (77, 2, 15);
INSERT INTO project_projects_technologies VALUES (78, 3, 15);
INSERT INTO project_projects_technologies VALUES (79, 9, 15);
INSERT INTO project_projects_technologies VALUES (80, 12, 15);
INSERT INTO project_projects_technologies VALUES (81, 13, 15);
INSERT INTO project_projects_technologies VALUES (82, 1, 16);
INSERT INTO project_projects_technologies VALUES (83, 2, 16);
INSERT INTO project_projects_technologies VALUES (84, 3, 16);
INSERT INTO project_projects_technologies VALUES (85, 6, 16);
INSERT INTO project_projects_technologies VALUES (86, 7, 16);
INSERT INTO project_projects_technologies VALUES (87, 1, 17);
INSERT INTO project_projects_technologies VALUES (88, 2, 17);
INSERT INTO project_projects_technologies VALUES (89, 3, 17);
INSERT INTO project_projects_technologies VALUES (90, 6, 17);
INSERT INTO project_projects_technologies VALUES (91, 7, 17);
INSERT INTO project_projects_technologies VALUES (92, 1, 18);
INSERT INTO project_projects_technologies VALUES (93, 2, 18);
INSERT INTO project_projects_technologies VALUES (94, 3, 18);
INSERT INTO project_projects_technologies VALUES (95, 6, 18);
INSERT INTO project_projects_technologies VALUES (96, 7, 18);
INSERT INTO project_projects_technologies VALUES (97, 9, 18);
INSERT INTO project_projects_technologies VALUES (98, 19, 18);
INSERT INTO project_projects_technologies VALUES (99, 1, 19);
INSERT INTO project_projects_technologies VALUES (100, 2, 19);
INSERT INTO project_projects_technologies VALUES (101, 3, 19);
INSERT INTO project_projects_technologies VALUES (102, 12, 19);
INSERT INTO project_projects_technologies VALUES (103, 1, 20);
INSERT INTO project_projects_technologies VALUES (104, 2, 20);
INSERT INTO project_projects_technologies VALUES (105, 3, 20);
INSERT INTO project_projects_technologies VALUES (106, 9, 20);
INSERT INTO project_projects_technologies VALUES (107, 12, 20);
INSERT INTO project_projects_technologies VALUES (108, 1, 21);
INSERT INTO project_projects_technologies VALUES (109, 2, 21);
INSERT INTO project_projects_technologies VALUES (110, 3, 21);
INSERT INTO project_projects_technologies VALUES (111, 12, 21);
INSERT INTO project_projects_technologies VALUES (112, 1, 22);
INSERT INTO project_projects_technologies VALUES (113, 2, 22);
INSERT INTO project_projects_technologies VALUES (114, 3, 22);
INSERT INTO project_projects_technologies VALUES (115, 18, 22);
INSERT INTO project_projects_technologies VALUES (116, 1, 23);
INSERT INTO project_projects_technologies VALUES (117, 2, 23);
INSERT INTO project_projects_technologies VALUES (118, 3, 23);
INSERT INTO project_projects_technologies VALUES (119, 12, 23);
INSERT INTO project_projects_technologies VALUES (120, 1, 24);
INSERT INTO project_projects_technologies VALUES (121, 2, 24);
INSERT INTO project_projects_technologies VALUES (122, 3, 24);
INSERT INTO project_projects_technologies VALUES (123, 4, 24);
INSERT INTO project_projects_technologies VALUES (124, 5, 24);
INSERT INTO project_projects_technologies VALUES (125, 18, 24);
INSERT INTO project_projects_technologies VALUES (126, 1, 25);
INSERT INTO project_projects_technologies VALUES (127, 2, 25);
INSERT INTO project_projects_technologies VALUES (128, 3, 25);
INSERT INTO project_projects_technologies VALUES (129, 4, 25);
INSERT INTO project_projects_technologies VALUES (130, 5, 25);
INSERT INTO project_projects_technologies VALUES (131, 18, 25);
INSERT INTO project_projects_technologies VALUES (132, 1, 26);
INSERT INTO project_projects_technologies VALUES (133, 2, 26);
INSERT INTO project_projects_technologies VALUES (134, 3, 26);
INSERT INTO project_projects_technologies VALUES (135, 18, 26);
INSERT INTO project_projects_technologies VALUES (136, 1, 27);
INSERT INTO project_projects_technologies VALUES (137, 2, 27);
INSERT INTO project_projects_technologies VALUES (138, 3, 27);
INSERT INTO project_projects_technologies VALUES (139, 18, 27);
INSERT INTO project_projects_technologies VALUES (140, 1, 28);
INSERT INTO project_projects_technologies VALUES (141, 2, 28);
INSERT INTO project_projects_technologies VALUES (142, 3, 28);
INSERT INTO project_projects_technologies VALUES (143, 4, 28);
INSERT INTO project_projects_technologies VALUES (144, 5, 28);
INSERT INTO project_projects_technologies VALUES (145, 18, 28);
INSERT INTO project_projects_technologies VALUES (146, 1, 29);
INSERT INTO project_projects_technologies VALUES (147, 2, 29);
INSERT INTO project_projects_technologies VALUES (148, 3, 29);
INSERT INTO project_projects_technologies VALUES (149, 18, 29);
INSERT INTO project_projects_technologies VALUES (150, 1, 30);
INSERT INTO project_projects_technologies VALUES (151, 2, 30);
INSERT INTO project_projects_technologies VALUES (152, 3, 30);
INSERT INTO project_projects_technologies VALUES (153, 18, 30);
INSERT INTO project_projects_technologies VALUES (154, 1, 31);
INSERT INTO project_projects_technologies VALUES (155, 2, 31);
INSERT INTO project_projects_technologies VALUES (156, 3, 31);
INSERT INTO project_projects_technologies VALUES (157, 18, 31);
INSERT INTO project_projects_technologies VALUES (158, 1, 32);
INSERT INTO project_projects_technologies VALUES (159, 2, 32);
INSERT INTO project_projects_technologies VALUES (160, 3, 32);
INSERT INTO project_projects_technologies VALUES (161, 18, 32);
INSERT INTO project_projects_technologies VALUES (162, 1, 33);
INSERT INTO project_projects_technologies VALUES (163, 2, 33);
INSERT INTO project_projects_technologies VALUES (164, 3, 33);
INSERT INTO project_projects_technologies VALUES (165, 18, 33);
INSERT INTO project_projects_technologies VALUES (166, 1, 34);
INSERT INTO project_projects_technologies VALUES (167, 2, 34);
INSERT INTO project_projects_technologies VALUES (168, 3, 34);
INSERT INTO project_projects_technologies VALUES (169, 4, 34);
INSERT INTO project_projects_technologies VALUES (170, 5, 34);
INSERT INTO project_projects_technologies VALUES (171, 18, 34);
INSERT INTO project_projects_technologies VALUES (172, 1, 35);
INSERT INTO project_projects_technologies VALUES (173, 2, 35);
INSERT INTO project_projects_technologies VALUES (174, 3, 35);
INSERT INTO project_projects_technologies VALUES (175, 4, 35);
INSERT INTO project_projects_technologies VALUES (176, 5, 35);
INSERT INTO project_projects_technologies VALUES (177, 18, 35);
INSERT INTO project_projects_technologies VALUES (178, 1, 36);
INSERT INTO project_projects_technologies VALUES (179, 2, 36);
INSERT INTO project_projects_technologies VALUES (180, 3, 36);
INSERT INTO project_projects_technologies VALUES (181, 4, 36);
INSERT INTO project_projects_technologies VALUES (182, 5, 36);
INSERT INTO project_projects_technologies VALUES (183, 18, 36);
INSERT INTO project_projects_technologies VALUES (184, 1, 37);
INSERT INTO project_projects_technologies VALUES (185, 2, 37);
INSERT INTO project_projects_technologies VALUES (186, 3, 37);
INSERT INTO project_projects_technologies VALUES (187, 4, 37);
INSERT INTO project_projects_technologies VALUES (188, 5, 37);
INSERT INTO project_projects_technologies VALUES (189, 1, 38);
INSERT INTO project_projects_technologies VALUES (190, 2, 38);
INSERT INTO project_projects_technologies VALUES (191, 3, 38);
INSERT INTO project_projects_technologies VALUES (192, 1, 39);
INSERT INTO project_projects_technologies VALUES (193, 2, 39);
INSERT INTO project_projects_technologies VALUES (194, 3, 39);
INSERT INTO project_projects_technologies VALUES (195, 18, 39);
INSERT INTO project_projects_technologies VALUES (196, 1, 40);
INSERT INTO project_projects_technologies VALUES (197, 2, 40);
INSERT INTO project_projects_technologies VALUES (198, 3, 40);
INSERT INTO project_projects_technologies VALUES (199, 18, 40);
INSERT INTO project_projects_technologies VALUES (200, 1, 41);
INSERT INTO project_projects_technologies VALUES (201, 2, 41);
INSERT INTO project_projects_technologies VALUES (202, 3, 41);
INSERT INTO project_projects_technologies VALUES (203, 12, 41);
INSERT INTO project_projects_technologies VALUES (204, 15, 41);
INSERT INTO project_projects_technologies VALUES (205, 1, 42);
INSERT INTO project_projects_technologies VALUES (206, 2, 42);
INSERT INTO project_projects_technologies VALUES (207, 3, 42);
INSERT INTO project_projects_technologies VALUES (208, 18, 42);
INSERT INTO project_projects_technologies VALUES (209, 1, 43);
INSERT INTO project_projects_technologies VALUES (210, 2, 43);
INSERT INTO project_projects_technologies VALUES (211, 3, 43);
INSERT INTO project_projects_technologies VALUES (212, 12, 43);
INSERT INTO project_projects_technologies VALUES (213, 18, 43);
INSERT INTO project_projects_technologies VALUES (214, 1, 44);
INSERT INTO project_projects_technologies VALUES (215, 2, 44);
INSERT INTO project_projects_technologies VALUES (216, 3, 44);
INSERT INTO project_projects_technologies VALUES (217, 4, 44);
INSERT INTO project_projects_technologies VALUES (218, 18, 44);
INSERT INTO project_projects_technologies VALUES (219, 1, 45);
INSERT INTO project_projects_technologies VALUES (220, 2, 45);
INSERT INTO project_projects_technologies VALUES (221, 3, 45);
INSERT INTO project_projects_technologies VALUES (222, 18, 45);
INSERT INTO project_projects_technologies VALUES (223, 1, 46);
INSERT INTO project_projects_technologies VALUES (224, 2, 46);
INSERT INTO project_projects_technologies VALUES (225, 3, 46);
INSERT INTO project_projects_technologies VALUES (226, 6, 46);
INSERT INTO project_projects_technologies VALUES (227, 7, 46);
INSERT INTO project_projects_technologies VALUES (228, 14, 46);
INSERT INTO project_projects_technologies VALUES (229, 1, 47);
INSERT INTO project_projects_technologies VALUES (230, 2, 47);
INSERT INTO project_projects_technologies VALUES (231, 3, 47);
INSERT INTO project_projects_technologies VALUES (232, 18, 47);
INSERT INTO project_projects_technologies VALUES (233, 1, 48);
INSERT INTO project_projects_technologies VALUES (234, 2, 48);
INSERT INTO project_projects_technologies VALUES (235, 3, 48);
INSERT INTO project_projects_technologies VALUES (236, 18, 48);
INSERT INTO project_projects_technologies VALUES (237, 1, 49);
INSERT INTO project_projects_technologies VALUES (238, 2, 49);
INSERT INTO project_projects_technologies VALUES (239, 3, 49);
INSERT INTO project_projects_technologies VALUES (240, 18, 49);
INSERT INTO project_projects_technologies VALUES (241, 1, 50);
INSERT INTO project_projects_technologies VALUES (242, 2, 50);
INSERT INTO project_projects_technologies VALUES (243, 3, 50);
INSERT INTO project_projects_technologies VALUES (244, 6, 50);
INSERT INTO project_projects_technologies VALUES (245, 7, 50);
INSERT INTO project_projects_technologies VALUES (246, 9, 50);
INSERT INTO project_projects_technologies VALUES (247, 12, 50);
INSERT INTO project_projects_technologies VALUES (248, 14, 50);
INSERT INTO project_projects_technologies VALUES (249, 1, 51);
INSERT INTO project_projects_technologies VALUES (250, 2, 51);
INSERT INTO project_projects_technologies VALUES (251, 3, 51);
INSERT INTO project_projects_technologies VALUES (252, 4, 51);
INSERT INTO project_projects_technologies VALUES (253, 5, 51);
INSERT INTO project_projects_technologies VALUES (254, 18, 51);


--
-- Name: project_activities_id_seq; Type: SEQUENCE SET; Schema: public; Owner: renaud
--

SELECT pg_catalog.setval('project_activities_id_seq', 1, false);


--
-- Name: project_functions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: renaud
--

SELECT pg_catalog.setval('project_functions_id_seq', 3, true);


--
-- Name: project_projects_id_seq; Type: SEQUENCE SET; Schema: public; Owner: renaud
--

SELECT pg_catalog.setval('project_projects_id_seq', 51, true);


--
-- Name: project_projects_technologies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: renaud
--

SELECT pg_catalog.setval('project_projects_technologies_id_seq', 254, true);


--
-- Name: project_technologies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: renaud
--

SELECT pg_catalog.setval('project_technologies_id_seq', 23, true);


--
-- PostgreSQL database dump complete
--

