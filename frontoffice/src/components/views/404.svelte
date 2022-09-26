<script>
    import {onMount, onDestroy} from 'svelte'

    onMount(()=>{
        console.log('404 loaded')
    })

    onDestroy(()=>{
        let end = setTimeout(()=>{

            console.log('404 unloaded')
            clearTimeout(end)
        }, 2000)
    })
</script>

<section>
    <article>
        <div>404</div>
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
