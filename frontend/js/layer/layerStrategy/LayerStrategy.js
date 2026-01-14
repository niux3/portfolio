export default class LayerStrategy {
    _layerElement

    constructor(layerElement) {
        this._layerElement = layerElement
    }

    init() {
        throw new Error('Method "init" must be implemented')
    }

    cleanup() {
        throw new Error('Method "cleanup" must be implemented')
    }
}