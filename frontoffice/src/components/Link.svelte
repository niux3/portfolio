<script>
    import {onMount} from 'svelte'
    import {current_view} from "../store";
    export let to;
    export let text;
    let onClick = e => current_view.set(e.target.closest('a').getAttribute('href'));
    let onMouseLeave = e => e.target.closest('a').textContent = text;
    let onMouseOver = e =>{
        let P,T,tag;
        let car = "-------------------- 0123456789abcdefghijklmnopqrstuvwxyz";
        let L = car.length;
        console.log(e.target.closest('a').getBoundingClientRect().width)
        // e.target.closest('a').style.width = (e.target.closest('a').getBoundingClientRect().width + 10) + "px";
        let Olink = node =>{
            let txt = node.innerHTML;
            let len_txt = txt.length;
            let txa = "";
            let txo = "";
            let run = false;
            let stop = false;
            let cp = [];
            let over = ()=>{
                txa="";
                for(let i=0; i<len_txt;i++){
                    cp[i] = Math.round(Math.random()*20);
                    txa += car.charAt(cp[i]);
                }
                node.innerHTML = txa;
                if(!run) display(node);
            }
            let display = (node)=>{
                if(!stop){
                    run = false;
                    for(let i=0; i<len_txt;i++){
                        var c = txa.charAt(i);
                        var d = txt.charAt(i);
                        if(c !== d){
                            cp[i]++;
                            run = true;
                            c = car.charAt(cp[i]);
                            if(cp[i] >= L) c=d;
                            txa = txa.substring(0,i)+c+txa.substring(i+1,999);
                        }
                    }
                    node.childNodes[0].nodeValue = txa;
                    if(run) setTimeout(function() {
                        display(node);
                    }, 32);
                } else {
                    run = false;
                    txa = txt;
                    console.log('>>', txa)
                }
            }
            //node.innerHTML = "";

            over();
            // node.addEventListener('mouseover', e =>{
            //     return false;
            // })

        }
        Olink(e.target.closest('a'));

    }
    onMount(()=>{
        console.log(document.querySelector('a').textContent);
    })
</script>

<a href={to} on:click={onClick} on:mouseenter={onMouseOver} on:focus={onMouseOver} on:mouseleave={onMouseLeave}>{text}</a>