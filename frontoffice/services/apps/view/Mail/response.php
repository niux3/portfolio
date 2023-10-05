<?php
    $this->layout = 'default';
?>
<style>
    html,
    body{
        margin: 0;
        padding: 0;
        background-color: #f5f5f5;
        font-family: sans-serif;
    }
    #base{
        width: 100%;
    }

    #view{
        max-width: 600px;
        margin: 0 25px;
    }
</style>
<table id="base">
    <tr>
        <td align="center">
            <table id="view">
                <tr>
                    <td align="center" style="height:200px"><img src="https://rb-webstudio.000webhostapp.com/logo.svg?v=1" width="100" alt=""></td>
                </tr>
                <tr>
                    <td style="color:#444 !important;">
                        
                        <p>Bonjour <?= $civility ?> <?= $firstname?? '' ?> <?= $lastname ?>, <br> <br>
                        Je suis ravi de faire votre connaissance. Merci pour l'email que vous m'avez transmis.  J'apprécie le fait que vous ayez pris le temps de le rédiger.</p>
                        <?php if(!empty($date_appointment)): ?>
                        <p>Je tiens à vous exprimer ma sincère gratitude pour avoir pris le temps de planifier un rendez-vous avec moi. C'est avec grand intérêt que j'en prends note. Votre intérêt pour notre rencontre me réjouit, et je suis enthousiaste à l'idée de discuter avec vous. Je suis persuadé que notre discussion sera constructive et enrichissante. N'hésitez pas à me contacter si vous avez des questions préliminaires ou des sujets que vous aimeriez aborder lors de notre rencontre.</p>
                        <ul>
                            <li><strong>date</strong> : <?= date('d/m/Y', strtotime($date_appointment))?></li>
                            <li><strong>heure</strong> : <?= str_replace(':', ' h ', $hour_appointment) ?></li>
                            <li><strong>téléphone</strong> : <?= $phone ?></li>
                        </ul>
                        <?php endif; ?>
                        <p>Je vous encourage à consulter <a href="https://www.linkedin.com/in/renaud-bourdeau-%F0%9F%90%A7-7639b944/">mon profil LinkedIn</a>. Vous y trouverez davantage d'informations sur mon parcours professionnel et mes compétences.</p>
                        <p>Je vous souhaite une excellente journée, et encore une fois, je vous remercie pour cette prise de contact.</p>
                        <p>Cordialement</p>
                    </td>
                </tr>
                <tr>
                    <td>&nbsp;</td>
                </tr>
            </table>
        </td>
    </tr>
</table>