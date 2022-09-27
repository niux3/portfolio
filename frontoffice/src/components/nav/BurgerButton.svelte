<script>
    import {debug} from "../../libs/store";
    import {createEventDispatcher} from 'svelte';
    export let is_burger_display;
    $: isClosedVisible = is_burger_display;
    let dispatch = createEventDispatcher();
    let toggleClosedVisible = e =>{
        isClosedVisible = !isClosedVisible;
        dispatch('nav_visible', {
            get: isClosedVisible
        });
    }
</script>
{#if $debug}
    <p style="position: fixed; right: 50px; top: 50px;">{is_burger_display}</p>
{/if}
<button class="burger {isClosedVisible ? 'isClosedVisible' : ''}" on:click={toggleClosedVisible}>
    <span></span>
</button>

<style lang="scss">
  :root{
    --pos:0%
  }
  .burger{
    position: absolute;
    left: 0;
    top: 0;
    width: 60px;
    height: 60px;
    background: #0189c7;
    border: none;
    border-radius: 50%;
    cursor: pointer;

    span{
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      left: 33%;
      background-color: white;
      width: 33%;
      height: 2px;
      transition: background-color 200ms;


      &:before,
      &:after{
        position: absolute;
        left: 0;
        content: '';
        width: 100%;
        height: 2px;
        background-color: white;
      }

      &:before{
        top: -6px;
        transition: top 200ms, transform 200ms;
      }

      &:after{
        bottom: -6px;
        transition: bottom 200ms, transform 200ms;
      }
    }

    &.isClosedVisible{
      span{
        background-color: transparent;
        &:before{
          transform: rotate(45deg);
          top: var(--pos);
        }

        &:after{
          transform: rotate(-45deg);
          bottom: var(--pos);
        }
      }
    }
  }
</style>
