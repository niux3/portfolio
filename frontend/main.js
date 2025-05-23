import './scss/index.scss'
import Validator from '@niuxe/validator'


window.addEventListener('load', () =>{
    let $fields = [
            document.querySelector('input[name="phone"]'),
            document.querySelector('input[name="date_appointment"]'),
            document.querySelector('input[name="hour_appointment"]'),
        ],
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
})
