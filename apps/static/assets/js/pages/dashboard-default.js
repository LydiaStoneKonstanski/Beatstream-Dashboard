'use strict';
document.addEventListener('DOMContentLoaded', function () {
  setTimeout(function () {
    floatchart();
  }, 500);
});

var sparkline_options = {
      chart: {
        type: 'line',
        height: 90,
        sparkline: {
          enabled: true
        }
      },
      dataLabels: {
        enabled: false
      },
      colors: ['#FFF'],
      stroke: {
        curve: 'smooth',
        width: 3
      },
      series: [
      ],
      yaxis: {
        min: 5,
        max: 95
      },
      tooltip: {
        theme: 'dark',
        fixed: {
          enabled: false
        },
        x: {
          show: false
        },
        y: {
          title: {
            formatter: function (seriesName) {
              return 'Total Earning';
            }
          }
        },
        marker: {
          show: false
        }
      }
    };

function apiget(api_url){
    const headers = {
        headers: {'Content-Type': 'application/json'}
    }
    return fetch("/api/"+api_url, {
        method: "GET",
        headers: headers
        }).then(response => response.json())
}


function floatchart() {
    apiget('graphdata').then(data => {
        (function () {
        var options = sparkline_options;
        options['series'] = [
        {
          name: 'series1',
          data: data
        }];
        var chart = new ApexCharts(document.querySelector('#tab-chart-1'), options);
        chart.render();
        })();
         });
  apiget('modelscores').then(data => {
  (function () {
    var options = {
      chart: {
        type: 'bar',
        height: 480,
        stacked: true,
        toolbar: {
          show: false
        }
      },
      plotOptions: {
        bar: {
          horizontal: true,
          columnWidth: '50%'
        }
      },
      dataLabels: {
        enabled: false
      },
      colors: ['#2196f3', '#aad7da'],
      series: data['series'],
      responsive: [
        {
          breakpoint: 480,
          options: {
            legend: {
              position: 'bottom',
              offsetX: -10,
              offsetY: 0
            }
          }
        }
      ],
      xaxis: {
        type: 'category',
        categories: data['categories']
      },
      grid: {
        strokeDashArray: 4
      },
      tooltip: {
        theme: 'dark'
      }
    };
    var chart = new ApexCharts(document.querySelector('#growthchart2'), options);
    chart.render();
  })();
  });
}
