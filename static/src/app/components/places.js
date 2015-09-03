(function() {
  'use strict';

  angular
    .module('static')
    .service('places', PlacesService);

  /** @ngInject */
  function PlacesService($http, baseUrl) {
    this.ratePlace = function(name) {
      return $http({
        url: baseUrl + 'rate',
        method: 'GET',
        params: { place: name }
      })
      .then(function (res) {
        return res.data;
      });
    };

    this.getPhotos = function(name, geo) {
      return $http({
        url: baseUrl + 'photos',
        method: 'GET',
        params: { place: name, geo: geo }
      })
      .then(function (res) {
        return res.data;
      });
    };
  }
})();
