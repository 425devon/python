$(document).ready(function(){
    $( ".draggable" ).draggable({
        containment: '.container', 
        scroll: false
    });
    $('.draggable').mouseup(function(){
        var pos = $(this).position();
        var id = ($(this).attr('id'))
        var info = {'top': pos.top,'left':pos.left,'id':id}
        console.log(pos)
        $.ajax({
            url: '/notes/location',
            method: 'post',
            data: {'top': pos.top,'left':pos.left,'id':id},
            success: function(serverResponse){
                console.log("Success recieved")
            }
        })
    })
     
    $('#create').keydown(function(e){
        if(e.which == 13){
            $.ajax({
                url: '/notes/create',
                method: 'post',
                data: $(this).serialize(),
                success: function(serverResponse){
                    $('#newNote').append(serverResponse);
                    document.getElementById("create").reset();
                    $(function() {
                        $( ".draggable" ).draggable({
                            containment: '.container', 
                            scroll: false
                        });
                        $('.draggable').mouseup(function(){
                            var pos = $(this).position();
                            var id = ($(this).attr('id'))
                            var info = {'top': pos.top,'left':pos.left,'id':id}
                            console.log(pos)
                            $.ajax({
                                url: '/notes/location',
                                method: 'post',
                                data: {'top': pos.top,'left':pos.left,'id':id},
                                success: function(serverResponse){
                                    console.log("Success recieved")
                                }
                            })
                        })
                     });
                }
            })
        }
    })
    
    
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    
})