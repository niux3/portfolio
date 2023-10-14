export default class Cursor{
    constructor(){
        document.body.insertAdjacentHTML('afterbegin', '<div id="cursor" />')
        this._$cursor = document.getElementById('cursor')
    }

    event(){
        let $cursor = this._$cursor
        window.addEventListener('mousemove', e =>{
            if(e.target.classList.contains('event-cursor')){
                //console.log(">> ", e.target)
                $cursor.style = [
                    `left: ${e.target.getBoundingClientRect().left}px`,
                    `top: ${e.target.getBoundingClientRect().top}px`,
                    `width:${e.target.getBoundingClientRect().width}px`,
                    `height:${e.target.getBoundingClientRect().height}px`,
                    `border-radius: 6px`,
                    `transform: translate(0, 0)`,
                ].join(';')
            }else{
                $cursor.style = [
                    `left: ${e.pageX}px`,
                    `top: ${e.pageY}px`,
                    `width:10px`,
                    `height:10px`,
                    `border-radius: 50%`,
                    `transform: translate(-50%, -50%)`,
                ].join(';')
            }
        })
        document.body.addEventListener('mouseenter', e => $cursor.style.display = 'block')
        document.body.addEventListener('mouseleave', e => $cursor.style.display = 'none')
        document.body.addEventListener('click', e => $cursor.style = [
            `left: ${e.pageX}px`,
            `top: ${e.pageY}px`,
            `width:10px`,
            `height:10px`,
            `border-radius: 50%`,
            `transform: translate(-50%, -50%)`,
        ].join(';'))
    }
}