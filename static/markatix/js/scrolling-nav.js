//jQuery to collapse the navbar on scroll
$(window).scroll(function() {
    if ($(".navbar").offset().top > 50) {
        $(".navbar-fixed-top").addClass("top-nav-collapse");
        $(".navbar-brand").addClass("navbar-brand-1");
        $(".navbar-styling").addClass("navbar-styling-1");
        $(".navbar-right").addClass("navbar-right-1");
        $(".dropdown-details").addClass("dropdown-details-1");
        $(".dropdown-heading").addClass("dropdown-heading-1");
    } else {
        $(".navbar-fixed-top").removeClass("top-nav-collapse");
        $(".navbar-brand").removeClass("navbar-brand-1");
        $(".navbar-styling").removeClass("navbar-styling-1");
        $(".navbar-right").removeClass("navbar-right-1");
        $(".dropdown-details").removeClass("dropdown-details-1");
        $(".dropdown-heading").removeClass("dropdown-heading-1");
    }
});

//jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
    $(document).on('click', 'a.page-scroll', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
});
