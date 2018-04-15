var app = angular.module('carplates', []);
// Configure the $http provider with the cookie and header names
app.config(['$httpProvider', function($httpProvider) {
  $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';}
]);

app.controller('carplatesController', function($scope, $http) {
	$http.get('/api/carplates/').then(function(response) {
		$scope.carplatesList = response.data;
	});

	$scope.saveData = function() {
		var data = {
			plate_number: $scope.carplatesInput,
			first_name: $scope.nameInput,
			last_name: $scope.surnameInput
		};
		$http.post('/api/carplates/', data)
	}

	$scope.carplatesAdd = function() {
		$scope.carplatesList.push({
			plate_number: $scope.carplatesInput,
			first_name: $scope.nameInput,
			last_name: $scope.surnameInput
		});
		$scope.carplatesInput = '';
	};

	$scope.remove = function() {
		var oldList = $scope.carplatesList;
		$scope.carplatesList = [];
		angular.forEach(oldList, function(carplate) {
			if (carplate.remove) {
				$http.delete('/api/carplates/' + carplate.id + '/');
			} else {
				$scope.carplatesList.push(carplate);
			}			
		})		
	}
})