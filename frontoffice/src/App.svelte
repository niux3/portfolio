<script>
    import {onMount} from 'svelte';
    import {current_view} from "./store";
    import Nav from './components/nav/Nav.svelte'
    import * as View from './components/views/index.js';
    let translate_views = {
        '#/portfolio': 'Portfolio',
        '#/a-propos-de-moi': 'About',
        '#/me-contacter': 'Contact',
        '#/accueil': 'Home',
    }
    async function hashChange(){
        current_view.set(window.location.hash);
    }

    onMount(hashChange)


</script>
<svelte:window on:hashchange={hashChange}/>
<Nav />
<main>
    <svelte:component this={View[translate_views[$current_view]]} />
</main>

