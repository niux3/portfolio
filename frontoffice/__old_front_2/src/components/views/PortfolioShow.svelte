<script>
    import {display, current_view} from "../../libs/store";
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
        <header>
            <div class="description">
                <p class="counter">1 - 50</p>
                <h1 class="name">John Paul</h1>
                <div class="wrap">
                    <div class="cartouche">
                        <dl>
                            <dt>Type</dt>
                            <dd>
                                <span>backend</span>
                            </dd>
                        </dl>
                        <dl>
                            <dt>description</dt>
                            <dd>
                                <span>conciergerie</span>
                            </dd>
                        </dl>
                        <dl>
                            <dt>année</dt>
                            <dd>
                                <span>2022</span>
                            </dd>
                        </dl>
                    </div>
                    <ul>
                        <li>Python 3</li>
                        <li>Django 3</li>
                        <li>PostgreSQL</li>
                    </ul>
                </div>
            </div>
        </header>
<!--        <div class="picture"><img src="./img/john-paul-2.webp" alt="" /></div>-->
        <div class="content">
            <div class="url"></div>

        </div>
    </article>
</section>
{/if}

<style lang="scss">
  section{

    article{

      header{
        margin-top: 21.5em;
        h1{
          max-width: 35vw;
          margin-top: 0.8rem;
          margin-bottom: 1rem;
          font-size: 4.4em;
          line-height: 1;
          font-weight: 400;
        }
        .wrap{
          display: flex;
          justify-content: space-between;
          .cartouche{
            display: flex;
            dl{
              margin: 0;
              &:nth-child(2){
                max-width: 10em;
                margin: 0 3rem;
              }
              dt{
                text-transform: uppercase;
              }
              dd{
                margin-left: 0;
              }
            }
          }
          ul{
            margin: 0;
            padding: 0;
            list-style: none;
            display: flex;

            li{
              margin: 0 16px;
              min-width: 120px;
              padding: 0.7em 2em;
              border: 1px solid #f8f8f8;
              border-radius: 100vw;
              font-size: .875em;
              font-weight: 400;
              text-align: center;
              text-transform: uppercase;
              border-color: #1d1d1d;
            }
          }
        }
      }
      .picture{
        max-width: 1790px;
        max-height: 1115px;
        margin-top: 4em;

        img{
          width: 100%;
          object-fit: cover;
        }
      }
    }
  }
</style>
