$(document).ready(function() {

    $(".filter-button").click(function() {
        var value = $(this).attr('data-filter');

        if (value == "all") {
            //$('.filter').removeClass('hidden');
            $('.filter').show('1000');
        } else {
            //            $('.filter[filter-item="'+value+'"]').removeClass('hidden');
            //            $(".filter").not('.filter[filter-item="'+value+'"]').addClass('hidden');
            $(".filter").not('.' + value).hide('3000');
            $('.filter').filter('.' + value).show('3000');

        }
    });


    // if ($(".filter-button").removeClass("active")) {
    //     $(this).removeClass("active");
    // }
    // $(this).addClass("active");

    $('[data-filter=".blog"]').click();
    $(".tabs-try li p").on("click", function() {
        $(".tabs-try li").toggleClass("active", false)
        $(this).parent().toggleClass("active", true);

    });



    var clickEvent = false;
    $('#myCarousel').carousel({
        interval: 4000
    }).on('click', '.list-group li', function() {
        clickEvent = true;
        $('.list-group li').removeClass('active');
        $(this).addClass('active');
    }).on('slid.bs.carousel', function(e) {
        if (!clickEvent) {
            var count = $('.list-group').children().length - 1;
            var current = $('.list-group li.active');
            current.removeClass('active').next().addClass('active');
            var id = parseInt(current.data('slide-to'));
            if (count == id) {
                $('.list-group li').first().addClass('active');
            }
        }
        clickEvent = false;
    });


    $(window).load(function() {
        var boxheight = $('#myCarousel .carousel-inner').innerHeight();
        var itemlength = $('#myCarousel .item').length;
        var triggerheight = Math.round(boxheight / itemlength + 1);
        $('#myCarousel .list-group-item').outerHeight(triggerheight);
    })
});


$(document).ready(
    function() {
        $('[data-filter="blog"]').click()
    }
);


$('.view-more').click(function(e) {
    e.preventDefault();
    $(this).prev('p').slideToggle();
    $(this).html('close');
});


$(document).ready(function() {
    $('#selectId').change(function() {
        var selectVal = $("#selectId option:selected").val();
        alert(selectVal);
        $('form').attr('action', selectVal);
    });

});

// $(document).ready(function(){
//     debugger;
//     var date_input= $('#arr-date'); //our date input has the name "date"
//     var date_input1= $('#dep-date'); //our date input has the name "date"
//     debugger;
//     alert(date_input);
//     var container= $('.bootstrap-iso form').length>0 ? $('.bootstrap-iso form').parent() : "body";
//     var options={
//         format: 'mm/dd/yyyy',
//         container: container,
//         todayHighlight: true,
//         autoclose: true,
//     };
//     $( "#datepicker6" ).datepicker(options);
//     date_input1.datepicker(options);
     
// });
 $(document).ready(function(){
      var date_input=$('input[name="date"]'); //our date input has the name "date"

      var container=$('.bootstrap-iso form').length>0 ? $('.bootstrap-iso form').parent() : "body";
      var options={
        format: 'dd/mm/yyyy',
        container: container,
        todayHighlight: true,
        autoclose: true,
      };
      date_input.datepicker(options);
    });

//  $(document).ready(function () {
//     $('#arr-date').datepicker({
//         onSelect: function (dateText, inst) {
//             $('#dep-date').datepicker('options', 'minDate', new Date(dateText));
//         },
//     });

//     $('#dep-date').datepicker({
//         onSelect: function (dateText, inst) {
//             $('#arr-date').datepicker('options', 'maxDate', new Date(dateText));
//         }
//     });
// });



$(document).ready(function() {
    $('#datetimepicker6').datetimepicker();
    $('#datetimepicker7').datetimepicker({
        useCurrent: false //Important! See issue #1075
    });
    $("#datetimepicker6").on("dp.change", function(e) {
        $('#datetimepicker7').data("DateTimePicker").minDate(e.date);
    });
    $("#datetimepicker7").on("dp.change", function(e) {
        $('#datetimepicker6').data("DateTimePicker").maxDate(e.date);
    });
});