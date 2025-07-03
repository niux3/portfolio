<?php
namespace src\controller;

use src\core\Controller;


class PostsController extends Controller{
    function __construct($request){
        parent::__construct($request);
        // Liste blanche des origines autorisées
        $allowed_origins = [
            'http://localhost:5000',
            'https://rb-webstudio.go.yj.fr'
        ];

        $origin = $_SERVER['HTTP_ORIGIN'] ?? '';

        if (in_array($origin, $allowed_origins)) {
            header("Access-Control-Allow-Origin: $origin");
        } else {
            // En prod, refuser (pas de CORS)
            header("Access-Control-Allow-Origin: null");
        }

        header("Access-Control-Allow-Methods: GET, POST, OPTIONS");
        header("Access-Control-Allow-Headers: Content-Type, X-Requested-With");
        if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
            // Réponse à la pré-requête CORS
            http_response_code(204);
            exit;
        }
    }

    function search(){
        if(!empty($_SERVER['HTTP_X_REQUESTED_WITH']) && $_SERVER['HTTP_X_REQUESTED_WITH'] === 'XMLHttpRequest'){
            if(!empty($_GET)){
                header('Content-Type: application/json; charset=utf-8');
                $public_folder = dirname(ROOT);
                $path_to_json = $public_folder.'/static/data-posts.json';
                $json = json_decode(file_get_contents($path_to_json));
                $output = array_filter($json->post, function($v){
                    return strstr($v->title, $_GET['q']) || strstr($v->body, $_GET['q']);
                });

                echo json_encode([
                     "data" => $output
                ]);
                die;
            }
        }
        die;
    }
}
