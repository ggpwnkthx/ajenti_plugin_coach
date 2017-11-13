angular.module('ajenti.coach').controller('CoachUsersController', function ($scope, notify, pageTitle, config, coach_users) {
	pageTitle.set('User Management');
	
	$scope.reload = () => {
		$scope.types = [];
		coach_users.getTypes().then((data) => {
			$scope.types = data;
			$scope.count = Object.keys(data).length;
		});
	}
	
	$scope.reload();
	
});