import babel from 'rollup-plugin-babel';
import resolve from 'rollup-plugin-node-resolve';
import scss from 'rollup-plugin-scss';
import { terser } from "rollup-plugin-terser";
import commonjs from 'rollup-plugin-commonjs';
import livereload from 'rollup-plugin-livereload';


let plugins = [
    resolve(),
    commonjs({
        include: 'node_modules/**',
    }),
    babel({
        exclude: 'node_modules/**',
    }),
    terser(),
    scss({
        output:'static/css/styles.css',
        failOnError: true,
        watch: 'front/scss/',
        outputStyle: "compressed",
    })
];
if(process.argv.includes('--dev')){
    plugins = [...plugins, livereload({
        watch: 'public',
        verbose: true,
        port: 9000,
        delay: 500,
    })]
}
console.log(plugins)
export default {
    input: 'front/js/index.js',
    output: {
        format: 'iife',
        file: 'static/js/app.js',
        name: 'app'
    },
    plugins:plugins
};
