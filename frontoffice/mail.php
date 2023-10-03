<?php 
    $data = [
        "message" => "ok"
    ];
    header('Content-Type: application/json; charset=utf-8');
    echo json_encode($data);
?>