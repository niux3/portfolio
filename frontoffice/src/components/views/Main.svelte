<script>
    // import { watchResize } from "svelte-watch-resize";
    import Pages from './Pages.svelte';
    export let current_view;
    let innerWidth = window.innerWidth;
    let innerHeight =  window.innerHeight;



    let changeDimension = node =>{
        innerWidth = node.clientWidth;
        innerHeight = node.clientHeight;
    }
</script>
<div style="position: fixed; top:75px;right:50px"><p><strong>dimentions screen: </strong>{innerWidth} x {innerHeight}</p></div>
<div style="position: fixed; top:95px;right:50px"><p><strong>dimentions container: </strong>{innerWidth * 3} x {innerHeight * 3}</p></div>
<svelte:window bind:innerWidth bind:innerHeight />

<p style="position: fixed; top:115px;right:50px"><strong>main: </strong>{current_view}</p>
<main>
    <Pages current_view={current_view} w={innerWidth} h={innerHeight} />
</main>

<style lang="scss">

</style>