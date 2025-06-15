<?php
namespace src\controller;

use src\core\Controller;
use src\core\libs\db\querybuilder\QueryBuilder;


class PagesController extends Controller{
    function __construct($request){
        parent::__construct($request);
        // $this->Page = $this->loadModel('Page');

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

    //function index($name=""){
        //$q = new QueryBuilder('select');
        //echo $q->select('field')->from('tables')->where('id = :id OR name = :name', 'city = :city')->where('firstname = :firstname');
        //$this->render([
            //'rows' => $this->Page->fetchAll(),
        //]);
    //}

    //protected function beforeRender(){
        //echo 'ok';
    //}

    //function show($id){
        //$this->render([
            //'row' => current($this->Page->fetch($id))
        //]);
    //}

    //function create(){
        //if(!empty($_POST)){
            //$this->Page->save($_POST);
            //header('location:/');
        //}
        //$this->render([]);
    //}

    private function getUserIP() {
        if (!empty($_SERVER['HTTP_CLIENT_IP'])) return $_SERVER['HTTP_CLIENT_IP'];
        if (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) return explode(',', $_SERVER['HTTP_X_FORWARDED_FOR'])[0];
        return $_SERVER['REMOTE_ADDR'];
    }

    function viewsLog(){
        if(!empty($_SERVER['HTTP_X_REQUESTED_WITH']) && $_SERVER['HTTP_X_REQUESTED_WITH'] === 'XMLHttpRequest'){
            if(!empty($_POST)){
                header('Content-Type: application/json; charset=utf-8');
                $path = isset($_POST['path']) ? $_POST['path'] : 'unknown';
                $type = isset($_POST['type']) ? $_POST['type'] : 'unknown';
                $theme = isset($_POST['theme']) ? $_POST['theme'] : 'unknown';
                $ip = $this->getUserIP();
                $date = date('c');

                $output = "$date | $ip | $type | $path | $theme";

                if($type === 'click'){
                    $url = isset($_POST['url']) ? $_POST['url'] : 'unknown';
                    $text = isset($_POST['text']) ? $_POST['text'] : 'unknown';
                    $output .= " | $url | $text";
                }

                $pathToLog = ROOT.'/log/pages_views.log';
                if(file_exists($pathToLog) && file_put_contents($pathToLog, $output."\n", FILE_APPEND) !== false){
                    echo json_encode(["post" => $_POST, "msg" => ROOT.'/log/pages_views.log']);
                }else{
                    //echo json_encode(["post" => $_POST, "msg" => 'ko', "file" => file_exists($pathToLog), 'path' => $pathToLog]);
                    echo json_encode(["msg" => 'ko');
                }
                die;
            }
        }
        die;
    }
}
