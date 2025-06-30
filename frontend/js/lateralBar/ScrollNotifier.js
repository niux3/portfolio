import Subject from './Subject'
import GoToTopObserver from './GoToTopObserver'
import ShareObserver from './ShareObserver'
import Utils from '../Utils'


export default class ScrollNotifier{
    #subject
    #goToTop
    #share

    constructor(LateralBar){
        this.#subject = new Subject()
        this.#goToTop = new GoToTopObserver(lateralBar.querySelector('a[href="#top"]'))
        this.#share = new ShareObserver(lateralBar.querySelector('.share'))
    }

    init(){
        this.#subject.add(this.#goToTop)
        this.#subject.add(this.#share)

        const notifyScroll = Utils.debounce(() => {
            this.#subject.notify(window.scrollY)
        }, 400)

        notifyScroll()
        window.addEventListener('scroll', notifyScroll)
    }
}
