import AbstractStrategy from "./AbstractStrategy"


export default class ArticleStrategy extends AbstractStrategy{
    logStart(path) {
        this.sendLog({ type: 'start', path })
    }

    logClick(id) {
        this.sendLog({ type: 'click', id })
    }

    logRead50(id) {
        this.sendLog({ type: 'read', id })
    }

    logEnd(path) {
        this.sendLog({ type: 'end', path })
    }
}
