<script>
    import BurgerButton from './BurgerButton.svelte';
    import Items from './Items.svelte';
    let isNavVisible = false;
    let nav_visible = e => isNavVisible = e.detail.get;
</script>
{isNavVisible}
<nav class="{isNavVisible ? 'isNavVisible' : ''}">
    <BurgerButton on:nav_visible={nav_visible}/>
    <Items content_visible={isNavVisible} />
</nav>

<style lang="scss">
  nav{
    position: fixed;
    left: 30px;
    top: 30px;
    z-index: 3;
    //background: red;
    padding-top: 60px;
    padding-bottom: 0;
    min-height: 60px;
    transition: padding-bottom 200ms;

    &:before{
      content:'';
      position: absolute;
      top: 30px;
      bottom: 30px;
      width: 60px;
      background-color: purple;
      transition: all 200ms;
    }
    &:after{
      content:'';
      position: absolute;
      z-index: -1;
      left: 0;
      bottom: 0;
      width: 60px;
      height: 60px;
      background-color: purple;
      border-radius: 50%;
    }

    &.isNavVisible{
      padding-bottom: 60px;
    }
  }
</style>
