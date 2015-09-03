(function() {
  'use strict';

  angular
    .module('static')
    .controller('MainController', MainController);

  /** @ngInject */
  function MainController(googlePlaces, places, $interval) {
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
          p.dValue = -1;
          return;
        }
        var stop = $interval(function() {
          p.dValue = (p.dValue || 0) + Math.random();
        }, 300);
        places.ratePlace(p.name)
          .then(function(ratePlace) {
            $interval.cancel(stop);
            p.rating = ratePlace.rating;
            p.dValue = 100;
          });
      });
    };
  }
})();
