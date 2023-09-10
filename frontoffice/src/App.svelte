<script>
    import Carousel from "./components/Carousel.svelte"
    import Nav from "./components/Nav.svelte"


    let index = 0
    console.log(index);
</script>
<main>
    <Nav></Nav>
    <Carousel {index}></Carousel>
</main>
