import path from 'path'
import dotenv from 'dotenv'
import { defineConfig } from 'vite'


dotenv.config()

export default defineConfig(({ command }) => ({
    root: path.join(__dirname),
    // Chemin remplacé dans les ressources compilées
    // (correspond au chemin public http vers le dossier contenant assetsDir)
    // base: command === 'build' ? `/themes/${process.env.WP_THEME}/assets/` : '/',

    // Dossier dans lequel on place les ressources statiques non compilées, qui seront copiées vers outDir
    // publicDir: 'resources/static',
    build: {
        outDir: `dist`, // Dossier destination du build
        assetsDir: 'assets', // Sous-dossier dans lequel placer les assets (js, css) générés par Vite
        emptyOutDir: true, // Vide le dossier destination à chaque build
        manifest: true, // Génère un manifeste json listant les chemins vers les assets
        rollupOptions: {
            input: {
                index: path.resolve(__dirname, 'index.html'), // Point d'entrée HTML
                // index: 'main.js', // Point d'entrée JS, important les assets
                // custom: 'resources/scripts/burger-menu.js',
            },
        },
        sourcemap: command === 'serve' ? 'inline' : false,
    },
    css: {
        devSourcemap: command === 'serve',
    },
    server: {
        origin: 'http://localhost:5173',
    }
}))
