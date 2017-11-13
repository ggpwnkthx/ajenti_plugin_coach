angular.module('ajenti.coach').service('coach_users', function($http) {
	
	this.getUsers = (type) => {
		return $http.get("/api/coach/auth/get_users/" + type).then(response => response.data)
	};
	this.getTypes = () => {
		return $http.get("/api/coach/auth/get_types").then(response => response.data)
	};
	this.deleteUser = (type, user) => {
		return $http.get("/api/coach/auth/delete/" + type + "/" + user).then(response => response.data)
	};
	
    return this;
});