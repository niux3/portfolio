<script>
    import {onMount} from 'svelte'
    import data from './data.js'

	// let data = {
    //     "sacla": "fa-solid fa-utensils",
    //     "cavadeos": "fa-solid fa-horse",
    //     "banquecasino": "fa-solid fa-piggy-bank",
    //     "peugeot 4008": "fa-solid fa-car",
    //     "mypeugeot": "fa-solid fa-car",
    //     "decolorstop": "fa-solid fa-soap",
    //     "qui est le moins cher": "fa-solid fa-cart-shopping",
    //     "michel edouard leclerc": "fa-brands fa-blogger",
    //     "fidelity vie": "fa-solid fa-piggy-bank",
    //     "algeco": "fa-solid fa-person-digging",
    //     "cfcopies": "fa-solid fa-book",
    //     "air Madagascar": "fa-solid fa-plane",
    //     "air caraïbes": "fa-solid fa-plane",
    //     "europcar": "fa-solid fa-car",
    //     "flyopenskies": "fa-solid fa-plane",
    //     "areva": "fa-solid fa-radiation",
    //     "leroy merlin": "fa-solid fa-cart-shopping",
    //     "peugeot": "fa-solid fa-car",
    //     "peugeot design lab": "fa-solid fa-car",
    //     "dyson affaire aireblade": "fa-sharp fa-solid fa-vacuum",
    //     "brasserie flo": "fa-solid fa-utensils",
    //     "bazarchic": "fa-solid fa-cart-shopping",
    //     "mytravelchic": "fa-solid fa-cart-shopping",
    //     "afflelou": "fa-solid fa-glasses",
    //     "adp": "fa-solid fa-plane",
    //     "atelier Renault": "fa-solid fa-car",
    //     "le siège renault": "fa-solid fa-car",
    //     "Renault kadjarquest": "fa-solid fa-car",
    //     "Renault clio RS Melody": "fa-solid fa-car",
    //     "upsa": "fa-solid fa-notes-medical",
    //     "system dacia": "fa-solid fa-car",
    //     "serie toplexil": "fa-solid fa-notes-medical",
    //     "honda moto": "fa-solid fa-motorcycle",
    //     "rene furterer": "fa-solid fa-scissors",
    //     "cevital": "fa-solid fa-shirt",
    //     "longchamp": "fa-solid fa-shirt",
    //     "rimowa": "fa-solid fa-suitcase-rolling",
    //     "carenity":"fa-solid fa-people-arrows",
    //     "le point":"fa-solid fa-newspaper",
    //     "palmares le point":"fa-solid fa-newspaper",
    //     "radio france": "fa-solid fa-radio",
    //     "john paul": "fa-solid fa-bell-concierge",
    // };
    let colors = [
        "#bbac4e",
        "#af9e93",
        "#c86d62",
        "#c5692c",
        "#34495e",
        "#0a5378",
        "#77a93a",
        "#ae0a36",
    ];
    let display_article = false;
    let scroll_event = true;
    onMount(()=>{
        const scrollContainer = document.querySelector("#work nav");
        display_article = false;
        scrollContainer.addEventListener("wheel", (evt) => {
            scrollContainer.scrollLeft += !display_article && scroll_event? evt.deltaY : 0;
        }, {passive:true});
    })

    let position_article = "";
    let indexHistory = [];
    let selectSlide = e =>{
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
        container.style = 'scroll-behavior: smooth';

        container.scrollLeft = scrollLeftValue;
        li.forEach((el, i) =>{
            let defaultValue = `width: ${width_li}vw;`;
            if(i === index){

                if(parseInt(item.style.width, 10) > 9){
                    el.classList.remove('current', 'left', 'right');
                    el.classList.add('before-left')
                    setTimeout(()=>{
                        el.style = defaultValue;
                    }, 400);
                    list.style = `width: ${42 * width_li}vw`;
                    display_article = false;
                    scroll_event = true;
                }else{
                    if(indexHistory.length > 1){
                        li[indexHistory[indexHistory.length - 2]].classList.add('before-' + direction)
                    }
                    el.classList.add('current', direction);
                    item.style.width = '82vw';
                    scroll_event = false;
                    position_article = i === 0? 'first': i === li.length - 1? 'last' : ''
                    setTimeout(()=>{
                        display_article = true;
                        work.parentNode.querySelector('article').style = ["z-index:1", "visibility: visible"].join(";");
                    }, 1200)
                }
            }else{
                el.classList.remove('current', 'left', 'right');
                el.style = defaultValue;
            }
        });
        setTimeout(()=>{
            container.scrollLeft = scrollLeftValue;
            if(indexHistory.length > 1) {
                li.forEach(el => el.classList.remove('before-right', 'before-left'))
            }
            container.removeAttribute('style');

        }, 800)
    }
</script>
<main id="work">
    <nav>
        <ul style="width: {(42 * 200)}px">
            {#each data as row, i }
                <li data-id="{row.name}">
                    <i class=""></i>
                    <button data-index="{i}" on:click={selectSlide}>
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
            <img id="logo" src="logo.svg" alt="">
            <header>
                <div class="description">
                    <p class="counter">1 - 50</p>
                    <h1 class="name">Air Caraïbes</h1>
                    <div class="wrap">
                        <div class="cartouche">
                            <dl>
                                <dt>type</dt>
                                <dd>
                                    <span>backend</span>
                                </dd>
                            </dl>
                            <dl>
                                <dt>description</dt>
                                <dd>
                                    <span>conciergerie</span>
                                </dd>
                            </dl>
                            <dl>
                                <dt>année</dt>
                                <dd>
                                    <span>2022</span>
                                </dd>
                            </dl>
                        </div>
                        <ul>
                            <li>python 3</li>
                            <li>django 3</li>
                            <li>postgresql</li>
                        </ul>
                    </div>
                </div>
            </header>
            <div class="content" style="height: 2000px"></div>
        </article>
    {/if}
</main>

