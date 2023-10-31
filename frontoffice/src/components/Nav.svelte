<script>
    import {onMount} from 'svelte'
    
    
    let hash = null
    let onHashChange = e => {
            hash = window.location.hash
            let $as = Array.from(document.querySelectorAll('nav a')),
                hrefs = []
            $as.map($a => hrefs.push($a.href))
            if(hrefs.every(href => href !== hash)){
                hash = $as[1].href
            }


        },
        onLoad = e => {
            hash = window.location.hash
            let selector = hash === ''? 'nav a' : `nav a[href="${hash}"]`
            if(document.querySelector(selector) === null){
                selector = 'nav a[href="#/projets"]'
            }
            document.querySelector(selector).classList.add('current')
        }
    
    onMount(()=>{
        let $as = document.querySelectorAll('nav a')
        for(let i = 0; i < $as.length; i++){
            let $a = $as[i]
            $a.addEventListener('pointerdown', e=>{
                Array.from($as).map($el => $el.classList.remove('current'))
                $a.classList.add('current')

            })
        }
        document.querySelector('.logo').addEventListener('pointerdown', e =>{
            Array.from($as).map($el => $el.classList.remove('current'))
            $as[0].classList.add('current')
        })

        let animNav = setTimeout(()=>{
            document.querySelector('.wrap-nav').classList.add('anim')
            clearTimeout(animNav)
        }, window.location.hash !== '' ? 800 : 3500);

        document.querySelector('.burger-button').addEventListener('click', e =>{
            let $wrap = document.querySelector('.wrap-nav'),
                method = $wrap.classList.contains('open')? 'remove' : 'add'
            $wrap.classList[method]('open')
        })

    })
</script>
<svelte:window on:hashchange={onHashChange} on:load={onLoad} />
<div class="wrap-nav">
    <a href="/" class="logo">
        <img src="logo.svg" alt="" class="event-cursor">
    </a>
    <button class="burger-button">
        <div class="bar1"></div>
        <div class="bar2"></div>
        <div class="bar3"></div>
    </button>
    <nav>
        <a href="#/a-propos-de-moi" class="event-cursor {hash === '#/a-propos-de-moi'? 'current' : ''}">à propos de</a>
        <a href="#/projets" class="event-cursor {hash === '#/projets'? 'current' : ''}">réalisations</a>
        <!-- <a href="#/projet">réalisation</a> -->
        <a href="#/contact" class="event-cursor {hash === '#/contact'? 'current' : ''}">contact</a>
    </nav>
</div>
