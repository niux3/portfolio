import Controller from './Controller';

export default class ProjectsController extends Controller{
    constructor(req){
        super(req);
    }


    project(id, slug){
        console.log('>> ', this._data.find(r => r.id === parseInt(id, 10)));
        // document.getElementById('app').innerHTML = `
        //     <h1>${id} - ${slug}</h1>
        //     <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eaque velit omnis quia soluta, a eligendi animi iusto fugiat reiciendis unde ab consequuntur aspernatur harum, voluptatum tempore, praesentium aut molestiae. Atque! Lorem ipsum dolor sit amet, consectetur adipisicing elit. Expedita quibusdam et vero quidem recusandae impedit, ipsam laudantium molestias sapiente, voluptas maxime rerum numquam, eius facere at amet ipsum, alias praesentium!</p>
        // `;
    }
}
