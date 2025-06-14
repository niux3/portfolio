<?php
namespace src\controller;

use src\core\Controller;
use src\core\libs\db\querybuilder\QueryBuilder;


class PagesController extends Controller{
    function __construct($request){
        parent::__construct($request);
        $this->Page = $this->loadModel('Page');
    }

    function index($name=""){
        $q = new QueryBuilder('select');
        echo $q->select('field')->from('tables')->where('id = :id OR name = :name', 'city = :city')->where('firstname = :firstname');
        $this->render([
            'rows' => $this->Page->fetchAll(),
        ]);
    }

    protected function beforeRender(){
        echo 'ok';
    }

    function show($id){
        $this->render([
            'row' => current($this->Page->fetch($id))
        ]);
    }

    function create(){
        if(!empty($_POST)){
            $this->Page->save($_POST);
            header('location:/');
        }
        $this->render([]);
    }

    function viewsLog(){
        header("Access-Control-Allow-Origin: *");
        header("Access-Control-Allow-Methods: GET, POST, OPTIONS");
        header("Access-Control-Allow-Headers: Content-Type, X-Requested-With");
        if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
            // Réponse à la pré-requête CORS
            http_response_code(204);
            exit;
        }

        if(!empty($_SERVER['HTTP_X_REQUESTED_WITH']) && $_SERVER['HTTP_X_REQUESTED_WITH'] === 'XMLHttpRequest' && !empty($_POST)){
            header('Content-Type: application/json; charset=utf-8');
            echo json_encode(["post" => $_POST, "msg" => 'ok']);
            exit;
        }
        // Pour tout autre cas (ex: accès direct via navigateur)
        echo json_encode(["msg" => "pas de POST"]);
        exit;
    }
}
