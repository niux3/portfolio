export default class LayerPanelController{
    #buttons
    #layers

    constructor(lateralBar){
        this.#buttons = lateralBar.querySelectorAll('button')
        this.#layers = document.querySelectorAll('.layer')
    }

    #resetLayer() {
        this.#buttons.forEach($btn => $btn.classList.remove('current'))
        this.#layers.forEach($layer => $layer.classList.remove('move'))
    }

    init() {
        this.#buttons.forEach($button => {
            $button.addEventListener('pointerdown', e => {
                if ($button.dataset.panel === "true") {
                    if ($button.classList.contains('current')) {
                        this.#resetLayer()
                        return
                    }
                    this.#resetLayer()
                    let targetId = $button.dataset.panelTarget?.substring(1)
                    let $targetLayer = Array.from(this.#layers).find($l => $l.id === targetId)
                    if ($targetLayer) $targetLayer.classList.add('move')
                    $button.classList.add('current')
                }
            })
        })

        document.querySelectorAll('.layer .close').forEach($btn => {
            $btn.addEventListener('pointerdown', e => {
                this.#resetLayer()
            })
        })
    }
}
