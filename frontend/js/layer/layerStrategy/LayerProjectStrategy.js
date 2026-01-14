import LayerStrategy from './LayerStrategy'
import TemplateEngine from '../../TemplateEngine'


export default class LayerProjectStrategy extends LayerStrategy {
    #output

    constructor(layerElement) {
        super(layerElement)
        this.#output = this._layerElement.querySelector('output')
    }

    init() {
        console.log('layer Project')
    }
}