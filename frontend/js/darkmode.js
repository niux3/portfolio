import Utils from "./Utils"


const darkmode = ()=>{
    let $btnChangeMode = document.querySelector('.changeMode'),
        storedTheme = localStorage.getItem('theme'),
        changeMode = $btn =>{
            let mode = {
                'light': {
                    'text': 'mode sombre',
                    'icon': 'fa-solid fa-moon',
                },
                'dark': {
                    'text': 'mode clair',
                    'icon':  'fa-solid fa-sun'
                }
            },
            isLigth = [undefined, 'light'].some(m => m === document.documentElement.dataset.themePreference),
            key = isLigth ? 'dark' : 'light',
            text = `Activer le ${mode[key]['text']}`

            $btn.setAttribute('aria-label', text)
            $btn.querySelector('.fa-solid').className = mode[key]['icon']
            $btn.querySelector('.text').textContent = text
            document.documentElement.dataset.themePreference = key
            localStorage.setItem('theme', key)
        }

    if(storedTheme){
        document.documentElement.dataset.themePreference = storedTheme
    }else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches){
        changeMode($btnChangeMode)
    }
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', event => {
        changeMode($btnChangeMode)
    })
    if($btnChangeMode !== null){
        $btnChangeMode.addEventListener(Utils.isMobile()? 'pointerdown' : 'click', e =>{
            changeMode($btnChangeMode)
        })
    }
}
export default darkmode
