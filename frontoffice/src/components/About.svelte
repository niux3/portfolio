<script>

    let now = new Date(), 
        year = now.getFullYear() - 2009

</script>
<div class="about" id="about">
    <div class="intro">
        <div>
<!--            <h1>Web développeur frontend et backend à Paris</h1>-->
            <h1>Découvrez un développeur full stack pour faire avancer vos projets web</h1>
<!--            <p>Bonjour, ancien infographiste, je suis désormais un professionnel dans le web. Mon expertise se situe principalement dans les technologies du web où j'excelle avec aisance dans le monde professionnel depuis {year} ans. À mon actif, j'ai plus de 50 beaux projets et j'ai été récompensé 5 fois. </p>-->
            <div class="mouse-icon"><div class="wheel"></div></div>
        </div>
    </div>
    <div class="resume">
        <div class="top">
            <p>à propos de moi</p>
            <p>Découvrez un talent créatif passionné qui excelle dans son domaine avec une vision unique et un savoir-faire depuis <strong>{year} ans</strong>. Que ce soit dans la conception graphique ou le développement web, j'offre des services personnalisés de hautes qualités. Je donne vie à vos idées et vous démarque de la concurrence. Contactez-moi dès maintenant pour collaborer avec un professionnel talentueux et dévoué.</p>
<!--            <p>Je suis passionné par tout ce qui a à voir avec la conception numérique. J'aime travailler avec des agences et des personnes enthousiastes qui veulent résoudre des problèmes grâce à une conception suivant les standards.</p>-->
<!--            <img src="" alt="Renaud Bourdeau" />-->
        </div>
        <div class="bottom">
            <div>
                <h2>Développement frontend</h2>
                <p>Démarquez-vous avec une interface utilisateur exceptionnelle grâce à mon expertise en développement frontend. Je suis un développeur talentueux qui maîtrise les dernières technologies et les meilleures pratiques pour créer des expériences utilisateur fluides et attrayantes. Que ce soit pour un site web ou une application, je m'engage à fournir un code propre, une conception responsive et des performances optimales. Vous pouvez compter sur mon expertise en développement frontend afin de concrétiser votre vision et captiver vos utilisateurs grâce à un rendu impressionnant.</p>
            </div>
            <div>
                <h2>Développement backend</h2>
                <p>Optimisez les performances de votre application grâce à mon expertise en développement backend. Je maîtrise les langages et les frameworks les plus avancés pour construire des systèmes robustes, sécurisés et évolutifs. Que ce soit pour la gestion de bases de données, la logique métier ou l'intégration de services tiers, je m'engage à fournir des solutions backend performantes qui répondent à vos besoins. Confiez moi votre infrastructure technique et concentrez-vous sur la croissance de votre entreprise en toute confiance.</p>
            </div>
            <div>
                <h2>Conception visuelle</h2>
                <p>De l'idée à l'impact visuel, je suis là pour donner vie à votre vision créative. Je fusionne l'art et la technologie pour créer des designs visuellement époustouflants qui captivent votre public. Que ce soit pour des logos percutants, des interfaces utilisateur intuitives ou des supports de communication attrayants, je mets en œuvre des concepts innovants et des esthétiques uniques. Comptez sur mes compétences pour donner vie à une identité visuelle distinctive et mémorable pour votre marque. N'hésitez pas à me contacter dès maintenant pour vivre une expérience visuelle inouïe.</p>
<!--                <p>Je suis passionné par tout ce qui a à voir avec la conception numérique. J'aime travailler avec des agences et des personnes enthousiastes qui veulent résoudre des problèmes grâce à une conception suivant les standards.</p>-->
            </div>
<!--            <div>-->
<!--                <button>portfolio</button>-->
<!--            </div>-->
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
                <span>2021&nbsp;&ndash;&nbsp;2022</span>
                <span>développeur front/back</span>
                <span>la Maison de la Radio</span>
            </li>
            <li>
                <span>2019&nbsp;&ndash;&nbsp;2021</span>
                <span>développeur front/back</span>
                <span>Journal LePoint</span>
            </li>
            <li>
                <span>2019</span>
                <span>développeur front/back</span>
                <span>Carenity</span>
            </li>
            <li>
                <span>2018&nbsp;&ndash;&nbsp;2019</span>
                <span>développeur front/back</span>
                <span>Groupe Creative</span>
            </li>
            <li>
                <span>2016&nbsp;&ndash;&nbsp;2018</span>
                <span>développeur front/back</span>
                <span>Prodigious</span>
            </li>
            <li>
                <span>2015&nbsp;&ndash;&nbsp;2016</span>
                <span>développeur front</span>
                <span>Fullsix</span>
            </li>
            <li>
                <span>2014&nbsp;&ndash;&nbsp;2015</span>
                <span>développeur front</span>
                <span>Groupe Bazarchic</span>
            </li>
            <li>
                <span>2010&nbsp;&ndash;&nbsp;2013</span>
                <span>développeur front</span>
                <span>Business Lab</span>
            </li>
        </ul>
    </div>
    <div class="awwards">
        <p>récompenses</p>
        <ul>
            <li>
