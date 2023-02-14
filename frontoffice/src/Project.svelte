<script>
    export let data
    export let len
</script>
<header>
    <div class="description">
        <p class="counter">✺&nbsp;&nbsp;{data.index} - {len}</p>
        <h1 class="name">{data.name}</h1>
        <div class="wrap">
            <div class="cartouche">
                <dl>
                    <dt>type</dt>
                    <dd>
                        <span>{data.function}</span>
                    </dd>
                </dl>
                <dl>
                    <dt>description</dt>
                    <dd>
                        <span>{data.activity_name}</span>
                    </dd>
                </dl>
                <dl>
                    <dt>année</dt>
                    <dd>
                        <span>{data.year}</span>
                    </dd>
                </dl>
            </div>
<!--                <ul>-->
<!--                    {#each data.technologies as technology, i}-->
<!--                        <li>{technology}</li>-->
<!--                    {/each}-->
<!--                </ul>-->
        </div>
    </div>
</header>
<div class="content">
    <img src="https://placekitten.com/g/914/533" alt="">
    <div class="info">
        <aside></aside>
        <div class="resume">
            <div>Touch my tail, i shred your hand purrrr put toy mouse in food bowl run out of litter box at full speed climb a tree, wait for a fireman jump to fireman then scratch his face so jump on fridge. I could pee on this if i had the energy i see a bird i stare at it i meow at it i do a wiggle come here birdy friends are not food.</div>
            <ul>
                <li><strong>client</strong><span>ACME</span></li>
                <li><strong>année</strong><span>2021</span></li>
                <li><strong>type</strong><span>frontend</span></li>
                <li><strong>lieu</strong><span>Paris</span></li>
            </ul>
        </div>
    </div>
</div>