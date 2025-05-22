import './scss/index.scss'
import Validator from '@niuxe/validator'


window.addEventListener('load', () =>{
    let $fields = [
            document.querySelector('input[name="phone"]'),
            document.querySelector('input[name="date_appointment"]'),
            document.querySelector('input[name="hour_appointment"]'),
        ]
    let defaultErrorMessage = "Ce champ ne doit pas être vide",
        errorMessage3chars = "Ce champ doit avoir minimum 3 caractères",
        optionValidator = {
            "selector" : "form",
            /*
            "fields" : {
                "civility" : {
                    "notempty":{
                        "error" : defaultErrorMessage
                    },
                },
                "lastname" : {
                    "notempty":{
                        "error" : defaultErrorMessage
                    },
                    "minlength":{
                        'params': 3,
                        "error" : errorMessage3chars
                    }
                },
                "email" : {
                    "notempty":{
                        "error" : defaultErrorMessage
                    },
                    "email":{
                        "error" : "Ce champ doit avoir la bonne saisie (dom@dom.com)"
                    }
                },
                "subject" : {
                    "notempty":{
                        "error" : defaultErrorMessage
                    },
                    "minlength":{
                        'params': 3,
                        "error" : errorMessage3chars
                    }
                },
                "message" : {
                    "notempty":{
                        "error" : defaultErrorMessage
                    },
                    "minlength":{
                        'params': 3,
                        "error" : errorMessage3chars
                    }
                },
                "hour_appointment" : {
                    "notempty" : {
                        "error" : defaultErrorMessage
                    },
                    "betweenhour" : {
                        'params': '9;18',
                        "error" :  "Les rendez vous sont compris entre 9 h 00 et 18 h 00"
                    },
                },
                "phone" : {
                    "notempty" : {
                        "error" : defaultErrorMessage
                    },
                    "checkphone" : {
                        "error" : "Le format ne semble pas être bon 0102030405"
                    },
                },
                "date_appointment" : {
                    "notempty":{
                        "error" : defaultErrorMessage
                    },
                    "datemin":{
                        "error" : "La date de rendez vous doit être suppérieur à aujourd'hui"
                    },
                    "businessday": {
                        "error":  "les rendez vous sont du lundi au vendredi"
                    },
                    "date":{
                        "error" : "Ce champ doit être une date valide"
                    }
                }
            }
            */
        }

    let validate = new Validator(optionValidator)

    document.querySelector('input[name=appointement]').addEventListener('change', e =>{
        for(let $field of $fields){
            $field.setAttribute('disabled', true)
            validate.removeRequireField($field)
            if(e.target.checked){
                $field.removeAttribute('disabled')
                validate.addRequireField($field)
            }
        }
    })
    validate.form()
})
