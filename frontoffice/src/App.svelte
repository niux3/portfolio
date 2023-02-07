<script>
    import {onMount} from 'svelte'
    import {debounce} from './helpers'
    import Footer from './Footer.svelte'
    import PreHeader from './Preheader.svelte'
    import data from './data.js'

    let is_clicked = false;
    let display_article = false;
    let scroll_event = true;
    onMount(()=>{
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
        }, {passive:true});

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
            let walk = (x - start_x) * 3;
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

            display_article = false;
            scroll_event = false;
            is_clicked = true;

            scrollLeftValue = (((width_li * innerWidth) / 100) * index) - ((width_li * innerWidth) / 100)
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

                        item.style.width = '82vw';
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
<div class="wrap-logo-anim">
    <div class="logo-anim">
        <svg width="79.375mm" height="79.375mm" version="1.1" viewBox="0 0 79.375 79.375" xmlns="http://www.w3.org/2000/svg" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <circle cx="39.6875" cy="39.6875" r="17" stroke-miterlimit="10" stroke-width="34" />
        </svg>
        <svg width="79.375mm" height="79.375mm" version="1.1" viewBox="0 0 79.375 79.375" xmlns="http://www.w3.org/2000/svg" xmlns:cc="http://creativecommons.org/ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
            <circle cx="97.246" cy="111.52" r="16.492" fill="none" stroke="" stroke-width="33.073" id="circle-stroke" />
            <g transform="translate(-57.558 -71.836)" id="content">
                <circle cx="97.246" cy="111.52" r="33.073" fill="#444" stroke-width=".177" style="paint-order:markers fill stroke"/>
                <g transform="matrix(.33371 0 0 .33371 -78.371 192.62)" fill="#f5f5f5">
                    <g transform="translate(243.55 81.615)" stroke-width=".67039" aria-label="rb">
                        <path d="m251.15-309.59v27.653h-25.077v-31.927q0-10.81 2.0112-16.843 2.0112-6.0963 6.8505-10.81 3.6452-3.6452 8.4846-5.6564 4.9022-2.074 9.8044-2.074 2.3882 0 4.7136 0.18855 2.3254 0.18854 4.5251 0.56563v26.396q-0.43994-0.0628-1.3198-0.18855-2.074-0.31424-2.6396-0.31424-4.0852 0-5.7192 2.6396-1.6341 2.6396-1.6341 10.37z"/>
                        <path d="m270.76-373.69h24.448v51.599q0 9.553 2.2626 13.324t7.5418 3.7709q3.8338 0 6.662-2.8282 2.8282-2.891 2.8282-6.7876 0-4.2109-2.7653-7.039-2.7653-2.891-6.7248-2.891-1.0056 0-2.1368 0.31425-1.1313 0.25139-3.2681 1.1313v-26.019q0.62849-0.0629 2.6396-0.18855 2.0112-0.18855 3.1424-0.18855 14.141 0 24.008 10.181 9.9301 10.119 9.9301 24.7 0 6.8505-2.514 13.135-2.5139 6.222-7.2276 11.061-4.9022 4.965-11.187 7.6675-6.222 2.6396-13.135 2.6396-10.181 0-18.415-5.2164-8.1703-5.2793-12.13-14.267-2.074-4.7765-3.0167-9.8672-0.94273-5.1536-0.94273-12.758v-4.9022z"/>
                    </g>
                    <path d="m542.38-288.15h-31.744l15.872-17.36z" stroke-width=".44511" style="paint-order:markers fill stroke"/>
                </g>

            </g>
        </svg>
    </div>
</div>
<main id="work">
    <nav>
        <ul style="width: {(data.length * 200)}px">
            <li>
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
        {#if data_article !== false}
        <article style="z-index: 1">
            <PreHeader onSelectFirstSlide={onFirstSlide} onCloseNav={onCloseNav} />
            <header>
                <div class="description">
                    <p class="counter">{data_article.index} - {data.length}</p>
                    <h1 class="name">{data_article.name}</h1>
                    <div class="wrap">
                        <div class="cartouche">
                            <dl>
                                <dt>type</dt>
                                <dd>
                                    <span>{data_article.function}</span>
                                </dd>
                            </dl>
                            <dl>
                                <dt>description</dt>
                                <dd>
                                    <span>{data_article.activity_name}</span>
                                </dd>
                            </dl>
                            <dl>
                                <dt>année</dt>
                                <dd>
                                    <span>{data_article.year}</span>
                                </dd>
                            </dl>
                        </div>
<!--                        <ul>-->
<!--                            {#each data_article.technologies as technology, i}-->
<!--                                <li>{technology}</li>-->
<!--                            {/each}-->
<!--                        </ul>-->
                    </div>
                </div>
            </header>
            <div class="content"></div>
            <Footer onSelectFirstSlide={onFirstSlide} />
        </article>
        {:else}
            <article class="first">
                <PreHeader onSelectFirstSlide={onFirstSlide} onCloseNav={onCloseNav} />
                <div class="content"></div>
                <Footer onSelectFirstSlide={onFirstSlide} />
            </article>
        {/if}
    {/if}
</main>

