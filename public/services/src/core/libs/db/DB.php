<?php
    namespace src\core\libs\db;
    use \PDO;

    class DB{
        private $pdo = null;
        private $query = null;

        public function __construct($params){
            $this->pdo = new PDO($params['dns'], $params['user'], $params['password']);
            $this->pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        }

        public function beginTransaction(){
            $this->pdo->beginTransaction();
        }

        public function commit(){
            $this->pdo->commit();
        }

        public function rollBack(){
            $this->pdo->rollBack();
        }

        public function query($sql, $params = []){
            try {
                if(count($params) > 0){
                    $this->query = $this->pdo->prepare($sql);
                    foreach($params as $key => $value){
                        $paramType = PDO::PARAM_STR;

                        if(is_int($value)){
                            $paramType = PDO::PARAM_INT;
                        } elseif(is_bool($value)){
                            $paramType = PDO::PARAM_BOOL;
                        } elseif(is_null($value)){
                            $paramType = PDO::PARAM_NULL;
                        }

                        if(is_string($key)){
                            $this->query->bindValue($key, $value, $paramType);
                        } else {
                            $this->query->bindValue($key + 1, $value, $paramType);
                        }
                    }
                    $this->query->execute();
                }else{
                    $this->query = $this->pdo->query($sql);
                }

                return $this;
            } catch (Exception $e) {
                error_log("Database error: " . $e->getMessage());
                return false;
            }
        }

        public function fetch(){
            return $this->query->fetchAll(PDO::FETCH_OBJ);
        }

        public function getLastInsertId(){
            return $this->pdo->lastInsertId();
        }
    }