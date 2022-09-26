<script>
    import {onMount, onDestroy} from 'svelte'

    onMount(()=>{
        console.log('about loaded')
    })

    onDestroy(()=>{
        console.log('about unloaded')
    })
</script>

<section>
    <article>
        <div>a propos de</div>
    </article>
</section>

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
