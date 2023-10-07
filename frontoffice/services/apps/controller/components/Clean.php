<?php
    namespace apps\controller\Component;

    class Clean{
        static function normalize($list){
            foreach($list as $k => $v){
                if(!is_array($v)){
                    $clean_methods = [
                        'trim',
                        'strip_tags',
                        'htmlspecialchars',
                    ];

                    foreach($clean_methods as $method){
                        $v = array_map($method, $v);
                    }
                }else{
                    Clean::normalize($v);
                }
            }
            return $list;
        }
    }