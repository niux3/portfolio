export default class Utils{
    static debounce(callback, delay){
        let timer;
        return function(){
            let args = arguments;
            let context = this;
            clearTimeout(timer);
            timer = setTimeout(function(){
                callback.apply(context, args);
            }, delay)
        }
    }

    static throttle(callback, delay) {
        let last;
        let timer;
        return function () {
            let context = this;
            let now = +new Date();
            let args = arguments;
            if (last && now < last + delay) {
                // le délai n'est pas écoulé on reset le timer
                clearTimeout(timer);
                timer = setTimeout(function () {
                    last = now;
                    callback.apply(context, args);
                }, delay);
            } else {
                last = now;
                callback.apply(context, args);
            }
        };
    }
}
