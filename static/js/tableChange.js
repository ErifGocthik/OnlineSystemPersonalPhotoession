// '<a href="#" class="btn-self-reservations"> ◀ </a> Ваши запросы <a href="#" class="btn-self-reservations"> ▶ </a>'
(function () {
    $(document).ready(function (event) {
        let tables = $('.user_reviews').find('table');
        let index = 1;
        $('.btn-change').click(function () {
            if (index === 0) {
                tables.eq(index).removeClass('visible');
                index++;
                tables.eq(index).addClass('visible');
                $('.user_reviews').find('span').text('Ваши запросы');
                console.log(index);
            } else {
                tables.eq(index).removeClass('visible');
                index--;
                tables.eq(index).addClass('visible');
                $('.user_reviews').find('span').text('Входящие запросы');
                console.log(index);
            }
        });
    });
})();