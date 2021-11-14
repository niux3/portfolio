<?php
    $data = [
        'leroy-merlin',
        'areva',
        'air-caraibes',
        'air-madagascar',
        'dyson-airblade',
    ];
?>
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <!--[if IE]><meta http-equiv="X-UA-Compatible" content="IE=edge"><![endif]-->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="./public/css/style.css?v=<?= time() ?>">
</head>
<body>
    <header class="container">
        <nav>
            <a href="#/about">à propos de nous</a>
            <a href="#/contact">contactez nous</a>
            <?php foreach($data as $k => $v): ?>
                <a href="#/project-<?= $k + 1 ?>-<?= $v ?>"><?= $v ?></a>
            <?php endforeach; ?>
        </nav>
    </header>
    <div class="container" id="app">

    </div>
    <script async defer src="./public/js/app.js?v=<?= time() ?>"></script>
</body>
</html>
