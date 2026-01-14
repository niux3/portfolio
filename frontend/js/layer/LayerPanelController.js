import { strategyConfig } from "./layerStrategy"
import Utils from "../Utils"


export default class LayerPanelController {
    #buttons
    #layers
    #strategies = new Map()
    #currentStrategy = null

    constructor(nodeParent) {
        this.#buttons = nodeParent.querySelectorAll('button')
        this.#layers = document.querySelectorAll('.layer')
        this.#initializeStrategies()
    }

    init() {
        this.#setupButtonHandlers()
        this.#setupCloseHandlers()
        this.#setupKeyboardHandlers()
    }

    #setupButtonHandlers() {
        const eventType = Utils.isMobile() ? 'pointerdown' : 'click'

        this.#buttons.forEach($button => {
            $button.addEventListener(eventType, this.#handleButtonClick.bind(this))
        })
    }

    #handleButtonClick(e) {
        const $button = e.currentTarget

        if ($button.dataset.panel !== "true") return
        if ($button.classList.contains('current')) {
            this.#resetLayer()
            return
        }
        this.#openLayer($button)
    }

    #openLayer($button) {
        this.#resetLayer()

        const targetId = $button.dataset.panelTarget?.substring(1)
        const $targetLayer = document.getElementById(targetId)

        if (!$targetLayer) return

        this.#activateLayer($targetLayer, $button)
        this.#activateStrategy(targetId)

        if (targetId === 'search') {
            $targetLayer.querySelector("input[name='q']").focus()
        }
    }

    #activateLayer(layer, button) {
        layer.classList.add('move')
        button.classList.add('current')
        button.setAttribute('aria-expanded', true)
    }

    #activateStrategy(layerId) {
        const strategy = this.#strategies.get(layerId)
        if (strategy) {
            strategy.init()
            this.#currentStrategy = strategy
        }
    }

    #setupCloseHandlers() {
        const eventType = Utils.isMobile() ? 'pointerdown' : 'click'

        document.querySelectorAll('.layer .close').forEach($btn => {
            $btn.addEventListener(eventType, () => this.#resetLayer())
        })
    }

    #setupKeyboardHandlers() {
        window.addEventListener('keyup', (e) => {
            if (e.key === 'Escape') {
                this.#resetLayer()
            }
        })
    }

    #initializeStrategies() {
        let strategy = null
        if (this.#layers.length) {
            this.#layers.forEach(layer => {
                strategy = new strategyConfig[layer.id](layer)
                if (strategy) {
                    this.#strategies.set(layer.id, strategy)
                } else {
                    console.error(`No strategy defined for layer: ${layer.id}`)
                }
            })
        }
    }

    #resetLayer() {
        this.#buttons.forEach($btn => {
            $btn.classList.remove('current')
            $btn.setAttribute('aria-expanded', false)
        })
        this.#layers.forEach($layer => {
            $layer.classList.remove('move')
            if ($layer.id === 'search') {
                $layer.querySelector("input[name='q']").blur()
            }
        })
        // Nettoyer la stratégie courante si nécessaire
        // if (this.#currentStrategy && this.#currentStrategy.cleanup) {
        //     this.#currentStrategy.cleanup();
        // }
        // this.#currentStrategy = null;
    }
}