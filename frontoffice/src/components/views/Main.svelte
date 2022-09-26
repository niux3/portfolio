<script>
    import {current_view} from "../../store";
    import Pages from './Pages.svelte';
</script>
<p style="position: fixed; top:115px;right:50px"><strong>main: </strong>{$current_view}</p>
<main>
    <Pages current_view={current_view} w={innerWidth} h={innerHeight} />
</main>