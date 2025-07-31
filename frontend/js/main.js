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
import DarkMode from './darkmode'


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
        let darkmode = new DarkMode()
        darkmode.init()

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
                    // console.log(document.querySelector('html'))
                    document.querySelector('html').classList.add('animate-home')
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
        plugins: [
            new SwupA11yPlugin(),
        ],
        animateHistoryBrowsing: true,
    })
    swup.hooks.on('visit:start', () => {
        // console.log('1. Swup: visit:start - Un clic a été détecté et Swup commence une nouvelle visite.')
        //console.log('visit:start - from:', swup.currentPageUrl, 'to:', swup.currentVisit.to.url)
        document.querySelector('html').classList.remove('animate-home')
        unmount()
    })
    swup.hooks.on('link:click', () => {
        document.querySelector('html').classList.remove('animate-home')
    })

    swup.hooks.on('page:load', () => {
        // console.log('2. Swup: page:load - La page actuelle est sur le point d\'être déchargée (avant l\'animation de sortie).')
        //let hasSeenAnimation = sessionStorage.getItem('introPlayed')
        //if(['/index.html', '/'].some(p => p === window.location.pathname) && !hasSeenAnimation){
            //return new Promise(resolve => {
                //setTimeout(() => {
                    //console.log('>> ', hasSeenAnimation)
                    //resolve()
                //}, 3100)
            //})
        //}
    })

    swup.hooks.on('animation:out:start', () => {
        // console.log('3. Swup: animation:out:start - L\'animation de sortie du contenu commence.')
        document.querySelector('html').classList.remove('animate-home')
    })

    swup.hooks.on('animation:in:await', (visit, args) =>{
        // console.log('4. Swup: animation:out:await - Le hook d\'attente de l\'animation de sortie est déclenché.')
    })

    swup.hooks.on('animation:in:start', (visit, args) =>{
        const elements = document.querySelectorAll('[class*=delay]');
        // console.log('>>', elements)
        elements.forEach(el => {
            //el.classList.remove('animate-in'); // reset si besoin
            void el.offsetWidth; // force reflow
            //el.classList.add('animate-in');

        });
    })

    swup.hooks.on('content:replace', (visit, args) =>{
        // console.log('5. Swup: content:replace - Le nouveau contenu a été injecté dans le DOM.')
        document.querySelector('main').classList.remove('hidden')
    })

    swup.hooks.on('page:view', () => {
        // console.log('6. Swup: page:view - La nouvelle page est entièrement chargée et prête.')
    })
    swup.hooks.on('visit:end', () => {
        // console.log('7. Swup: page:view - La nouvelle page est entièrement chargée et prête.')
        mount()
    })
})
