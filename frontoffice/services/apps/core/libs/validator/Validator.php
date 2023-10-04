<?php
    namespace apps\core\libs\validator;
    

    class Validator{
        private $configuration = [];

        function __construct($configuration){
            $this->configuration = $configuration;
        }
    }