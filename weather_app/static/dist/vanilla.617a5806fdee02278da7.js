$((function(){$(".weather-box input[type=submit]").click((function(){var e=$(".weather-box input[type=text]").val();$.post("js/api",{q:e},(function(e,t){console.log(e),function(e){$(".weather-res .city").text(e.city),$(".weather-res .temp").text(e.temp),$(".weather-res img").attr("src",e.icon),$(".weather-res .text").text(e.text),$(".weather-res .max").text("H: "+e.maxtemp+"&deg"),$(".weather-res .min").text("L: "+e.mintemp+"&deg"),$(".weather-res").removeClass("hide")}(e)})).fail((function(e,t){console.log(e.responseJSON.error),alert(e.responseJSON.error)}))}))}));