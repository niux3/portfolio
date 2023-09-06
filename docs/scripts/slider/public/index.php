<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <!--[if IE]><meta http-equiv="X-UA-Compatible" content="IE=edge"><![endif]-->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="./public/css/style.css">
</head>
<body>
    <div class="container">
        <div class="slider">
            <ul>
                <?php for($i = 1; $i <= 4; $i++): ?>
                <li<?= $i === 1? ' class="at-middle"' : ''?>><img src="https://picsum.photos/400/300?random=<?= $i ?>" alt=""></li>
                <?php endfor; ?>
            </ul>
            <button class="previous">précédent</button><button class="next">suivant</button>
        </div>
    </div>
    <script async defer src="./public/js/app.js"></script>
</body>
</html>
