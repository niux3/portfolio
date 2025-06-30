import '../scss/index.scss'
import ProgressBarBehavior from './progressBar/ProgressBarBehavior'
import darkmode from './darkmode'
import formContact from './formContact'
import LogReaderActivity from './logReaderActivity/LogReaderActivity'
import Utils from './Utils'


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

    class Subject{
        #observers

        constructor(){
            this.#observers = []
        }

        add(o){
            this.#observers.push(o)
        }

        notify(data){
            for(let o of this.#observers){
                o.update(data)
            }
        }
    }

    class Observer{
        #isVisible

        constructor($el){
            this._el = $el
            this.#isVisible = false
        }

        get $el(){
            return this._el
        }

        checkVisibility(data) {
            throw new Error("Method 'checkVisibility' must be implemented")
        }

        update(data){
            this.#isVisible = this.checkVisibility(data)
            this._el.setAttribute('aria-hidden', this.#isVisible)
            this._el.classList[this.#isVisible? 'add' : 'remove']('visible')
        }
    }

    class GoToTopObserver extends Observer{
        checkVisibility(data){
            return data > window.innerHeight
        }
    }

    class ShareObserver extends Observer{
        checkVisibility(data){
            return document.querySelector('article .share').getBoundingClientRect().y < 0
        }
    }

    if(document.getElementById('lateralBar')){
        let $lateralBar = document.getElementById('lateralBar'),
            $buttons = document.querySelectorAll('#lateralBar button'),
            $main = document.body.querySelector('main'),
            heightWindow = window.innerHeight,
            placementLateralBar = ()=>{
                if(window.matchMedia('( min-width: 961px )').matches){
                    let widthMain = $main.getBoundingClientRect().width,
                        widthWindow = window.innerWidth
                    $lateralBar.classList.remove('visible')
                    $lateralBar.style.right = `${( (widthWindow - widthMain) / 2 ) - 40}px`
                    $lateralBar.addEventListener('transitionend', e => {
                        setTimeout(()=>{
                            $lateralBar.classList.add('visible')
                        }, 1200)
                    })
                }else if(window.matchMedia('(max-width: 960px)').matches){
                    $lateralBar.classList.add('visible')
                }
            }

            placementLateralBar()
            window.addEventListener('resize', e =>{
                Utils.debounce(placementLateralBar, 50)()
            })
        let subject = new Subject(),
            goToTop = new GoToTopObserver(document.querySelector('#lateralBar a[href="#top"]')),
            shareLateralBar = new ShareObserver(document.querySelector('#lateralBar .share'))
        subject.add(goToTop)
        subject.add(shareLateralBar)

        Utils.debounce(()=>{
            subject.notify(window.scrollY)
        }, 400)()
        window.addEventListener('scroll', e =>{
            Utils.debounce(()=>{
                subject.notify(window.scrollY)
            }, 400)()

        })


        let $layers = document.querySelectorAll('.layer')
        const resetLayer = () =>{
            $buttons.forEach($btn => $btn.classList.remove('current'))
            $layers.forEach($layer => $layer.classList.remove('move'))
        }
        $buttons.forEach($button =>{
            $button.addEventListener('pointerdown', e =>{
                if($button.dataset.panel === "true"){
                    if($button.classList.contains('current')){
                        resetLayer()
                        return;
                    }
                    resetLayer()
                    let [$currentLayer, ...$othersLayers] = Array.from($layers).filter($l => $l.id === $button.dataset.panelTarget.substr(1))
                    $currentLayer.classList.add('move')
                    $button.classList.add('current')
                }
            })
        })
        document.querySelectorAll('.layer .close').forEach($btn =>{
            $btn.addEventListener('pointerdown', e => {
                resetLayer()
            })
        })
    }

})
