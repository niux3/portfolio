import '../scss/index.scss';

(()=>{
    // ???
    document.body.style.margin = 0;
    document.body.style.background = '#2ecc71';
    document.querySelector('section').style.height = '929px';

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
                `width:${props_window.w - 16}px`,
                `height:${props_window.h}px`,
            ];
            $header.style = style.join(';');

    }
    set_resize_header();
    window.addEventListener('resize', set_resize_header)
})()
