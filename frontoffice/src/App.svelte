<script>
    import {onMount} from 'svelte'
    import {debounce} from './helpers'
    import Preload from './Preload.svelte'
    import Article from './Article.svelte'
    import data from './data.js'

    let is_clicked = false;
    let display_article = false;
    let scroll_event = true;
    let id_slide_clicked = 0
    onMount(()=>{
        (()=>{
            if(document.querySelectorAll('a[href*="000webhost"]').length){
                document.querySelector('a[href*="000webhost"]').closest('div').remove()
            }
        })()

        const scrollContainer = document.querySelector("#work nav");
        display_article = false;
        let cls_on_scroll = 'on-scroll'

        scrollContainer.addEventListener("wheel", (evt) => {
            if(!scrollContainer.classList.contains(cls_on_scroll)){
                scrollContainer.classList.add(cls_on_scroll)
            }
            scrollContainer.scrollLeft += !display_article && scroll_event? evt.deltaY : 0;
            debounce(()=>{
                if(scrollContainer.classList.contains(cls_on_scroll)){
                    scrollContainer.classList.remove(cls_on_scroll)
                }
            }, 250)()
        }, {passive:true})

        let is_down = false
        let start_x
        let scroll_left
        let event_mouse_button = (event_type, callback) =>{
            scrollContainer.addEventListener(event_type, e =>{
                if(scrollContainer.classList.contains('on-nav')){
                    callback(e)
                }
            })
        }
        event_mouse_button('mousedown', e =>{
            if(scrollContainer.classList.contains('on-nav')){
                is_down = true
                start_x = e.pageX - scrollContainer.offsetLeft
                scroll_left = scrollContainer.scrollLeft
            }
        })
        event_mouse_button('mouseleave', e => is_down = false)
        event_mouse_button('mouseup', e => is_down = false)
        event_mouse_button('mousemove', e =>{
            if(!is_down) return
            e.preventDefault()
            let x = e.pageX - scrollContainer.offsetLeft;
            let walk = (x - start_x) * 3;   //accelarateur
            scrollContainer.scrollLeft = scroll_left - walk;
        })

        scrollContainer.classList.remove('on-nav')
        let anim_intro = true
        if(anim_intro) {
            setTimeout(()=>{
                let li = Array.from(document.querySelectorAll('li'))
                let count = 0

                document.querySelector('.wrap-logo-anim').remove()

                let timer = setInterval(() => {
                    if (count < li.slice(0, 13).length) {
                        li[count].classList.add('display')
                        ++count
                    } else {
                        clearInterval(timer)
                        li.map(el => el.classList.add('display'))
                        document.querySelector('nav li button').click()
                    }
                }, 75)
            }, 3500);
        }else{
            document.querySelector('.wrap-logo-anim').remove()
            let li = Array.from(document.querySelectorAll('li'))
            li.map(el => el.classList.add('display'))
            document.querySelector('nav li button').click()
        }
        window.addEventListener('resize', e => {
            display_article = false
            debounce(()=>{
                if(document.querySelector('nav li.current button') !== null){
                    document.querySelector('nav li.current button').click()
                    let timer = setTimeout(()=>{
                        document.querySelector(`nav li[data-id="${id_slide_clicked}"] button`).click()
                        clearTimeout(timer)
                    }, 1200)
                }
            }, 400)()
        })
    })

    // let position_article = "";
    let data_article = data[0]
    let indexHistory = [];
    let selectSlide = e =>{
        if(!is_clicked){
            let index = parseInt(e.target.closest('button').dataset.index, 10);
            let id = parseInt(e.target.closest('button').dataset.id, 10)
            let work = e.target.closest('#work')
            let container = work.querySelector("nav");
            let list = work.querySelector("ul");
            let li = work.querySelectorAll(`nav ul li`);
            let width_li = 9
            let item = work.querySelector(`nav ul li:nth-child(${index + 1})`);
            let innerWidth = window.innerWidth;
            let itemWidth = (innerWidth - width_li * 2);
            let scrollLeftValue = (width_li * index) - width_li;
            let responsiveScrollLeftContainer = window.matchMedia('(min-width: 768px)').matches? 0 : 1
            let styleItemWidth = window.matchMedia('(min-width: 768px)').matches? '82vw' : '100vw'
            display_article = false;
            scroll_event = false;
            is_clicked = true;

            id_slide_clicked = id

            scrollLeftValue = (((width_li * innerWidth) / 100) * (index + responsiveScrollLeftContainer)) - ((width_li * innerWidth) / 100)
            // console.log(innerWidth, width_li, ' -- ', (width_li * innerWidth) / 100)
            let direction = (()=>{
                let output = 'right';
                if(indexHistory.slice(-1) < index){
                    output = 'left'
                }
                return output;
            })()
            indexHistory = [...indexHistory, index];


            list.style = `width: ${(42 * width_li) + itemWidth}vw`;
            container.classList.remove('on-nav');
            container.style = 'scroll-behavior: smooth';

            container.scrollLeft = scrollLeftValue;
            li.forEach((el, i) =>{
                let defaultValue = `width: ${width_li}vw;`;
                if(i === index){
                    if(9 < parseInt(item.style.width, 10)){
                        el.classList.remove('current', 'left', 'right');
                        el.classList.add('before-left')
                        setTimeout(()=>{
                            el.style = defaultValue;
                        }, 400);
                        list.style = `width: ${42 * width_li + 2}vw`;
                        work.classList.remove('on-article')
                        display_article = false;
                        scroll_event = true;
                        is_clicked = false;
                    }else{
                        if(indexHistory.length > 1){
                            li[indexHistory[indexHistory.length - 2]].classList.add('before-' + direction)
                        }
                        el.classList.add('current', direction);

                        item.style.width = styleItemWidth;
                        scroll_event = false;
                        // position_article = i === 0? 'first': i === li.length - 1? 'last' : ''
                        if(id !== 0){
                            data_article = data.filter(r => r.id === id)[0]
                            data_article['index'] = index + 1
                        }else{
                            data_article = false
                        }

                        let timeout = setTimeout(()=>{
                            is_clicked = false;
                            display_article = true;
                            work.classList.add('on-article')
                            // work.querySelector('article').style = ["z-index:1", "visibility: visible"].join(";");
                            clearTimeout(timeout);
                        }, 1200)
                    }
                }else{
                    el.classList.remove('current', 'left', 'right');
                    el.style = defaultValue;
                }
            });
            let timeout = setTimeout(()=>{
                container.scrollLeft = scrollLeftValue;
                if(indexHistory.length > 1) {
                    li.forEach(el => el.classList.remove('before-right', 'before-left'))
                }
                container.removeAttribute('style');
                clearTimeout(timeout);
            }, 800)
        }
    }
    let onFirstSlide = e =>{
        if(!document.querySelector('nav li').classList.contains('current')){
            document.querySelector("nav li button").click()
        }
    }
    let onCloseNav = e =>{
        document.querySelector('#work li.current button').click()
        let timeout = setTimeout(()=>{
            document.querySelector('#work nav').classList.add('on-nav');
            clearTimeout(timeout);
        }, 400)
    }
</script>
<Preload />
<main id="work">
    <nav>
        <ul style="width: {(data.length * 200)}px">
            <li data-id="0">
                <span class="fa-solid fa-address-card"></span>
                <button data-index="0" data-id="0" on:click={selectSlide}>
                        <span>
                            <span>À PROPOS DE MOI</span>
                        </span>
                </button>
            </li>
            {#each data as row, i }
                <li data-id="{row.id}">
                    <span class="{row.activity_icon}"></span>
                    <button data-index="{i + 1}" data-id="{row.id}" on:click={selectSlide}>
                        <span>
                            <span>{row.name.toUpperCase()}</span>
                        </span>
                    </button>
                </li>
            {/each}
        </ul>
    </nav>
    {#if display_article}
        <Article
                is_not_first={data_article}
                onSelectFirstSlide={onFirstSlide}
                onCloseNav={onCloseNav}
                len={data.length}
                data={data_article}
        />
    {/if}
</main>

