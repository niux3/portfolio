export default class Styles{
    constructor(){

        let tpl = `
            <style>
                p{
                    color: #212529;
                }
            </style>
        `;
        document.head.insertAdjacentHTML('beforeend', tpl);
    }
}
