<script>
    import Footer from './Footer.svelte'
    import PreHeader from './Preheader.svelte'
    import About from './About.svelte'
    import Project from './Project.svelte'

    export let is_not_first
    export let onSelectFirstSlide
    export let onCloseNav
    export let len
    export let data

    $: view = is_not_first? Project : About
</script>
<article class={!is_not_first? "first": ''}>
    <PreHeader onSelectFirstSlide={onSelectFirstSlide} onCloseNav={onCloseNav} />
    <svelte:component this={view} data={data} len={len} />
    <Footer onSelectFirstSlide={onSelectFirstSlide} />
</article>