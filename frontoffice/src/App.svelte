<script>
    import {onMount} from 'svelte'
    import Carousel from "./components/Carousel.svelte"
    import Nav from "./components/Nav.svelte"
    import Preload from "./components/Preload.svelte"
    import Cursor from './libs/cursor/Cursor'


    let index = 0

    onMount(()=>{
        let cursor = new Cursor()
        cursor.event()

        let isDoAnim = window.location.hash === ''
        let $logoAnim = document.querySelector('.wrap-logo-anim')
        if(isDoAnim){
            let animLogo = setTimeout(()=>{
                $logoAnim.remove()
            }, 3500)
        }else{
            $logoAnim.remove()

        }
    })
</script>

<Preload />
<main>
    <Nav />
    <Carousel {index}></Carousel>
</main>