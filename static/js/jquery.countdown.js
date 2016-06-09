(function(jQuery){
    
    var aoSegments = [
        {
            title: 'Days',
            milliseconds: 24 * 60 * 60 * 1000,
            digits: 4
        },
        {
            title: 'Hours',
            milliseconds: 60 * 60 * 1000,
            digits: 2
        },
        {
            title: 'Minutes',
            milliseconds: 60 * 1000,
            digits: 2
        },
        {
            title: 'Seconds',
            milliseconds: 1000,
            digits: 2
        }
    ];
    
    var iRepeatInterval = 1000;
    
    // Creating the plugin
    jQuery.fn.countdown = function(prop){
        
        var options = jQuery.extend({
            timestamp   : 0,
            movement: 0
        }, prop);
        
        // Initialize the plugin
        init(this, options);
        
        var jSlots = this.find('.digit-slot');
        
        (function Update(){

            // calc milliseconds remaining until deadline
            var iMillisecondsLeft = Math.max(0, Math.floor((options.timestamp - new Date())));
            var sCountdown = '';
            // for each countdown display segment
            for (var i = 0; i < aoSegments.length; ++i) {
            // calculate the displayable value
                var iSegment = Math.floor(iMillisecondsLeft / aoSegments[i].milliseconds);
                // add it to the countdown string, padded with leading zeroes
                sCountdown += ('0000000000' + iSegment).slice(-aoSegments[i].digits)
                // decrease the unprocessed milliseconds 
                iMillisecondsLeft -= iSegment * aoSegments[i].milliseconds;
            }
            // update all the digits
            for (var i = 0; i < sCountdown.length; ++i) {
                switchDigit(jSlots.eq(i), sCountdown.charAt(i));
            }

            // schedule a repeat of this function
            setTimeout(Update, iRepeatInterval);
        })();
        
        return this;

        // utility functions 
                
        function init(elem, options) {
            elem.addClass('countdown');
            for (var i = 0; i < aoSegments.length; ++i) {
                var sHTML = '<div class="segment '+aoSegments[i].title+'"><div class="digits">';
                for (var j = 0; j < aoSegments[i].digits; ++j) {
                    sHTML += '<div class="digit-slot"><div class="digit">0</div></div>';
                }
                sHTML += '</div><div class="title">'+aoSegments[i].title+'</div><div class="divider"></div></div>';
                jQuery(sHTML).appendTo(elem);
            }
        }
    
        // Creates an animated transition between the two numbers
        function switchDigit(slot,number){
            
            var digit = slot.find('.digit');
            
            if (digit.is(':animated') || slot.data('digit') == number) {
                return;
            }
            
            slot.data('digit', number);
            
            var replacement = jQuery('<div>',{
                'class': 'digit',
                css: { top: -options.movement, opacity: 0 },
                html: number
            });
            
            digit
                .before(replacement)
                .animate({ top: options.movement, opacity: 0 }, 300);
                
            replacement
                .animate({ top: 0, opacity: 1 }, 300 ,function(){ digit.remove() });
    
        }
        
    };

})(jQuery);