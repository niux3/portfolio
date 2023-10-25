<?php 
	try{
        ini_set('display_errors', 0);
        ini_set('display_startup_errors', 0);
        error_reporting(E_ALL);
        

        define('ROOT', dirname(__FILE__));

		$files = [
			'global' => './css/global.css',
			'bundlecss' => './build/bundle.css',
			'bundlejs' => './build/bundle.js',
		];

    }catch(Exception $e){
        echo $e->getMessage();
    }
?>
<!DOCTYPE html>
<html lang="fr">
<head>
	<meta charset='utf-8'>
	<meta name='viewport' content='width=device-width,initial-scale=1'>

	<title>RB webstudio - digital designer - développeur frontend & backend - Python - TS/JS/ESnext - ExpressJS - React/Svelte - NodeJS</title>
	<meta name="description"  content="Book en ligne de rb webstudio, digital designer - développeur frontend & backend - Python - TS/JS/ESnext - ExpressJS - React/Svelte - NodeJS." />

	<link rel='icon' type='image/png' href='/favicon.png'>
	<link rel='stylesheet' href='<?= $files["global"] ?>?version=<?= filemtime($files["global"]) ?>'>
	<link rel='stylesheet' href='<?= $files["bundlecss"] ?>?version=<?= filemtime($files["bundlecss"]) ?>'>
	<style>
		.seo{
			display: none !important;
		}
	</style>
	<script defer src='<?= $files["bundlejs"] ?>?version=<?= filemtime($files["bundlejs"]) ?>'></script>
</head>

<body>
	<div class="seo">
		<h1>RB webstudio - digital designer - développeur frontend & backend - Python - TS/JS/ESnext - ExpressJS - React/Svelte - NodeJS</h1>
		<h2>Découvrez un développeur full stack pour faire avancer vos projets web</h2>
		<div>
			<h3>Développement frontend</h3>
			<p>Démarquez-vous avec une interface utilisateur exceptionnelle grâce à mon expertise en développement frontend. Je suis un développeur talentueux qui maîtrise les dernières technologies et les meilleures pratiques pour créer des expériences utilisateur fluides et attrayantes. Que ce soit pour un site web ou une application, je m'engage à fournir un code propre, une conception responsive et des performances optimales. Vous pouvez compter sur mon expertise en développement frontend afin de concrétiser votre vision et captiver vos utilisateurs grâce à un rendu impressionnant.</p>
		</div>
		<div>
			<h3>Développement backend</h3>
			<p>Optimisez les performances de votre application grâce à mon expertise en développement backend. Je maîtrise les langages et les frameworks les plus avancés pour construire des systèmes robustes, sécurisés et évolutifs. Que ce soit pour la gestion de bases de données, la logique métier ou l'intégration de services tiers, je m'engage à fournir des solutions backend performantes qui répondent à vos besoins. Confiez moi votre infrastructure technique et concentrez-vous sur la croissance de votre entreprise en toute confiance.</p>
		</div>
		<div>
			<h3>Conception visuelle</h3>
			<p>De l'idée à l'impact visuel, je suis là pour donner vie à votre vision créative. Je fusionne l'art et la technologie pour créer des designs visuellement époustouflants qui captivent votre public. Que ce soit pour des logos percutants, des interfaces utilisateur intuitives ou des supports de communication attrayants, je mets en œuvre des concepts innovants et des esthétiques uniques. Comptez sur mes compétences pour donner vie à une identité visuelle distinctive et mémorable pour votre marque. N'hésitez pas à me contacter dès maintenant pour vivre une expérience visuelle inouïe.</p>
		</div>
		<div class="experience">
			<h2>expérience</h2>
			<ul>
				<li>
					<span>2022</span>
					<span>développeur backend</span>
					<span>John Paul</span>
				</li>
				<li>
					<span>2021&nbsp;&ndash;&nbsp;2022</span>
					<span>développeur front/back</span>
					<span>la Maison de la Radio</span>
				</li>
				<li>
					<span>2019&nbsp;&ndash;&nbsp;2021</span>
					<span>développeur front/back</span>
					<span>Journal LePoint</span>
				</li>
				<li>
					<span>2019</span>
					<span>développeur front/back</span>
					<span>Carenity</span>
				</li>
				<li>
					<span>2018&nbsp;&ndash;&nbsp;2019</span>
					<span>développeur front/back</span>
					<span>Groupe Creative</span>
				</li>
				<li>
					<span>2016&nbsp;&ndash;&nbsp;2018</span>
					<span>développeur front/back</span>
					<span>Prodigious</span>
				</li>
				<li>
					<span>2015&nbsp;&ndash;&nbsp;2016</span>
					<span>développeur front</span>
					<span>Fullsix</span>
				</li>
				<li>
					<span>2014&nbsp;&ndash;&nbsp;2015</span>
					<span>développeur front</span>
					<span>Groupe Bazarchic</span>
				</li>
				<li>
					<span>2010&nbsp;&ndash;&nbsp;2013</span>
					<span>développeur front</span>
					<span>Business Lab</span>
				</li>
			</ul>
		</div>
		<div class="awwards">
			<h2>récompenses</h2>
			<ul>
				<li>
					<span>Top Com Or</span>
					<span>Renault Clio RS</span>
				</li>
				<li>
					<span>Top Com Or</span>
					<span>Leroy Merlin</span>
				</li>
				<li>
					<span>Top Com Or</span>
					<span>Peugeot</span>
				</li>
				<li>
					<span>Top Com Or</span>
					<span>Peugeot 4008</span>
				</li>
				<li>
					<span>Top Com Or</span>
					<span>Areva</span>
				</li>
			</ul>
		</div>
	</div>
</body>
</html>
