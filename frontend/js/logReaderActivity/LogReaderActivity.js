import Context from "./Context"
import ArticleStrategy from "./ArticleStrategy"


export default class LogReaderActivity{
    static execute(){
        let context = new Context()

        context.setStrategy(new ArticleStrategy())
        context.logStart('/articles/quelque-chose-123.html')
    }
}
