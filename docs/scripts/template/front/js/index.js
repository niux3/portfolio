import '../scss/index.scss';

(()=>{
    // ???
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

    let $nav = document.querySelector('nav');
    document.querySelector('.global').style.top = `${get_properties_window().h - $nav.getBoundingClientRect().height}px`;

})()
