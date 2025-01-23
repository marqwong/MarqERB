const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

$(document).ready(function(){
    setTimeout(()=>{
        $("#message").fadeOut("slow");
    },3000);
});