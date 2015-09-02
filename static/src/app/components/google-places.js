(function() {
  'use strict';

  angular
    .module('static')
    .service('GooglePlaces', GooglePlacesService);

  /** @ngInject */
  function GooglePlacesService(google, $q) {
    this.getPlaces = function() {
      return $q(function(resolve, reject) {
        navigator.geolocation.getCurrentPosition(function(loc) {
          // Get coordinate
          var latitude = loc.coords.latitude;
          var longitude = loc.coords.longitude;
          var latlng = new google.maps.LatLng(latitude, longitude);
          var map = new google.maps.Map(document.getElementById('map'), {
            zoom: 12,
            center: latlng,
            mapTypeId: google.maps.MapTypeId.ROADMAP
          });
          var service = new google.maps.places.PlacesService(map);
          service.nearbySearch({
            location: latlng,
            radius: '500',                    // TODO:
            types: ['bars', 'restaurant']     // Move to config
          }, onSuccess);
          function onSuccess(results, status) {
            if (status != google.maps.places.PlacesServiceStatus.OK) reject('Failed to get places');
            else resolve(results);
          }
        });
      });
    };
  }
})();
