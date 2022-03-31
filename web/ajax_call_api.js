$(document).ready(function(){

    function addTable(data) {
        //console.log(data);
        var obj_length = Object.keys(data['City']).length;
        var t = document.getElementById("cityList");
        var markup = '<table class="w3-table-all"><tr>';
        markup += "<th>Country</th><th>City</th><th>Region</th>";
        markup += "<th>Latitude</th><th>Longitude</th></tr>";
        for(var i = 0; i < obj_length; i++) {
          markup += "<tr>" + "<td>" + data['Country'][i].toUpperCase() + "</td>";
          markup += "<td>" + data['City'][i] + "</td>";
          markup += "<td>" + data['Region'][i] + "</td>";
          markup += "<td>" + data['Latitude'][i] + "</td>";
          markup += "<td>" + data['Longitude'][i] + "</td></tr>";
        }
        markup += "</table>"
        t.innerHTML = markup;
    }
    
    $("#getData").click(function(){
    var latitude = document.getElementById("latitude").value;
    var json = { latitude: latitude };
    $.ajax({
            url: "http://127.0.0.1/api/query",
            type: "POST",
            crossDomain: true,
            data: JSON.stringify(json),
            contentType: "application/json",
            success: function (response) {
                var data = JSON.parse(response);
                addTable(data);
            },
            error: function (xhr, status) {
                alert("error");
            }
        });
    });

});