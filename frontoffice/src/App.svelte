<script>
    import Nav from './components/nav/Nav.svelte'
    import Main from './components/views/Main.svelte';

    let current_view = window.location.hash.length === 0? "#/accueil" : window.location.hash;
    let navClick = e =>{
        current_view = e.detail.current_view
    }
</script>
<Nav on:nav_click={navClick} current_view={current_view}/>
<Main current_view={current_view} />
