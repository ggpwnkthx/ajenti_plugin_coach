'use strict';

angular.module('ajenti.coach', ['core']);


'use strict';

angular.module('ajenti.coach').config(function ($routeProvider) {
    return $routeProvider.when('/view/cluster/users', {
        templateUrl: '/coach:resources/partial/users.html',
        controller: 'CoachUsersController'
    });
});


'use strict';

angular.module('ajenti.coach').controller('CoachUsersController', function ($scope, notify, pageTitle, config, coach_users) {
	pageTitle.set('User Management');

	$scope.reload = function () {
		$scope.types = [];
		coach_users.getTypes().then(function (data) {
			$scope.types = data;
			$scope.count = Object.keys(data).length;
		});
	};

	$scope.reload();
});


'use strict';

angular.module('ajenti.coach').service('coach_users', function ($http) {

	this.getUsers = function (type) {
		return $http.get("/api/coach/auth/get_users/" + type).then(function (response) {
			return response.data;
		});
	};
	this.getTypes = function () {
		return $http.get("/api/coach/auth/get_types").then(function (response) {
			return response.data;
		});
	};
	this.deleteUser = function (type, user) {
		return $http.get("/api/coach/auth/delete/" + type + "/" + user).then(function (response) {
			return response.data;
		});
	};

	return this;
});


