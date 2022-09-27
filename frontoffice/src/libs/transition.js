export let toVisible = (callback) =>{
    document.getElementById('overlayTransition').classList.add('visible');
    callback();
}


export let toInvisible = (callback) =>{
    let end = setTimeout(()=>{
        document.getElementById('overlayTransition').classList.add('invisible');
        let destroy = setTimeout(()=>{
            document.getElementById('overlayTransition').classList.remove('visible', 'invisible');
            callback();
            clearTimeout(destroy);
        }, 400)
        clearTimeout(end)
    }, 800)
}
