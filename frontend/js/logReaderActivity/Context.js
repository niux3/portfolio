export default class Context{
    #strategy

    setStrategy(strategy){
        this.#strategy = strategy
    }

    execute(data){
        this.#strategy?.execute(data)
    }
}
