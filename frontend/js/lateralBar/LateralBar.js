import ScrollNotifier from "./ScrollNotifier"
import LayerPanelController from "./LayerPanelController"


export default class LateralBar{
    #lateralBar
    #buttons
    #main
    constructor(){
        if(document.getElementById('lateralBar')){
            this.#lateralBar = document.getElementById('lateralBar')
            this.#buttons = this.#lateralBar.querySelectorAll('button')
            this.#main = document.querySelector('main')

            new ScrollNotifier(this.#lateralBar).init()
            new LayerPanelController(this.#lateralBar).init()
        }
    }

    display(){
        if(window.matchMedia('( min-width: 961px )').matches){
            let widthMain = this.#main.getBoundingClientRect().width,
                widthWindow = window.innerWidth


            this.#lateralBar.classList.remove('visible')
            this.#lateralBar.style.right = `${( (widthWindow - widthMain) / 2 ) - 40}px`
            this.#lateralBar.addEventListener('transitionend', e => {
                setTimeout(()=>{
                    this.#lateralBar.classList.add('visible')
                }, 500)
            })
        }else if(window.matchMedia('(max-width: 960px)').matches){
            this.#lateralBar.classList.add('visible')
        }
    }
}
