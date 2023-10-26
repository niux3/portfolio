<?php
    namespace apps\controller;

    use apps\core\Controller;
    use apps\controller\Component\Clean;
    use apps\core\libs\validator\Rules;
    use apps\core\libs\validator\Validator;
    use apps\core\libs\captcha\AsciiCaptcha;

    use PHPMailer\PHPMailer\PHPMailer;
    use PHPMailer\PHPMailer\Exception;
    use PHPMailer\PHPMailer\SMTP;


    class MailController extends Controller{
        public function __construct(){
            header("Access-Control-Allow-Origin: *");
            header("Access-Control-Allow-Headers: *");

            // if(empty($_GET['apikey'])){
            //     header('HTTP/1.1 400 Internal Server Error');
            //     $ctx["errors"] = "mauvaise url";
            //     $ctx["status"] = false;
            //     echo json_encode($ctx);
            //     die;
            // }
        }


        function send(){
            if(!empty($_SERVER['HTTP_X_REQUESTED_WITH']) && $_SERVER['HTTP_X_REQUESTED_WITH'] === 'XMLHttpRequest' && !empty($_POST)){
                header('Content-Type: application/json; charset=utf-8');

                $_POST = Clean::normalize($_POST);

                $mail_model = $this->loadModel('Mail');
                $validator = new Validator($mail_model->get_validator());
                $validator->check($_POST);
                
                unset($_POST['token']);
                $ctx = [
                    "data" => $_POST,
                    "errors" => []
                ];
                

                if(count($validator->get_errors()) > 0){
                    $ctx["errors"] = $validator->get_errors();
                    $ctx["status"] = false;
                    echo json_encode($ctx);
                    die;
                }else{
                    try{
                        $mail = new PHPMailer(true);
                        $mail->isSMTP();

                        $mail->SMTPSecure = PHPMailer::ENCRYPTION_SMTPS;
                        $mail->SMTPAuth = true;

                        $mail->Host = 'smtp.gmail.com';
                        $mail->Username = 'renaudbourdeau@gmail.com';
                        $mail->Password = 'pvcr uiwq xjlt vlig ';
                        $mail->Port = 465;
                        $mail->charSet = "UTF-8"; 

                        $mail->setFrom('renaudbourdeau@gmail.com');
                        $mail->addAddress('renaudbourdeau@gmail.com');

                        $mail->isHTML(false);

                        extract($_POST);
                        require_once APPS.'view/Mail/template_txt.php'; // $output_txt
                        require_once APPS.'view/Mail/template_html.php'; // $output_html
                        
                        $mail->Subject = sprintf('[PORTFOLIO] %s', $_POST['subject']);
                        $mail->Body = $output_txt;
                        
                        // mail txt (à moi)
                        if (!$mail->send()) {
                            throw new Exception('Mailer Error: ' . $mail->ErrorInfo);
                        } else {
                            sleep(1);
                            $mail->clearAddresses();
                            $mail->addAddress($_POST['email']);
                            $mail->isHTML(true);
                            $mail->Subject = "A propos de votre visite sur rb webstudio le ".date('d/m/Y');
                            $mail->Body = $output_html;
                            $mail->AltBody = "Bonjour, je suis ravi de faire votre connaissance. Merci pour l'email que vous m'avez transmis.  J'apprécie le fait que vous ayez pris le temps de le rédiger. Je vous encourage à consulter mon profil LinkedIn : https://www.linkedin.com/in/renaud-bourdeau-%F0%9F%90%A7-7639b944 . Vous y trouverez davantage d'informations sur mon parcours professionnel et mes compétences. Je vous souhaite une excellente journée, et encore une fois, je vous remercie pour cette prise de contact. Cordialement.";
                            
                            // réponse automatique
                            if (!$mail->send()) {
                                throw new Exception('Mailer Error: ' . $mail->ErrorInfo);
                            } else {
                                $ctx["status"] = true;
                            }
                        }
                        echo json_encode($ctx);
                        die;
                    } catch (Exception $e) {
                        header('HTTP/1.1 400 Internal Server Error');
                        $ctx["errors"] = [
                            'mail_lib' => 'Mailer Error: ' . $mail->ErrorInfo
                        ];
                        $ctx["status"] = false;
                        echo json_encode($ctx);
                        die;
                    }
                }
            }
        }


        function show(){
            if(!empty($_SERVER['HTTP_X_REQUESTED_WITH']) && $_SERVER['HTTP_X_REQUESTED_WITH'] === 'XMLHttpRequest'){
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

        /*
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
            require_once APPS.'view/Mail/template_html.php';

            
            printf('<pre>%s</pre>', $output_html);
            print_r($data);


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


        function test_send(){
            $mail = new PHPMailer(true);
            $mail->isSMTP();
            // $mail->SMTPDebug = SMTP::DEBUG_SERVER;
            $mail->SMTPSecure = PHPMailer::ENCRYPTION_SMTPS;
            $mail->SMTPAuth = true;
    
    
            $mail->Host = 'smtp.gmail.com';
            $mail->Username = 'renaudbourdeau@gmail.com';
            $mail->Password = 'pvcr uiwq xjlt vlig ';
            $mail->Port = 465;
    
            $mail->setFrom('renaudbourdeau@gmail.com');
            $mail->addAddress('renaudbourdeau@gmail.com'); // destinataire
    
            $mail->isHTML(true);
    
            $mail->Subject = 'un super sujet';
            $mail->Body = "super contenu";
    
            if (!$mail->send()) {
                echo 'Mailer Error: ' . $mail->ErrorInfo;
            } else {
                echo 'Message sent!';
                //Section 2: IMAP
                //Uncomment these to save your message in the 'Sent Mail' folder.
                #if (save_mail($mail)) {
                #    echo "Message saved!";
                #}
            }
        }
        */
    }
