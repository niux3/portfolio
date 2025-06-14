import './scss/index.scss'
import ProgressBarBehavior from './js/progressBar/ProgressBarBehavior'
import darkmode from './js/darkmode'
import formContact from './js/formContact'


window.addEventListener('DOMContentLoaded', () =>{
    // progressBar
    ProgressBarBehavior.run()

    // darkmode
    darkmode()

    // form contact
    formContact()
})
