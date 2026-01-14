import LayerStrategy from './LayerStrategy'
import TemplateEngine from '../../TemplateEngine'
import Subject from '../../observer/Subject'
import NavLayerSummaryObserver from './NavLayerSummaryObserver'
import Utils from '../../Utils'


export default class LayerSummaryStrategy extends LayerStrategy {
    #isArticleAvailable
    #articleEl
    #subject

    constructor(layerElement) {
        super(layerElement)
        this.#isArticleAvailable = document.querySelector('article')
        if (this.#isArticleAvailable) {
            this.#subject = new Subject()
            this.#articleEl = document.querySelector('article')
        }
    }

    init() {
        if (this.#isArticleAvailable && this._layerElement) {
            let $nav = this._layerElement.querySelector('nav'),
                reference = 130,
                numbers = [...Array(6).keys()],
                titles = numbers.map(x => `article h${x + 1}`),
                selectors = [...titles, '[id^=exempl]'],
                elements = document.querySelectorAll(selectors.join(', ')),
                tpl = document.getElementById('tplLayer'),
                templateEngine = new TemplateEngine(),
                elementsOutput = []

            elements.forEach((el, i) => {
                let text,
                    url

                if (el.id.startsWith('exemple-')) {
                    text = el.parentNode.textContent
                } else {
                    el.setAttribute('id', `_${i}-${Utils.slugify(el.textContent)}`)
                    text = el.textContent
                }
                url = `#${el.id}`

                elementsOutput.push({
                    url,
                    text
                })
            })

            $nav.style.height = `${window.innerHeight - reference}px`
            window.addEventListener('resize', e => {
                Utils.debounce(() => {
                    $nav.style.height = `${window.innerHeight - reference}px`
                }, 200)()
            })

            $nav.insertAdjacentHTML('beforeend', templateEngine.render(tpl.textContent, { 'rows': elementsOutput }))
            $nav.addEventListener('click', e => {
                if (window.matchMedia("(max-width: 420px)").matches) {
                    if (e.target.nodeName == 'A') {
                        const btn = $nav.closest('.wrap').querySelector('.close');
                        if (btn) {
                            btn.dispatchEvent(new Event('click', { bubbles: true }));
                        }
                    }
                }
            })
            elements.forEach(el => new NavLayerSummaryObserver({ el }, this.#subject))

            this.#subject.notify(window.scrollY)
            window.addEventListener('scroll', e => {
                Utils.debounce(() => {
                    this.#subject.notify(window.scrollY)
                }, 500)()
            })
        }
    }
}