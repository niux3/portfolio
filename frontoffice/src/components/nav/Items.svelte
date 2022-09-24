<script>
    import {onMount} from 'svelte';
    export let content_visible;
    let data = {
        'accueil': {
            'icon': 'iconHome',
            'slug': 'accueil',
        },
        'à propos de moi': {
            'icon': 'iconAbout',
            'slug': 'a-propos-de-moi',
        },
        'portfolio': {
            'icon': 'iconBook',
            'slug': 'portfolio',
        },
        'me contacter': {
            'icon': 'iconContact',
            'slug': 'me-contacter',
        },
    }

    onMount(()=>{
        let len_item = Object.keys(data).length,
            output = '';
        for(let i = 1; i <= len_item; i++){
            let str = `
                header .isNavVisible .visible li:nth-child(${i}) a{
                    animation-delay: ${i === 1? 0 : i * 75}ms;
                }
            `;
            output += str;
        }
        document.querySelector('head').insertAdjacentHTML('beforeend', `<style>${output}</style>`)

    })
</script>
<ul class="{content_visible? 'visible' : 'isNotVisible'}">
    {#each Object.entries(data) as [key, value], i}
    <li>
        <a href="#/{value.slug}">{key.toUpperCase()}</a>
    </li>
    {/each}
</ul>

<style lang="scss">
  ul{
    overflow: hidden;
    position: relative;
    margin: 10px 0 0 0;
    padding: 0;
    list-style: none;
    max-height: 300px;
    visibility: visible;
    transition: max-height 800ms;

    li{
      //transition: opacity 800ms;
      a{
        display: block;
        padding: 15px 0 16px 75px;
        font-weight: 600;
      }
    }

    &.isNotVisible{
      max-height: 0;
      visibility: hidden;

      li{
        //opacity: 0;

        a{
        }
      }
    }
    &.visible{
      li{
        //opacity: 1;

        a{
          opacity: 0;
          transform: scale(0);
          animation-name: link;
          animation-duration: 400ms;
          animation-fill-mode: forwards;
          //animation-delay: 2000ms;
        }
      }
    }

  }

  @keyframes link {
    0%{
      opacity: 0;
      transform: scale(0);
      padding-left: 15px;
    }
    75%{
      opacity: 0;
      transform: scale(1.2);
      padding-left: 90px;
    }
    100%{
      transform: scale(1);
      opacity: 1;
      padding-left: 75px;
    }

  }
</style>