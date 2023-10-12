<script>
    import {onMount} from 'svelte'
    
    
    let hash = window.location.hash
    
    onMount(()=>{
        let $as = document.querySelectorAll('nav a')

        $as.forEach( $a =>{
            $a.addEventListener('pointerdown', e=>{
                Array.from($as).map($el => $el.classList.remove('current'))
                $a.classList.add('current')
            })
        })
    })
</script>
<nav>
    <a href="#/a-propos-de-moi" class="event-cursor {hash === '#/a-propos-de-moi'? 'current' : ''}">à propos de moi</a>
    <a href="#/projets" class="event-cursor {hash === '#/projets'? 'current' : ''}">réalisations</a>
    <!-- <a href="#/projet">réalisation</a> -->
    <a href="#/contact" class="event-cursor {hash === '#/contact'? 'current' : ''}">contact</a>
</nav>


<style lang="scss">
    nav{
        position: fixed;
        top: 25px;right: 0;left: 0;
        z-index: 1000;
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
</style>
