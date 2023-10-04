<?php
    namespace apps\core\libs\validator;

    use apps\core\libs\validator\Rules;
    

    class Validator{
        private $configuration = [];
        private $errors = [];

        function __construct($configuration = []){
            $this->configuration = $configuration;
        }


        function check($data){
            foreach($data as $k => $v){
                if(!empty($this->configuration[$k])){
                    foreach($this->configuration[$k] as $method => $config_method){
                        $args = [$v];
                        if(!empty($config_method['params'])){
                            $args[] = $config_method['params'];
                        }
                        if(Rules::$method(...$args)){
                            $this->errors[$k] = $config_method['error'];
                        }
                    }
                }
            }
        }

        function get_errors(){
            return $this->errors;
        }

        function set_configuration($config){
            $this->configuration = $config;
        }
    }

