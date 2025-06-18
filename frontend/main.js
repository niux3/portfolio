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


    // lateralBar
    if(document.getElementById('lateralBar')){
        let $lateralBar = document.getElementById('lateralBar'),
            $buttons = document.querySelectorAll('#lateralBar button'),
            $main = document.body.querySelector('main')

        $buttons.forEach($button =>{
            $button.addEventListener('pointerdown', e =>{
                console.log($button.dataset.panel)
                if($button.dataset.panel === "true"){
                    $buttons.forEach($btn => $btn.classList.remove('current'))
                    $button.classList.add('current')

                    $main.classList.add('move')
                    $lateralBar.classList.add('move')
                }
            })
        })
    }

})
