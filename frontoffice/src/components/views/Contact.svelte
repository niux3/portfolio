<script>
    import {display} from "../../libs/store";
    import {onMount, onDestroy} from 'svelte'
    import {toVisible, toInvisible} from "../../libs/transition";
    onMount(()=>{
        toVisible();
    })

    onDestroy(()=>{
        toInvisible();
    })

</script>


{#if $display}
<section>
    <article>
        <div>me contacter</div>
    </article>
</section>
{/if}

<style lang="scss">
  section{
    overflow: auto;
    max-width: 1024px;
    width: 100%;
    height: 100%;
    margin: 0 auto;
    article{

      div{

      }
    }
  }
</style>
