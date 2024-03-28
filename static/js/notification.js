(function () {
    $(document).ready(function (e) {
        // e.preventDefault();
        // let notification = document.getElementsByClassName('notification')[0]
        $('.reservation-btn').click(function (event) {
            event.preventDefault();
            alert(`${$('#id_email').val()}`)
            $.ajax({
                url: `/main/reservation/`,
                type: 'POST',
                dataType: 'json',
                success: function (response) {
                    $('.notification').html(`${response['notification']}`)
                },
                error: function (response) {
                    console.error(response)
                },
            });
        })
    })
})();