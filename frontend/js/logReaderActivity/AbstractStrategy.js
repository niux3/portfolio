export default class AbstractStrategy{
    constructor(){
        if (new.target === AbstractStrategy) {
            throw new Error("Cannot instantiate AbstractStrategy directly")
        }
    }

    _sendLog(data) {
        data = {...data, 'theme': localStorage.getItem('theme')}
        let headers = new Headers({
                "X-Requested-With": "XMLHttpRequest",
                "Accept": "application/json",
            }),
            formData = new FormData()

        for (let key in data) {
            formData.append(key, data[key])
        }
        let params = {
                method: 'POST',
                headers,
                cache: 'no-cache',
                redirect: 'follow',
                referrerPolicy: 'no-referrer',
                mode: "cors",
                keepalive: true,
                body: formData
            },
            suffixUrl = '/services/pages/views-log.html',
            url = window.location.origin.includes('rb-webstudio') ? suffixUrl : `http://localhost/portfolio/public/${suffixUrl}`

        fetch(url, params).then(resp =>{
            if(resp.ok === true) return resp.json()
        }).catch(e => console.warn("error >", e))
    }

    _logStart(path) {
        throw new Error("Cannot instantiate AbstractStrategy directly")
    }

    _logClick(path) {
        throw new Error("Cannot instantiate AbstractStrategy directly")
    }

    _logRead(path) {
        throw new Error("Cannot instantiate AbstractStrategy directly")
    }

    _logEnd(path) {
        throw new Error("Cannot instantiate AbstractStrategy directly")
    }

    execute(){
        throw new Error("Cannot instantiate AbstractStrategy directly")
    }
}
