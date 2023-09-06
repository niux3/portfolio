class Router{
    constructor(options){
        this._routes = [];

        return this;
    }


    _clearSlashes(path){
        return path.toString().replace(/\/$/, '').replace(/^\//, '');
    }


    _getFragment(){
        let fragment = '',
            match = window.location.href.match(/#(.*)$/);
        fragment = match ? match[1] : '';
        return this._clearSlashes(fragment);
    }


    add(re, handler){
        if(typeof re == 'function') {
            handler = re;
            re = '';
        }
        this._routes.push({ re: re, handler: handler});
        return this;
    }


    remove(param){
        for(let i = 0, r; i < this._routes.length, r = this._routes[i]; i++) {
            if(r.handler === param || r.re.toString() === param.toString()) {
                this.routes.splice(i, 1);
                return this;
            }
        }
        return this;
    }


    reset(){
        this._routes = [];
        return this;
    }


    _check(f) {
        let fragment = f || this._getFragment();
        for(let i = 0; i < this._routes.length; i++) {
            let match = fragment.match(this._routes[i].re);
            if(match) {
                match.shift();
                this._routes[i].handler.apply({}, match);
                return this;
            }
        }
        return this;
    }


    listen(){
        window.addEventListener('hashchange', e =>{
            let current = this._getFragment();
            this._check(current);
        });
        return this;
    }


    navigate(path){
        path = path ? path : '';
        window.location.href = `${window.location.href.replace(/#(.*)$/, '')}#${path}`;
        return this;
    }
}
let router = new Router();
router.add(/about/, function(){
    console.log('about page !!');
});
router.add(/contact/, function(){
    console.log('contact page !!');
});
router.listen().navigate('/about');
