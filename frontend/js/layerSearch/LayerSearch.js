import TemplateEngine from '../TemplateEngine'


export default class LayerSearch{
    #search
    #formSearch
    #resultSearch
    #output

    constructor(){
        if(document.getElementById('search')){
            this.#search = document.getElementById('search')
            this.#formSearch = this.#search.querySelector('form')
            this.#resultSearch = this.#search.querySelector('#resultSearch')
            this.#output = this.#search.querySelector('output')
        }
    }

    init(){

        this.#formSearch.addEventListener('submit', e =>{
            e.preventDefault()
            let headers = new Headers({
                "X-Requested-With": "XMLHttpRequest",
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded"
            }),
                object = {},
                formData = new FormData(this.#formSearch)

            formData.forEach((value, key) =>{
                object[key] = value
            })

            let data = Object.entries(object).map(([k,v]) => `${encodeURIComponent(k)}=${encodeURIComponent(v)}`).join('&'),
                params = {
                    method: this.#formSearch.method.toUpperCase(),
                    headers,
                    cache: 'no-cache',
                    redirect: 'follow',
                    referrerPolicy: 'no-referrer',
                    mode: "cors",
                },
                url = window.location.origin.includes('rb-webstudio') ? this.#formSearch.action : `http://localhost/portfolio/public${this.#formSearch.getAttribute('action')}`
            fetch(`${url}?${data}`, params).then(resp =>{
                if(resp.ok === true)
                    return resp.json()
            }).then(({ data }) =>{
                let templateEngine = new TemplateEngine(),
                    tpl = document.getElementById('tplLayer'),
                    lenResult = Object.keys(data).length,
                    rows = []
                this.#output.innerHTML = `<strong>${lenResult}</strong> résultat${lenResult > 1? 's': ''} trouvé${lenResult > 1? 's': ''}`

                if(lenResult > 0){
                    let reference = 250,
                        $nav = document.createElement('nav')

                    for(let v of Object.values(data)){
                        rows.push({
                            url: `/articles/${v.slug}-${v.id}.html`,
                            text: v.title
                        })
                    }

                    $nav.style.height = `${window.innerHeight - reference}px`
                    window.addEventListener('resize', e =>{
                        Utils.debounce(()=>{
                            $nav.style.height = `${window.innerHeight - reference}px`
                        }, 200)()

                    })
                    $nav.innerHTML = templateEngine.render(tpl.textContent, {rows})
                    this.#resultSearch.innerHTML = $nav.outerHTML
                }
            })
        })



    }
}
