<script>
    import { onMount } from 'svelte'
    import Validator from '../libs/validator/Validator'


    let getCaptcha = () =>{
        fetch('http://localhost/portfolio/frontoffice/services/mail/show').then(resp =>{
            if(resp.ok === true){
                return resp.json()
            }
        }).then( data =>{
            if(document.querySelectorAll('input[name="token"]').length === 0){
                let tpl =  `<input type="hidden" tabindex="0" name="token" value="${data['token']}" />`
                document.querySelector('#form-contact').insertAdjacentHTML('afterbegin',tpl)
            }
            document.querySelector('input[name="token"]').value = data['token']
            let outputChars = ''

            for(let i = 0, len = data['captcha'].length; i < len; i++){
                let styles = [
                    'font-size:.5vw',
                    'overflow:hidden', 
                    'margin:auto 0',
                ]
                outputChars += `<pre class="cell-3" style="${styles.join(';')}">${data['captcha'][i]}</pre>`
            }
            document.querySelector('.captcha-pattern').innerHTML = outputChars
        })
    }
    let status_send_form = 'onForm'

    onMount(()=>{
        getCaptcha()

        let $isAppointment = document.querySelector('input[name=appointment]')
        
        $isAppointment.addEventListener('change', e =>{
            let $requires = $isAppointment.closest('.col').querySelectorAll('.required input')
            for(let $input of $requires){
                if($isAppointment.checked){
                    $input.parentNode.style.height = '100%'
                    $input.setAttribute('tabindex', 1)
                    $input.classList.add('require')
                    validate.addRequireField($input)
                }else{
                    $input.parentNode.style.height = '0%'
                    $input.setAttribute('tabindex', 0)
                    $input.classList.remove('require')
                    validate.removeRequireField($input)
                }
            }
        })
        let defaultErrorMessage = "<span>Ce champ ne doit pas être vide</span>",
            errorMessage3chars = "<span>Ce champ doit avoir minimum 3 caractères</span>",
            optionValidator = {
                "selector" : "#form-contact",
                "mode" : "object",
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
                            "error" : "<span>Ce champ doit avoir la bonne saisie (dom@dom.com)</span>"
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
                            "error" :  "<span>Les rendez vous sont compris entre 9 h 00 et 18 h 00</span>"
                        },
                    },
                    "phone" : {
                        "notempty" : {
                            "error" : defaultErrorMessage
                        },
                        "checkphone" : {
                            "error" : "<span>Le format ne semble pas être bon 0102030405</span>"
                        },
                    },
                    "captcha" : {
                        "notempty" : {
                            "error" : defaultErrorMessage
                        },
                        "minlength" : {
                            "params": 4,
                            "error" : "<span>ce champ doit contenir 4 caractères</span>"
                        },
                        "alpha" : {
                            "error" : "<span>ce champ doit contenir que des caractères alphabétiques</span>"
                        },
                    },
                    "date_appointment" : {
                        "notempty":{
                            "error" : defaultErrorMessage
                        },
                        "businessday": {
                            "error":  "<span>les rendez vous sont du lundi au vendredi</span>"
                        },
                        "date":{
                            "error" : "<span>Ce champ doit être une date valide</span>"
                        }
                    }
                }
            }
            let validate = new Validator(optionValidator)

        validate.addRules('checkphone', (value)=> !/^0[1-8][ .-]?(\d{2}[ .-]?){4}$/.test(value))
        validate.addRules('businessday', (value)=> [0, 6].includes(new Date(value).getDay()))
        validate.addRules('betweenhour', (...args)=>{
            let [value, params_validate] = args,
                {params, error} = params_validate,
                [min, max] = params.split(';'),
                [hour, minutes] = value.split(':')
            
            return parseInt(min, 10) > parseInt(hour, 10) || parseInt(max, 10) < parseInt(hour, 10)
        })

        validate.middleware.formOnSuccess = (e, $el)=>{
            e.preventDefault()
            status_send_form = 'onLoading'

            let headers = new Headers({
                    "X-Requested-With": "XMLHttpRequest",
                    "Accept": "application/json",
                    "Content-Type": "application/x-www-form-urlencoded"
                }),
                $form = e.target,
                object = {},
                formData = new FormData($form),
                optionalFields = [
                    'phone',
                    'date_appointment',
                    'hour_appointment',
                ]
            formData.forEach((value, key) =>{
                object[key] = value
            })
            if(!$isAppointment.checked){
                optionalFields.forEach(input => delete object[input])
            }
            let data = Object.entries(object).map(([k,v]) => `${k}=${v}`).join('&'),
                params = {
                    method: 'POST',
                    headers,
                    cache: 'no-cache',
                    redirect: 'follow',
                    referrerPolicy: 'no-referrer',
                    mode: "cors",
                    body: data
                },
                url ='http://localhost/portfolio/frontoffice/services/mail/send'
            fetch(url, params).then(resp =>{
                if(resp.ok === true) 
                    return resp.json()
            }).then(({data, errors}) =>{
                document.querySelectorAll('span.error').forEach($el => $el.remove())
                document.querySelectorAll('.require').forEach($el => $el.classList.remove('error'))
                if(Object.keys(errors).length > 0){
                    status_send_form = 'onForm'
                    getCaptcha()
                    document.querySelector('input[name="captcha"]').value = ''
                    for(let k in errors){
                        if(Object.keys(errors).includes(k)){
                            let $input = document.querySelector(`*[name="${k}"]`)
                            $input.classList.add('error')
                            $input.insertAdjacentHTML('afterend', `<span class="error">${errors[k]}</span>`)
                        }else{
                            throw new Error("Une erreur est survenue. Veuillez réessayer plus tard.");
                        }
                    }
                }else{
                    // $el.reset()
                    status_send_form = 'onSucess'
                    alert('ok !')
                }
            }).catch(err => {
                console.error(err)
                status_send_form = 'onError'
            })
        }


        let listRequireField = [
            'input[type=text]',
            'input[type=date]',
            'input[type=time]',
            'input[type=password]',
            'textarea',
            'select',
        ]
        document.querySelectorAll(listRequireField.join(',')).forEach(($field)=>{
            $field.addEventListener('blur', (e)=>{
                validate.element(e.target)
            })
        })

        validate.form()
    })
