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
    ]
    onMount(()=>{
        const scrollContainer = document.querySelector("#work nav");
        scrollContainer.addEventListener("wheel", (evt) => {
            scrollContainer.scrollLeft += evt.deltaY;
        }, {passive:true});
    })

    let selectSlide = e =>{
        let index = parseInt(e.target.closest('button').dataset.index, 10)
        let work = e.target.closest('#work')
        let container = work.querySelector("nav");
        let list = work.querySelector("ul");
        let item = work.querySelector(`nav ul li:nth-child(${index + 1})`);
        let innerWidth = window.innerWidth;
        let itemWidth = (innerWidth - 110);

        list.style = `width: ${(42 * 110) + itemWidth}px`;
        container.style = 'scroll-behavior: smooth';

        container.scrollLeft = 110 * index;
        work.querySelectorAll(`nav ul li`).forEach((el, i) =>{
            let defaultValue = `width: 110px; background-color: ${colors[i % colors.length]}`;
            if(i === index){
                if(parseInt(item.style.width, 10) > 110){
                    el.style = defaultValue;
                    list.style = `width: ${42 * 110}px`;

                }else{
                    item.style.width = itemWidth + 'px';
                }
            }else{
                el.style = defaultValue;
            }
        });
        list.addEventListener('transitionend', e =>{
            container.scrollLeft = 110 * index;
            container.removeAttribute('style');
        })
    }
</script>

<main id="work">
    <nav>
        <ul style="width: {(42 * 110) + 0}px">
            {#each data as row, i}
            <li data-id="{row}" style="background-color: {colors[i % colors.length]}">
                <button data-index="{i}" on:click={selectSlide}>
                    <span>{row.toUpperCase()}</span>
                </button>


            </li>
                {/each}
        </ul>
    </nav>
</main>
