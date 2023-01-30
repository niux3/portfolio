<script>
    import {onMount} from 'svelte'
    import {debounce} from './helpers'
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

        scrollContainer.classList.remove('on-nav')
        let anim_intro = true
        if(anim_intro) {
            let li = Array.from(document.querySelectorAll('li'))
            let count = 0
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
        }else{
            let li = Array.from(document.querySelectorAll('li'))
            li.map(el => el.classList.add('display'))
            document.querySelector('nav li button').click()
        }
    })

    let position_article = "";
    let data_article = data[0]
    let indexHistory = [];
    let selectSlide = e =>{
        if(!is_clicked){
            let index = parseInt(e.target.closest('button').dataset.index, 10);
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
                        position_article = i === 0? 'first': i === li.length - 1? 'last' : ''
                        data_article = data.filter(r => r.id === parseInt(e.target.closest('button').dataset.id, 10))[0]
                        data_article['index'] = index + 1;

                        let timeout = setTimeout(()=>{
                            is_clicked = false;
                            display_article = true;
                            work.parentNode.querySelector('article').style = ["z-index:1", "visibility: visible"].join(";");
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
    let onCloseNav = e =>{
        document.querySelector('#work li.current button').click()
        let timeout = setTimeout(()=>{
            document.querySelector('#work nav').classList.add('on-nav');
            clearTimeout(timeout);
        }, 400)
    }
</script>
<main id="work">
    <nav>
        <ul style="width: {(data.length * 200)}px">
<!--            <li>-->
<!--                <i class=""></i>-->
<!--                <button on:click={selectSlide}>-->
<!--                        <span>-->
<!--                            <span>À PROPOS DE MOI</span>-->
<!--                        </span>-->
<!--                </button>-->
<!--            </li>-->
            {#each data as row, i }
                <li data-id="{row.id}">
                    <span class="{row.activity_icon}"></span>
                    <button data-index="{i}" data-id="{row.id}" on:click={selectSlide}>
                        <span>
                            <span>{row.name.toUpperCase()}</span>
                        </span>
                    </button>
                </li>
            {/each}
        </ul>
    </nav>
    {#if display_article}
        <article class="{position_article}" style="z-index: 1">
            <div class="wrap-nav">
                <img id="logo" src="logo.svg" alt="">
                <button on:click={onCloseNav}><i class="fa-solid fa-bars"></i></button>
            </div>
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
            <footer> -- footer -- </footer>
        </article>
    {/if}
</main>

