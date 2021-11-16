import Portfolio from '../model/Portfolio';

export default class Controller{
    constructor(req){
        console.log('controller', req);
        new Portfolio().get()
        this._data = JSON.parse(sessionStorage.getItem('data'));
    }
}
