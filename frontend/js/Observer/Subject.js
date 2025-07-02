export default class Subject{
    constructor(){
        this._observers = []
    }

    add(o){
        this._observers.push(o)
    }

    notify(data){
        for(let o of this._observers){
            o.update(data)
        }
    }

    get observers(){
        return this._observers
    }
}
