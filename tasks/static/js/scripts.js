(function(win,doc){  //funcao para confirmar a deletação
    'use strict';

    //Vericamos  se realmente ira deletar o dado
    if(doc.querySelector('.delete-btn')){
        let btnDel = doc.querySelectorAll('.delete-btn');
        for(let i=0; i < btnDel.length; i++){
            btnDel[i].addEventListener('click', function(event){
                if(confirm('Deseje mesmo deletar? ')){
                    return true;
                }else{
                    event.preventDefault();
                }
            });
        }
    }
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    var baseUrl =  window.location.origin;
    var filter = $('#filter');

    $(searchBtn).on('click',function() {
        searchForm.submit();
    });

    $(filter).change(function() {
       var filter = $(this).val();
       window.location.href = baseUrl + '?filter=' + filter;
    });

})(window,document);
