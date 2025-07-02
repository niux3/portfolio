export default class Subject{
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
