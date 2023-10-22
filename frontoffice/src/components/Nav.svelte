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
            console.log(document.querySelector(selector));
            document.querySelector(selector).classList.add('current')
        }
    
    onMount(()=>{
        let $as = document.querySelectorAll('nav a')

        $as.forEach( $a =>{
            $a.addEventListener('pointerdown', e=>{
                Array.from($as).map($el => $el.classList.remove('current'))
                $a.classList.add('current')
            })
        })
        document.querySelector('.logo').addEventListener('pointerdown', e =>{
            Array.from($as).map($el => $el.classList.remove('current'))
            $as[0].classList.add('current')
        })

        let animNav = setTimeout(()=>{
            document.querySelector('.wrap-nav').classList.add('anim')
            clearTimeout(animNav)
        }, window.location.hash !== '' ? 800 : 3500);

    })
</script>
<svelte:window on:hashchange={onHashChange} on:load={onLoad} />
<div class="wrap-nav">
    <a href="#/a-propos-de-moi" class="logo">
        <img src="logo.svg" alt="" class="event-cursor">
    </a>
    <nav>
        <a href="#/a-propos-de-moi" class="event-cursor {hash === '#/a-propos-de-moi'? 'current' : ''}">à propos de moi</a>
        <a href="#/projets" class="event-cursor {hash === '#/projets'? 'current' : ''}">réalisations</a>
        <!-- <a href="#/projet">réalisation</a> -->
        <a href="#/contact" class="event-cursor {hash === '#/contact'? 'current' : ''}">contact</a>
    </nav>
</div>

<style lang="scss">
    .wrap-nav {
        display: flex;
        align-items: center;
        position: fixed;
        top: 25px;right: 0;left: 25px;
        z-index: 1000;

        .logo{
            display: block;
            left: 10px;
            top: 10px;
            z-index: 50;

            img{
                width: 3vw;
                height: 3vw;
                display: block;

            }
        }
        nav{
            display: flex;

            a{
                padding: 10px 20px;
                margin: 0 15px;
                position: relative;
                z-index: 1;
                display: block;
                color: #444;
                text-decoration: none;
                text-transform: uppercase;
                display: flex;
                align-items: center;

                &:before{
                    content: '\25AA';
                    margin-right: 10px;
                    font-size: 32px;
                    line-height: 0;
                    opacity: 0;
                    transition: opacity 400ms;
                }

                &:hover, &.current{
                    &::before{
                        opacity: 1;
                    }
                }
            }
        }
    }
</style>
