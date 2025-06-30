import Observer from './Observer'


export default class ShareObserver extends Observer{
    checkVisibility(data){
        return document.querySelector('article .share').getBoundingClientRect().y < 0
    }
}
