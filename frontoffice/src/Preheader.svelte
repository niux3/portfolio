<script>
    export let onSelectFirstSlide
    export let onCloseNav
</script>

<div class="wrap-nav">
    <img on:click={onSelectFirstSlide} id="logo" src="logo.svg?v=1" alt="">
    <a href="/" on:click|preventDefault={onCloseNav} class="burger-button">
        <div class="bar1"></div>
        <div class="bar2"></div>
        <div class="bar3"></div>
    </a>
</div>
