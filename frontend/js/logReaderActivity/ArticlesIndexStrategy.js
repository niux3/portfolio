import AbstractStrategy from "./AbstractStrategy"


export default class ArticlesIndexStrategy extends AbstractStrategy{
    _logClick(path) {
        document.querySelectorAll('.posts .items-articles li a').forEach($a =>{
            $a.addEventListener('pointerdown', e =>{
                let data = {
                    'url': $a.getAttribute('href'),
                    'text': $a.textContent
                }
                this._sendLog({ type: 'click', path, ...data })
            })
        })
    }

    execute(path){
        this._logStart(path)
        //this._logClick(path)
        //this._logEnd(path)
    }
}
