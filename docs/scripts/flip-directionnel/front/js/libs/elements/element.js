import Style from '../styles/style';

export default class Element{
    constructor($el){
        this.$el = $el;
        new Style();
        console.log(">>>", this.$el);
    }
}