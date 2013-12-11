var log = function(data) {
  for ( i in data ) {
    $("#log").append("<div class='panel panel-default'><div class='panel-heading'>" + $('<span/>').text(i).html() + "</div><div class='panel-body'>" + $('<span/>').text(data[i]).html() + "</div></div>");
    $("#log").stop().animate({
    scrollTop: $('#log')[0].scrollHeight
    }, 800);
  }
};

setInterval(function(){$.getJSON('/roll', log)}, 5000);