import '../scss/index.scss';


(()=>{
    let $sliders = document.querySelectorAll('.slider');

    $sliders.forEach($slider =>{
        let $lis = Array.from($slider.querySelectorAll('ul li')),
            index = 0,
            save_index = index,
            next_position = '',
            onEvent = false;

        $slider.addEventListener('pointerdown', e =>{
            if(e.target.closest('button') && !onEvent){
                let sign = '';

                onEvent = true;
                save_index = index;
                if(e.target.closest('button').classList.contains('next')){
                    index = index >= $lis.length - 1? 0 : ++index;
                    next_position = 'at-right';
                    sign = '-';
                }else{
                    index = index <= 0? $lis.length - 1 : --index;
                    next_position = 'at-left';
                }
                $lis.forEach($li => $li.className.replace(/at-(left|right)/g, ''));
                $lis[index].classList.add(next_position);
                setTimeout(()=>{
                    $lis[index].style.left = 0;
                }, 0);
                $lis[save_index].style.left = `${sign}100%`;
                $lis[index].addEventListener('transitionend', e =>{
                    $lis.forEach($li => {
                        $li.removeAttribute('style');
                        $li.classList.remove('at-middle');
                    });
                    $lis[index].removeAttribute('class');
                    $lis[index].classList.add('at-middle');
                    onEvent = false;
                });
            }
        });
    });
})()
