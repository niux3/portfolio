<?php 
    namespace src\core\libs\validator;
    

    use src\core\libs\captcha\AsciiCaptcha;


    class Rules{

        static function notempty(){
            return intval(strlen(func_get_args()[0])) === 0;
        }

        static function honeypot(){
            return intval(strlen(func_get_args()[0])) !== 0;
        }

        static function email(){
            return filter_var(func_get_args()[0], FILTER_VALIDATE_EMAIL) === false;
        }

        static function minlength(){
            return intval(strlen(func_get_args()[0])) <= func_get_args()[1];
        }

        static function equalto(){
            return intval(strlen(func_get_args()[0])) !== func_get_args()[1];
        }

        static function phone(){
            return preg_match('#^0[1-8][ .-]?(\d{2}[ .-]?){4}$#', func_get_args()[0]) === 0;
        }

        static function alpha(){
            return preg_match('#^[a-z]+$#i', func_get_args()[0]) === 0;
        }

        static function date(){
            return strtotime(func_get_args()[0]) <= time();
        }

        static function captcha(){
            $salt = AsciiCaptcha::getSalt();
            $args_file = sprintf('%s/%s/%s.json', ROOT, 'logs', 'captcha');
            $data = json_decode(file_get_contents($args_file), true);

            $not_equalto = strtoupper(func_get_args()[0]) !== implode('', array_keys($data['captcha']));
            $not_token = $_POST[func_get_args()[1]] !== hash('sha256', strtoupper(func_get_args()[0]).$salt);
            
            return $not_token && $not_equalto;
        }
    }
