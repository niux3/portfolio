import AbstractLateralObserver from './AbstractLateralObserver'


export default class ShareObserver extends AbstractLateralObserver {
    checkVisibility(data) {
        if (document.querySelector('article .share')) {
            return document.querySelector('article .share').getBoundingClientRect().y < 0
        }
    }
}