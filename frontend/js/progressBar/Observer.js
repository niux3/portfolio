export default class Observer{
    #observers = []
    constructor(){
    }

    get observers(){
        return this.#observers
    }

    add(observer){
        this.#observers = [...this.#observers, observer]
    }

    notify(callback=null){
        for(let i = 0; i < this.#observers.length; i++){
            this.#observers[i].update(callback)
        }
    }
}
