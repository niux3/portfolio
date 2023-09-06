<script>
    export let data
    export let len
    let thumb = data.images.find(img => /\d+--1/.test(img)) !== undefined?
        data.images.find(img => /\d+--1/.test(img)) :
        "https://placekitten.com/g/914/533"
    console.log(data.images.find(img => /\d+--1/.test(img)))
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
                <ul>
                    {#each data.technologies as technology, i}
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
            <a href={data.url} target="_blank">{data.url} <span class="fa-solid fa-caret-right"></span></a>
        </aside>
        <div class="resume">
            <div>{data.description}</div>
            <ul>
                <li><strong>client</strong><span>ACME</span></li>
                <li><strong>année</strong><span>2021</span></li>
                <li><strong>type</strong><span>frontend</span></li>
                <li><strong>lieu</strong><span>Paris</span></li>
            </ul>
        </div>
    </div>
</div>