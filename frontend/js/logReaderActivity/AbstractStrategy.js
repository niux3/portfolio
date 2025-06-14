export default class AbstractStrategy{
    constructor(){
        if (new.target === AbstractStrategy) {
            throw new Error("Cannot instantiate AbstractStrategy directly")
        }
    }

    sendLog(data) {
        console.log('envoie ajax ->', data)
        //fetch('/log.php', {
            //method: 'POST',
            //body: JSON.stringify(data),
            //headers: { 'Content-Type': 'application/json' },
        //}).catch((e) => console.error("Log error:", e));
    }

    logStart(path) {
        this.sendLog({ type: 'start', path })
    }

    logClick(id) {
        this.sendLog({ type: 'click', id })
    }

    logRead50(id) {
        this.sendLog({ type: 'read', id })
    }

    logEnd(path) {
        this.sendLog({ type: 'end', path })
    }
}
