export default class AbstractStrategy{
    constructor(){
        if (new.target === AbstractStrategy) {
            throw new Error("Cannot instantiate AbstractStrategy directly")
        }
    }

    _sendLog(data) {
        console.log('envoie ajax ->', data)

        let headers = new Headers({
                "X-Requested-With": "XMLHttpRequest",
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded"
            }),
            //object = {},
            //formData = new FormData()

        //formData.forEach((value, key) =>{
            //object[key] = value
        //})
        //let data = Object.entries(object).map(([k,v]) => `${k}=${v}`).join('&'),
            params = {
                method: 'POST',
                headers,
                cache: 'no-cache',
                redirect: 'follow',
                referrerPolicy: 'no-referrer',
                mode: "cors",
                keepalive: true,
                body: JSON.stringify(data)
            },
            suffixUrl = '/services/pages/views-log.html',
            url = window.location.origin.includes('rb-webstudio') ? suffixUrl : `http://localhost/portfolio/public/${suffixUrl}`

        fetch(url, params).then(resp =>{
            if(resp.ok === true)
                return resp.json()
        }).then(({data, errors}) =>{
            console.log('>>', data)
        }).catch(e => console.warn("error >", e))
    }

    _logStart(path) {
        this._sendLog({ type: 'start', path })
    }

    _logClick(path) {
        this._sendLog({ type: 'click', path })
    }

    _logRead(path) {
        this._sendLog({ type: 'read', path })
    }

    _logEnd(path) {
        this._sendLog({ type: 'end', path })
    }

    execute(){
        throw new Error("Cannot instantiate AbstractStrategy directly")
    }
}
