(function() {
  'use strict';

  angular
    .module('static')
    .service('googlePlaces', GooglePlacesService);

  /** @ngInject */
  function GooglePlacesService(google, $q, $window) {
    this.getPlaces = function() {
      return $q(function(resolve, reject) {
        $window.navigator.geolocation.getCurrentPosition(function(loc) {
          // Get coordinate
          var latitude = loc.coords.latitude
            , longitude = loc.coords.longitude
            , latlng = new google.maps.LatLng(latitude, longitude)
            , map = new google.maps.Map($window.document.getElementById('map'), {
              zoom: 12,
              center: latlng,
              mapTypeId: google.maps.MapTypeId.ROADMAP
            })
            , service = new google.maps.places.PlacesService(map);
          service.nearbySearch({
            location: latlng,
            radius: '500',                    // TODO:
            types: ['bars', 'restaurant']     // Move to config or based arguments
          }, onSuccess);
          function onSuccess(places, status) {
            return status !== google.maps.places.PlacesServiceStatus.OK
              ? reject('Failed to get places')
              : resolve(places.map(function(p) {
                // Calculate distance
                var disFn = google.maps.geometry.spherical.computeDistanceBetween
                  , pLat = new google.maps.LatLng(p.geometry.location.G, p.geometry.location.K);
                p.distance = disFn(latlng, pLat);
                return p;
              }));
          }
        });
      });
    };
  }
})();
