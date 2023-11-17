<?php
namespace src\controller;

use src\core\Controller;
use src\core\Exception;


class MailController extends Controller{
    function show($uuid){
        $mask = '%s/model/data/%s';
        $path = sprintf($mask, SRC, 'data_recruteurs.json');
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
            'user' => $row,
        ]);
    }


    function mail_read($id){
        header("Content-Type: image/png");
        $path = sprintf('%s/logs/mail_read.csv', ROOT);
        $resource = fopen($path, 'a+');
        $row = [
            $id,
            strftime('%d/%m/%Y %H:%M:%S', time())
        ];
        fwrite($resource, implode(', ', $row)."\n");
        fclose($resource);
        $im = imagecreate(1, 1);
        $background_color = imagecolorallocate($im, 0, 0, 0);
        imagepng($im);
    }
}

