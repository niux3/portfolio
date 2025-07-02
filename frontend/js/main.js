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
            let headers = new Headers({
                    "X-Requested-With": "XMLHttpRequest",
                    "Accept": "application/json",
                    "Content-Type": "application/x-www-form-urlencoded"
                }),
                object = {},
                formData = new FormData($formSearch)
            formData.forEach((value, key) =>{
                object[key] = value
            })
            let data = Object.entries(object).map(([k,v]) => `${k}=${v}`).join('&'),
                params = {
                    method: $formSearch.method.toUpperCase(),
                    headers,
                    cache: 'no-cache',
                    redirect: 'follow',
                    referrerPolicy: 'no-referrer',
                    mode: "cors",
                    //body: data
                },
                url = window.location.origin.includes('rb-webstudio') ? $formSearch.action : `http://localhost/portfolio/public${$formSearch.getAttribute('action')}`
            console.log('>', url)
            if (params.method !== 'GET' && params.method !== 'HEAD') {
                params.body = data;
            }
            fetch(url, params).then(resp =>{
                if(resp.ok === true)
                    return resp.json()
            }).then(data =>{
                console.log('>', data)
            })
        })
    }
})
