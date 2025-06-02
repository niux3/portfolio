export default class View{
    constructor(){
        this.$progressTrue = document.getElementById('progressTrue')

        this.$progressTrue.insertAdjacentHTML('afterend', document.getElementById('tplProgressFalse').innerHTML)
        this.$progressFalse = document.getElementById('progressFalse'),
        this.$cursorProgress = document.getElementById('cursorProgress')
    }

    execute(value){
        this.$progressTrue.value = value
        this.$cursorProgress.style.width = `${value}%`
    }
}
