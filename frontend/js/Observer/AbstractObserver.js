export default class AbstractObserver{
    #properties

    constructor(properties){
        this.#properties = properties
    }

    get $el(){
        return this.#properties.el
    }

    update(data){
        throw new Error("Method 'update' must be implemented")
    }
}
