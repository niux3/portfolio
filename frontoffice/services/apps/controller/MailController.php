<?php
    namespace apps\controller;
    use apps\core\Controller;


    class MailController extends Controller{
        public function __construct(){
            header("Access-Control-Allow-Origin: *");
            header("Access-Control-Allow-Headers: *");
        }


        function send(){
            if(!empty($_SERVER['HTTP_X_REQUESTED_WITH']) && $_SERVER['HTTP_X_REQUESTED_WITH'] === 'XMLHttpRequest' && !empty($_POST)){
                header('Content-Type: application/json; charset=utf-8');

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
            }else{
                echo 'ok';
            }
        }


        function show(){
            $rules = new \apps\core\libs\validator\Rules();
            echo date('d M Y', strtotime('2023-10-05')).'<hr>';
            echo $rules::date('2023-10-05')? 'ok': 'ko';
            echo '<hr>';
        }
    }
