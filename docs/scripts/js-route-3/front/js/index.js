import '../scss/index.scss';
import Dispatcher from './libs/dispatcher/Dispatcher';


(()=>{
    let dispatcher = new Dispatcher()
    dispatcher.run();
    if(window.location.hash === ""){
        dispatcher.navigateTo('/about')
    }
})()
