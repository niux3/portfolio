import '../scss/index.scss'
import ProgressBarBehavior from './progressBar/ProgressBarBehavior'
import darkmode from './darkmode'
import formContact from './formContact'
import LogReaderActivity from './logReaderActivity/LogReaderActivity'
import Utils from './Utils'
import LateralBar from './lateralBar/LateralBar'
import LayerSummary from './layerSummary/LayerSummary'


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
    let lateralBar = new LateralBar()
    lateralBar.display()

    window.addEventListener('resize', e =>{
        Utils.debounce(lateralBar.display(), 50)()
    })

    let layerSummary = new LayerSummary()
    layerSummary.init()

    if(document.getElementById('search')){
        let $search = document.getElementById('search'),
            $formSearch = $search.querySelector('form')
        $formSearch.addEventListener('submit', e =>{
            e.preventDefault()
            let formData = new FormData($formSearch)
            console.table(formData.get('q'))
        })
    }
})
