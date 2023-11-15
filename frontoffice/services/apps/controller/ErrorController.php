<?php
    namespace apps\controller;

    use apps\core\Controller;


    class ErrorController extends Controller{
        function page_introuvable(){
            // echo 'Publipostage/voir.html';
            // echo '<br>';
            // echo uniqid();
            // echo '<br>';
            // var_dump($_REQUEST);
            // $this->render([], '404');
            // die;
            $this->render([], 'Error/page_introuvable');
        }

    }
