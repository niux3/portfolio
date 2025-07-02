import TemplateEngine from '../TemplateEngine'
import Subject from '../observer/Subject'
import NavLayerSummaryObserver from './NavLayerSummaryObserver'
import Utils from '../Utils'


export default class LayerSummary{
    #isArticleAvailable
    #articleEl
    #summaryLayerEl
    #subject

    constructor(){
        this.#isArticleAvailable = document.querySelector('article')
        if(this.#isArticleAvailable){
            this.#subject = new Subject()
            this.#articleEl = document.querySelector('article')
            this.#summaryLayerEl = document.getElementById('summary')
        }
    }

    init(){
        if(this.#isArticleAvailable && this.#summaryLayerEl){
            let $nav = this.#summaryLayerEl.querySelector('nav'),
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
            elements.forEach(el => new NavLayerSummaryObserver({el}, this.#subject))

            this.#subject.notify(window.scrollY)
            window.addEventListener('scroll', e =>{
                Utils.debounce(()=>{
                    this.#subject.notify(window.scrollY)
                }, 500)()
            })
        }
    }
}
