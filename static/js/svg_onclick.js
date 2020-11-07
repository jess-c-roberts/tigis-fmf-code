function fieldInfo(event) {
  var width = parseFloat(event.target.getAttributeNS(null,"width"));
  var height = parseFloat(event.target.getAttributeNS(null,"height"));
  var field_id = parseFloat(event.target.getAttributeNS(null,"id"));
  var owner = event.target.getAttributeNS(null,"owner");
  var crop = event.target.getAttributeNS(null,"crop");
  var crop_start = event.target.getAttributeNS(null,"crop_start");
  var crop_end = event.target.getAttributeNS(null,"crop_end");
  var area = (width*height);
  document.getElementById("side-results").innerHTML = ("<p style='color:#000'><b>Field: </b>" +field_id+ "<br/><b>Area: </b>" +area+ " sq. units<br/><b>Owner: </b>" +owner+ "<br/><b>Crop: </b>"+crop+ "<br/><b>Growing season: </b>"+crop_start+" to "+crop_end+"</p>");
}

function findInfo(event) {
  var find_id = parseFloat(event.target.getAttributeNS(null,"id"));
  var loc_x = parseFloat(event.target.getAttributeNS(null,"cx"));
  var loc_y = parseFloat(event.target.getAttributeNS(null,"cy"));
  var depth = event.target.getAttributeNS(null,"depth");
  var type = event.target.getAttributeNS(null,"type");
  var notes = event.target.getAttributeNS(null,"field_notes");
  var era = event.target.getAttributeNS(null,"era");
  var use = event.target.getAttributeNS(null,"use");
  document.getElementById("side-results").innerHTML = ("<p style='color:#000'><b>Find: </b>" +find_id+ "<br/><b>Location found: </b>(" +loc_x+ ", " +loc_y+ ")<br/><b>Depth found: </b>" +depth+ "<br/><b>Era: </b>" +era+ "<br/><b>Type: </b>" +type+ "<br/><b>Use: </b>" +use+ "<br/><b>Comments: </b>"+notes+"</p>");
}
