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

        function template(){
            $data = [
                "civility" => 'M',
                "firstname" => "Pierre",
                "lastname" => "Durant",
                "email" => "dom@dom.com",
                "subject" => "un sujet",
                "phone" => "0102030405",
                "date_appointment" => "2023-10-11",
                "hour_appointment" => "10:00",
                "message" => "
Si je t'emmerde, tu me le dis, même si on frime comme on appelle ça en France... le cycle du cosmos dans la vie... c'est une grande roue et cela même si les gens ne le savent pas ! C'est pour ça que j'ai fait des films avec des replicants.
Ça sounds good, je suis mon meilleur modèle car il faut se recréer... pour recréer... a better you et c'est une sensation réelle qui se produit si on veut ! Tu vas te dire : J'aurais jamais cru que le karaté guy pouvait parler comme ça !
Ah non attention, là on voit qu'on a beaucoup à travailler sur nous-mêmes car c'est juste une question d'awareness et c'est une sensation réelle qui se produit si on veut ! Et j'ai toujours grandi parmi les chiens.
Ça sounds good, je suis mon meilleur modèle car on vit dans une réalité qu'on a créée et que j'appelle illusion puisque the final conclusion of the spirit is perfection C'est cette année que j'ai eu la révélation !
Tu vois, même si on frime comme on appelle ça en France... il faut se recréer... pour recréer... a better you et ça, c'est très dur, et, et, et... c'est très facile en même temps. Mais ça, c'est uniquement lié au spirit.
"
            ];

            extract($data);
            require_once APPS.'/view/template_destination.php';
            
            printf('<pre>%s</pre>', $output);


        }


        function response(){
            $data = [
                "civility" => 'Monsieur',
                "firstname" => "Pierre",
                "lastname" => "Durant",
                "email" => "dom@dom.com",
                "subject" => "un sujet",
                "phone" => "0102030405",
                "date_appointment" => "2023-10-11",
                "hour_appointment" => "10:00",
                "message" => "
Si je t'emmerde, tu me le dis, même si on frime comme on appelle ça en France... le cycle du cosmos dans la vie... c'est une grande roue et cela même si les gens ne le savent pas ! C'est pour ça que j'ai fait des films avec des replicants.
Ça sounds good, je suis mon meilleur modèle car il faut se recréer... pour recréer... a better you et c'est une sensation réelle qui se produit si on veut ! Tu vas te dire : J'aurais jamais cru que le karaté guy pouvait parler comme ça !
Ah non attention, là on voit qu'on a beaucoup à travailler sur nous-mêmes car c'est juste une question d'awareness et c'est une sensation réelle qui se produit si on veut ! Et j'ai toujours grandi parmi les chiens.
Ça sounds good, je suis mon meilleur modèle car on vit dans une réalité qu'on a créée et que j'appelle illusion puisque the final conclusion of the spirit is perfection C'est cette année que j'ai eu la révélation !
Tu vois, même si on frime comme on appelle ça en France... il faut se recréer... pour recréer... a better you et ça, c'est très dur, et, et, et... c'est très facile en même temps. Mais ça, c'est uniquement lié au spirit.
"
            ];

            $this->render($data);
        }
    }
