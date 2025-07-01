import AbstractLateralObserver from './AbstractLateralObserver'


export default class ShareObserver extends AbstractLateralObserver{
    checkVisibility(data){
        return document.querySelector('article .share').getBoundingClientRect().y < 0
    }
}
