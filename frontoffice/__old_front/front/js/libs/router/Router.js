import routes from './routes';

export default class Router{
    constructor() {
        this._routes = routes;
    }


    getFragment(){
        let match = window.location.href.match(/#(.*)$/);
        return match ? match[1] : '';
    }


    check(request){
        for(let i = 0, len = this._routes.length; i < len; i++){
            let route = this._routes[i],
                matches = this.getFragment().match(route.re);
            if(matches){
                let [action, controller] = route.action.split('@');

                request.controller = controller;
                request.action = action;
                request.params = matches.slice(1);
                break;
            }
        }
    }

}
