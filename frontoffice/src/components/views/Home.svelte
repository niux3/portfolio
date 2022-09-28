<script>
    import {display} from "../../libs/store";
    import {onMount, onDestroy} from 'svelte'
    import {toVisible, toInvisible} from "../../libs/transition";

    let innerWidth = window.innerWidth;
    let innerHeight = window.innerHeight;
    let year = parseInt(new Date().getFullYear(), 10) - 2010;
    let pt_body = window.getComputedStyle(document.body).getPropertyValue('padding-top');
    let pb_body = window.getComputedStyle(document.body).getPropertyValue('padding-bottom');
    $: difference = parseInt(pt_body, 10) + parseInt(pb_body, 10) - 10;

    onMount(()=>{
        toVisible();
    })

    onDestroy(()=>{
        toInvisible();
    })

</script>

<svelte:window bind:innerWidth bind:innerHeight />
{#if $display}
<section>
    <article>
        <div style="height: {innerHeight - difference}px">
            <div>
                <h1>Web développeur frontend et backend à Paris</h1>
                <p>Bonjour, ancien infographiste, je suis désormais un professionnel dans le web. Mon expertise se situe principalement dans les technologies du web où j'excelle avec aisance dans le monde professionnel depuis {year} ans. À mon actif, j'ai plus de 50 beaux projets et j'ai été récompensé 5 fois. </p>
                <button></button>
            </div>
        </div>
        <div class="about">
            <div class="aboutGrid top">
                <p>à propos de moi</p>
                <p>Je suis passionné par tout ce qui a à voir avec la conception numérique. J'aime travailler avec des agences et des personnes enthousiastes qui veulent résoudre des problèmes grâce à une conception suivant les standards.</p>
                <img src="" alt="Renaud Bourdeau" />
            </div>
            <div class="aboutGrid bottom">
                <div>
                    <h2>Développement frontend</h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus dolorem mollitia quam quia sint? Atque aut illum odio quia rem saepe? Ad at aut doloribus illo, obcaecati omnis pariatur! Est?</p>
                </div>
                <div>
                    <h2>Développement backend</h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deserunt earum error harum iusto laboriosam minima nesciunt officiis quidem reprehenderit soluta. Amet architecto dolor et, id laboriosam possimus reprehenderit saepe sapiente!</p>
                </div>
                <div>
                    <h2>Conception visuelle</h2>
                    <p>En utilisant mon expertise, je m'assure qu'une identité visuelle puisse être utilisée dans toute son étendue. Non seulement intemporel, mais utilisable dans le monde numérique d'aujourd'hui.</p>
                </div>
                <div>
                    <button>portfolio</button>
                </div>
            </div>
        </div>
        <div class="experience">
            <p>expérience</p>
            <ul>
                <li>
                    <span>2022</span>
                    <span>développeur backend</span>
                    <span>John Paul</span>
                </li>
                <li>
                    <span>2021 - 2022</span>
                    <span>développeur front/back</span>
                    <span>la Maison de la Radio</span>
                </li>
                <li>
                    <span>2019 - 2021</span>
                    <span>développeur front/back</span>
                    <span>Journal LePoint</span>
                </li>
                <li>
                    <span>2019</span>
                    <span>développeur front/back</span>
                    <span>Carenity</span>
                </li>
                <li>
                    <span>2018 - 2019</span>
                    <span>développeur front/back</span>
                    <span>Groupe Creative</span>
                </li>
                <li>
                    <span>2016 - 2018</span>
                    <span>développeur front/back</span>
                    <span>Prodigious</span>
                </li>
                <li>
                    <span>2015 - 2016</span>
                    <span>développeur front</span>
                    <span>Fullsix</span>
                </li>
                <li>
                    <span>2014 - 2015</span>
                    <span>développeur front</span>
                    <span>Groupe Bazarchic</span>
                </li>
                <li>
                    <span>2010 - 2013</span>
                    <span>développeur front</span>
                    <span>Business Lab</span>
                </li>
            </ul>
        </div>
    </article>
</section>
{/if}

<style lang="scss">
  .aboutGrid{
    display: grid;
    grid-auto-columns: 1fr;
    grid-column-gap: 0px;
    grid-row-gap: 16px;
    justify-content: space-between;
    grid-template-columns: minmax(200px,20vw) minmax(200px,20vw) minmax(200px,20vw) 20vw;
    grid-template-rows: auto;
  }
  section{
    overflow: auto;
    width: 100%;
;
    article{

      > div{
        &:nth-child(1){
          display: flex;
          justify-content: center;
          align-items: flex-end;
          flex-direction: column;
          margin-left: 59%;

          > div{
            text-align: left;
            margin-right: 14%;

            h1{
              font-size: 4em;
              font-weight: 200;
              margin-bottom: 15px;
              line-height: 1em;
            }

          }
        }
        &.about{
          border-top: 1px solid #444;
          padding-top: 4vw;
          .top{

            margin-bottom: 7em;

            p{
              margin: 0;
              &:nth-child(1){
                text-transform: uppercase;
              }

              &:nth-child(2){
                font-size: 2.4em;
                grid-column-start: span 2;
              }
            }
          }
          .bottom{
            > div{
              h2{
                font-size: 1.3em;
                line-height: 1;
                font-weight: 400;
              }
            }
          }
        }
        &.experience{
          display: grid;
          width: 100%;
          grid-auto-columns: 1fr;
          grid-column-gap: 0px;
          grid-row-gap: 16px;
          grid-template-columns: 1.75fr 1fr 1fr 1fr;
          grid-template-rows: auto;
          border-top: 1px solid #444;
          padding-top: 4vw;
          margin-top: 4vw;

          p:first-of-type{
            text-transform: uppercase;
          }

          ul{
            list-style: none;
            grid-column-start: span 3;
            display: grid;
            align-items: start;
            align-content: start;
            grid-auto-columns: 1fr;
            grid-auto-rows: max-content;
            grid-column-gap: 0px;
            grid-row-gap: 3vw;
            grid-template-columns: 1fr 1fr 1fr;
            grid-template-rows: max-content;

            li{
              display: flex;
              flex-direction: column;
              font-size: 1.25vw;

              span{
                margin: .2vw 0;
              }
            }
          }
        }
      }
    }
  }
</style>
