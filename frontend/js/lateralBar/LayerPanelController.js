import Utils from "../Utils"


export default class LayerPanelController{
    #buttons
    #layers

    constructor(lateralBar){
        this.#buttons = lateralBar.querySelectorAll('button')
        this.#layers = document.querySelectorAll('.layer')
    }

    #resetLayer() {
        this.#buttons.forEach($btn => {
            $btn.classList.remove('current')
            $btn.setAttribute('aria-expanded', false)
        })
        this.#layers.forEach($layer => {
            $layer.classList.remove('move')
            if($layer.id === 'search'){
                $layer.querySelector("input[name='q']").blur()
            }
        })
    }

    init() {
        let event = Utils.isMobile()? 'pointerdown' : 'click'
        this.#buttons.forEach($button => {
            $button.addEventListener(event, e => {
                if ($button.dataset.panel === "true") {
                    if ($button.classList.contains('current')) {
                        this.#resetLayer()
                        return
                    }
                    this.#resetLayer()
                    let targetId = $button.dataset.panelTarget?.substring(1)
                    let $targetLayer = Array.from(this.#layers).find($l => $l.id === targetId)
                    console.log($targetLayer)
                    if ($targetLayer){
                        if($targetLayer.id === 'search'){
                            $targetLayer.querySelector("input[name='q']").focus()
                        }
                        $targetLayer.classList.add('move')
                    }
                    $button.classList.add('current')
                    $button.setAttribute('aria-expanded', true)
                }
            })
        })

        document.querySelectorAll('.layer .close').forEach($btn => {
            $btn.addEventListener(event, e => {
                this.#resetLayer()
            })
        })

        window.addEventListener('keyup', e =>{
            if(e.key === 'Escape'){
                this.#resetLayer()
            }
        })
    }
}
