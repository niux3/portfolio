<?php
    namespace apps\controller;
    use apps\core\Controller;


    class PageController extends Controller{
        public function __construct(){
            
        }


        function index(){
            echo 'ok';
        }


        function show(){
            $this->render(['test2' => 'bla']);
        }
    }
