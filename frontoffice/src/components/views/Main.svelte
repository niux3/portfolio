<script>
    let innerWidth = window.innerWidth;
    let innerHeight =  window.innerHeight;
</script>
<div style="position: fixed; top:75px;right:50px"><p>{innerWidth} x {innerHeight}</p></div>
<div style="position: fixed; top:95px;right:50px"><p>{innerWidth * 3} x {innerHeight * 3}</p></div>
<svelte:window bind:innerWidth bind:innerHeight />
<main style="width: {innerWidth}px; height: {innerHeight}px;">
    <div class="container" style="width: {innerWidth * 3}px; height: {innerHeight * 3}px;">

    </div>
</main>

<style lang="scss">
    main{
        position: relative;
        overflow: hidden;
      .container{
        position: absolute;
        top: 0;
        left: 0;
        transition: left 400ms, top 400ms;
        background:
		linear-gradient(90deg, #f5f5f5 19px, transparent 1%) center,
		linear-gradient(#f5f5f5 19px, transparent 1%) center,
		#e8e8e8;
	background-size: 22px 22px;

      }
    }
</style>