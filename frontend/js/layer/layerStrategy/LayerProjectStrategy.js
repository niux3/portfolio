import LayerStrategy from './LayerStrategy'
import TemplateEngine from '../../TemplateEngine'


export default class LayerProjectStrategy extends LayerStrategy {
    #output = null
    #data = null
    #engine = null

    constructor(layerElement) {
        super(layerElement)
        this.#engine = new TemplateEngine()
        this.#output = this._layerElement.querySelector('.content')
    }

    async init() {
        if (!this.#data) {
            this.#data = await this.#fetchData()
        }
        let projectId = parseInt(sessionStorage.getItem('project-id'), 10),
            row = this.#data.find(r => r.id === projectId)
        this.#output.innerHTML = this.#engine.render(document.getElementById('tplLayerProject').innerHTML, row)
    }

    async #fetchData() {
        try {
            let base_url = import.meta.env.DEV ? 'http://localhost:5173' : '',
                url = `${base_url}/public/static/data-projects.json`

            const response = await fetch(url)
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`)
            }
            const data = await response.json()
            return data
        } catch (e) {
            console.error('Failed to fetch project details:', e)
            return {}
        }

    }
}