import '../scss/index.scss'
import ProgressBarBehavior from './progressBar/ProgressBarBehavior'
import darkmode from './darkmode'
import formContact from './formContact'
import LogReaderActivity from './logReaderActivity/LogReaderActivity'
import Utils from './Utils'
import LateralBar from './lateralBar/LateralBar'
import TemplateEngine from './TemplateEngine'


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

    if(document.querySelector('article')){
        let $article = document.querySelector('article'),
            $summaryLayer = document.getElementById('summary')
        if($summaryLayer){
            let $nav = $summaryLayer.querySelector('nav'),
                numbers = [...Array(6).keys()],
                titles = numbers.map(x => `article h${x + 1}`),
                selectors = [...titles, '[id^=exempl]'],
                elements = document.querySelectorAll(selectors.join(', ')),
                tpl = document.getElementById('tplSummary'),
                templateEngine = new TemplateEngine(),
                elementsOutput = []

            elements.forEach((el, i) => {
                let url, text
                if(el.id.startsWith('exemple-')){
                    text = el.parentNode.textContent
                    url = el.id
                }else{
                    el.setAttribute('id', `_${i}-${Utils.slugify(el.textContent)}`)
                    url = el.id
                    text = el.textContent
                }
                elementsOutput.push({
                    url,
                    text
                })
            })
            $nav.style.height = `${window.innerHeight - 130}px`
            $nav.insertAdjacentHTML('beforeend', templateEngine.render(tpl.textContent, {'rows': elementsOutput}))
        }
    }
})
