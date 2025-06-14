import Context from "./Context"
import ArticleStrategy from "./ArticleStrategy"
import HomeStrategy from "./HomeStrategy"


export default class LogReaderActivity{
    #path
    #strategiesUrls

    constructor(){
        this.#path = window.location.pathname
        this.#strategiesUrls = {
            '^\\/articles\\/[a-zA-Z0-9\\-]+-\\d+\\.html$': ArticleStrategy,
            //'^\\/articles\\/index\\.html$': ArticlesIndexStrategy,
            //'^\\/chercher-articles-par-[a-zA-Z0-9\\-]+\\.html$': TagsIndexStrategy,
            '^\\/$|^\\/index\\.html$': HomeStrategy,
        }
    }

    execute(){
        let context = new Context(),
            strategy = this.#resolveStrategy(this.#path)
        if(strategy !== null){
            context.setStrategy(new strategy())
            context.execute(this.#path)
        }else{
            console.warn('No strategy found for path:', this.#path)
        }
    }

    #resolveStrategy(path){
        let ref = null
        for(let [strPattern, RefObjectStrategy] of Object.entries(this.#strategiesUrls)){
            const regex = new RegExp(strPattern)
            if (regex.test(path)) {
                ref = RefObjectStrategy
            }
        }
        return ref
    }
}
