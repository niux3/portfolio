import Request from '../request/Request';
import Router from '../router/Router';
import * as Controllers from '../controller/index';


export default class Dispatcher{
    constructor(){
        this._request = new Request();
    }


    run(){
        let router = new Router();
        ['load', 'hashchange'].forEach(event =>{
            window.addEventListener(event, e =>{
                try{
                    this._request.controller = null;
                    this._request.params = null;
                    this._request.action = null;
                    this._request.url = window.location.hash;
                    router.check(this._request);
                    let controller = this._load();
                    controller[this._request.action].apply({}, this._request.params);
                }catch(e){
                    this._errors(e);
                }
            });
        });
    }


    _load(){
        try{
            return new Controllers[this._request.controller](this._request);
        }catch(e){
            this._errors(e);
        }
    }

    _errors(e){
        let controller = new Controllers['ErrorsController'](this._request);
        controller['e404']();
    }


    navigateTo(path){
        path = path ? path : '';
        window.location.href = `${window.location.href.replace(/#(.*)$/, '')}#${path}`;
        return this;
    }
}
