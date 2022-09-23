<script>
    import {onMount} from 'svelte';
    export let content_visible;
    let data = {
        'accueil': 'iconHome',
        'à propos de moi': 'iconAbout',
        'portfolio': 'iconBook',
        'me contacter': 'iconContact',
    }
    let height_items = 0;
    onMount(()=>{
        height_items = document.querySelector('header nav ul').getBoundingClientRect().height
    })
</script>
<ul class="{content_visible? '' : 'isNotVisible'}">
    {#each Object.entries(data) as [category, icon], i}
    <li>{category}</li>
    {/each}
</ul>

<style lang="scss">
  ul{
    overflow: hidden;
    position: relative;
    margin: 0;
    max-height: 300px;
    transition: max-height 200ms;

    &.isNotVisible{
      max-height: 0;
    }

    li{
      padding: 15px 0;
    ;
    }
  }
</style>