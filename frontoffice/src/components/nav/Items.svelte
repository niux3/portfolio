<script>
    import {onMount} from 'svelte';
    export let content_visible;
    export let current_view;

    let data = {
        'accueil': {
            'icon': '<path d="M575.8 255.5c0 18-15 32.1-32 32.1h-32l.7 160.2c0 2.7-.2 5.4-.5 8.1V472c0 22.1-17.9 40-40 40H456c-1.1 0-2.2 0-3.3-.1c-1.4 .1-2.8 .1-4.2 .1H416 392c-22.1 0-40-17.9-40-40V448 384c0-17.7-14.3-32-32-32H256c-17.7 0-32 14.3-32 32v64 24c0 22.1-17.9 40-40 40H160 128.1c-1.5 0-3-.1-4.5-.2c-1.2 .1-2.4 .2-3.6 .2H104c-22.1 0-40-17.9-40-40V360c0-.9 0-1.9 .1-2.8V287.6H32c-18 0-32-14-32-32.1c0-9 3-17 10-24L266.4 8c7-7 15-8 22-8s15 2 21 7L564.8 231.5c8 7 12 15 11 24z"/>',
            'size': 576,
            'slug': 'accueil',
        },
        'à propos de moi': {
            'icon': '<path d="M208 256c35.35 0 64-28.65 64-64c0-35.35-28.65-64-64-64s-64 28.65-64 64C144 227.3 172.7 256 208 256zM464 232h-96c-13.25 0-24 10.75-24 24s10.75 24 24 24h96c13.25 0 24-10.75 24-24S477.3 232 464 232zM240 288h-64C131.8 288 96 323.8 96 368C96 376.8 103.2 384 112 384h192c8.836 0 16-7.164 16-16C320 323.8 284.2 288 240 288zM464 152h-96c-13.25 0-24 10.75-24 24s10.75 24 24 24h96c13.25 0 24-10.75 24-24S477.3 152 464 152zM512 32H64C28.65 32 0 60.65 0 96v320c0 35.35 28.65 64 64 64h448c35.35 0 64-28.65 64-64V96C576 60.65 547.3 32 512 32zM528 416c0 8.822-7.178 16-16 16H64c-8.822 0-16-7.178-16-16V96c0-8.822 7.178-16 16-16h448c8.822 0 16 7.178 16 16V416z"/>',
            'size': 576,
            'slug': 'a-propos-de-moi',
        },
        'portfolio': {
            'icon': '<path d="M176 56V96H336V56c0-4.4-3.6-8-8-8H184c-4.4 0-8 3.6-8 8zM128 96V56c0-30.9 25.1-56 56-56H328c30.9 0 56 25.1 56 56V96v32V480H128V128 96zM64 96H96V480H64c-35.3 0-64-28.7-64-64V160c0-35.3 28.7-64 64-64zM448 480H416V96h32c35.3 0 64 28.7 64 64V416c0 35.3-28.7 64-64 64z"/>',
            'size': 512,
            'slug': 'portfolio',
        },
        'me contacter': {
            'icon': '<path d="M48 64C21.5 64 0 85.5 0 112c0 15.1 7.1 29.3 19.2 38.4L236.8 313.6c11.4 8.5 27 8.5 38.4 0L492.8 150.4c12.1-9.1 19.2-23.3 19.2-38.4c0-26.5-21.5-48-48-48H48zM0 176V384c0 35.3 28.7 64 64 64H448c35.3 0 64-28.7 64-64V176L294.4 339.2c-22.8 17.1-54 17.1-76.8 0L0 176z"/>',
            'size': 512,
            'slug': 'me-contacter',
        },
    }

    onMount(()=>{
        let len_item = Object.keys(data).length,
            output = '';
        for(let i = 1; i <= len_item; i++){
            let str = `
                header .isNavVisible .visible li:nth-child(${i}) svg{
                    animation-delay: ${i === 1? 0 : i * 75}ms;
                }
            `;
            output += str;
        }
        document.querySelector('head').insertAdjacentHTML('beforeend', `<style>${output}</style>`);

    })
</script>
<ul class="{content_visible? 'visible' : 'isNotVisible'}">
    {#each Object.entries(data) as [key, value], i}
    <li>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {value.size} 512">{@html value.icon}</svg>
        <a href="#/{value.slug}">
            <span>{key.toUpperCase()}</span>
        </a>
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
      position: relative;
      cursor: pointer;
      svg{
        width: 16px;
        display: block;
        position: absolute;
        left: 22px;
        top: 50%;
        transform: scale(1) translateY(-50%);
        fill:white;
        opacity: 0;
      }
      a{
        display: block;
        opacity: 0;
        padding: 15px 0 16px 75px;
        color: #88878c;
        transition: color 400ms;
        line-break: 0;

        &:before{
          content:"";
        }

        &:hover{
          color: #0189c7;
          text-decoration: none;
        }
      }
    }

    &.isNotVisible{
      max-height: 0;
      visibility: hidden;

      li{
        a{
        }
      }
    }
    &.visible{
      li{
        svg{
          animation-name: svg;
          animation-duration: 400ms;
          animation-fill-mode: forwards;
          pointer-events: none;
        }
        a{
          padding-left: 95px;
          opacity: 0;
          transition: opacity 400ms, padding-left 400ms;
        }
        &:hover {
          a {
            opacity: 1;
            padding-left: 75px;
          }
        }
      }
    }

  }
  @keyframes svg {
    0%{
      opacity: 0;
      transform: scale(1) translateY(-50%);
    }
    75%{
      opacity: .1;
      transform: scale(1.5) translateY(-50%);
    }
    100%{
      transform: scale(1) translateY(-50%);
      opacity: 1;
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