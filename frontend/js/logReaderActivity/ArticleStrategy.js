import AbstractStrategy from "./AbstractStrategy"
import Utils from '../Utils'


export default class ArticleStrategy extends AbstractStrategy{
    _logRead(path) {
        let $progress = document.querySelector('progress'),
            isAlreadyRead = false
        window.addEventListener('scroll', e =>{
            Utils.debounce(()=>{
                if($progress.value >= 50 && !isAlreadyRead){
                    this._sendLog({ type: 'read', path })
                    isAlreadyRead = true
                }
            }, 200)()
        })
    }

    execute(path){
        this._logStart(path)
        this._logRead(path)
        //this._logEnd(path)
    }
}
