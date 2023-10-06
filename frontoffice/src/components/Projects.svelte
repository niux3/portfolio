<script>
    export let data
</script>

<ul>
    {#each data as row}
        <li>{ row.id }</li>
    {/each}
</ul>

