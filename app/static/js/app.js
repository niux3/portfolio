$(function(){
    if($('.slug').length){
        $('.name').on('keyup', function(){
            $('.slug').val($(this).val().slugify());
        });
    }
    if($('.description').length){
        $('.description').on('keyup', function(){
            if($(this).val() === 'lorem'){
                $(this).val("Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet laborum illum maxime iusto minima reiciendis praesentium labore ab, sed sapiente officia enim consequuntur atque non rerum nostrum quibusdam rem molestiae!")
            }
        });
    }
    if($('.toggle-online.btn-danger, .delete').length){
        $('.toggle-online.btn-success, .delete').on('click', function(e){
            var answer = $(this).hasClass('delete')? "supprimer" : 'mettre hors ligne';
            var response = confirm("Voulez vous vraiment "+ answer +" cet article ?");
            if(!response){
                e.preventDefault();
            }
        });
    }
});