<!--                <span>2016</span>-->
                <span>Top Com Or</span>
                <span>Renault Clio RS</span>
            </li>
            <li>
<!--                <span>2013</span>-->
                <span>Top Com Or</span>
                <span>Leroy Merlin</span>
            </li>
            <li>
<!--                <span>2012</span>-->
                <span>Top Com Or</span>
                <span>Peugeot</span>
            </li>
            <li>
<!--                <span>2012</span>-->
                <span>Top Com Or</span>
                <span>Peugeot 4008</span>
            </li>
            <li>
<!--                <span>2011</span>-->
                <span>Top Com Or</span>
                <span>Areva</span>
            </li>
        </ul>
    </div>
</div>

<style lang="scss">

.about{
    padding-right: 1.3vw;
}

.about .intro{
    min-height: 440px;
    height: calc(100vh - 25px);
    margin-right: 10%;
    margin-left: 50%;
    display: flex;
    flex-direction: column;
    position: relative;
}
.about .intro > div{
    margin: auto 0;
}

.about .intro h1{
    font-size: 4vw;
    margin-top: 0;
    margin-bottom: 15px;
    line-height: 1em;
    position: relative;
    right: -50px;
    opacity: 1;
}
.about .intro p{
    font-size: 1.3vw;
    position: relative;
    left: -50px;
    opacity: 0;
}

.on-article .about .intro h1{
   animation: on_display_intro_h1 .4s forwards .4s;
}

.on-article .about .intro p{
    animation: on_display_intro_p .4s forwards .4s;

}
@keyframes on_display_intro_h1 {
   0%{
       opacity: 0;
       right: -50px;
   }
    100%{
        opacity: 1;
        right: 0;
    }
}

@keyframes on_display_intro_p {
    0%{
        opacity: 0;
        left: -50px;
    }
    100%{
        opacity: 1;
        left: 0;
    }
}

@media (max-width: 900px){
    .about .intro p{
        font-size: 1.7vw;
    }

}
@media (max-width: 767px){
    .about .intro{
        margin-left: 0;
    }

    .about .intro > div{
        position: absolute;
        left: 1vw;
        bottom: 6vh;
        width: 75%;
    }

    .about .intro h1{
        font-size: 6vw;
    }
    .about .intro p{
        font-size: 2vw;
    }
}

.about .resume{
    padding: 4vw 0;
    border-top: 1px solid #444;
}

.about .resume .top,
.about .resume .bottom{
    display: grid;
    grid-auto-columns: 1fr;
    grid-column-gap: 0px;
    grid-row-gap: 16px;
    justify-content: space-between;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: auto;
}

.about .resume .top{
    margin-bottom: 4vw;
}
.about .resume .top p{
    margin: 0;
}
.about .resume .top p:nth-child(1){
    text-transform: uppercase;
}
.about .resume .top p:nth-child(2){
    font-size: 1.75vw;
    grid-column-start: span 3;
    line-height: 1em;
}
.about .resume .top,
.about .resume .bottom{
    grid-column-gap: 2vw;
}
.about .resume .bottom > div:first-child{
    grid-column-start: 2;
}


@media (max-width: 900px){
    .about .resume .top{
        display: block;
    }
    .about .resume .top p:nth-child(1){
        display: none;
    }

    .about .resume .top p:nth-child(2){
        font-size: 2vw;
    }
    .about .resume .bottom{
        display: flex;
        flex-direction: column;
    }
    .about .resume .bottom > div{
        border-top: 1px solid #444;
        display: flex;
        justify-content: space-between;
    }
    .about .resume .bottom > div > *{
        width: 50%;
    }
    .about .resume .bottom > div h2{
        font-size: 2vw;
    }
    .about .resume .bottom > div p{
        font-size: 1.7vw;
    }
}

.about .experience,
.about .awwards{
    display: grid;
    width: 100%;
    grid-auto-columns: 1fr;
    grid-column-gap: 0px;
    grid-row-gap: 16px;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: auto;
    border-top: 1px solid #444;
    padding-top: 4vw;
    margin-top: 4vw;
}
.about .experience{
    margin-top: 0;
}
.about .experience p,
.about .awwards p{
    text-transform: uppercase;
}

.about .experience ul,
.about .awwards ul{
    list-style: none;
    margin: 0;
    padding: 0;
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
}
.about .experience li,
.about .awwards li{
    display: flex;
    flex-direction: column;
    font-size: 1.25vw;
}
.about .experience li span,
.about .awwards li span{
    margin: .2vw 0;
}
@media (max-width: 900px){
    .about .experience,
    .about .awwards{
        display: flex;
        flex-direction: column;
    }

    .about .experience li,
    .about .awwards li{
        font-size: 1.7vw;
    }

    .about .experience p,
    .about .awwards p{
        margin-top: 0;
    }
}
</style>