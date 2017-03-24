var start = null;
var timer = 0;

//when patient is arrived, start timer
$("#arrived").click(function() {
    if (start !== null) return;
    start = setInterval(function() {
        timer += 1;
        $("timer").val(value);
        }, interval);
    });

$("#checkbox").click(function() {
//    stop running timer when checkbox is checked

})