</script>
<div class="contact">
    <div class="wrap-contact">
        <h1>Travaillons ensemble</h1>
        <p class="intro">proposition de carrière &#x2022; me dire bonjour</p>
            <form id="form-contact" class="accordeon" style="{status_send_form !== 'onForm'? 'max-height:0%; opacity:0;' : 'max-height:100%; opacity:1'}">
                <div class="col">
                    <div class="input select required cell-4">
                        <label>
                            <span>Civilité</span>
                            <select name="civility" required tabindex="1">
                                <option value="">choisir</option>
                                <option value="Mademoiselle">Mademoiselle</option>
                                <option value="Madame">Madame</option>
                                <option value="Monsieur" selected>Monsieur</option>
                            </select>
                        </label>
                    </div>
                    <div class="input text cell-4">
                        <label>
                            <span>Prénom</span>
                            <input type="text" name="firstname" tabindex="1">
                        </label>
                    </div>
                    <div class="input text required cell-4">
                        <label>
                            <span>Nom</span>
                            <input type="text" name="lastname" required tabindex="1" value="Delanoé">
                        </label>
                    </div>
                </div>
                <div class="col">
                    <div class="input text required cell-6">
                        <label>
                            <span>Email</span>
                            <input type="text" name="email" required tabindex="1" value="renaudbourdeau@gmail.com">
                        </label>
                    </div>
                    <div class="input text required cell-6">
                        <label>
                            <span>Sujet</span>
                            <input type="text" name="subject" required tabindex="1" value="un sujet">
                        </label>
                    </div>
                </div>
                <div class="col">
                    <div class="cell-3 input checkbox">
                        <label>
                            <input type="checkbox" name="appointment" tabindex="1">
                            <span>Prendre rendez vous avec moi&nbsp;?&nbsp;</span>
                        </label>
                    </div>
                    <div class="cell-3 input tel required">
                        <label>
                            <span>Téléphone</span>
                            <input type="text" name="phone" tabindex="0">
                        </label>
                    </div>
                    <div class="cell-3 input date required">
                        <label>
                            <span>Date</span>
                            <input type="date" name="date_appointment" tabindex="0">
                        </label>
                    </div>
                    <div class="cell-3 input time required">
                        <label>
                            <span>Heure</span>
                            <input type="time" name="hour_appointment" tabindex="0">
                        </label>
                    </div>
                </div>
                <input type="text" name="address" value="">
                <div class="input textarea required">
                    <label>
                        <span>Message</span>
                        <textarea name="message" required tabindex="1">lorem ipsum</textarea>
                    </label>
                </div>
                <div class="col">
                    <div class="cell-4">
                        <div class="col captcha-pattern"></div>
                    </div>
                    <div class="cell-4">
                        <div class="input text required no-margin">
                            <label>
                                <span>Recopier le motif</span>
                                <input type="text" maxlength="4" required name="captcha" tabindex="1">
                            </label>
                        </div>
                    </div>
                    <div class="cell-4">
                        <div class="input submit">
                            <button type="submit" tabindex="1">envoyer</button>
                        </div>
                    </div>
                </div>
            </form>

            <div class="accordeon loading" style="{status_send_form !== 'onLoading'? 'max-height:0%; opacity:0;' : 'max-height:100%; opacity:1'}">

            
            </div>
            <div class="accordeon" style="{status_send_form !== 'onSucess'? 'max-height:0%; opacity:0;' : 'max-height:100%; opacity:1'}">success</div>
            <div class="accordeon" style="{status_send_form !== 'onError'? 'max-height:0%; opacity:0;' : 'max-height:100%; opacity:1'}">error</div>
    </div>
