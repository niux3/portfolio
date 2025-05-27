<?php
namespace src\controller;

use src\core\Controller;
use src\core\libs\captcha\AsciiCaptcha;
use src\controller\components\Clean;
use src\core\libs\validator\Rules;
use src\core\libs\validator\Validator;

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;
use PHPMailer\PHPMailer\SMTP;



class ContactController extends Controller{
    function __construct($request){
        parent::__construct($request);
        header("Access-Control-Allow-Origin: *");
        header("Access-Control-Allow-Headers: *");
    }

    function show(){
        if(!empty($_SERVER['HTTP_X_REQUESTED_WITH']) && $_SERVER['HTTP_X_REQUESTED_WITH'] === 'XMLHttpRequest'){
            header('Content-Type: application/json; charset=utf-8');
            $captcha = new AsciiCaptcha('AnsiShadow');
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


    function send(){
        if(!empty($_SERVER['HTTP_X_REQUESTED_WITH']) && $_SERVER['HTTP_X_REQUESTED_WITH'] === 'XMLHttpRequest' && !empty($_POST)){
            header('Content-Type: application/json; charset=utf-8');
            if(!empty($_POST['address'])){
                $ctx['status'] = true;
                $ctx['errors'] = [];
                echo json_encode($ctx);
                die;
            }
            $_POST = Clean::normalize($_POST);

            $contact_model = $this->loadModel('Contact');
            $validator = new Validator($contact_model->get_validator());
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
                    require_once SRC.'view/contact/template_txt.php'; // $output_txt
                    require_once SRC.'view/contact/template_html.php'; // $output_html

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
}
