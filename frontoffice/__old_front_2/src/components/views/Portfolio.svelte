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
            <ol>
                <li>
                    <a href="#/projets/leroy-merlin">
                        <img src="./img/john-paul-2.webp" alt="" />
                        <div class="description">
                            <p class="counter">1 - 50</p>
                            <h2 class="name">John Paul</h2>
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
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#/projets/areva">
                        <img src="./img/radio-france.jpg" alt="" />
                        <div class="description">
                            <div class="counter">2 - 50</div>
                            <h2 class="name">Radio France</h2>
                            <div class="cartouche">
                                <dl>
                                    <dt>Type</dt>
                                    <dd>
                                        <span>frontend</span>
                                    </dd>
                                </dl>
                                <dl>
                                    <dt>description</dt>
                                    <dd>
                                        <span>Média</span>
                                    </dd>
                                </dl>
                                <dl>
                                    <dt>année</dt>
                                    <dd>
                                        <span>2021 - 2022</span>
                                    </dd>
                                </dl>
                            </div>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#/projets/dyson-airblade">
                        <img src="./img/lepoint.png" alt="" />
                        <div class="description">
                            <div class="counter">3 - 50</div>
                            <h2 class="name">Le Point</h2>
                            <div class="cartouche">
                                <dl>
                                    <dt>Type</dt>
                                    <dd>
                                        <span>fullstack</span>
                                    </dd>
                                </dl>
                                <dl>
                                    <dt>description</dt>
                                    <dd>
                                        <span>Média</span>
                                    </dd>
                                </dl>
                                <dl>
                                    <dt>année</dt>
                                    <dd>
                                        <span>2019 - 2021</span>
                                    </dd>
                                </dl>
                            </div>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#/projets/dyson-airblade">
                        <img src="./img/carenity.jpg" alt="" />
                        <div class="description">
                            <div class="counter">4 - 50</div>
                            <h2 class="name">Carenity</h2>
                            <div class="cartouche">
                                <dl>
                                    <dt>Type</dt>
                                    <dd>
                                        <span>fullstack</span>
                                    </dd>
                                </dl>
                                <dl>
                                    <dt>description</dt>
                                    <dd>
                                        <span>Réseau social</span>
                                    </dd>
                                </dl>
                                <dl>
                                    <dt>année</dt>
                                    <dd>
                                        <span>2019</span>
                                    </dd>
                                </dl>
                            </div>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#/projets/dyson-airblade">
                        <img src="./img/rimowa.jpg" alt="" />
                        <div class="description">
                            <div class="counter">5 - 50</div>
                            <h2 class="name">Rimowa</h2>
                            <div class="cartouche">
                                <dl>
                                    <dt>Type</dt>
                                    <dd>
                                        <span>frontend</span>
                                    </dd>
                                </dl>
                                <dl>
                                    <dt>description</dt>
                                    <dd>
                                        <span>Luxe</span>
                                    </dd>
                                </dl>
                                <dl>
                                    <dt>année</dt>
                                    <dd>
                                        <span>2018</span>
                                    </dd>
                                </dl>
                            </div>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#/projets/dyson-airblade">
                        <img src="./img/longchamp.jpg" alt="" />
                        <div class="description">
                            <div class="counter">6 - 50</div>
                            <h2 class="name">Longchamp</h2>
                            <div class="cartouche">
                                <dl>
                                    <dt>Type</dt>
                                    <dd>
                                        <span>frontend</span>
                                    </dd>
                                </dl>
                                <dl>
                                    <dt>description</dt>
                                    <dd>
                                        <span>Luxe</span>
                                    </dd>
                                </dl>
                                <dl>
                                    <dt>année</dt>
                                    <dd>
                                        <span>2018</span>
                                    </dd>
                                </dl>
                            </div>
                        </div>
                    </a>
                </li>
            </ol>
        </article>
    </section>
{/if}
<style lang="scss">
  section{
    margin-top: 40px;
    article{
      ol{
        list-style: none;
        margin: 0;
        padding: 0;
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        grid-column-gap: 2vw;
        grid-row-gap: 2vw;
        grid-auto-columns: 1fr;
        width: 100%;

        li{
          position: relative;
            &:before{
              content:"";
              position: absolute;
              top: 0;
              right: 0;
              bottom: 0;
              left: 0;
              background: rgba(32,32,32, .5);
              z-index: 10;
              pointer-events: none;

            }
          img{
            display: block;
            width: 100%;
            height: 100%;
            object-fit: cover;
            //filter: grayscale(100%) blur(1px);
          }
          .description{
            position: absolute;
            right: 0;
            bottom: 0;
            left: 0;
            color: #fff;
            padding: 0 2.5vw 2.5vw 2.5vw;
            z-index: 20;

            text-shadow: 0 0px 1px #444;

            h2{
              max-width: 35vw;
              margin-top: 0.8rem;
              margin-bottom: 1rem;
              font-size: 3em;
              line-height: 1;
              font-weight: 400;
            }

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
          }

        }

      }
    }
  }
</style>
