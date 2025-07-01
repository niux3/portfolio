import AbstractLateralBarObserver from "./AbstractLateralObserver"


export default class GoToTopObserver extends AbstractLateralBarObserver{
    checkVisibility(data){
        return data > window.innerHeight
    }
}
