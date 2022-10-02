import {display} from "./store";


export let toVisible = () =>{
    // document.getElementById('overlayTransition').classList.add('visible');
    // setTimeout(()=>{
    //     display.set(false);
    // }, 100)
    setTimeout(()=>{
        document.querySelector('body').classList.remove('invisible');
    }, 400)
}


export let toInvisible = () =>{
    document.querySelector('body').classList.add('invisible');
    let end = setTimeout(()=>{

    }, 400)
    // let end = setTimeout(()=>{
    //     document.getElementById('overlayTransition').classList.add('invisible');
    //     let destroy = setTimeout(()=>{
    //         display.set(true);
    //         document.querySelector('main').classList.remove('invisible');
    //         document.getElementById('overlayTransition').classList.remove('visible', 'invisible');
    //         clearTimeout(end)
    //         clearTimeout(destroy);
    //     }, 400)
    // }, 800)
}
