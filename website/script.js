// init
$( function() {
	
// global var init
var axisMap = [];
var defaults = {};

// AUX
function getVariationSettings(element) {
	// get the font variation settings object from the css
	var settings = {};
	var fontvariations = $(element).css("font-variation-settings");
	if(fontvariations == "normal") { // default
		return defaults;
	}
	var array = fontvariations.split(",");
	for (var i = 0; i < array.length; i++) {
		setting = array[i].split("'");
		key = setting[1];
		value = parseFloat(setting[2]);
		settings[key] = value;
	}
	return settings;
}

function setVariationSettings(element, settings) {
	// set the font variation settings css
	var css = "";
	for (var key in settings) {
		css+="'"+key+"' "+settings[key]+", ";
	}
	css = css.slice(0, -2); // remove last comma and space
	$(element).css("font-variation-settings", css);
}

// CALLBACKS

function updateVariations(event, ui) {
	if(event.originalEvent) { // only if triggered by slider, not us
		// this slider, for reference
		key = $(this).attr('id');
		value = ui.value;
		
		// find the related label and display the current value
		$('#sliders').find('#'+key+'-label span.value').html(value);
		
		// get the variations settings
		var settings = {};
		// loop through all sliders
		$('#sliders').find('.slider').each(function() {
			key = $(this).attr('id');
			value = $(this).slider( "value" );
			settings[key] = value;
		});
		// set the variation settings
		setVariationSettings('.variations.selected', settings);
	}
}

// Load the fvar and name table
// and init the variations textarea
var url = fvar;
$.ajax({
	type: "GET",
	url: url,
	dataType: "xml",
	success: function (ttx) {
		
		//console.log('success');
		// loop through the fvar axis to build the axisMap and set the defaults
		$(ttx).find('fvar').find('Axis').each(function() {
			tag = $(this).find('AxisTag').text();
			min = parseFloat($(this).find('MinValue').text());
			dflt = parseFloat($(this).find('DefaultValue').text());
			max = parseFloat($(this).find('MaxValue').text());
			nameId = $(this).find('AxisNameID').text();
			axisName = $(ttx).find('namerecord[nameID="'+nameId+'"]').first().text().trim();
			//console.log(axisName);
			axis = {
				tag: tag, min: min, dflt: dflt, max: max, name: axisName
			}
			axisMap.push(axis);
			defaults[tag] = dflt;
		});
		
		// build the labels and sliders
		for (var i = 0; i < axisMap.length; i++) {
			axis = axisMap[i];
			$('#sliders').append('<div id="'+axis.tag+'-label" class="label"><span class="name">'+axis.name+'</span> <span class="values">('+axis.min+', <span class="value">'+axis.dflt+'</span>, '+axis.max+')</span></div>');
			$('#sliders').append('<div id="'+axis.tag+'" class="slider"></div>');
			$('#'+axis.tag).slider({
				orientation: "horizontal",
				min: axis.min,
				value: axis.dflt,
				max: axis.max,
				slide: updateVariations,
				change: updateVariations,
			});
		}
		
		$('#article-head').focus();
		
		$('.variations').each(function() {
			setVariationSettings($(this), defaults);
		})
		
	}
});

// UI

$( ".resizable" ).resizable();

$('#default').button();
$('#default').click(function() {
	setVariationSettings($('.variations.selected'), defaults);
	for(key in defaults) {
		value = defaults[key];
		$('#'+key).slider("value", value);
		$('#sliders').find('#'+key+'-label span.value').html(value);
	}
});

function updateFontSize(event, ui) {
	value = ui.value;
	$('.variations.selected').css('font-size', value+'px');
	$('#fontsize-slider .label').find('span.value').html(value);
}

$('#fontsize-slider .slider').slider({
	orientation: "horizontal",
	min: 16,
	value: 72,
	max: 200,
	slide: updateFontSize,
	change: updateFontSize,
});

$('.variations').bind('paste', function(e) {
	// prevent pasting formatted text
	e.preventDefault();
	// retrieve plain text
	plainText = (e.originalEvent || e).clipboardData.getData('text/plain');
	// paste
	$(this).html(plainText);
});

$('.variations').focus(function() {
	$('.variations').removeClass('selected');
	$(this).addClass('selected');
	settings = getVariationSettings(this);
	for(key in settings) {
		value = settings[key];
		$('#'+key).slider("value", value);
		$('#sliders').find('#'+key+'-label span.value').html(value);
	}
	fontsize = parseInt($(this).css("font-size"), 10);
	$('#fontsize-slider .slider').slider("value", fontsize);
});


});