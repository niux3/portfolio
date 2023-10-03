<?php 
    header("Access-Control-Allow-Origin: *");
    header("Access-Control-Allow-Headers: *");
    header('Content-Type: application/json; charset=utf-8');


    if(!empty($_SERVER['HTTP_X_REQUESTED_WITH']) && $_SERVER['HTTP_X_REQUESTED_WITH'] === 'XMLHttpRequest' && !empty($_POST)){
        $clean_methods = [
            'trim',
            'strip_tags',
            'htmlspecialchars',
        ];

        foreach($clean_methods as $method){
            $_POST = array_map($method, $_POST);
        }
        
        foreach($_POST as $k => $v){
            switch($k){
                case 'civility':
                case 'lastname':
                
            }
        }



        $rows = [
            "data" => $_POST
        ];
        echo json_encode($rows);
    }
?>