<?php 
    namespace apps\model;
    use apps\core\Model;
    
    class Mail extends Model{
        protected $validator = [
            "civility" => [
                "notempty" => [
                    "error" => "<span>Ce champ ne doit pas être vide</span>",
                ],
            ],
            "lastname" =>[
                "minlength" => [
                    "params" => 3,
                    "error" => "<span>Ce champ doit avoir minimum 3 caractères</span>"
                ],
                "notempty" => [
                    "error" => "<span>Ce champ ne doit pas être vide</span>",
                ],
            ],
            "email" =>[
                "email" => [
                    "error"=> "<span>Ce champ doit avoir la bonne saisie (dom@dom.com)</span>"
                ],
                "notempty" => [
                    "error" => "<span>Ce champ ne doit pas être vide</span>",
                ],
            ],
            "subject" =>[
                "minlength" => [
                    "params" => 3,
                    "error" => "<span>Ce champ doit avoir minimum 3 caractères</span>"
                ],
                "notempty" => [
                    "error" => "<span>Ce champ ne doit pas être vide</span>",
                ],
            ],
            "message" =>[
                "minlength" => [
                    "params" => 3,
                    "error" => "<span>Ce champ doit avoir minimum 3 caractères</span>"
                ],
                "notempty" => [
                    "error" => "<span>Ce champ ne doit pas être vide</span>",
                ],
            ],
            "hour_appointment" => [
                "notempty" => [
                    "error" => "<span>Ce champ ne doit pas être vide</span>",
                ],
            ],
            "phone" =>[
                "phone" => [
                    "error" => "<span>Le format ne semble pas être bon 0102030405</span>"
                ],
                "notempty" => [
                    "error" => "<span>Ce champ ne doit pas être vide</span>",
                ],
            ],
            "date_appointment" =>[
                "date" => [
                    "error" => "<span>Ce champ doit être une date valide</span>"
                ],
                "notempty" => [
                    "error" => "<span>Ce champ ne doit pas être vide</span>",
                ],
            ],
            "captcha" =>[
                "equalto" => [
                    "params"=> 4,
                    "error" => "<span>Ce champ doit avoir 4 caractères</span>"
                ],
                "notempty" => [
                    "error" => "<span>Ce champ ne doit pas être vide</span>",
                ],
                "captcha" => [
                    "params"=> 'token',
                    "error" => "<span>captcha le motif ne correspond pas</span>",
                ],
            ],
        ];
    }
