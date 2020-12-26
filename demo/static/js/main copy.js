(function ($) {
  // USE STRICT
  "use strict";

  function render_skillgraph() {
    $.getJSON("http://localhost:5000/api/v1/resource/skillGraph/all", function (data) {
      console.log(data);
      try {
        //radar chart
        var ctx = document.getElementById("radarChart");
        if (ctx) {
          ctx.height = 200;
          var myChart = new Chart(ctx, {
            type: "radar",
            data: {
              labels: [
                "SUY LUẬN",
                "XỬ LÝ",
                "GHI NHỚ",
                "KỸ THUẬT",
                "SỨC KHỎE",
                "SÁNG TẠO",
                "CẢM XÚC",
                "GIAO TIẾP",
              ],
              defaultFontFamily: "Poppins",
              datasets: [
                {
                  label: "Student 1",
                  data: data,
                  borderColor: "rgba(0, 123, 255, 0.6)",
                  borderWidth: "1",
                  backgroundColor: "rgba(0, 123, 255, 0.4)",
                },
              ],
            },
            options: {
              legend: {
                position: "top",
                labels: {
                  fontFamily: "Poppins",
                },
              },
              scale: {
                ticks: {
                  beginAtZero: true,
                  fontFamily: "Poppins",
                },
              },
            },
          });
        }
      } catch (error) {
        console.log(error);
      }
    });

    
  }

  render_skillgraph();
})(jQuery);

//===============================================================================//

(function ($) {
  // USE STRICT
  "use strict";
  var navbars = ["header", "aside"];
  var hrefSelector =
    'a:not([target="_blank"]):not([href^="#"]):not([class^="chosen-single"])';
  var linkElement = navbars
    .map((element) => element + " " + hrefSelector)
    .join(", ");
  $(".animsition").animsition({
    inClass: "fade-in",
    outClass: "fade-out",
    inDuration: 900,
    outDuration: 900,
    linkElement: linkElement,
    loading: true,
    loadingParentElement: "html",
    loadingClass: "page-loader",
    loadingInner: '<div class="page-loader__spin"></div>',
    timeout: false,
    timeoutCountdown: 5000,
    onLoadEvent: true,
    browser: ["animation-duration", "-webkit-animation-duration"],
    overlay: false,
    overlayClass: "animsition-overlay-slide",
    overlayParentElement: "html",
    transition: function (url) {
      window.location.href = url;
    },
  });
})(jQuery);
