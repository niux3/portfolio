import Observer from './Observer'


export default class LateralBarObserver extends Observer{
    checkVisibility(data){
        let $header = document.querySelector('header'),
            height = $header.getBoundingClientRect().height,
            marginTop = parseInt(window.getComputedStyle($header).getPropertyValue('margin-top'), 10)
        return data > height + marginTop
    }
}
