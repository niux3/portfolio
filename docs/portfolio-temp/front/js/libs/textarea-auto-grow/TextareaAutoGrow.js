import Elements from './Elements';
import Utils from '../utils/Utils';


export default class TextareaAutoGrow{
    constructor(selector){
        this._$textareas = new Elements(selector);
        this._$currentElement = null;
        this._$textareas.$els.forEach($el => $el.addEventListener('focus', this._onFocus.bind(this)));
        this._$textareas.$els.forEach($el => $el.addEventListener('input', this._autoGrow.bind(this)));
    }

    _onFocus(e){
        this._$currentElement = e.target;
        this._autoGrow();
        window.addEventListener('resize', Utils.debounce(this._onResize.bind(this), 300));
        e.target.removeEventListener('focus', this.onFocus);
    }

    _onResize(e){
        this._autoGrow();
    }

    _autoGrow(){
        this._$currentElement.height = 'auto';
        let styles = [
            'overflow:hidden',
            `height:${this._$currentElement.scrollHeight}px`
        ];
        this._$currentElement.style = styles.join(';');
    }
}
