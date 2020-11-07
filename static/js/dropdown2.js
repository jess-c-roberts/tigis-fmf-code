$(function () {
  $("#farmer-crit-dropdown").change(function() {
    $("#farmer-choice1-dropdown").load("https://www.geos.ed.ac.uk/~s1434165/static/textdata/" + $(this).val() + "1.txt");
    $("#farmer-choice2-dropdown").load("https://www.geos.ed.ac.uk/~s1434165/static/textdata/" + $(this).val() + "2.txt");
   });
 });

 $(function () {
   $("#archaeo-crit-dropdown").change(function() {
     $("#archaeo-choice1-dropdown").load("https://www.geos.ed.ac.uk/~s1434165/static/textdata/" + $(this).val() + "1.txt");
     $("#archaeo-choice2-dropdown").load("https://www.geos.ed.ac.uk/~s1434165/static/textdata/" + $(this).val() + "2.txt");
    });
 });
