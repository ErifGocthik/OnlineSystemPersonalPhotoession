(function () {
    $(document).ready(function (event) {
        let slider = $('.slider');
        let sliders = slider.find('.slide');
        let lenght = slider.find('.slide').length;
        let index = 0;
        slider.on('mousewheel DOMMouseScroll', function (e) {
            // if (e.originalEvent.wheelDelta > 0)
            if(e.originalEvent.wheelDelta >= 0)
            {
                if (index !== 0) {
                    e.preventDefault();
                    sliders.eq(index).removeClass('active');
                    index--;
                    sliders.eq(index).addClass('active');
                }
                // console.log(e.currentTarget.className.split(''))
            } else {
                if (index !== lenght - 1) {
                    e.preventDefault();
                    sliders.eq(index).removeClass('active');
                    index++;
                    sliders.eq(index).addClass('active');
                }
            }
        });
    });
})();