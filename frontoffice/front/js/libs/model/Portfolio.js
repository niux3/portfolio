export default class Portfolio {
    constructor(){
        if(sessionStorage.getItem('data') === null){
            fetch('./public/js/export.json').then(d => d.text().then(d =>{
                sessionStorage.setItem('data', d);
            }))
            // let xhr = new XMLHttpRequest();
            // xhr.open('GET', './public/js/export.json', true);
            // xhr.addEventListener('readystatechange', e =>{
            //     sessionStorage.setItem('data', xhr.responseText);
            // });
            // xhr.send();
        }
        this._data = sessionStorage.getItem('data');
    }


    get(){
        return this._data;
    }
}
