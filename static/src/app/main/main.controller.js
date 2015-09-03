(function() {
  'use strict';

  angular
    .module('static')
    .controller('MainController', MainController);

  /** @ngInject */
  function MainController(googlePlaces, places) {
    var vm = this;
    vm.places = [];
    // Search for places based geo location
    vm.search = function() {
      vm.places = [];
      googlePlaces.getPlaces()
        .then(function(places) {
          vm.spin = !vm.spin;
          return (vm.places = places);
        })
        .then(vm.ratePlaces);
    };
    // rate places
    vm.ratePlaces = function(list) {
      list.forEach(function(p) {
        if (!/^[A-Za-z][A-Za-z0-9 ]*$/.test(p.name)) {
          return;
        }
        places.ratePlace(p.name)
          .then(function(ratePlace) {
            p.rating = ratePlace.rating;
          });
      });
    };
  }
})();
