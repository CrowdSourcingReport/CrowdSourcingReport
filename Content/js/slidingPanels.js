$(function(){
    
        // Top projects pane configuration
        $("#top_proj").carouFredSel({
            items        : 1,
            direction    : "up",
            responsive    : true,
            auto        : false,
            pagination    : {
                        container    : ".menu",
                        anchorBuilder    : false
                          }
        });
});
