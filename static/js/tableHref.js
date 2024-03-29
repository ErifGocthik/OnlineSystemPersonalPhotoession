(function () {
    $(document).ready(function () {
        let classSplit = '';
        let idSplit = '';
        let id = '';
        let class_id = '';
        let tr = $('.tr-hover');
        let cookie = document.cookie
        let csrfToken = cookie.substring(cookie.indexOf('=') + 1)
        tr.mouseover(function (event) {
            classSplit = event.currentTarget.className.split(' ');
            idSplit = classSplit[classSplit.length - 1];
            id = idSplit.split('-')[idSplit.split('-').length - 1];
            class_id = $(`.id-${id}`);
            class_id.css({
                'background-color': '#d5d5d5',
                'cursor': 'pointer'
            });
            class_id.mousedown(function (e) {
                let idId = $(`.id-${id}`);
                let email = idId.find('.email').text();
                idId.css({
                    'background-color': '#e1e1e1',
                });
                $('.modal-window').find('span').html(email);
                $('.modal-background').css({'display': 'flex', 'opacity': '1'});
            });
            class_id.mouseup(function (e) {
                let idId = $(`.id-${id}`);
                idId.css({
                    'background-color': '#d5d5d5',
                });
            });
        });
        tr.mouseout(function (event) {
            classSplit = event.currentTarget.className.split(' ');
            idSplit = classSplit[classSplit.length - 1];
            id = idSplit.split('-')[idSplit.split('-').length - 1]
            $(`.id-${id}`).css({
                'background-color': '#ffffff'
            });
        });
        $('.btn-close').click(function () {
            $('.modal-background').css({'display': 'none'});
            $('.modal-window').find('textarea').val('');
        });
       $('.btn-input').click(function (e) {
           e.preventDefault();
           let answer = $('.modal-window').find('textarea').val();
           $.ajax({
               url: `/main/setanswer/${id}/`,
               type: 'post',
               dataType: 'json',
               data: {answer: answer, id: id, 'csrfmiddlewaretoken': csrfToken},
               success: function (data) {
                   // console.log(data);
                   $('.modal-background').css({'display': 'none'});
               },
               error: function (data) {
                   alert('Что-то пошло не так пожалуйста перезагрузите страницу');
               }
           })

       })
    });
})();