import './scss/index.scss'
import Validator from '@niuxe/validator'


window.addEventListener('load', () =>{
    let $fields = [
            document.querySelector('input[name="phone"]'),
            document.querySelector('input[name="date_appointment"]'),
            document.querySelector('input[name="hour_appointment"]'),
        ],
        $formContact = document.getElementById('formContact'),
        validate = new Validator()


    document.querySelector('input[name=appointement]').addEventListener('change', e =>{
        for(let $field of $fields){
            $field.setAttribute('disabled', true)
            validate.removeRequireField($field)
            if(document.querySelectorAll('#errorAppointment .error').length > 0){
                document.querySelectorAll('#errorAppointment .error').forEach(el => el.remove())

            }
            if(e.target.checked){
                $field.removeAttribute('disabled')
                validate.addRequireField($field)
            }
        }
    })
    validate.addRules('checkphone', value => /^0[1-8][ .-]?(\d{2}[ .-]?){4}$/.test(value))
    validate.addRules('datemin', value =>{
        let now = new Date(),
            dateUser = new Date(value)

        dateUser.setHours(0)
        dateUser.setMinutes(0)
        now.setHours(0)
        now.setMinutes(0)

        return now.getTime() <= dateUser.getTime()
    })
    validate.addRules('businessday', value => ![0, 6].includes(new Date(value).getDay()))
    validate.addRules('betweenhour', (...args)=>{
        let [value, params] = args,
            [min, max] = params.split(';'),
            [hour, minutes] = value.split(':')
        return parseInt(min, 10) <= parseInt(hour, 10) && parseInt(max, 10) > parseInt(hour, 10)
    })
    validate.form()
    validate.middleware.formOnSuccess = (e, $el) =>{
        if($el === $formContact){
            let headers = new Headers({
                    "X-Requested-With": "XMLHttpRequest",
                    "Accept": "application/json",
                    "Content-Type": "application/x-www-form-urlencoded"
                }),
                $isAppointment = document.querySelector('input[name=appointement]'),
                $form = e.target,
                object = {},
                formData = new FormData($form),
                optionalFields = [
                    'phone',
                    'date_appointment',
                    'hour_appointment',
                ],
                onresponse = ($form, text ) =>{
                    let $content = $form.closest('.content')
                    let $result = document.createElement('div')
                    $result.classList.add('result')
                    $result.insertAdjacentHTML('beforeend', `<p class="text-center"><span>${text}</span></p>`)
                    $content.insertAdjacentElement('afterend', $result)
                    $content.classList.add('minimize')
                    setTimeout(()=>{
                        $result.classList.add('show')
                    }, 0)
                }
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
                url = window.location.origin.includes('rb-webstudio') ? $form.action : 'http://localhost/portfolio/dist/services/mail/send.html'
            fetch(url, params).then(resp =>{
                if(resp.ok === true)
                    return resp.json()
            }).then(({data, errors}) =>{
                document.querySelectorAll('span.error').forEach($el => $el.remove())
                document.querySelectorAll('.require').forEach($el => $el.classList.remove('error'))
                if(Object.keys(errors).length > 0){
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
                    $form.reset()
                    onresponse($form, "Merci pour votre message. <br>Je vous recontacte dans les plus brefs délais. <br>Vous allez recevoir une réponse automatique")
                }
            }).catch(err => {
                console.error(err)
                onresponse($form, "Une erreur est survenue. Veuillez réessayer plus tard.")
            })
        }
    }
})
