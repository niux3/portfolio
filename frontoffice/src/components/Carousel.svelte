<script>
    import {onMount} from 'svelte'
    import {debounce} from '../helpers'
    import About from './About.svelte'
    import CarouselContact from './CarouselContact.svelte'
    import Projects from './Projects.svelte'
    import Project from './Project.svelte'


    export let index


    let data = [
        {
            id: 1,
            name: "Renaud",
            slug: "renaud"
        },
        {
            id: 2,
            name: "Denis",
            slug: "denise"
        },
    ];

    let row = {}


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
        console.log("routes >>", routes)
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
        row = data.find(r => r.slug === hash.substring(2))

        if(hash === document.querySelector('nav a:last-child').getAttribute('href')){
            document.querySelector('.carousel').style.transform = `translateY(-${getWindowProperties().h}px)`
        }else{
            index = routes.indexOf(window.location.hash) > 2 ? 2 : routes.indexOf(window.location.hash)
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
            <Project {row} />
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
            background-color: tomato;
        }

        .contact{
            /*background-color: tan;*/
        }
    }
</style>
