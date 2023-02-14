$(function() {
    var make_weather_display = function(data) {
        $('.weather-res .city').text(data.city);
        $('.weather-res .temp').text(data.temp);
        $('.weather-res img').attr("src", data.icon);
        $('.weather-res .text').text(data.text);
        $('.weather-res .max').text('H: ' + data.maxtemp + '&deg');
        $('.weather-res .min').text('L: ' + data.mintemp + '&deg');
        $('.weather-res').removeClass("hide");
    }
    $('.weather-box input[type=submit]').click(function() {
        var query = $('.weather-box input[type=text]').val();
        $.post("js/api",
            {
                q: query,
            },
            function(data, status) {
                console.log(data);
                make_weather_display(data);
            }
        )
    });
});