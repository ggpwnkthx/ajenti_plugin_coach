angular.module('ajenti.coach').config($routeProvider =>
    $routeProvider.when('/view/cluster/users', {
        templateUrl: '/coach:resources/partial/users.html',
        controller: 'CoachUsersController'
    })
);
