export default class Carousel{
    constructor(){
        [this._$ulTitle, this._$ulIllustration] = document.querySelectorAll('.carousel-project .projects ul')
        this._$lisTitle = this._$ulTitle.querySelectorAll('li')
        this._$lisIllustration = this._$ulIllustration.querySelectorAll('li')
        this._lenLi = parseInt(this._$ulTitle.closest('.carousel-project').dataset.len, 10)
        this._roundHeightLiTitle = 0
        this._roundHeightLiIllustration = 0
        this._index = 0
        this._step = 0
        this._operatorStep = 0
    }

    _setHeightLiTitle(){
        this._roundHeightLiTitle = Math.ceil(this._$lisTitle[0].getBoundingClientRect().height)
    }

    _setHeightLiIllustration(){
        this._roundHeightLiIllustration = Math.ceil(this._$lisIllustration[0].getBoundingClientRect().height)
    }

    _setCenterY(){
        let referencePos = this._lenLi * 4 - 1,
            posUlBaseTitle = this._roundHeightLiTitle / 2,
            posUlBaseIllustration = this._roundHeightLiIllustration / 2,
            posUlTitle = referencePos * this._$lisTitle[0].getBoundingClientRect().height,
            posUlIllustration = referencePos * this._$lisIllustration[0].getBoundingClientRect().height

        this._$ulTitle.closest('.wrap').style.marginTop = `-${posUlBaseTitle + posUlTitle}px`
        this._$ulIllustration.closest('.wrap').style.marginTop = `-${posUlBaseIllustration + posUlIllustration}px`
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
        this._operatorStep = e.deltaY >= 0?  1 : - 1
    }

    onResize(utils){
        window.addEventListener('resize', utils.debounce(e =>{
            this._setHeightLiTitle()
            this._setHeightLiIllustration()
            this._setPosMask()
            this._setCenterY()
            this._setCenterY()
            this._setCenterY()
            this._setCenterY()
        }, 800))
    }

    onLoad(){
        window.addEventListener('load', e => {
            this._setHeightLiTitle()
            this._setHeightLiIllustration()
            this._setPosMask()
            this._setCenterY()
        })
    }

    onWheel(utils){
        window.addEventListener('wheel', utils.throttle(e=>{
            this._setIndex(e)
            let heightLiTitle = this._$lisTitle[0].getBoundingClientRect().height,
                heightLiIllustration = this._$lisIllustration[0].getBoundingClientRect().height,
                [directionTitle, directionIllustation] = this._index >= 0? ['', '-'] : ['-', ''],
                indexDirection = this._index >= 0? this._index : Math.abs(this._index)

            if(this._index % this._lenLi == 0){
                // console.error('>> ', this._step)
                // console.error('-> ', directionIllustation, directionTitle)
                // console.log(this._step <= 0? 'negatif' : 'positif')

                this._step = this._operatorStep === 1? this._step + 1 : this._step - 1
                let titleMarginTop = this._step <= 0? `${this._step * this._lenLi * heightLiTitle * (-1)}px` : `-${this._step * this._lenLi * heightLiTitle}px` 
                this._$ulTitle.style.marginTop = titleMarginTop
                this._$ulIllustration.style.marginTop = `${this._step * this._lenLi * heightLiIllustration}px`
            }

            this._$ulTitle.style.transform = `translateY(${directionTitle}${indexDirection * heightLiTitle}px)`
            this._$ulIllustration.style.transform = `translateY(${directionIllustation}${indexDirection * heightLiIllustration}px)`

            // let current = (this._lenLi * 4 - 1) - 1
            // this._$lisTitle[current].querySelector('a').style.color = 'red'
            // console.log('>>>>',this._$lisTitle[current]);
            // let animEndSlide;
            // clearTimeout(animEndSlide)
            // animEndSlide = null
            // animEndSlide = setTimeout(()=>{
            //     Array.from(this._$lisTitle).map(li => li.style.color = '#444')
            //     let current = (this._lenLi * 4 - 1)
            //     this._$lisTitle[current].style.color = 'red'
            //     clearTimeout(animEndSlide)
            //     animEndSlide = null
            // }, 1000)
        }, 80))
    }
}