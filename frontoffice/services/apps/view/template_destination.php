<?php

$appointment = '';
if(!empty($date_appointment) || !empty($hour_appointment)){
    $appointment = <<<APPOINTMENT
-------------------------------------------------------------
rendez vous : 
    - date : $date_appointment
    - heure : $hour_appointment
    - téléphone : $phone
-------------------------------------------------------------
APPOINTMENT;
}

$output = <<<TPL
Bonjour Renaud, 

tu viens de recevoir un mail de ton portfolio : 

*************************************************************

civilité : $civility 
prénom : $firstname 
nom : $lastname 
email : $email 

$appointment

sujet : $subject

$message

*************************************************************
TPL;
?>