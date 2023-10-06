<?php

$appointment = '';
if(!empty($date_appointment) || !empty($hour_appointment)){
    $date =  date('d/m/Y', strtotime($date_appointment));
    $appointment = <<<APPOINTMENT
-------------------------------------------------------------
rendez vous : 
    - date : $date
    - heure : $hour_appointment
    - téléphone : $phone
-------------------------------------------------------------
APPOINTMENT;
}

$output_txt = <<<TPL
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