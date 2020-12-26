(function ($) {
  // USE STRICT
  "use strict";

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
              data: [65, 59, 66, 45, 56, 55, 40, 12],
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
})(jQuery);
