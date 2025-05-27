<?php
namespace src\controller;

use src\core\Controller;
use src\core\Exception;


class MailController extends Controller{
    function show($uuid){
        $mask = '%s/model/data/%s';
        $path = sprintf($mask, SRC, 'contacts_mailing.json');
        $resource = file_get_contents($path);
        $data = json_decode($resource, false);
        $row = [];
        foreach($data as $v){
            if($v->id === $uuid){
                $row = $v;
                break;
            }
        }
        if(empty($row)){
            throw new Exception('page not found', 404);
        }
        $fullname = sprintf('%s %s', $row->firstname, $row->lastname);
        $this->render([
            'fullname' => $fullname,
        ]);
    }
}

