import Utils from '../Utils'
import Manager from './Manager'


export default class ProgressBarBehavior{
    static run(){
        if(document.querySelectorAll('article').length > 0){
            let manager = new Manager(),
                eventsType = ['resize', 'load']

            window.addEventListener('scroll', e =>{
                Utils.debounce(()=>{
                    manager.setProgression(window.scrollY)
                }, 200)()
            }, {passive:true})

            for(let ev of eventsType){
                window.addEventListener(ev, () =>{
                    Utils.debounce(()=>{
                        manager.setProgression(window.scrollY)
                    }, 200)()
                })
            }
        }
    }
}
