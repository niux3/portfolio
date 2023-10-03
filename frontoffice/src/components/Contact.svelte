<script>
    import { onMount } from 'svelte'
    import Validator from '../libs/validator/Validator'

    onMount(()=>{
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
                        }
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
                        "date":{
                            "error" : "<span>Ce champ doit être une date valide</span>"
                        }
                    }
                }
            },
            validate = new Validator(optionValidator)

        //add rules for phone input
        validate.addRules('checkphone', (value)=>{
            return !/^0[1-8][ .-]?(\d{2}[ .-]?){4}$/.test(value);
        });

        validate.middleware.formOnSuccess = (e, $el)=>{
            console.log('formOnSuccess', e, $el);
            let headers = new Headers({
                    "X-Requested-With": "XMLHttpRequest",
                    "Accept": "application/json",
                    "Content-Type": "application/x-www-form-urlencoded"
                }),
                $form = e.target,
                object = {},
                formData = new FormData($form)
            formData.forEach((value, key) => object[key] = value)

            let data = Object.entries(object).map(([k,v]) => `${k}=${v}`).join('&'),
                params = {
                    method: $form.method,
                    headers,
                    cache: 'no-cache',
                    redirect: 'follow',
                    referrerPolicy: 'no-referrer',
                    mode: "same-origin",
                    body: data
                }
            fetch('http://localhost/portfolio/frontoffice/mail.php', params).then(resp =>{
                if(resp.ok === true) 
                    return resp.json()
            }).then(d => console.table(d))
        }

        let $isAppointment = document.querySelector('input[name=appointment]')
        
        $isAppointment.addEventListener('change', e =>{
            let $requires = $isAppointment.closest('.col').querySelectorAll('.required input')
            for(let $input of $requires){
                if($isAppointment.checked){
                    $input.parentNode.style.height = '100%'
                    $input.classList.add('require')
                    validate.addRequireField($input)
                }else{
                    $input.parentNode.style.height = '0%'
                    $input.classList.remove('require')
                    validate.removeRequireField($input)
                }
            }
        })

        let listRequireField = [
            'input[type=text]',
            'input[type=date]',
            'input[type=password]',
            'textarea',
        ];
        document.querySelectorAll(listRequireField.join(',')).forEach(($field)=>{
            $field.addEventListener('blur', (e)=>{
                validate.element(e.target);
            });
        });

        validate.form();
    })
</script>
<div class="contact">
    <div class="wrap-contact">
        <h1>Travaillons ensemble</h1>
        <p class="intro">proposition de carrière &#x2022; me dire bonjour</p>
        <form id="form-contact" method="post">
            <div class="col">
                <div class="input select required cell-4">
                    <label>
                        <span>Civilité</span>
                        <select name="civility" required>
                            <option value="">choisir</option>
                            <option value="Mlle">Mademoiselle</option>
                            <option value="Mme">Madame</option>
                            <option value="M">Monsieur</option>
                        </select>
                    </label>
                </div>
                <div class="input text cell-4">
                    <label>
                        <span>Prénom</span>
                        <input type="text" name="firstname">
                    </label>
                </div>
                <div class="input text required cell-4">
                    <label>
                        <span>Nom</span>
                    <input type="text" name="lastname" required>
                    </label>
                </div>
            </div>
            <div class="col">
                <div class="input text required cell-6">
                    <label>
                        <span>Email</span>
                        <input type="text" name="email" required>
                    </label>
                </div>
                <div class="input text required cell-6">
                    <label>
                        <span>Sujet</span>
                        <input type="text" name="subject" required>
                    </label>
                </div>
            </div>
            <div class="col">
                <div class="cell-3 input checkbox">
                    <label>
                        <input type="checkbox" name="appointment">
                        <span>Prendre rendez vous avec moi&nbsp;?&nbsp;</span>
                    </label>
                </div>
                <div class="cell-3 input tel required">
                    <label>
                        <span>Téléphone</span>
                        <input type="text" name="phone">
                    </label>
                </div>
                <div class="cell-3 input date required">
                    <label>
                        <span>Date</span>
                        <input type="date" name="date_appointment">
                    </label>
                </div>
                <div class="cell-3 input time required">
                    <label>
                        <span>Heure</span>
                        <input type="time" min="09:00" max="18:00" name="hour_appointment">
                    </label>
                </div>
            </div>
            <input type="text" name="address" value="">
            <div class="input textarea required">
                <label>
                    <span>Message</span>
                    <textarea name="message" required></textarea>
                </label>
            </div>
            <div class="col">
                <div class="cell-4">
                    <div class="col captcha-pattern">
<pre class="cell-3">
     █████╗ 
    ██╔══██╗
    ███████║
    ██╔══██║
    ██║  ██║
    ╚═╝  ╚═╝
</pre>
<pre class="cell-3">
     ███████╗
     ██╔════╝
     █████╗  
     ██╔══╝  
     ██║     
     ╚═╝     
</pre>
<pre class="cell-3">
     ███╗   ███╗
     ████╗ ████║
     ██╔████╔██║
     ██║╚██╔╝██║
     ██║ ╚═╝ ██║
     ╚═╝     ╚═╝
</pre>
<pre class="cell-3">
     ██╗    ██╗
     ██║    ██║
     ██║ █╗ ██║
     ██║███╗██║
     ╚███╔███╔╝
      ╚══╝╚══╝ 
</pre>
                    </div>
                </div>
                <div class="cell-4">
                    <div class="input text required no-margin">
                        <label>
                            <span>Recopier le motif</span>
                            <input type="text" maxlength="4" required name="captcha">
                        </label>
                    </div>
                </div>
                <div class="cell-4">
                    <div class="input submit">
                        <button type="submit">envoyer</button>
                    </div>
                </div>
            </div>
        </form>
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
                label{
                    display: block;
                    text-transform: uppercase;
                    font-size: .8rem;
                }
                .captcha-pattern{
                    height: 100%;
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

                            &.animate{
                                height: 100%;
                            }
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
                        }
                    }
                }
            }
        }

        .col{
            display: flex;
            justify-content:space-between;

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
    }
</style>

