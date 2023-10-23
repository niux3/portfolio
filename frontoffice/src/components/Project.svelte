<script>
    export let row
    export let index
    export let len
    $: thumb = row.images.find(img => /\d+--1/.test(img)) !== undefined?
        row.images.find(img => /\d+--1/.test(img)) :
        "https://placekitten.com/g/914/533"
</script>
<article id="projet">
    <header>
        <div class="description">
            <p class="counter">✺&nbsp;&nbsp;{index} - {len}</p>
            <h1 class="name">{row.name}</h1>
            <div class="wrap">
                <div class="cartouche">
                    <dl>
                        <dt>type</dt>
                        <dd>
                            <span>{row.function}</span>
                        </dd>
                    </dl>
                    <dl>
                        <dt>description</dt>
                        <dd>
                            <span>{row.activity_name}</span>
                        </dd>
                    </dl>
                    <dl>
                        <dt>année</dt>
                        <dd>
                            <span>{row.year}</span>
                        </dd>
                    </dl>
                </div>
                    <ul>
                        {#each row.technologies as technology, i}
                            <li>{technology}</li>
                        {/each}
                    </ul>
            </div>
        </div>
    </header>
    <div class="content">
            <div class="wrap-thumb">
                <img src={thumb} alt="" loading="lazy">
            </div>
        <div class="info">
            <aside>
                <a href={row.url} target="_blank">{row.url} <span class="fa-solid fa-caret-right"></span></a>
            </aside>
            <div class="resume">
                <div>{row.description}</div>
                <ul>
                    <li><strong>client</strong><span>{row.customer}</span></li>
                    <li><strong>année</strong><span>{row.year}</span></li>
                    <li><strong>type</strong><span>{row.function}</span></li>
                    <li><strong>lieu</strong><span>{row.location}</span></li>
                </ul>
            </div>
        </div>
    </div>
</article>
