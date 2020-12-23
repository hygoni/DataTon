<!-- Styles -->
<style>
    #chartdiv {
      width: 100%;
      height: 500px;
    }
    
    </style>
    
    <!-- Resources -->
    <script src="https://cdn.amcharts.com/lib/4/core.js"></script>
    <script src="https://cdn.amcharts.com/lib/4/charts.js"></script>
    <script src="https://cdn.amcharts.com/lib/4/themes/animated.js"></script>
    
    <!-- Chart code -->
    <script>
    am4core.ready(function() {
    
    // Themes begin
    am4core.useTheme(am4themes_animated);
    // Themes end
    
    // Create chart instance
    var chart = am4core.create("chartdiv", am4charts.PieChart);
    
    // Add data
    chart.data = [ 
    {name: "먹스타그램", value: 652},
    {name: "맛스타그램", value: 269},
    {name: "일상", value: 198},
    {name: "먹방", value: 143},
    {name: "소통", value: 139},
    {name: "맞팔", value: 134},
    {name: "food", value: 118},
    {name: "맛집", value: 118},
    {name: "daily", value: 112},
    {name: "좋아요", value: 111},
    {name: "선팔", value: 100},
    {name: "데일리", value: 97},
    {name: "먹스타", value: 84},
    {name: "먹팔", value: 80},
    {name: "foodstagram", value: 76},
    {name: "instafood", value: 65},
    {name: "집밥", value: 62},
    {name: "instagood", value: 61},
    {name: "일상스타그램", value: 61},
    {name: "좋아요반사", value: 59},
    {name: "팔로우", value: 59},
    {name: "선팔하면맞팔", value: 59},
    {name: "좋반", value: 55},
    {name: "셀스타그램", value: 53},
    {name: "fff", value: 52},
    {name: "먹스타맞팔", value: 52},
    {name: "jmt", value: 51},
];
    
    // Add and configure Series
    var pieSeries = chart.series.push(new am4charts.PieSeries());
    pieSeries.dataFields.value = "value";
    pieSeries.dataFields.category = "name";
    pieSeries.slices.template.stroke = am4core.color("#fff");
    pieSeries.slices.template.strokeWidth = 2;
    pieSeries.slices.template.strokeOpacity = 1;
    
    // This creates initial animation
    pieSeries.hiddenState.properties.opacity = 1;
    pieSeries.hiddenState.properties.endAngle = -90;
    pieSeries.hiddenState.properties.startAngle = -90;
    
    }); // end am4core.ready()
    </script>
    
    <!-- HTML -->
    <div id="chartdiv"></div>