<script>
    import {onMount} from 'svelte'
    import Contact from './Contact.svelte'
    import Loading from './Loading.svelte'


    let slide_status = 'form',
        getWindowProperties = ()=>{
            return {
                w: window.innerWidth,
                h: window.innerHeight
            }
        },
        position = {
            x : getWindowProperties().w * 1,
            y: 0
        },
        getCoord = ()=>{
            let {w, h} = getWindowProperties(),
                registry = {
                    'loading': {
                        x : w * 1,
                        y : h
                    },
                    'form': {
                        x: w * 1,
                        y: 0
                    },
                    'error': {
                        x: 0,
                        y: h
                    },
                    'success':{
                        x: w * 2,
                        y: h
                    }
                }
            return registry
        },
        resize = ()=>{
            carouselSize()
            let {w, h} = getWindowProperties()
            let coord = getCoord()
            position = coord['form']
        },
        carouselSize = () =>{
            let {w, h} = getWindowProperties(),
                $wrap = document.querySelector('.carousel-contact .wrap'),
                $fullscreens = $wrap.querySelectorAll('.fullscreen'),
                styles = [
                    `width: ${w}px`,
                    `height: ${h}px`,
                ]

            $wrap.style.width = `${w * $fullscreens.length }px`
            $fullscreens.forEach($el =>{
                $el.style = styles.join(';')
            })
        },
        onSlideStatus = e =>{
            let key_redirection = e.target.dataset.redirection,
                redirection = getCoord()[key_redirection]

            position.x = redirection.x
            position.y = redirection.y
        },
        hashchange = e =>{
            if(window.location.hash !== '#/contact'){
                position = getCoord()['form']
            }
        }

    onMount(()=>{
        carouselSize()
    })
</script>

<svelte:window on:hashchange={hashchange} on:resize={resize} />
<div class="carousel-contact">
    <div class="wrap-parent" style="margin-top: -{position.y}px;">
        <div class="fullscreen form">
                <button on:click={onSlideStatus} data-redirection="loading">go back</button>
            <Contact />
        </div>
        <div class="wrap" style="margin-left: -{position.x}px;">
            <div class="fullscreen error">
                <h1>error</h1>
                <button on:click={onSlideStatus} data-redirection="form">go back</button>
            </div>
            <div class="fullscreen loading">
                <Loading width="50" />
            </div>
            <div class="fullscreen success">
                <h1>success</h1>
                <button on:click={onSlideStatus} data-redirection="form">go back</button>
            </div>
        </div>
    </div>
</div>


<style lang="scss">
    .carousel-contact{
        overflow: hidden;
        .wrap-parent{
            transition: margin-top 400ms 400ms;
        }
        .fullscreen{
            padding: 2.5rem;
            overflow: auto;
        }

        .wrap{
            display: flex;
            flex-wrap: nowrap;
            transition: margin-left 400ms 400ms;
        }

        .success{
            background-color: teal;
        }

        .loading{
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .error{
            background-color: orangered;
        }


    }
</style>