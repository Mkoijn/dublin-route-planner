
      function initMap() {
        var start = {lat: {{start_coordinates.lat}}, lng: {{start_coordinates.lng}}};
        var start_station = {lat: {{start_station.lat}}, lng: {{start_station.lng}}};
        var finish_station = {lat: {{finish_station.lat}}, lng: {{finish_station.lng}}};
        var finish = {lat: {{finish_coordinates.lat}}, lng: {{finish_coordinates.lng}}};
        var total_time = 0;
        var directionsService = new google.maps.DirectionsService();
        var directionsDisplay = new google.maps.DirectionsRenderer();
        var mapOptions = {
                          zoom: 13,
                          center: start_station
                         }
        var map = new google.maps.Map(document.getElementById('map'), mapOptions);
        directionsDisplay.setMap(map);

        var marker = new google.maps.Marker({
          position: start,
          map: map,
          label: 'YOU'
        });

        var marker2 = new google.maps.Marker({
          position: start_station,
          map: map,
          title: '{{start_station.name}}' + '\n Available Stands: '
                  + '{{start_station.stands}}' + '\n Available Bikes: '
                  + '{{start_station.bikes}}',
          label: 'BIKES'
        });

        var marker3 = new google.maps.Marker({
          position: finish_station,
          map: map,
          title: '{{finish_station.name}}' + '\n Available Stands: '
                  + '{{finish_station.stands}}' + '\n Available Bikes: '
                  + '{{finish_station.bikes}}',
          label: 'BIKES'
        });

        var marker4 = new google.maps.Marker({
          position: finish,
          map: map,
          label: 'TARGET'
        });


        function renderDirections(result, color) {
          var directionsRenderer = new google.maps.DirectionsRenderer({suppressMarkers: true,
                                                                       suppressBicyclingLayer: true,
                                                                       polylineOptions: {
                                                                         strokeColor: color
                                                                       }
                                                                     });
          directionsRenderer.setMap(map);
          directionsRenderer.setDirections(result);
          directionsRenderer.setOptions({ preserveViewport: true });
        }

        function requestDirections(start, end, mode, color) {
          directionsService.route({
            origin: start,
            destination: end,
            travelMode: mode
          }, function(result) {
            renderDirections(result, color);
          });
        }
        requestDirections(finish_station, finish, 'WALKING', 'blue');
        requestDirections(start_station, finish_station,'BICYCLING', 'green');
        requestDirections(start, start_station, 'WALKING', 'blue');

        // Output Results
        function one(){
        var service = new google.maps.DistanceMatrixService;
        service.getDistanceMatrix({
          origins: [start],
          destinations: [start_station],
          travelMode: 'WALKING',
          unitSystem: google.maps.UnitSystem.METRIC,
          avoidHighways: false,
          avoidTolls: false
        }, function(response, status) {
          if (status !== 'OK') {
            alert('Error was: ' + status);
          } else {
            var originList = response.originAddresses;
            var destinationList = response.destinationAddresses;
            var outputDiv = document.getElementById('walk1');
            var results = response.rows[0].elements;
            outputDiv.innerHTML += originList[0] + ' to ' + destinationList[0] +
                                ': ' + '<strong>' + results[0].distance.text + ' in ' +
                                results[0].duration.text + '</strong><br>';

            var time = results[0].duration.value;
            total_time = total_time + time;
            console.log(total_time);
            console.log(time);
          }
        });
      }
        // Output Results
        function two(){
        var service2 = new google.maps.DistanceMatrixService;
        service2.getDistanceMatrix({
          origins: [start_station],
          destinations: [finish_station],
          travelMode: 'BICYCLING',
          unitSystem: google.maps.UnitSystem.METRIC,
          avoidHighways: false,
          avoidTolls: false
        }, function(response, status) {
          if (status !== 'OK') {
            alert('Error was: ' + status);
          } else {
            var originList = response.originAddresses;
            var destinationList = response.destinationAddresses;
            var outputDiv = document.getElementById('bike');
            var results = response.rows[0].elements;
            outputDiv.innerHTML += originList[0] + ' to ' + destinationList[0] +
                                ': ' + '<strong>' + results[0].distance.text + ' in ' +
                                results[0].duration.text + '</strong><br>';

            outputDiv.innerHTML += '<br>' + 'Bike Pick Up: ' + '{{start_station.name}}' + '<br>'
                                    + 'Available bikes: ' + '{{start_station.bikes}}' + '<br>';
            outputDiv.innerHTML += 'Bike Return: ' + '{{finish_station.name}}' + '<br>'
                                    + 'Available spaces: ' + '{{finish_station.stands}}' + '<br>';

            var time = results[0].duration.value;
            total_time = total_time + time;
            console.log(total_time);
            console.log(time);
          }
        });
      }
        // Output Results
        function three(){
        var service3 = new google.maps.DistanceMatrixService;
        service3.getDistanceMatrix({
          origins: [finish_station],
          destinations: [finish],
          travelMode: 'WALKING',
          unitSystem: google.maps.UnitSystem.METRIC,
          avoidHighways: false,
          avoidTolls: false
        }, function(response, status) {
          if (status !== 'OK') {
            alert('Error was: ' + status);
          } else {
            var originList = response.originAddresses;
            var destinationList = response.destinationAddresses;
            var outputDiv = document.getElementById('walk2');
            var results = response.rows[0].elements;
            outputDiv.innerHTML += originList[0] + ' to ' + destinationList[0] +
                                ': ' + '<strong>' + results[0].distance.text + ' in ' +
                                results[0].duration.text + '</strong><br>';

            var time = results[0].duration.value;
            total_time = total_time + time;
            console.log(total_time);
            console.log(time);
            var outputDiv2 = document.getElementById('time');
            outputDiv2.innerHTML = 'Total Time: ' + Math.ceil(total_time/60) + ' ' + 'minutes';
          }
        });
      }
      one();
      two();
      setTimeout(function() {
        three();
        }, 500);
  }
