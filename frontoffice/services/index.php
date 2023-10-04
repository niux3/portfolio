<?php
    define('ROOT', dirname(__FILE__));
    define('APPS', sprintf('%s/apps/', ROOT));
    try{
        require_once APPS.'core/Autoloader.php';

        $loader = new \apps\core\Autoloader();
        $loader->register();
        $namespaces = [
            'apps\core\libs\db' => APPS.'core/libs/db/',
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
    }
