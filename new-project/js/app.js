var newProjectApp = angular.module('newProjectApp', []);

newProjectApp.controller('npCtrl', ['$scope', '$http', function ($scope, $http) {

    $http.get('/file.json').success(function (data) {
        	$scope.files = data;
	});
}]);

