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

        //// darkmode
        darkmode()

        ////logReader
        logReaderActivity = new LogReaderActivity()
        logReaderActivity.execute()

        //// form contact
        formContact()


        let $main = document.querySelector('main'),
            hasSeenAnimation = sessionStorage.getItem('introPlayed'),
            $html = document.querySelector('html')

        const playSwupLikeTransition = () => {
            $html.classList.add('is-changing', 'is-animating', 'is-leaving')

            // Force un reflow pour déclencher les transitions
            requestAnimationFrame(() => {
                $html.classList.remove('is-leaving')
                $html.classList.add('is-rendering')
                //void $html.offsetWidth
                // Reflow encore une fois pour bien préparer la transition
                requestAnimationFrame(() => {
                    $html.classList.remove('is-rendering', 'is-animating')
                    //void $html.offsetWidth

                    setTimeout(() => {
                        $html.classList.remove('is-changing')
                    }, 200)
                })
            })
        }

        if(['/index.html', '/'].some(p => p === window.location.pathname) && !hasSeenAnimation){
            hasSeenAnimation = sessionStorage.setItem('introPlayed', true)
            let $tplAnimLogo = document.getElementById('tplAnimLogo')
            $main.insertAdjacentHTML('beforebegin', $tplAnimLogo.innerHTML)

            let $animLogo = document.getElementById('anim-logo')
            $animLogo.classList.add('animate-progress')
            setTimeout(()=>{
                $animLogo.remove()
                $main.classList.remove('hide')
                playSwupLikeTransition()
            }, 3100)
        }else{
            $main.classList.remove('hide')
            playSwupLikeTransition()

            // progressBar
            ProgressBarBehavior.run()
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
