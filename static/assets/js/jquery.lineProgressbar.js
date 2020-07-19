/**
 * jQuery Line Progressbar
 * Author: KingRayhan<rayhan095@gmail.com>
 * Author URL: http://rayhan.info
 * Version: 1.0.0
 */

(function ($) {
    'use strict';


    $.fn.LineProgressbar = function (options) {

        options = $.extend({
            percentage: null,
            ShowProgressCount: true,
            duration: 1000,

            // Styling Options
            fillBackgroundColor: '#3498db',
            backgroundColor: '#EEEEEE',
            radius: '0px',
            height: '10px',
            width: '100%'
        }, options);

        $.options = options;
        return this.each(function (index, el) {
            // Markup
            $(el).html('<div class="progressbar"><div class="proggress"></div><div class="percentCount"></div></div>');



            var progressFill = $(el).find('.proggress');
            var progressBar = $(el).find('.progressbar');
            var percentCount = $(el).find('.percentCount');


            progressFill.css({
                backgroundColor: options.fillBackgroundColor,
                height: options.height,
                borderRadius: options.radius
            });
            progressBar.css({
                width: options.width,
                backgroundColor: options.backgroundColor,
                borderRadius: options.radius
            });
            percentCount.css({
                'margin-left': options.percentage + '%'
            });

            // Progressing
            progressFill.animate(
                {
                    width: options.percentage + "%"
                },
                {
                    step: function (x) {
                        if (options.ShowProgressCount) {
                            $(el).find(".percentCount").text(Math.round(x) + "%");
                        }
                    },
                    duration: options.duration
                }
            );
            ////////////////////////////////////////////////////////////////////
        });
    }
    $.fn.progressTo = function (next) {

        let options = $.options;

        return this.each(function (index, el) {

            var progressFill = $(el).find('.proggress');
            var progressBar = $(el).find('.progressbar');

            progressFill.animate(
                {
                    width: next + "%"
                },
                {
                    step: function (x) {
                        if (options.ShowProgressCount) {
                            $(el).find(".percentCount").text(Math.round(x) + "%");
                        }
                    },
                    duration: options.duration
                }
            );
            ////////////////////////////////////////////////////////////////////
        });
    }

})(jQuery);