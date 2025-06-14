import AbstractStrategy from "./AbstractStrategy"


export default class ArticleStrategy extends AbstractStrategy{
    _logStart(path) {
        this._sendLog({ type: 'start', path })
    }

    _logClick(path) {
        this._sendLog({ type: 'click', path })
    }

    _logRead(path) {
        this._sendLog({ type: 'read', path })
    }

    _logEnd(path) {
        this._sendLog({ type: 'end', path })
    }

    execute(path){
        console.log("execute ArticleStrategy")
    }
}
