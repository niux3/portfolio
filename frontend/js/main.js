import '../scss/index.scss'
import ProgressBarBehavior from './progressBar/ProgressBarBehavior'
import darkmode from './darkmode'
import formContact from './formContact'
import LogReaderActivity from './logReaderActivity/LogReaderActivity'
import Utils from './Utils'
import LateralBar from './lateralBar/LateralBar'
import TemplateEngine from './TemplateEngine'
import AbstractObserver from './Observer/AbstractObserver'
import Subject from './Observer/Subject'


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

    class NavLayerSummaryObserver extends AbstractObserver{
        #linkNav
        #subject

        constructor(props, subject){
            super(props)
            let selector = `#summary nav a[href="#${this.$el.id}"]`
            this.#linkNav = document.querySelector(selector)
            this.#subject = subject
            subject.add(this)
        }

        update(data){
            let halfHeightWindow = Math.round(window.innerHeight / 3)
            if(this.$el.getBoundingClientRect().y - halfHeightWindow < 0){
                this.#linkNav.parentNode.classList.add('active')
                this.#linkNav.parentNode.scrollIntoView({
                    behavior: 'smooth',
                    block: 'center'
                })
            }else{
                this.#linkNav.parentNode.classList.remove('active')
            }
            this.#desactiveBefore()
        }

        #desactiveBefore(){
            let $navLinks = Array.from(document.querySelectorAll('#summary nav a')),
                index = $navLinks.findLastIndex($el => $el.parentNode.classList.contains('active'))
            if(index > 0){
                $navLinks.slice(0, index).map(e => e.parentNode.classList.remove('active'))
            }
        }
    }

    if(document.querySelector('article')){
        let $article = document.querySelector('article'),
            $summaryLayer = document.getElementById('summary')
        let subject = new Subject()

        if($summaryLayer){
            let $nav = $summaryLayer.querySelector('nav'),
                reference = 130,
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
                    el,
                    url,
                    text
                })
            })
            $nav.style.height = `${window.innerHeight - reference}px`
            window.addEventListener('resize', e =>{
                Utils.debounce(()=>{
                    $nav.style.height = `${window.innerHeight - reference}px`
                }, 200)()

            })
            $nav.insertAdjacentHTML('beforeend', templateEngine.render(tpl.textContent, {'rows': elementsOutput}))
            elements.forEach(el => { new NavLayerSummaryObserver({el}, subject) })

            subject.notify(window.scrollY)
            window.addEventListener('scroll', e =>{
                Utils.debounce(()=>{
                    subject.notify(window.scrollY)
                }, 500)()
            })
        }
    }
})
