<?php
    namespace src\controller\components;

    class Clean{
        static function normalize($list){
            $clean_methods = [
                'trim',
                'strip_tags',
                'htmlspecialchars',
            ];
            foreach($clean_methods as $method){
                $list = array_map($method, $list);
            }
            return $list;
        }
    }