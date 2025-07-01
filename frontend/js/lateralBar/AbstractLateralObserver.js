import AbstractObserver from '../Observer/AbstractObserver'


export default class AbstractLateralBarObserver extends AbstractObserver{
    #isVisible

    constructor(properties){
        super(properties)
        this.#isVisible = false
    }

    checkVisibility(data) {
        throw new Error("Method 'checkVisibility' must be implemented")
    }

    update(data){
        this.#isVisible = this.checkVisibility(data)
        this.$el.setAttribute('aria-hidden', this.#isVisible)
        this.$el.classList[this.#isVisible? 'add' : 'remove']('displayObserve')
    }
}
