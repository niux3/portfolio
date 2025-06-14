import './scss/index.scss'
import ProgressBarBehavior from './js/progressBar/ProgressBarBehavior'
import darkmode from './js/darkmode'
import formContact from './js/formContact'
import LogReaderActivity from './js/logReaderActivity/LogReaderActivity'


window.addEventListener('DOMContentLoaded', () =>{
    // progressBar
    ProgressBarBehavior.run()

    // darkmode
    darkmode()

    //logReader
    let logReaderActivity = new LogReaderActivity()
    logReaderActivity.execute()

    // form contact
    formContact()
})
