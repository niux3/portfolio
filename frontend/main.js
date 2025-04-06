import './scss/index.scss'


(()=>{
    let $fields = [
        document.querySelector('input[name="phone"]'),
        document.querySelector('input[name="date_appointment"]'),
        document.querySelector('input[name="hour_appointment"]'),
    ]
    document.querySelector('input[name=appointement]').addEventListener('change', e =>{
        $fields.forEach($field => e.target.checked? $field.removeAttribute('disabled') : $field.setAttribute('disabled', true))
    })
})()
