<?php
    namespace apps\controller;

    use apps\core\Controller;
    use apps\core\libs\validator\Rules;
    use apps\core\libs\validator\Validator;
    use apps\core\libs\captcha\AsciiCaptcha;


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
            header('Content-Type: application/json; charset=utf-8');
            $captcha = new \apps\core\libs\captcha\AsciiCaptcha('AnsiShadow');
            $data = $captcha->getCaptcha();

            $arg_file = sprintf('%s/%s/%s.json', ROOT, 'logs', 'captcha');
            file_put_contents($arg_file, json_encode($data));

            echo json_encode([
                'token' => $data['token'],
                'captcha' => array_values($data['captcha'])
            ]);
            die;
        }
    }
