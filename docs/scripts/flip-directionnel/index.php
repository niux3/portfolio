<?php
    $rows = json_decode(file_get_contents('./data.json'));
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="./public/css/style.css">
</head>
<body>
    <div id="projects">
        <ol>
            <?php foreach($rows as $k => $row): ?>
                <li>
                    <div class="flip-card">
                        <div class="flip-card-inner">
                            <div class="flip-card-front">
                                <img src="./public/img/img_avatar.png" alt="Avatar">
                            </div>
                            <div class="flip-card-back">
                                <h1>John Doe</h1>
                                <p>Architect & Engineer</p>
                                <p>We love that guy</p>
                            </div>
                        </div>
                    </div>
                </li>
            <?php endforeach; ?>
        </ol>
    </div>
    <script src="./public/js/app.js"></script>
</body>
</html>
