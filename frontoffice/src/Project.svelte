<script>
    export let data
    export let len
</script>
<header>
    <div class="description">
        <p class="counter">{data.index} - {len}</p>
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
            <!--                        <ul>-->
            <!--                            {#each data.technologies as technology, i}-->
            <!--                                <li>{technology}</li>-->
            <!--                            {/each}-->
            <!--                        </ul>-->
        </div>
    </div>
</header>
<div class="content"></div>