<script>
    import {onMount} from 'svelte'
	let data = [
        "sacla",
        "cavadeos",
        "banquecasino",
        "peugeot 4008",
        "mypeugeot",
        "decolorstop",
        "qui est le moins cher",
        "michel edouard leclerc",
        "fidelity vie",
        "algeco",
        "cfcopies",
        "air Madagascar",
        "air caraïbes",
        "europcar",
        "flyopenskies",
        "areva",
        "leroy merlin",
        "peugeot",
        "peugeot design lab",
        "dyson affaire aireblade",
        "brasserie flo",
        "bazarchic",
        "mytravelchic",
        "afflelou",
        "adp",
        "atelier Renault",
        "le siège renault",
        "Renault kadjarquest",
        "Renault clio RS Melody",
        "upsa",
        "system dacia",
        "serie toplexil",
        "honda moto",
        "rene furterer",
        "cevital",
        "longchamp",
        "rimowa",
        "carenity",
        "le point",
        "palmares le point",
        "radio france",
        "john paul",
    ];
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
        let item = work.querySelector(`nav ul li:nth-child(${index + 1})`);
        let innerWidth = window.innerWidth;
        let itemWidth = (innerWidth - 220);
        let scrollLeftValue = (110 * index) - 110;

        let direction = (()=>{
            let output = 'right';
             if(indexHistory.slice(-1) < index){
                output = 'left'
             }
             return output;
        })()
        indexHistory = [...indexHistory, index];
        console.log(indexHistory,' - - - ',indexHistory.slice(-2, 1))


        list.style = `width: ${(42 * 110) + itemWidth}px`;
        container.style = 'scroll-behavior: smooth';

        container.scrollLeft = scrollLeftValue;
        li.forEach((el, i) =>{
            let defaultValue = `width: 110px;`;
            if(i === index){
                if(parseInt(item.style.width, 10) > 110){
                    el.classList.remove('current', 'left', 'right');
                    el.style = defaultValue;
                    list.style = `width: ${42 * 110}px`;
                }else{
                    if(indexHistory.length > 1){
                        console.log(li[indexHistory[indexHistory.length - 2]])
                        li[indexHistory[indexHistory.length - 2]].classList.add('before-' + direction)
                    }
                    el.classList.add('current', direction);
                    item.style.width = itemWidth + 'px';
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
        <ul style="width: {(42 * 110)}px">
            {#each data as row, i}
                <li data-id="{row}">
                    <button data-index="{i}" on:click={selectSlide}>
                        <span>
                            <span>{row.toUpperCase()}</span>
                        </span>
                    </button>
                </li>
            {/each}
        </ul>
    </nav>
</main>
