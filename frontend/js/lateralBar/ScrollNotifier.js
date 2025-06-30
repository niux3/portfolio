import Subject from './Subject'
import GoToTopObserver from './GoToTopObserver'
import ShareObserver from './ShareObserver'
import LateralBarObserver from './LateralBarObserver'
import Utils from '../Utils'


export default class ScrollNotifier{
    #subject
    #goToTopObserver
    #shareObserver
    #lateralBarObserver

    constructor(LateralBar){
        this.#subject = new Subject()
        this.#goToTopObserver = new GoToTopObserver(lateralBar.querySelector('a[href="#top"]'))
        this.#shareObserver = new ShareObserver(lateralBar.querySelector('.share'))
        this.#lateralBarObserver = new LateralBarObserver(lateralBar)
    }

    init(){
        this.#subject.add(this.#goToTopObserver)
        this.#subject.add(this.#shareObserver)
        this.#subject.add(this.#lateralBarObserver)

        const notifyScroll = Utils.debounce(() => {
            this.#subject.notify(window.scrollY)
        }, 400)

        notifyScroll()
        window.addEventListener('scroll', notifyScroll)
    }
}
