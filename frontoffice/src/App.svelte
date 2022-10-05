<script>
    import {onMount} from 'svelte'
	let data = {
        "sacla": "fa-solid fa-utensils",
        "cavadeos": "fa-solid fa-horse",
        "banquecasino": "fa-solid fa-piggy-bank",
        "peugeot 4008": "fa-solid fa-car",
        "mypeugeot": "fa-solid fa-car",
        "decolorstop": "fa-solid fa-soap",
        "qui est le moins cher": "fa-solid fa-cart-shopping",
        "michel edouard leclerc": "fa-brands fa-blogger",
        "fidelity vie": "fa-solid fa-piggy-bank",
        "algeco": "fa-solid fa-person-digging",
        "cfcopies": "fa-solid fa-book",
        "air Madagascar": "fa-solid fa-plane",
        "air caraïbes": "fa-solid fa-plane",
        "europcar": "fa-solid fa-car",
        "flyopenskies": "fa-solid fa-plane",
        "areva": "fa-solid fa-radiation",
        "leroy merlin": "fa-solid fa-cart-shopping",
        "peugeot": "fa-solid fa-car",
        "peugeot design lab": "fa-solid fa-car",
        "dyson affaire aireblade": "fa-sharp fa-solid fa-vacuum",
        "brasserie flo": "fa-solid fa-utensils",
        "bazarchic": "fa-solid fa-cart-shopping",
        "mytravelchic": "fa-solid fa-cart-shopping",
        "afflelou": "fa-solid fa-glasses",
        "adp": "fa-solid fa-plane",
        "atelier Renault": "fa-solid fa-car",
        "le siège renault": "fa-solid fa-car",
        "Renault kadjarquest": "fa-solid fa-car",
        "Renault clio RS Melody": "fa-solid fa-car",
        "upsa": "fa-solid fa-notes-medical",
        "system dacia": "fa-solid fa-car",
        "serie toplexil": "fa-solid fa-notes-medical",
        "honda moto": "fa-solid fa-motorcycle",
        "rene furterer": "fa-solid fa-scissors",
        "cevital": "fa-solid fa-shirt",
        "longchamp": "fa-solid fa-shirt",
        "rimowa": "fa-solid fa-suitcase-rolling",
        "carenity":"fa-solid fa-people-arrows",
        "le point":"fa-solid fa-newspaper",
        "palmares le point":"fa-solid fa-newspaper",
        "radio france": "fa-solid fa-radio",
        "john paul": "fa-solid fa-bell-concierge",
    };
    let colors = [
        "#1abc9c",
        "#2ecc71",
        "#3498db",
        "#9b59b6",
        "#34495e",
        "#e67e22",
        "#e74c3c",
        "#95a5a6",
    ];

    onMount(()=>{
        const scrollContainer = document.querySelector("#work nav");
        scrollContainer.addEventListener("wheel", (evt) => {
            scrollContainer.scrollLeft += evt.deltaY;
        }, {passive:true});

        // document.querySelectorAll('#work button span').forEach(el =>{
        //     let txt = el.textContent;
        //     let output = '';
        //     for(let i=0; i < txt.length; i++){
        //         output += `<span>${txt[i]}</span>`;
        //     }
        //     el.innerHTML = output;
        // });

    })

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
        scrollLeftValue = (((width_li * innerWidth) / 100) * index) - ((width_li * innerWidth) / 100)
        console.log(innerWidth, width_li, ' -- ', (width_li * innerWidth) / 100)
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
                }else{
                    if(indexHistory.length > 1){
                        li[indexHistory[indexHistory.length - 2]].classList.add('before-' + direction)
                    }
                    el.classList.add('current', direction);
                    item.style.width = '82vw';
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
            {#each Object.entries(data) as [name, icon], i }
                <li data-id="{name}">
                    <i class="{icon}"></i>
                    <button data-index="{i}" on:click={selectSlide}>
                        <span>
                            <span>{name.toUpperCase()}</span>
                        </span>
                    </button>
                </li>
            {/each}
        </ul>
    </nav>
    <article>
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
</main>

