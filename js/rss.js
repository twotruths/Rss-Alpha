var startPoint = 0;

$(document).ready(function(){
   $(window).scroll(loadList);
});

function loadList(){
    if (isAtBottom()){
        startPoint += 20;
        getList();
    }
}

function reloadList(){
    startPoint = 0;
    $("#itemContainer").empty();
    loadList();
}

function isAtBottom(){
    return ((($(document).height() - $(window).height()) - $(window).scrollTop()) <= 50) ? true : false;
}

function getList(){
    $(window).unbind('scroll');
    $.post(
        'getItemList',
        {
            start:startPoint
        },
        function(data, status){
            $("#itemContainer").append(data);
            $(window).scroll(loadList);
        }
    );
}
