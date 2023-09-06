export default class Styles{
    constructor(){

        let tpl = `
            <style>
                p{
                    color:red;
                }
            </style>
        `;
        document.head.insertAdjacentHTML('beforeend', tpl);
    }
}