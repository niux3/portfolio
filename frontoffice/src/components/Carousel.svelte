<script>
    import {onMount} from 'svelte'
    import {debounce} from '../helpers'


    export let index


    let getWindowProperties = ()=>{
        return {
            w: window.innerWidth,
            h: window.innerHeight
        }
    }
    let carouselSize = ()=>{
        let {w, h} = getWindowProperties(),
            styles = [
                `width: ${w}px`,
                `height: ${h}px`,
            ],
            $wrap = document.querySelector('.carousel .wrap'),
            $fullscreenWrapped = $wrap.querySelectorAll('.fullscreen')
        $wrap.style.width = `${w * $fullscreenWrapped.length }px`
        document.querySelectorAll('.fullscreen').forEach($el =>{
            $el.style = styles.join(';')
        })
    }


    let routes = []
    onMount(()=>{
        carouselSize()
        document.querySelectorAll('nav a').forEach(($a, i) =>{
            routes.push($a.getAttribute('href'))
            if(i === 0 && window.location.hash === ''){
                $a.click()
            }
        })
    })

    let resize = e =>{
        carouselSize()
        
        debounce(() => {
            document.querySelector(`nav a`).click()
        }, 200)()
    }
    let hashchange = e =>{
        // console.log(window.location.hash, routes)
        let hash = window.location.hash
        if(hash === document.querySelector('nav a:last-child').getAttribute('href')){
            document.querySelector('.carousel').style.transform = `translateY(-${getWindowProperties().h}px)`
        }else{
            index = routes.indexOf(window.location.hash)
            let sleep = 0
            if(!/translateY\(0(px)?\)/.test(document.querySelector('.carousel').style.transform)){
                document.querySelector('.carousel').style.transform = `translateY(0)`
                let transitionDuration = window.getComputedStyle(document.querySelector('.carousel')).getPropertyValue('transition-duration')
                sleep = transitionDuration.includes('.')? parseFloat(transitionDuration) * 1000 : parseInt(transitionDuration, 10)
            }
            let animTransition = setTimeout(()=>{
                document.querySelector('.wrap').style.transform = `translateX(-${index * getWindowProperties().w}px)`
                clearTimeout(animTransition)
            }, sleep)
        }
    }
</script>

<svelte:window  on:hashchange={hashchange} on:resize={resize} />
<div class="carousel fullscreen">
    <div class="wrap">
        <div class="fullscreen about">à propos de</div>
        <div class="fullscreen projects">home project</div>
        <div class="fullscreen project">project</div>
    </div>
    <div class="fullscreen contact">contact</div>
</div>


<style lang="scss">
    .carousel{
        overflow: hidden;
        transition: transform 400ms cubic-bezier(0.770, 0.000, 0.175, 1.000);

        .wrap{
            display: flex;
            flex-wrap: nowrap;
            transition: transform 400ms cubic-bezier(0.770, 0.000, 0.175, 1.000);
        }

        .about{
            background-color: orangered;
        }

        .projects{
            background-color: tan;
        }

        .project{
            background-color: tomato;
        }

        .contact{
            background-color: tan;
        }
    }
</style>