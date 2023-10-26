<script>
    import {onMount} from 'svelte'
    import Carousel from "./components/Carousel.svelte"
    import Nav from "./components/Nav.svelte"
    import Preload from "./components/Preload.svelte"
    import Cursor from './libs/cursor/Cursor'


    let index = 0

    onMount(()=>{
        if (!/Android|iPhone/i.test(navigator.userAgent)) {
            document.querySelector('html').classList.add('desktop')
            let cursor = new Cursor()
            cursor.event()
        }

        let slides = Array.from(document.querySelectorAll('#about, #home, #contact, #projet'))
        let animSlide = (sleep)=>{
            let registryAnim = {
                '#about' : '#/a-propos-de-moi',
                '#home': '#/projets',
                '#contact' : '#/contact',
                '#projet': '#/'
            }
            let sleepTimeout = setTimeout(()=>{
                let index = Object.values(registryAnim).indexOf(window.location.hash),
                    registryHash = Object.keys(registryAnim)
                index = index !== -1 ? index : registryHash.length - 1
                
                Array.from(document.querySelectorAll(registryHash.join(','))).map($el => $el.parentNode.scrollTop = 0)
                document.querySelector(registryHash[index]).classList.add('anim')
                clearTimeout(sleepTimeout)
            }, sleep)
        }

        let isDoAnim = window.location.hash === ''
        let $logoAnim = document.querySelector('.wrap-logo-anim')
        if(isDoAnim){
            let removeClassSlide = setTimeout(()=>{
                    slides.map(s => s.classList.remove('anim'))
                    clearTimeout(removeClassSlide)
                }, 400),
                animLogo = setTimeout(()=>{
                    document.querySelector('nav a').click()
                    $logoAnim.remove()
                    animSlide(200)
                    clearTimeout(animLogo)
                }, 3500)
        }else{
            $logoAnim.remove()
            animSlide(1000)
        }

        window.addEventListener('hashchange', e =>{
            slides.map(s => s.classList.remove('anim'))
            animSlide(window.location.hash === '' ? 3800 : 100)
        })
        /* shoot pub */
        if(document.querySelectorAll('a[href*="000webhost"]').length){
            document.querySelector('a[href*="000webhost"]').closest('div').remove()
        }
    })
</script>

<Preload />
<main style="overflow: hidden;">
    <Nav />
    <Carousel {index}></Carousel>
</main>