import Observer from './Observer'


export default class GoToTopObserver extends Observer{
    checkVisibility(data){
        return data > window.innerHeight
    }
}
