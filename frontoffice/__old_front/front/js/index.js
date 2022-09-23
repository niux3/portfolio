import '../scss/index.scss';
import Dispatcher from './libs/dispatcher/Dispatcher';


(()=>{
    document.querySelector('section').style.height = '2000px';

    let get_properties_window = ()=>{
        return {
            w : window.innerWidth,
            h : window.innerHeight
        };
    }
    let set_resize_header = ()=>{
        let props_window = get_properties_window(),
            $header = document.querySelector('header'),
            style = [
                `height:${props_window.h}px`,
            ];
            $header.style = style.join(';');

    }
    set_resize_header();
    window.addEventListener('resize', set_resize_header);

    let animNavTop = setTimeout(()=>{
        let $nav = document.querySelector('nav');
        document.querySelector('.global').style.top = `${get_properties_window().h - $nav.getBoundingClientRect().height}px`;
        clearTimeout(animNavTop);
    }, 800);


    let dispatcher = new Dispatcher()
    dispatcher.run();

    if(window.location.hash === ""){
        dispatcher.navigateTo('/home')
    }
})()
