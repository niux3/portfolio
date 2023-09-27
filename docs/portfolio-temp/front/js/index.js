import '../scss/index.scss';
import Utils from "./libs/utils/Utils";

class Carousel{
    constructor(){
        [this._$ulTitle, this._$ulIllustration] = document.querySelectorAll('.carousel .projects ul')
        this._$lisTitle = this._$ulTitle.querySelectorAll('li')
        this._$lisIllustration = this._$ulIllustration.querySelectorAll('li')
        this._lenLi = parseInt(this._$ulTitle.closest('.carousel').dataset.len, 10)
        this._roundHeightLiTitle = 0
        this._roundHeightLiIllustration = 0
        this._index = 0
    }

    _setHeightLiTitle(){
        this._roundHeightLiTitle = Math.ceil(this._$lisTitle[0].getBoundingClientRect().height)
    }

    _setHeightLiIllustration(){
        this._roundHeightLiIllustration = Math.ceil(this._$lisIllustration[0].getBoundingClientRect().height)
    }

    _setCenterY(){
        this._$ulTitle.closest('.wrap').style.marginTop = `-${this._roundHeightLiTitle / 2}px`
        this._$ulIllustration.closest('.wrap').style.marginTop = `-${this._roundHeightLiIllustration / 2}px`
    }

    _setPosMask(){
        let tpl = `
                <style class="before-after">
                    .carousel .title:before{
                        bottom: %%VALUE%%px;
                    }
                    .carousel .title:after{
                        top: %%VALUE%%px;
                    }
                </style>
            `,
            value = (window.innerHeight / 2) + (this._roundHeightLiTitle / 2)

        if(document.querySelectorAll('style.before-after').length){
            document.querySelector('style.before-after').remove()
        }
        document.head.insertAdjacentHTML('beforeend', tpl.replace(/%%VALUE%%/g, value))
    }

    _setIndex(e){
        this._index = e.deltaY >= 0? this._index + 1 : this._index - 1
    }

    _setPosUl(){
        let referencePos = (this._lenLi * 2) - 2
        this._$ulTitle.style.marginTop = `-${referencePos * this._$lisTitle[0].getBoundingClientRect().height}px`
        this._$ulIllustration.style.marginTop = `-${referencePos * this._$lisIllustration[0].getBoundingClientRect().height}px`
    }

    onResize(utils){
        window.addEventListener('resize', utils.debounce(e =>{
            console.log('onresize');
            this._setHeightLiTitle()
            this._setHeightLiIllustration()
            this._setPosMask()
            this._setCenterY()
            this._setPosUl()
        }, 50))
    }

    onLoad(){
        window.addEventListener('load', e => {
            console.log('onload');
            // console.log('>>', this._lenLi, this._lenLi / 3)
            this._setHeightLiTitle()
            this._setHeightLiIllustration()
            this._setPosMask()
            this._setCenterY()
            this._setPosUl()
        })
    }

    onWheel(utils){
        window.addEventListener('wheel', utils.debounce(e=>{
            console.log('onWheel');
            this._setIndex(e)
            console.log(this._index)
            let heightLiTitle = this._$lisTitle[0].getBoundingClientRect().height,
                heightLiIllustration = this._$lisIllustration[0].getBoundingClientRect().height
            this._$ulTitle.style.transform = 'translateY('+ (this._index * heightLiTitle) +'px)'
            this._$ulIllustration.style.transform = 'translateY(-'+ (this._index * heightLiIllustration) +'px)'
        }, 50))
    }
}

let carousel = new Carousel()
carousel.onLoad()
carousel.onResize(Utils)
carousel.onWheel(Utils)
