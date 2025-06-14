import AbstractStrategy from "./AbstractStrategy"


export default class HomeStrategy extends AbstractStrategy{
    _logStart(path) {
        this._sendLog({ type: 'start', path })
    }

    _logClick(path) {
        document.querySelectorAll('.work a').forEach($a =>{
            $a.addEventListener('pointerdown', e =>{
                let data = {
                    'url': $a.getAttribute('href'),
                    'text': $a.querySelector('.bold').textContent
                }
                this._sendLog({ type: 'click', path, data })
            })
        })
    }

    _logRead(path) {
        console.warn('this view does not use sendlog method (logRead)')
    }

    _logEnd(path) {
        console.warn('this view does not use sendlog method (logEnd)')
    }

    execute(path){
        this._logStart(path)
        this._logClick(path)
    }
}
