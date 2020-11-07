// JQuery functions to change dropdown dynamically based on the button clicked by the user //

// General structure is as follows:
// STEP ONE: When radio button is clicked, perform function
// STEP TWO: Take array of relevant values
// STEP THREE: Find the relevant dropdown and clear all current options
// STEP FOUR: For the length of the array values, incorporate them as new options
// in the selected dropdown.

$(document).ready(function(){
  // Field specific //
        $("#btn-field-IDs").click(function(){
             var IDS = new Array("1","2","3","4","5","6","7","8");
                $("#field-dropdown").find('option').remove();
                for(i=0; i < IDS.length; i++){
                     $("#field-dropdown").append('<option value="'+IDS[i]+'">'+IDS[i]+'</option>');
                 }
        });
        $("#btn-crops").click(function(){
              var CROPS = new Array("strawberries","turnips","potatoes","peas","oil seed rape");
                  $("#field-dropdown").find('option').remove();
                  for(i=0; i < CROPS.length; i++){
                      $("#field-dropdown").append('<option value="'+CROPS [i]+'">'+CROPS [i]+'</option>');
                   }
         });
         $("#btn-area").click(function(){
               var AREA = new Array("0 and 1","1 and 2","2 and 3","3 and 4");
                   $("#field-dropdown").find('option').remove();
                   for(i=0; i < AREA.length; i++){
                       $("#field-dropdown").append('<option value="'+AREA [i]+'">'+AREA [i]+'</option>');
                    }
          });
         $("#btn-owners").click(function(){
              var OWNERS = new Array("Farmer Black","Farmer White","Farmer Green","Farmer Brown");
                  $("#field-dropdown").find('option').remove()
                  for(i=0; i < OWNERS.length; i++){
                      $("#field-dropdown").append('<option value="'+OWNERS [i]+'">'+OWNERS [i]+'</option>');
                   }
          });
          $("#btn-all-fields").click(function(){
                var ALL = new Array("all");
                    $("#field-dropdown").find('option').remove()
                    for(i=0; i < ALL.length; i++){
                        $("#field-dropdown").append('<option value="'+ALL [i]+'">'+ALL [i]+'</option>');
                     }
          });
    // Finds Specific //
          $("#btn-find-IDs").click(function(){
                var IDS = new Array("1","2","3","4","5","6","7","8");
                    $("#find-dropdown").find('option').remove();
                    for(i=0; i < IDS.length; i++){
                      $("#find-dropdown").append('<option value="'+IDS [i]+'">'+IDS [i]+'</option>');
                   }
          });
          $("#btn-types").click(function(){
                var TYPES = new Array("shard","metal_work","flint","bone");
                    $("#find-dropdown").find('option').remove()
                    for(i=0; i < TYPES.length; i++){
                        $("#find-dropdown").append('<option value="'+TYPES [i]+'">'+TYPES [i]+'</option>');
                     }
          });
          $("#btn-eras").click(function(){
                var ERAS = new Array("bronze","iron_age","mesolithic","recent");
                    $("#find-dropdown").find('option').remove()
                    for(i=0; i < ERAS.length; i++){
                        $("#find-dropdown").append('<option value="'+ERAS [i]+'">'+ERAS [i]+'</option>');
                     }
          });
          $("#btn-uses").click(function(){
                var USES = new Array("domestic","decorative","hunting","food");
                    $("#find-dropdown").find('option').remove()
                    for(i=0; i < USES.length; i++){
                        $("#find-dropdown").append('<option value="'+USES [i]+'">'+USES [i]+'</option>');
                     }
          });
          $("#btn-all-finds").click(function(){
                var ALL = new Array("all");
                    $("#find-dropdown").find('option').remove()
                    for(i=0; i < ALL.length; i++){
                        $("#find-dropdown").append('<option value="'+ALL [i]+'">'+ALL [i]+'</option>');
                     }
          });
});
