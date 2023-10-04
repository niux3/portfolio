<?php 
    namespace apps\core;

    class Model{

        protected $db = null;
        protected $params_db = [];
        protected $validator = [];

        public function __construct(){}

        public function get_validator(){
            return $this->validator;
        }

        protected function set_params_db(){
            $params = [
                'driver' => Configuration::get('driver'),
                'path' => Configuration::get('path'),
                'host' => Configuration::get('host'),
                'database' => Configuration::get('database'),
                'user' => Configuration::get('user'),
                'password' => Configuration::get('password'),
            ];
            $this->params_db = $params;
            return $this;
        }

        protected function get_params_db(){
            return $this->params_db;
        }
        
        protected function get_db(){
            $params = $this->set_params_db()->get_params_db();
            $this->db = \apps\core\libs\db\FactoryDB::initialize($params);
        }
    }
