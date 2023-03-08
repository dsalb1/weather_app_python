/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./src/js/vanilla_js.js":
/*!******************************!*\
  !*** ./src/js/vanilla_js.js ***!
  \******************************/
/***/ (() => {

eval("$(function() {\n    var make_weather_display = function(data) {\n        $('.weather-res .city').text(data.city);\n        $('.weather-res .temp').text(data.temp);\n        $('.weather-res img').attr(\"src\", data.icon);\n        $('.weather-res .text').text(data.text);\n        $('.weather-res .max').text('H: ' + data.maxtemp + '&deg');\n        $('.weather-res .min').text('L: ' + data.mintemp + '&deg');\n        $('.weather-res').removeClass(\"hide\");\n    }\n    $('.weather-box input[type=submit]').click(function() {\n        var query = $('.weather-box input[type=text]').val();\n        $.post(\"js/api\",\n            {\n                q: query,\n            },\n            function(data, status) {\n                console.log(data);\n                make_weather_display(data);\n            }\n        ).fail(function(data, status) {\n            console.log(data.responseJSON[\"error\"])\n            alert(data.responseJSON[\"error\"]);\n        });\n    });\n});\n\n//# sourceURL=webpack://assets/./src/js/vanilla_js.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./src/js/vanilla_js.js"]();
/******/ 	
/******/ })()
;