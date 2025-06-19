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

    class Observer{
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

    class Element{
        #el

        constructor($el){
            this.#el = $el
        }

        get $el(){
            return this.#el
        }

        update(data){
            let isVisible = data > window.innerHeight
            this.#el.setAttribute('aria-hidden', isVisible? 'true': 'false')
            this.#el.classList[isVisible? 'add' : 'remove']('visible')
        }
    }

    if(document.getElementById('lateralBar')){
        let $lateralBar = document.getElementById('lateralBar'),
            $buttons = document.querySelectorAll('#lateralBar button'),
            $main = document.body.querySelector('main'),
            heightWindow = window.innerHeight,
            placementLateralBar = ()=>{
                if(window.matchMedia('( min-width: 961px )').matches){
                    console.log('matches')
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
        let obserser = new Observer(),
            goToTop = new Element(document.querySelector('#lateralBar a[href="#top"]'))
        obserser.add(goToTop)
        Utils.debounce(()=>{
            obserser.notify(window.scrollY)
        }, 400)()
        window.addEventListener('scroll', e =>{
            Utils.debounce(()=>{
                obserser.notify(window.scrollY)
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
