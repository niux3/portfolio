<script>
    import {onMount} from 'svelte'
    import Carousel from "../libs/carousel_project/Carousel";
    import Utils from "../libs/utils/Utils";

    export let data

    let len_data = data.length
    let data_reverse = [...data].reverse()
    let data_minus_one = [...data].reverse().slice(0, -1)
    let data_changed = data_reverse.concat(data_reverse, data_reverse, data_minus_one, data, data, data, data)
    
    let positionCarousel = () =>{
        let w = window.innerWidth,
            h = window.innerHeight

        document.querySelector('.carousel-project').style = [
            `width:${w}px`, 
            `height:${h}px`, 
            `top:0`, 
            `left:${w}px`, 
            `right:${w}px`, 
            `bottom:${h}px`, 
        ].join(';')
    }
    let onResize = e =>{
        Utils.debounce(positionCarousel, 200)()
    }
    onMount(()=>{
        positionCarousel()
        let carousel = new Carousel()

        carousel.onLoad()
        carousel.onResize(Utils)
        carousel.onWheel(Utils)

        let $lisTitle = Array.from(document.querySelectorAll('.projects.title li')),
            $lisIllus = Array.from(document.querySelectorAll('.projects.illustrations li')),
            searchCurrent = setTimeout(()=>{
                let $liIllusCurrent = document.querySelector('.projects.illustrations .current'),
                    indexIllusCurrent = $lisIllus.indexOf($liIllusCurrent),
                    $lisIllusParts = [...$lisIllus].slice(indexIllusCurrent - 3, indexIllusCurrent + 3)
                $lisIllusParts.map($el => $el.classList.add('anim'))
                console.log('>>> ', $liIllusCurrent);
                console.log('>>> ', $lisIllusParts);
            

            }, 600)
        // window.addEventListener('hashchange', e =>{
        //     if(window.location.hash === '#/projets'){
        //     console.log(carousel.getIndex())
        //         let i = 0,
        //             animInterval = setInterval(()=>{
        //                 $lisTitle[i].classList.add('anim')
        //                 $lisIllus[i].classList.add('anim')
                        
        //                 i += 1
        //                 if(i >= $lisTitle.length){
        //                     clearInterval(animInterval);
        //                 }
        //             }, 5)
        //     }else{
        //         let animRemoveClass = setTimeout(()=>{
        //             $lisTitle.map($el => $el.classList.remove('anim'))
        //             $lisIllus.map($el => $el.classList.remove('anim'))
        //             clearTimeout(animRemoveClass)
        //         }, 800)
        //     }
        // })

    })
    
</script>
<svelte:window on:resize={onResize} />
<div id="home" class="carousel-project" data-len="{ len_data }">
    <div class="projects title">
        <div class="wrap">
            <ul>
                {#each data_changed as row}
                <li>
                    <h2><a href={`#/${row.slug}`} class="event-cursor">{ row.name }</a></h2>
                </li>
                {/each}
            </ul>
        </div>
    </div>
    <div class="projects illustrations">
        <div class="wrap">
            <ul>
                {#each data_changed as row}
                <li>
                    <a href={`#/${row.slug}`}>
                      <span class="event-cursor"></span>
                      <img src="./mask.gif" alt="" width="800" height="400">
                      <!-- <img src="https://fakeimg.pl/800x400/?text={ row.slug }" alt="" class="project-illustration" width="800"> -->
                      <img src={row.images.find(img => /\d+--1/.test(img)) !== undefined?row.images.find(img => /\d+--1/.test(img)) : ''} loading="lazy" alt={row.name} class="project-illustration">
                    </a>
                </li>
                {/each}
            </ul>
        </div>
    </div>
</div>

<style lang="scss">
    /*
#home{
  display: grid;
  grid-template-columns: 50% 50%;
  grid-template-rows: 100%;
  height: 100%;
//   position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;

  &.onFixed{
    position: fixed;
  }

  hr{
    position: fixed;
    top: 50%;
    left: 0;
    right: 0;
    z-index: 10;
    border: 1px solid red;
  }

  > .projects{
    position: relative;
    height: 100%;
    .wrap{
      position: absolute;
      top: 50%;
      bottom: 0;
      right: 44px;
      left: 44px;
      ul{
        transition: transform 200ms;
        list-style: none;
        margin: 0;
        padding: 0;
      }
    }

    &.title{
      &:before{
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        //bottom: 53%;
        left: 0;
        z-index: 2;
        // background-color: map-get($colors, black12);
        //background-color: red;
        // opacity: .0;
      }

      &:after{
        content: '';
        position: absolute;
        //top: 53%;
        right: 0;
        bottom: 0;
        left: 0;
        // background-color: map-get($colors, black12);
        //background-color: blue;
        z-index: 2;
        opacity: .9;
        // opacity: .0;
      }


      ul{
        li{
          margin: 0;
          h2{
            font-size: 3.9vw;
            line-height: 4.94vw;
            margin: 0;
            font-family: 'boldcondensed', sans-serif;
          }
        }
      }
    }

    &.illustrations{
      ul{
        li{
          display: flex;
          justify-content: right;
          margin-bottom: 0;
          img{
            margin-bottom: 30px;
            display: block;
            width: 90%;
          }
        }
      }
    }
  }
}
*/
</style>
