import Portfolio from '../model/Portfolio';

export default class Controller{
    constructor(req){
        new Portfolio().get()
        this._data = JSON.parse(sessionStorage.getItem('data'));
    }
}
