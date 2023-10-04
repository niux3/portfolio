<?php 
    namespace apps\core\libs\validator;


    class Rules{
        static function notempty($value){
            return intval(strlen($value)) === 0;
        }

        static function email($value){
            return filter_var($value, FILTER_VALIDATE_EMAIL) === false;
        }

        static function minlen($value, $number){
            return intval(strlen($value)) >= $number;
        }

        static function phone($value){
            return preg_match('#^0[1-8][ .-]?(\d{2}[ .-]?){4}$#', $value) === 0;
        }

        static function alpha($value){
            return preg_match('#^[a-z]+$#i', $value) === 0;
        }

        static function date($value){
            return strtotime($value) <= time();
        }
    }