(function($){
    $(document).ready(function(){
        $(".view-link").on("click", function(){
            console.log("oh")
            var viewUrl = $(this).data("url");
            // window.open(viewUrl, '_blank');
        });
    });
})(django.jQuery);