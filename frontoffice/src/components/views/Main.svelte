<script>
    import { watchResize } from "svelte-watch-resize";
    export let current_view;
    let innerWidth = window.innerWidth;
    let innerHeight =  window.innerHeight;


    $: coord = {
        "#/accueil": [innerWidth, 0],
        "#/portfolio": [innerWidth * 2, innerHeight],
        "#/me-contacter": [innerWidth, innerHeight * 2],
        "#/a-propos-de-moi": [0, innerHeight],
    }
    let changeDimension = node =>{
        innerWidth = node.clientWidth;
        innerHeight = node.clientHeight;
    }
</script>
<div style="position: fixed; top:75px;right:50px"><p><strong>dimentions screen: </strong>{innerWidth} x {innerHeight}</p></div>
<div style="position: fixed; top:95px;right:50px"><p><strong>dimentions container: </strong>{innerWidth * 3} x {innerHeight * 3}</p></div>
<svelte:window bind:innerWidth bind:innerHeight />

<p style="position: fixed; top:115px;right:50px"><strong>main: </strong>{current_view} - {coord[current_view][0]} - {coord[current_view][1]}</p>
<main style="width: {innerWidth}px; height: {innerHeight}px;" use:watchResize={changeDimension}>
    <div class="container" style="width: {innerWidth * 3}px; height: {innerHeight * 3}px;left:-{coord[current_view][0]}px; top:-{coord[current_view][1]}px">

    </div>
</main>

<style lang="scss">
    main{
        position: relative;
        overflow: hidden;
      z-index: -1;
      .container{
        position: absolute;
        top: 0;
        left: 0;
        transition: left 800ms, top 800ms;
        background:
		linear-gradient(90deg, #f5f5f5 19px, transparent 1%) center,
		linear-gradient(#f5f5f5 19px, transparent 1%) center,
		#e1e1e1;
	background-size: 22px 22px;

      }
    }
</style>