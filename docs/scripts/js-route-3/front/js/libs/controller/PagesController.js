export default class PagesController{
    constructor(req){
        console.log('pagesController loaded', req);
    }


    about(){
        document.getElementById('app').innerHTML = `
            <h1>à propos de nous</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Maxime illum, autem dignissimos. Est saepe consectetur itaque repellendus ab eum eveniet modi temporibus, minima maiores, veniam optio doloremque. Possimus dolore, iure.</p>
        `;
    }


    contact(){
        document.getElementById('app').innerHTML = `
            <h1>contact</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Maxime illum, autem dignissimos. Est saepe consectetur itaque repellendus ab eum eveniet modi temporibus, minima maiores, veniam optio doloremque. Possimus dolore, iure.</p>
        `;
    }
}
