<script>
    export let data
</script>

<ul>
    {#each data as row}
        <li><a href="#/{row.slug}">{ row.id } {row.name}</a></li>
    {/each}
</ul>

