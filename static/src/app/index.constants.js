/* global google:false, moment:false */
(function() {
  'use strict';
  angular
    .module('static')
    .constant('moment', moment)
    .constant('google', google);
})();