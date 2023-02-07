<script>
    export let onSelectFirstSlide
    export let onCloseNav
</script>

<div class="wrap-nav">
    <img on:click={onSelectFirstSlide} id="logo" src="logo.svg?v=1" alt="">
    <button on:click={onCloseNav}><i class="fa-solid fa-bars"></i></button>
</div>
