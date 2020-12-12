$(document).ready(function(){

	/*************************************************/
	/****************** EVENEMENTS *******************/
	/*************************************************/

	// Double-Clic sur wrapper change sa couleur et celle de tous les <li>
	jQuery("body").on("dblclick", "ul", function() {
		jQuery(this).css("background-color", "white");
		jQuery("li").css("background-color", "yellow");
	});

	






});
