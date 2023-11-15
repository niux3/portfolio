<?php
    namespace apps\controller;

    use apps\core\Controller;


    class PublipostageController extends Controller{
        public function __construct(){
        }


        function voir(){
            // echo 'Publipostage/voir.html';
            // echo '<br>';
            // echo uniqid();
            // echo '<br>';
            // var_dump($_REQUEST);
            // $this->render([], '404');
            // die;
            $this->render([
                'contact' => "Monsieur Bourdeau"
            ]);
        }

    }
