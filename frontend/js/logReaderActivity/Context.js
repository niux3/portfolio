export default class Context{
    #strategy

    setStrategy(strategy){
        this.#strategy = strategy
    }

    logStart(path) {
        this.#strategy?.logStart(path)
    }

    logClick(id) {
        this.#strategy?.logClick(id)
    }

    logRead50(id) {
        this.#strategy?.logEnd(id)
    }

    logEnd(path) {
        this.#strategy?.logEnd(path)
    }
}
