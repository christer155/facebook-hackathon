!function(){"use strict";angular.module("static",["ui.router","ngMaterial"])}(),function(){"use strict";function e(e,t,a){var n=this;n.places=[],n.search=function(){n.places=[],e.getPlaces().then(function(e){return n.spin=!n.spin,n.places=e}).then(n.ratePlaces)},n.ratePlaces=function(e){e.forEach(function(e){if(!/^[A-Za-z][A-Za-z0-9 ]*$/.test(e.name))return void(e.dValue=-1);var n=a(function(){e.dValue=(e.dValue||0)+Math.random()},300);t.ratePlace(e.name).then(function(t){a.cancel(n),e.rating=t.rating,e.dValue=100})})}}angular.module("static").controller("MainController",e),e.$inject=["googlePlaces","places","$interval"]}(),function(){"use strict";function e(e){this.ratePlace=function(t){return e({url:"rate",method:"GET",params:{place:t}}).then(function(e){return e.data})}}angular.module("static").service("places",e),e.$inject=["$http"]}(),function(){"use strict";function e(e,t,a){this.getPlaces=function(){return t(function(t,n){a.navigator.geolocation.getCurrentPosition(function(i){function c(a,i){return i!==e.maps.places.PlacesServiceStatus.OK?n("Failed to get places"):t(a.map(function(t){var a=e.maps.geometry.spherical.computeDistanceBetween,n=new e.maps.LatLng(t.geometry.location.G,t.geometry.location.K);return t.distance=a(s,n),t.rating=0,t}))}var r=i.coords.latitude,o=i.coords.longitude,s=new e.maps.LatLng(r,o),l=new e.maps.Map(a.document.getElementById("map"),{zoom:12,center:s,mapTypeId:e.maps.MapTypeId.ROADMAP}),u=new e.maps.places.PlacesService(l);u.nearbySearch({location:s,radius:"500",types:["bars","restaurant"]},c)})})}}angular.module("static").service("googlePlaces",e),e.$inject=["google","$q","$window"]}(),function(){"use strict";function e(e){e.debug("runBlock end")}angular.module("static").run(e),e.$inject=["$log"]}(),function(){"use strict";function e(e,t){e.state("home",{url:"/",templateUrl:"app/main/main.html",controller:"MainController",controllerAs:"main"}),t.otherwise("/")}angular.module("static").config(e),e.$inject=["$stateProvider","$urlRouterProvider"]}(),function(){"use strict";angular.module("static").constant("moment",moment).constant("google",google)}(),function(){"use strict";function e(e){e.debugEnabled(!0)}angular.module("static").config(e),e.$inject=["$logProvider"]}(),angular.module("static").run(["$templateCache",function(e){e.put("app/main/main.html",'<div layout="column" layout-fill="" style="padding-bottom: 32px;"><md-button class="md-raised md-primary" ng-click="main.spin=!main.spin;main.search()">Search for places</md-button><md-progress-circular style="margin: 20px auto;" ng-show="main.spin" class="md-hue-2" md-mode="indeterminate"></md-progress-circular><md-whiteframe class="md-whiteframe-z3" layout="" ng-repeat="place in main.places | orderBy: [\'-rating\', \'+distance\']"><md-card-content><h2 class="md-title">Name: {{ place.name }}</h2><p class="md-body-1">Distance: {{ place.distance | number: 2 }} Meters</p><p class="md-body-1" ng-show="place.dValue == 100">Rating: {{ place.rating }} stars</p><img style="position: absolute; top: 10%; right: 1%; width: 30px;" ng-src="{{ place.icon }}"></md-card-content><md-progress-linear md-mode="determinate" ng-show="place.dValue >= 0" value="{{ place.dValue || 0 }}"></md-progress-linear></md-whiteframe></div>')}]);