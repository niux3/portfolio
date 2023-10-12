<script>
    import {onMount} from 'svelte'
    import Carousel from "./components/Carousel.svelte"
    import Nav from "./components/Nav.svelte"
    import Cursor from './libs/cursor/Cursor'


    let index = 0

    onMount(()=>{
        let cursor = new Cursor()
        cursor.event()
    })
</script>
<main>
    <Nav />
    <Carousel {index}></Carousel>
</main>
