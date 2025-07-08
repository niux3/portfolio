import '../scss/index.scss'
import ProgressBarBehavior from './progressBar/ProgressBarBehavior'
import darkmode from './darkmode'
import formContact from './formContact'
import LogReaderActivity from './logReaderActivity/LogReaderActivity'
import Utils from './Utils'
import LateralBar from './lateralBar/LateralBar'
import LayerSummary from './layerSummary/LayerSummary'
import LayerSearch from './layerSearch/LayerSearch'
import Swup from 'swup'
import SwupA11yPlugin from '@swup/a11y-plugin'


window.addEventListener('DOMContentLoaded', () =>{
    let logReaderActivity = null,
        lateralBar = null,
        layerSummary = null,
        layerSearch = null

    const mount = ()=>{
        // progressBar
        ProgressBarBehavior.run()

        //// darkmode
        darkmode()

        ////logReader
        logReaderActivity = new LogReaderActivity()
        logReaderActivity.execute()

        //// form contact
        formContact()

        //// lateralBar
        if(document.getElementById('lateralBar')){
            lateralBar = new LateralBar()
            lateralBar.display()
            window.addEventListener('resize', e =>{
                Utils.debounce(lateralBar.display(), 50)()
            })

            layerSummary = new LayerSummary()
            layerSummary.init()

            layerSearch = new LayerSearch()
            layerSearch.init()
        }
    }
    const unmount = ()=>{
        logReaderActivity = null
        lateralBar = null
        layerSummary = null
        layerSearch = null
    }
    mount()
    const swup = new Swup({
        containers: ['#viewsTransition'],
        hooks: {
            'visit:end': (...args) => {
                mount()
            },
            'animation:out:start': () =>{
            },
            'animation:in:start': () =>{
            },
            'page:view': (...args) => {
                unmount()
            }
        },
        plugins: [
            new SwupA11yPlugin(),
        ],
        animateHistoryBrowsing: true,
    })
})
