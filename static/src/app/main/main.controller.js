(function() {
  'use strict';

  angular
    .module('static')
    .controller('MainController', MainController);

  /** @ngInject */
  function MainController(googlePlaces) {
    var vm = this;
    vm.places = [];
    vm.search = function() {
      vm.places = [];
      googlePlaces.getPlaces()
        .then(function(places) {
          vm.spin = !vm.spin;
          vm.places = places;
        });
    };
  }
})();
