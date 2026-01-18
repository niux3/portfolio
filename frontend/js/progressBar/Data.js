export default class Data {
    constructor($article) {
        this.$article = $article
        // this.$article.insertAdjacentHTML('beforeend', '<div class="debug"></div>')
        // this.$debug = document.querySelector('.debug')

    }

    getPercent(valueScroll) {
        this._offsetTop = this.$article.offsetTop;
        this._heightTotalArticle = this.$article.getBoundingClientRect().height;
        let value = null,
            modifier = 0

        if (valueScroll > this._offsetTop) {
            value = ((valueScroll + this._offsetTop) * 100) / this._heightTotalArticle;
        }
        modifier = (window.innerHeight * (parseInt(value, 10) / 100))
        // let stylesModifier = [
        //     'position:fixed',
        //     'left:0',
        //     'right:0',
        //     'top:' + parseInt(modifier, 10) + 'px',
        //     'height:1px',
        //     'background: blue',
        //     'z-index: 10000',
        // ];
        // this.$debug.style = stylesModifier.join(';');
        value = (((valueScroll + modifier) - this._offsetTop) * 100) / this._heightTotalArticle;

        if (0 > value || isNaN(value)) {
            value = 0
        }

        if (100 < value) {
            value = 100
        }

        return value
    }
}