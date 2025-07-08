import '../scss/index.scss'
import ProgressBarBehavior from './progressBar/ProgressBarBehavior'
import darkmode from './darkmode'
import formContact from './formContact'
import LogReaderActivity from './logReaderActivity/LogReaderActivity'
import Utils from './Utils'
import LateralBar from './lateralBar/LateralBar'
import LayerSummary from './layerSummary/LayerSummary'
import TemplateEngine from './TemplateEngine'
import Swup from 'swup'
import SwupA11yPlugin from '@swup/a11y-plugin'


window.addEventListener('DOMContentLoaded', () =>{
    let logReaderActivity = null,
        lateralBar = null,
        layerSummary = null

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
        }


        layerSummary = new LayerSummary()
        layerSummary.init()

        if(document.getElementById('search')){
            let $search = document.getElementById('search'),
                $formSearch = $search.querySelector('form'),
                $resultSearch = $search.querySelector('#resultSearch'),
                $output = $search.querySelector('output')

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

                let data = Object.entries(object).map(([k,v]) => `${encodeURIComponent(k)}=${encodeURIComponent(v)}`).join('&'),
                    params = {
                        method: $formSearch.method.toUpperCase(),
                        headers,
                        cache: 'no-cache',
                        redirect: 'follow',
                        referrerPolicy: 'no-referrer',
                        mode: "cors",
                    },
                    url = window.location.origin.includes('rb-webstudio') ? $formSearch.action : `http://localhost/portfolio/public${$formSearch.getAttribute('action')}`
                fetch(`${url}?${data}`, params).then(resp =>{
                    if(resp.ok === true)
                        return resp.json()
                }).then(({ data }) =>{
                    let templateEngine = new TemplateEngine(),
                        tpl = document.getElementById('tplLayer'),
                        lenResult = Object.keys(data).length,
                        rows = []
                    $output.innerHTML = `<strong>${lenResult}</strong> résultat${lenResult > 1? 's': ''} trouvé${lenResult > 1? 's': ''}`

                    if(lenResult > 0){
                        let reference = 250,
                            $nav = document.createElement('nav')

                        for(let v of Object.values(data)){
                            rows.push({
                                url: `/articles/${v.slug}-${v.id}.html`,
                                text: v.title
                            })
                        }

                        $nav.style.height = `${window.innerHeight - reference}px`
                        window.addEventListener('resize', e =>{
                            Utils.debounce(()=>{
                                $nav.style.height = `${window.innerHeight - reference}px`
                            }, 200)()

                        })
                        $nav.innerHTML = templateEngine.render(tpl.textContent, {rows})
                        $resultSearch.innerHTML = $nav.outerHTML
                    }
                })
            })
        }
    }
    const unmount = ()=>{
        logReaderActivity = null
        lateralBar = null
        layerSummary = null
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
    })
})
