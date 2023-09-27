import Element from './Element';

export default class Elements{
    constructor(selector){
        this.$els = Array.from(document.querySelectorAll(selector));
        this.$els.map($item => new Element($item));
    }
}
