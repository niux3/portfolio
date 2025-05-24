/*
document.querySelector('form').addEventListener('submit', e =>{
    e.preventDefault()
    console.log('ok')
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
        url = window.location.origin.includes('rb-webstudio') ? $form.action : 'http://localhost/portfolio/dist/services/mail/send.html'
    fetch(url, params).then(resp =>{
        if(resp.ok === true)
            return resp.json()
    }).then(({data, errors}) =>{
        document.querySelectorAll('span.error').forEach($el => $el.remove())
        document.querySelectorAll('.require').forEach($el => $el.classList.remove('error'))
        if(Object.keys(errors).length > 0){
            //onSlideStatus('onForm')
            //getCaptcha()
            //document.querySelector('input[name="captcha"]').value = ''
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
            //onSlideStatus('onSuccess')
        }
    }).catch(err => {
        console.error(err)
        //onSlideStatus('onError')
    })
})
*/
