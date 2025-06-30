export default class Observer{
    #isVisible

    constructor($el){
        this._el = $el
        this.#isVisible = false
    }

    get $el(){
        return this._el
    }

    checkVisibility(data) {
        throw new Error("Method 'checkVisibility' must be implemented")
    }

    update(data){
        this.#isVisible = this.checkVisibility(data)
        this._el.setAttribute('aria-hidden', this.#isVisible)
        this._el.classList[this.#isVisible? 'add' : 'remove']('visible')
    }
}
