<script>
    import {onMount} from 'svelte'
    import Contact from './Contact.svelte'
    import Loading from './Loading.svelte'
    import OnSuccess from './OnSuccess.svelte'


    let dataForm = {},
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
                    'onLoading': {
                        x : w * 1,
                        y : h
                    },
                    'onForm': {
                        x: w * 1,
                        y: 0
                    },
                    'onError': {
                        x: 0,
                        y: h
                    },
                    'onSuccess':{
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
            position = coord['onForm']
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
        onSlideStatus = key_redirection =>{
            let redirection = getCoord()[key_redirection]

            position.x = redirection.x
            position.y = redirection.y
        },
        hashchange = e =>{
            if(window.location.hash !== '#/contact'){
                position = getCoord()['onForm']
            }
        },
        onChange = e => dataForm[e.target.name] = e.target.value

    onMount(()=>{
        carouselSize()
    })
</script>

<svelte:window on:hashchange={hashchange} on:resize={resize} />
<div class="carousel-contact">
    <div class="wrap-parent" style="margin-top: -{position.y}px;">
        <div class="fullscreen form">
            <Contact {onSlideStatus} bind:dataForm />
        </div>
        <div class="wrap" style="margin-left: -{position.x}px;">
            <div class="fullscreen error">
                <h1>error</h1>
            </div>
            <div class="fullscreen loading">
                <Loading width="50" />
            </div>
            <div class="fullscreen success">
                <OnSuccess {dataForm} />
            </div>
        </div>
    </div>
</div>


<style lang="scss">
    .carousel-contact{
        overflow: hidden;
        .wrap-parent{
            transition: margin-top 400ms 400ms cubic-bezier(0.770, 0.000, 0.175, 1.000);
        }
        .fullscreen{
            padding: 2.5rem;
            overflow: auto;
        }

        .wrap{
            display: flex;
            flex-wrap: nowrap;
            transition: margin-left 400ms 400ms cubic-bezier(0.770, 0.000, 0.175, 1.000);
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