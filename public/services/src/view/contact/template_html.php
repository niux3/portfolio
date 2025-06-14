<?php

$lastname = htmlentities($lastname, ENT_NOQUOTES);

$appointment = '';
if(!empty($date_appointment) || !empty($hour_appointment)){
    $date =  date('d/m/Y', strtotime($date_appointment));
    $hour =  str_replace(':', ' h ', $hour_appointment);
    $appointment = <<<APPOINTMENT
    <p>Je tiens &agrave; vous exprimer ma sinc&egrave;re gratitude pour avoir pris le temps de planifier un rendez-vous avec moi. C&#039;est avec grand int&eacute;r&ecirc;t que j&#039;en prends note. Votre int&eacute;r&ecirc;t pour notre rencontre me r&eacute;jouit, et je suis enthousiaste &agrave; l&#039;id&eacute;e de discuter avec vous. Je suis persuad&eacute; que notre discussion sera constructive et enrichissante. N&#039;h&eacute;sitez pas &agrave; me contacter si vous avez des questions pr&eacute;liminaires ou des sujets que vous aimeriez aborder lors de notre rencontre.</p>
    <ul>
        <li><strong>date</strong> : $date </li>
        <li><strong>heure</strong> : $hour</li>
        <li><strong>t&eacute;l&eacute;phone</strong> : $phone </li>
    </ul>
APPOINTMENT;
}


$output_html = <<<TPL
<html>
<head>
<style>
    html,
    body{
        margin: 0;
        padding: 0;
        background-color: #eeeeee;
        font-family: sans-serif;
        height: 100%;
    }
    #base{
        width: 100%;
    }

    #view{
        max-width: 600px;
        margin: 0 25px;
    }
</style>
</head>
<body>
<table id="base" style="background-color:#eeeeee; height:100%; width: 100%;">
    <tr>
        <td align="center">
            <table id="view" style="max-width:600px; width:100%;">
                <tr>
                    <td align="center" style="height:200px"><a href="https://rb-webstudio.go.yj.fr/" target="_blank"><span style="display:none !important">RB webstudio - digital designer - développeur frontend & backend - Python - TS/JS/ESnext - ExpressJS - React/Svelte - NodeJS</span><img src="https://rb-webstudio.go.yj.fr/logo-mail.png?v=1" width="100" alt="RB webstudio - digital designer - développeur frontend & backend - Python - TS/JS/ESnext - ExpressJS - React/Svelte - NodeJS" /></a></td>
                </tr>
                <tr>
                    <td style="color:#355269 !important; padding-right:25px; padding-left:25px;">
                        <p>Bonjour $civility $lastname, <br> <br>
                        Je suis ravi de faire votre connaissance. Merci pour l&#039;email que vous m&#039;avez transmis.  J&#039;appr&eacute;cie le fait que vous ayez pris le temps de le r&eacute;diger.</p>
                        $appointment
                        <p>Je vous encourage &agrave; consulter <a href="https://www.linkedin.com/in/renaud-bourdeau-%F0%9F%90%A7-7639b944/">mon profil LinkedIn</a>. Vous y trouverez davantage d&#039;informations sur mon parcours professionnel et mes comp&eacute;tences.</p>
                        <p>Je vous souhaite une excellente journ&eacute;e, et encore une fois, je vous remercie pour cette prise de contact.</p>
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
</body>
</html>
TPL;

?>