</div>
<style lang="scss">
    .contact{
        display: flex;
        flex-direction:column;
        height: 100%;

        input[name="address"]{
            position: absolute;
            top: -500000px;
        }

        .wrap-contact{
            margin: auto;
            width: 100%;

            .accordeon{
                transition: max-height 400ms, opacity 400ms;
                overflow: hidden;
                max-height: 0%;

                &.loading{
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    height: 50vh;
                }
            }
            
            h1, .intro{
                text-transform: uppercase;
                text-align: center;
            }

            h1{
                margin-bottom: 0;
            }

            .no-margin{
                margin: 0 !important;
            }
            
            form{
                max-width: 1124px;
                margin: 50px auto;

                label{
                    display: block;
                    text-transform: uppercase;
                    font-size: .8rem;
                }
                .captcha-pattern{
                    height: 100%;
                    justify-content: center;
                    pre{
                        font-size: .5vw;
                        overflow: hidden;
                        margin: auto 0;
                    }
                }
                
                .input{
                    &.text, 
                    &.date,
                    &.time,
                    &.textarea,
                    &.tel,
                    &.select{
                        margin-bottom: 25px;

                        @media screen and (max-width: 639px) {
                            margin-bottom: 0;
                        }


                        label > span:first-of-type{
                            display: inline-block;
                            margin-bottom: 10px;
                        }
                        input, textarea, select{
                            width: 100%;
                            height: 50px;
                            border-radius: 3px;
                            border: 1px solid darken(#f5f5f5, 30%);
                            font-size: 1rem;
                            padding: 0 15px;
                            background-color: darken(#f5f5f5, 5%);
                            transition: border-color 400ms, background-color 400ms;

                            &:focus, &:active{
                                outline:none !important;
                                border-color: darken(#f5f5f5, 70%);
                                background-color: #f5f5f5;
                            }

                            &[name=captcha]{
                                text-transform: uppercase;
                            }
                        }

                        textarea{
                            padding: 15px;
                            height: 100%;
                        }
                    }

                    &.date, 
                    &.time,
                    &.tel{
                        label{
                            height: 0%;
                            transition: height 400ms;
                            overflow: hidden;
                        }
                    }

                    &.checkbox{
                        margin: auto 0;
                    }

                    &.required{
                        label > span:first-of-type{
                            &:after{
                                content : ' *';
                                color: red;
                                font-weight: 600;
                            }
                        }
                    }


                    &.submit{
                        height: 100%;
                        display: flex;
                        align-items: end;

                        button{
                            border: 2px solid darken(#f5f5f5, 30%);
                            background-color: transparent;
                            text-transform: uppercase;
                            width: 100%;
                            height: 50px;
                            border-radius:3px;
                            margin-bottom: 8px;
                            cursor: pointer;
                        }
                    }
                }
            }
        }

        .col{
            display: flex;
            justify-content:space-between;
            flex-wrap: wrap;

            .cell-6{
                width: 49%;
            }

            .cell-3{
                width: 24%;
            }

            .cell-4{
                width: 32%;
            }
        }

        @media screen and (max-width: 639px) {
            *[class*=cell]{
                width: 100% !important;
            }
        }
    }
</style>

