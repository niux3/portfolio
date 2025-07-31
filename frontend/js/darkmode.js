import Utils from './Utils'


class DarkMode {
    #button
    #modes

    constructor(selector = '.changeMode') {
        this.#button = document.querySelector(selector)
        this.#modes = {
            light: {
                text: 'mode sombre',
                icon: 'fa-solid fa-moon',
            },
            dark: {
                text: 'mode clair',
                icon: 'fa-solid fa-sun',
            }
        }
    }

    init() {
        const storedTheme = localStorage.getItem('theme')

        if (storedTheme) {
            this.#applyMode(storedTheme)
        } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
            this.#applyMode('dark')
        }

        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
            this.#applyMode(e.matches ? 'dark' : 'light')
        })

        if (this.#button) {
            this.#button.addEventListener(Utils.isMobile() ? 'pointerdown' : 'click', () => {
                this.#toggleMode()
            })
        }
    }

    #applyMode(modeKey) {
        const mode = this.#modes[modeKey]
        document.documentElement.dataset.themePreference = modeKey
        localStorage.setItem('theme', modeKey)

        if (this.#button) {
            this.#button.setAttribute('aria-label', `Activer le ${mode.text}`)
            this.#button.querySelector('.fa-solid').className = mode.icon
            this.#button.querySelector('.text').textContent = `Activer le ${mode.text}`
        }
    }

    #toggleMode() {
        const current = document.documentElement.dataset.themePreference
        const next = [undefined, 'light'].includes(current) ? 'dark' : 'light'
        this.#applyMode(next)
    }
}

export default DarkMode
