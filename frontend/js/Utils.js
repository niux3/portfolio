export default class Utils{
    static debounce(func, wait, immediate, context){
        var result,
            timeout = null;
        return function() {
            var ctx = context || this, args = arguments;
            var later = function() {
                timeout = null;
                if (!immediate) result = func.apply(ctx, args);
            };
            var callNow = immediate && !timeout;
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
            if (callNow) result = func.apply(ctx, args);
            return result;
        };
    }

    static throttle(func, wait, leading, trailing, context){
        var ctx, args, result,
            timeout = null,
            previous = 0,
            later = function() {
                previous = new Date;
                timeout = null;
                result = func.apply(ctx, args);
            };
        return function() {
            var now = new Date;
            if (!previous && !leading) previous = now;
            var remaining = wait - (now - previous);
            ctx = context || this;
            args = arguments;
            // Si la période d'attente est écoulée
            if (remaining <= 0) {
                // Réinitialiser les compteurs
                clearTimeout(timeout);
                timeout = null;
                // Enregistrer le moment du dernier appel
                previous = now;
                // Appeler la fonction
                result = func.apply(ctx, args);
            } else if (!timeout && trailing) {
                // Sinon on s’endort pendant le temps restant
                timeout = setTimeout(later, remaining);
            }
            return result;
        };
    }

    static slugify(text) {
        return text
            .normalize('NFD')
            .replace(/[\u0300-\u036f]/g, '')
            .toLowerCase()
            .trim()
            .replace(/[^a-z0-9 -]/g, '')
            .replace(/\s+/g, '-')
            .replace(/-+/g, '-')
    }

    static isMobile() {
        const userAgent = navigator.userAgent || navigator.vendor || window.opera;
        const isMobileUA = /android|iphone|ipad|ipod|opera mini|iemobile|blackberry|webos/i.test(userAgent.toLowerCase());
        const isTouch = window.matchMedia("(pointer: coarse)").matches;
        return isMobileUA || isTouch;
    }
}
