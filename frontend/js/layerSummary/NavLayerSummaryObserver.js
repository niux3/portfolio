import AbstractObserver from '../observer/AbstractObserver'


export default class NavLayerSummaryObserver extends AbstractObserver{
    #linkNav
    #subject

    constructor(props, subject){
        super(props)
        let selector = `#summary nav a[href="#${this.$el.id}"]`
        this.#linkNav = document.querySelector(selector)
        this.#subject = subject
        subject.add(this)
    }

    update(data){
        let halfHeightWindow = Math.round(window.innerHeight / 3)
        if(this.$el.getBoundingClientRect().y - halfHeightWindow < 0){
            this.#linkNav.parentNode.classList.add('active')
            this.#linkNav.parentNode.scrollIntoView({
                behavior: 'smooth',
                block: 'center'
            })
        }else{
            this.#linkNav.parentNode.classList.remove('active')
        }
        this.#desactiveBefore()
    }

    #desactiveBefore(){
        let $navLinks = Array.from(document.querySelectorAll('#summary nav a')),
            index = $navLinks.findLastIndex($el => $el.parentNode.classList.contains('active'))
        if(index > 0){
            $navLinks.slice(0, index).map(e => e.parentNode.classList.remove('active'))
        }
    }
}
