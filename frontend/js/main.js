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
            //console.log(this.$el)
            //console.log(document.querySelector('article .share').getBoundingClientRect())
            return document.querySelector('article .share').getBoundingClientRect().y < 0
            //return data > window.innerHeight
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
                    $lateralBar.addEventListener('transitionend', e => $lateralBar.classList.add('visible'))
                }else if(window.matchMedia('(max-width: 960px)').matches){
                    $lateralBar.classList.add('visible')
                }
            }

            placementLateralBar()
            window.addEventListener('resize', e =>{
                console.log('resize')
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


        $buttons.forEach($button =>{
            $button.addEventListener('pointerdown', e =>{
                console.log($button.dataset.panel)
                if($button.dataset.panel === "true"){
                    $buttons.forEach($btn => $btn.classList.remove('current'))
                    $button.classList.add('current')

                    //$main.classList.add('move')
                    //$lateralBar.classList.add('move')
                }
            })
        })
    }

})
