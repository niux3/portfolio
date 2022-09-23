<script>
    import {createEventDispatcher} from 'svelte';

    let isClosedVisible = false;
    let dispatch = createEventDispatcher();
    let toggleClosedVisible = e =>{
        isClosedVisible = !isClosedVisible;
        dispatch('nav_visible', {
            get: isClosedVisible
        });
    }
</script>

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
    background: purple;
    border: none;
    border-radius: 50%;
    cursor: pointer;

    span{
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      left: 33%;
      background-color: red;
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
        background-color: red;
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
