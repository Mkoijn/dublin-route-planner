function renderDirections(result, map, poly) {

  poly.setMap(map);
  poly.setDirections(result);
  poly.setOptions({ preserveViewport: true });
}

function requestDirections(start, end, mode, map, poly, directionsService) {
  directionsService.route({
    origin: start,
    destination: end,
    travelMode: mode
  }, function(result) {
    renderDirections(result, map, poly);
  });
}
