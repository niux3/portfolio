<script>
    import {onMount} from 'svelte';
    import {current_view, display} from "./libs/store";
    import Header from './components/Header.svelte'
    import Nav from './components/nav/Nav.svelte'
    import * as View from './components/views/index.js';
    let translate_views = {
        '#/portfolio': 'Portfolio',
        '#/a-propos-de-moi': 'About',
        '#/me-contacter': 'Contact',
        '#/accueil': 'Home',
    }

    async function hashChange(){
        current_view.set(window.location.hash.length === 0? '#/accueil' : window.location.hash);
    }

    $: view = Object.keys(translate_views).includes($current_view)? View[translate_views[$current_view]] : View['View_404'];
    onMount(()=>{
        hashChange();
    })
</script>
<svelte:window on:hashchange={hashChange}/>
<Header />
<main>
    <svelte:component this={view} />
</main>

