<script>
    import {onMount} from 'svelte';
    import {current_view, display} from "./libs/store";
    import Header from './components/Header.svelte'
    import * as View from './components/views/index.js';
    let translate_views = {
        '#\/projets/[a-z0-9 _-]+': 'PortfolioShow',
        '#/projets': 'Portfolio',
        '#/a-propos-de-moi': 'About',
        // '#/me-contacter': 'Contact',
        '#/accueil': 'Home',
    }

    async function hashChange(){
        current_view.set(window.location.hash.length === 0? '#/accueil' : window.location.hash);
    }

    $: view = (()=>{
        let v = null;
        if(Object.keys(translate_views).slice(1).includes($current_view)){
            v = View[translate_views[$current_view]];
        }

        if(new RegExp(Object.keys(translate_views)[0], 'i').test($current_view)){
            v = View[Object.values(translate_views)[0]];
        }

        if(v === null){
            v = View['View_404'];
        }
        return v;
    })();

    onMount(()=>{
        hashChange();
    })
</script>
<svelte:window on:hashchange={hashChange}/>
<Header />
<main>
    <svelte:component this={view} />
</main>

