(function() {
  'use strict';

  angular
    .module('static')
    .service('places', PlacesService);

  /** @ngInject */
  function PlacesService($http) {
    this.ratePlace = function(name) {
      return $http({
        url: 'rate',
        method: 'GET',
        params: { place: name }
      })
      .then(function (res) {
        return res.data;
      });
    };
  }
})();
