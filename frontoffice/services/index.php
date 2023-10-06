<?php
    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    error_reporting(E_STRICT);

    define('ROOT', dirname(__FILE__));
    define('APPS', sprintf('%s/apps/', ROOT));
    try{
        require_once APPS.'core/Autoloader.php';


        $loader = new \apps\core\Autoloader();
        $loader->register();
        $namespaces = [
            'apps\core\libs\db' => APPS.'core/libs/db/',
            'PHPMailer\PHPMailer' => APPS.'core/libs/phpmailer/src/',
            'apps\core\libs\validator' => APPS.'core/libs/validator/',
            'apps\core\libs\captcha' => APPS.'core/libs/captcha/',
            'apps\core\libs\captcha\chars' => APPS.'core/libs/captcha/chars',
            'apps\core' => APPS.'core/',
            'apps\controller' => APPS.'controller/',
            'apps\model' => APPS.'model/',
        ];

        foreach($namespaces as $namespace => $path){
            $loader->addNamespace($namespace, $path);
        }
        
        $router = new \apps\core\Router();
        $router->executeRequest();
    }catch(Exception $e){
        echo $e->getMessage();
        header('HTTP/1.1 500 Internal Server Error');
    }
