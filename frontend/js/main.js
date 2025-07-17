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
        layerSearch = null,
        $main = document.querySelector('main'),
        duration = 3100,
        hasSeenAnimation = sessionStorage.getItem('introPlayed')

    const mount = ()=>{

        // darkmode
        darkmode()

        // lateralBar
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

            ProgressBarBehavior.run()
        }

        //logReader
        logReaderActivity = new LogReaderActivity()
        logReaderActivity.execute()

        // form contact
        formContact()


        const handleIntroAnimation = () =>{
            if(['/index.html', '/'].some(p => p === window.location.pathname) && !hasSeenAnimation){
                $main.classList.add('hidden')
                let $tplAnimLogo = document.getElementById('tplAnimLogo')
                $main.insertAdjacentHTML('beforebegin', $tplAnimLogo.innerHTML)

                let $animLogo = document.getElementById('anim-logo')
                $animLogo.classList.add('animate-progress')
                setTimeout(()=>{
                    $animLogo.remove()
                    sessionStorage.setItem('introPlayed', true)
                    $main.classList.remove('hidden')
                    document.getElementById('logo').classList.add('transition-fade')
                }, duration)
            }else{
                $main.classList.remove('hidden')
            }
        }

        handleIntroAnimation()
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
        //hooks: {
            //'visit:end': (...args) => {
                //mount()
            //},
            //'animation:out:await': (visit, args) =>{
                //if(['/index.html', '/'].some(p => p === window.location.pathname) && !hasSeenAnimation){
                    //alert('ok')
                    //return new Promise(resolve => {
                        //setTimeout(() => {
                            //resolve()
                        //}, duration)
                    //})
                //}
            //},
            //'content:replace': () =>{
                //$main.classList.remove('hidden')
            //},
            //'animation:in:start': () =>{
            //},
            //'page:view': (...args) => {
                //unmount()
            //}
        //},
        plugins: [
            new SwupA11yPlugin(),
        ],
        animateHistoryBrowsing: true,
    })
    swup.hooks.on('visit:start', () => {
        alert('1. Swup: visit:start - Un clic a été détecté et Swup commence une nouvelle visite.')
        console.log('visit:start - from:', swup.currentPageUrl, 'to:', swup.currentVisit.to.url)
        unmount()
    })

    swup.hooks.on('page:load', () => {
        alert('2. Swup: page:load - La page actuelle est sur le point d\'être déchargée (avant l\'animation de sortie).')
        let hasSeenAnimation = sessionStorage.getItem('introPlayed')
        if(['/index.html', '/'].some(p => p === window.location.pathname) && !hasSeenAnimation){
            return new Promise(resolve => {
                setTimeout(() => {
                    alert('ok')
                    console.log('>> ', hasSeenAnimation)
                    resolve()
                }, 3100)
            })
        }
    })

    swup.hooks.on('animation:out:start', () => {
        alert('3. Swup: animation:out:start - L\'animation de sortie du contenu commence.')
    })

    swup.hooks.on('animation:in:await', (visit, args) =>{
        alert('4. Swup: animation:out:await - Le hook d\'attente de l\'animation de sortie est déclenché.')
    })

    swup.hooks.on('content:replace', (visit, args) =>{
        alert('5. Swup: content:replace - Le nouveau contenu a été injecté dans le DOM.')
        document.querySelector('main').classList.remove('hidden')
    })

    swup.hooks.on('page:view', () => {
        alert('6. Swup: page:view - La nouvelle page est entièrement chargée et prête.')
    })
    swup.hooks.on('visit:end', () => {
        alert('7. Swup: page:view - La nouvelle page est entièrement chargée et prête.')
        mount()
    })
})
