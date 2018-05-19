var app = angular.module('cait_rocks_app');

// create a controller containing functions and variables made available in the controller's scope
app.controller('recipe_list_controller', ['$scope', 'recipe_service', function ($scope, recipe_service) {
    'use strict';

    $scope.retrieve_recipes = function () {
        recipe_service.get_recipes().then(
            function (response) {
                $scope.recipe_list = response.data;
            }
        );
    };

    $scope.filter_table_rows = function () {
        // Declare variables
        var filter, table, tr, td, i, j, inner_a;
        filter = $scope.filterText.toUpperCase();
        table = document.getElementById('recipeListTable');
        tr = table.getElementsByTagName('tr');

        // make sure all rows are shown first
        for (i = 0; i < tr.length; i++) {
            tr[i].style.display = '';
        }

        // leave early with everything shown if the search string is too short
        if (filter.length < 2) {
            return;
        }

        // Loop through all table rows, and hide those who don't match the search query
        for (i = 1; i < tr.length; i++) {

            // we will check each token of the search string
            var tokens_to_check = filter.split(' ');

            for (j = 0; j < tokens_to_check.length; j++) {
                var token = tokens_to_check[j];
                var token_found = false;
                // check the title of the recipe
                td = tr[i].getElementsByTagName('td')[1];
                inner_a = td.getElementsByTagName('a')[0];
                if (inner_a.innerHTML.toUpperCase().indexOf(token) > -1) {
                    token_found = true;
                }
                // check the author of the recipe
                if (!token_found) {
                    td = tr[i].getElementsByTagName('td')[2];
                    if (td.innerHTML.toUpperCase().indexOf(token) > -1) {
                        token_found = true;
                    }
                }
                if (!token_found) {
                    // check the ingredients of the recipe
                    td = tr[i].getElementsByTagName('td')[3];
                    if (td.innerHTML.toUpperCase().indexOf(token) > -1) {
                        token_found = true;
                    }
                }
                tokens_to_check[j] = token_found;
            }

            // now turn that one
            if (tokens_to_check.every(function (t) {
                    return t;
                })) {
                // woo-hoo we have a match! leave it shown
            } else {
                tr[i].style.display = 'none';
            }
        }
    };

    $scope.clear_filter = function () {
        $scope.filterText = '';
        $scope.filter_table_rows();
    };

    var init = function () {
        // use this init for pages where you aren't getting the full list of recipes
        $scope.filterText = '';
        $scope.recipe_list = [];
        $scope.retrieve_recipes();
    };

    init();

}]);
