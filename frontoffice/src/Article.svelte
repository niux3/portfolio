<script>
    import {onMount} from 'svelte'
    import {debounce} from './helpers'
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

    onMount(()=>{
        let lastScrollTop = 0,
            clsOnScrollUp = 'on-scroll-up'
        document.querySelector('article').addEventListener('scroll', e =>{
            debounce(()=>{
                let currentScrollTop = e.target.scrollTop
                console.log('>>', currentScrollTop)
                if(currentScrollTop > lastScrollTop && e.target.classList.contains(clsOnScrollUp)){
                    e.target.classList.remove(clsOnScrollUp)
                }else if(currentScrollTop < lastScrollTop && !e.target.classList.contains(clsOnScrollUp)){
                    e.target.classList.add(clsOnScrollUp)
                }
                lastScrollTop = currentScrollTop
            }, 800)()
        })
    })

</script>
<article class={!is_not_first? 'first on-scroll-up': 'on-scroll-up'}>
    <PreHeader onSelectFirstSlide={onSelectFirstSlide} onCloseNav={onCloseNav} />
    <svelte:component this={view} data={data} len={len} />
    <Footer onSelectFirstSlide={onSelectFirstSlide} />
</article>