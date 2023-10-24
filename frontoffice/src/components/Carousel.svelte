<script>
    import {onMount} from 'svelte'
    import Utils from '../libs/utils/Utils'
    import About from './About.svelte'
    import CarouselContact from './CarouselContact.svelte'
    import Projects from './Projects.svelte'
    import Project from './Project.svelte'
    import data from '../data'


    export let index

    let row = data[0],
        rowindex = 1

    let getWindowProperties = ()=>{
            return {
                w: window.innerWidth,
                h: window.innerHeight
            }
        },
        carouselSize = ()=>{
            let {w, h} = getWindowProperties(),
                styles = [
                    `width: ${w}px`,
                    `height: ${h}px`,
                ],
                $wrap = document.querySelector('.carousel .wrap'),
                $fullscreens = $wrap.querySelectorAll('.fullscreen')

            $wrap.style.width = `${w * $fullscreens.length }px`
            document.querySelectorAll('.fullscreen').forEach($el =>{
                $el.style = styles.join(';')
            })
        }


    let routes = []
    onMount(()=>{

        // preload ??
        /*
        let $images = document.querySelectorAll('#home .project-illustration'),
            lenImgs = $images.length
        for(let i = 0; i < lenImgs; i++){
            let img = new Image()
            img.src = $images[i].src

            img.addEventListener('load', e =>{
                let percent = (i + 1) * 100 / lenImgs
                if(i >= lenImgs - 1){
                    console.log('100');

                }
                    console.log(percent)
            })
        }
        */

        carouselSize()
        document.querySelectorAll('nav a').forEach(($a, i) =>{
            routes.push($a.getAttribute('href'))
            if(i === 0 && window.location.hash === ''){
                $a.click()
            }
        })
        for(let row of data){
            routes.push(`#/${row.slug}`)
        }

        if(window.location.hash !== ''){
            hashchange(null) // pas de var event !
        }
    })

    let resize = e =>{
        carouselSize()
        
        Utils.debounce(() => {
            document.querySelector(`nav a`).click()
        }, 200)()
    }
    let hashchange = e =>{
        // console.log(window.location.hash, routes)
        let hash = window.location.hash

        if(hash === document.querySelector('nav a:last-child').getAttribute('href')){
            document.querySelector('.carousel').style.transform = `translateY(-${getWindowProperties().h}px)`
        }else{
            index = routes.indexOf(window.location.hash) > 2 ? 2 : routes.indexOf(window.location.hash)
            if(index >= 2){
                row = data.find(r => r.slug === hash.substring(2))
                rowindex = data.indexOf(row) + 1
            }
            if(index === 1){
                document.querySelector('.wrap').addEventListener('transitionend', e =>{
                    document.querySelector('#home').classList.add('onFixed')
                })
            }

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
        <div class="fullscreen about">
            <About />
        </div>
        <div class="fullscreen projects">
            <Projects {data} />
        </div>
        <div class="fullscreen project">
            <Project {row} len={data.length} index={rowindex} />
        </div>
    </div>
    <div class="contact">
        <CarouselContact />
    </div>
</div>


<style lang="scss">
    .carousel{
        /*overflow: hidden;*/
        transition: transform 400ms cubic-bezier(0.770, 0.000, 0.175, 1.000);

        .fullscreen{
            overflow: auto;
            padding: 2.5rem;
        }

        .wrap{
            display: flex;
            flex-wrap: nowrap;
            transition: transform 400ms cubic-bezier(0.770, 0.000, 0.175, 1.000);
        }

        .about{
            // background-color: orangered;
        }

        .projects{
            // background-color: tan;
        }

        .project{
            // background-color: tomato;
        }

        .contact{
            /*background-color: tan;*/
        }
    }
</style>
