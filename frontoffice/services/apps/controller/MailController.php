<?php
    namespace apps\controller;

    use apps\core\Controller;
    use apps\core\libs\validator\Rules;
    use apps\core\libs\validator\Validator;


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
                
                $mail_model = $this->loadModel('Mail');
                $validator = new Validator($mail_model->get_validator());
                $validator->check($_POST);

                $rows = [
                    "data" => $_POST,
                    "errors" => $validator->get_errors()
                ];
                echo json_encode($rows);
            }
        }


        function show(){
            $data = [
                "civility" => "",
                "lastname" => "a",
                "email" => "",
                "subject" => "",
                "message" => "",
                "hour_appointment" => "",
                "date_appointment" => "",
                "phone" => "",
                "captcha" => "",
                "firstname" => "",
            ];
            $mail_model = $this->loadModel('Mail');
            $validator = new Validator($mail_model->get_validator());
            $validator->check($data);

            print_r($validator->get_errors());
        }
    }
