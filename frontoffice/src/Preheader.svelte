<script>
    import {onMount} from 'svelte'
    export let onSelectFirstSlide
    export let onCloseNav

    onMount(()=>{
        let scale_burger = ()=>{
            let $burgerButton = document.querySelector('.burger-button')
            $burgerButton.style.transform = `scale(${parseFloat((window.innerWidth * 1 / 1920).toFixed(2))})`
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
