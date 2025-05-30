import Data from './Data'
import View from './View'


export default class Manager{
    #data
    #view

    constructor(){
        this.$article = document.querySelector('article')

        this.#data = new Data(this.$article)
        this.#view = new View()
    }

    setProgression(value){
        let context = Math.floor(this.#data.getPercent(value))
        this.render(context)
    }

    render(value){
        this.#view.execute(value)
    }
}
