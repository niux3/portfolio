<script>
    import Link from './Link.svelte';
</script>

<header>
    <Link to="#/accueil" text="Renaud Bourdeau" />
    <nav>
        <ol>
            <li><Link to="#/accueil" text="à propos de moi" /></li>
            <li><Link to="#/portfolio" text="projets" /></li>
            <li><Link to="#/me-contacter" text="me contacter" /></li>
        </ol>
    </nav>
</header>