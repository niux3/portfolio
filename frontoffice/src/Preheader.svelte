<script>
    import {onMount} from 'svelte'
    export let onSelectFirstSlide
    export let onCloseNav

    onMount(()=>{
        let scale_burger = ()=>{
            let $burgerButton = document.querySelector('.burger-button'),
                quotient = 0
            if(matchMedia('(min-width: 960px)').matches){
                quotient = 1920
            }else if(matchMedia('(min-width: 900px)').matches){
                quotient = 1000
            }else if(matchMedia('(min-width: 768px)').matches){
                quotient = 1200
            }else if(matchMedia('(min-width: 680px)').matches){
                quotient = 1000
            }else if(matchMedia('(min-width: 320px)').matches){
                quotient = 800
            }
            if($burgerButton.style !== null){
                $burgerButton.style.transform = `scale(${parseFloat((window.innerWidth * 1 / quotient).toFixed(2))})`
            }
        }
        scale_burger()
        window.addEventListener('resize', e =>{
            scale_burger()
        })
    })

</script>

<div class="wrap-nav">
    <img on:click={onSelectFirstSlide} id="logo" src="logo.svg?v=1" alt="">
    <a href="/" on:click|preventDefault={onCloseNav} class="burger-button">
        <div class="bar1"></div>
        <div class="bar2"></div>
        <div class="bar3"></div>
    </a>
</div>
