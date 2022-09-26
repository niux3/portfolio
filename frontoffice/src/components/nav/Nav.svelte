<script>
    import {createEventDispatcher} from 'svelte';
    import BurgerButton from './BurgerButton.svelte';
    import Items from './Items.svelte';

    export let current_view;

    let isNavVisible = false;
    let nav_visible = e => isNavVisible = e.detail.get;
    let dispatch = createEventDispatcher()

    let onNavClick = e =>{
        isNavVisible = e.detail.visible;
        current_view = e.detail.url;
        dispatch('nav_click', {
            current_view
        })
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
