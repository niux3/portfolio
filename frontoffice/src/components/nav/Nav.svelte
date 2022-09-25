<script>
    import {onMount} from 'svelte';
    import BurgerButton from './BurgerButton.svelte';
    import Items from './Items.svelte';

    let isNavVisible = false;
    let nav_visible = e => isNavVisible = e.detail.get;
    let current_view;
    onMount(()=>{
        current_view = window.location.hash;
        window.addEventListener('hashchange', e =>{
            console.log(">>", window.location.hash);
        })
    });
    let onNavClick = e =>{
        isNavVisible = e.detail.visible;
        current_view = e.detail.url;
        console.log('-> ', e.detail);
    }
</script>
<nav class="{isNavVisible ? 'isNavVisible' : ''}">
    <BurgerButton on:nav_visible={nav_visible} is_burger_display="{isNavVisible}"/>
    <Items content_visible={isNavVisible} current_view={current_view} on:nav_click={onNavClick} />
</nav>

<style lang="scss">
  nav{
    position: fixed;
    left: 30px;
    top: 30px;
    z-index: 3;
    padding-top: 30px;
    padding-bottom: 0;
    min-height: 60px;
    transition: padding-bottom 800ms;

    &:before{
      content:'';
      position: absolute;
      top: 30px;
      bottom: 30px;
      width: 60px;
      background-color: #0189c7;
      transition: all 800ms;
    }
    &:after{
      content:'';
      position: absolute;
      z-index: -1;
      left: 0;
      bottom: 0;
      width: 60px;
      height: 60px;
      background-color: #0189c7;
      border-radius: 50%;
    }

    &.isNavVisible{
      padding-bottom: 30px;
    }
  }
</style>
