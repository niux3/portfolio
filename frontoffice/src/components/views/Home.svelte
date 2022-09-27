<script>
    import {display} from "../../libs/store";
    import {onMount, onDestroy} from 'svelte'
    import {toVisible, toInvisible} from "../../libs/transition";

    let innerWidth = window.innerWidth;
    let innerHeight = window.innerHeight;
    let year = parseInt(new Date().getFullYear(), 10) - 2009;
    onMount(()=>{
        toVisible();
    })

    onDestroy(()=>{
        toInvisible();
    })

</script>

<svelte:window bind:innerWidth bind:innerHeight />
{#if $display}
<section>
    <article>
        <div style="height: {innerHeight - 60}px">
            <div>
                <h1>Web développeur frontend et backend à Paris</h1>
                <p>Bonjour, ancien infographiste, je suis désormais un professionnel dans le web. Mon expertise se situe principalement dans les technologies du web où j'excelle avec aisance dans le monde professionnel depuis {year} ans. À mon actif, j'ai plus de 50 beaux projets et j'ai été récompensé 5 fois. </p>
                <button></button>
            </div>
        </div>
        <div style="height: {innerHeight - 60}px">
            hello
        </div>
    </article>
</section>
{/if}

<style lang="scss">
  section{
    overflow: auto;
    width: 100%;
;
    article{

      > div{
        &:first-of-type{
          display: flex;
          justify-content: center;
          align-items: flex-end;
          flex-direction: column;
          margin-left: 59%;

          > div{
            text-align: left;
            margin-right: 14%;

            h1{
              font-size: 75px;
              font-weight: 200;
              margin-bottom: 15px;
              line-height: 75px;
            }

          }
        }
      }
    }
  }
</style>
