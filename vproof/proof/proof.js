document.addEventListener('DOMContentLoaded', function() {
	"use strict";
	
	var head = document.getElementsByTagName('head')[0];
	var script;

	var temp; //general use
	
	var controls = $('#controls');
	var proof = $('#proof-grid');
	var glyphselect = $('#select-glyphs');
	var showExtended = document.getElementById('show-extended-glyphs');
	var currentFont;
	
	//find characters in the font that aren't in any of the defined glyph groups
	function getMiscChars() {
		var definedGlyphs = {};
		Array.from(getKnownGlyphs()).forEach(function(c) {
			definedGlyphs[c] = true;
		});
		var result = "";
		Object.keys(currentFont.tables.cmap.glyphIndexMap).forEach(function(u) {
			var c = String.fromCodePoint(u);
			if (!(c in definedGlyphs)) {
				result += c;
			}
		});
		return result;
	}
	
	function getKnownGlyphs() {
		var glyphset = '';
		var addthing = function(thing) {
			if (typeof thing === 'string') {
				glyphset += thing;
				return true;
/*
			} elseif (typeof thing === 'object' && 'chars' in thing) {
				glyphset += thing.chars;
				return true;
*/
			}
			return false;
		};
		$.each(window.glyphsets, function(group, sets) {
			if (addthing(sets)) {
				return;
			} else {
				$.each(sets, function(i, set) {
					addthing(set);
				});
			}
		});
		return glyphset;
	}
	
	function getAllGlyphs() {
		return getKnownGlyphs() + getMiscChars();
	}
	
	function getGlyphString() {
		var groupSet = glyphselect.val().split('::');
		var glyphset;

		if (groupSet.length > 1) {
			if (groupSet[1] in window.glyphsets[groupSet[0]]) {
				glyphset = window.glyphsets[groupSet[0]][groupSet[1]];
			} else if (groupSet[1] === 'concat') {
				glyphset = [];
				$.each(window.glyphsets[groupSet[0]], function(label, glyphs) {
					if (typeof glyphs === 'string') {
						glyphset.push(glyphs);
					}
				});
				glyphset = glyphset.join('').trim();
			}
		} else if (groupSet[0] === 'misc') {
			glyphset = getMiscChars();
		} else if (groupSet[0] === 'all-gid') {
			glyphset = [];
			
		} else {
			glyphset = window.glyphsets[groupSet[0]];
		}
		
		if (groupSet.length === 1 && typeof glyphset === 'object' && 'default' in glyphset) {
			if (!showExtended.checked) {
				return glyphset['default'];
			} else {
				var result = "";
				$.each(glyphset, function(k, v) {
					result += typeof v === 'string' ? v : v.chars;
				});
				return result;
			}
		}

		return glyphset ? glyphset : getAllGlyphs();
	}
	
	function populateGrid() {
		var cmap = currentFont.tables.cmap.glyphIndexMap;
		var glyphset = getGlyphString();
		var glyphsort = $('#select-glyphs').val() === 'all-gid' ? 'glyph' : 'glyphset';

		if (typeof glyphset === 'object' && glyphset.chars && glyphset.feature) {
			proof.css('font-feature-settings', '"' + glyphset.feature + '" 1');
			glyphset = glyphset.chars;
		} else {
			proof.css('font-feature-settings', '');
		}

		var unicodes = [];
		var checkCmap = false;
		switch (glyphsort) {
			case 'glyph':
				unicodes = Object.keys(cmap);
				unicodes.sort(function(a, b) { return cmap[a] - cmap[b]; });
				unicodes.forEach(function(u, i) {
					unicodes[i] = String.fromCodePoint(u);
				});
				break;
			case 'glyphset':
				unicodes = Array.from(glyphset);
				checkCmap = true;
				break;
			default:
				unicodes = Object.keys(cmap);
				unicodes.sort(function(a, b) { return a-b; });
				unicodes.forEach(function(u, i) {
					unicodes[i] = String.fromCodePoint(u);
				});
				break;
		}

		proof.empty();
		unicodes.forEach(function(c) {
			if (!checkCmap || c.codePointAt(0) in cmap) {
				proof.append('<span>' + c + '</span>');
			}
		});
		
		TNTools.slidersToElement();
		TNTools.doGridSize();
	}
	
	$('#select-font')	.on('change', function() {
		var fonturl = $(this).val();
		proof.html('<span style="font-size:1rem">Loading…</span>');

		if (window.fontInfo[fonturl] && window.fontInfo[fonturl].fontobj) {
			window.font = currentFont = window.fontInfo[fonturl].fontobj;
			populateGrid();
		} else {
			var url = 'fonts/' + fonturl + '.woff';
			window.opentype.load(url, function (err, font) {
				if (err) {
					alert(err);
					return;
				}
				window.font = window.fontInfo[fonturl].fontobj = currentFont = font;
				populateGrid();
			});
		}
	});
	
	$('#select-glyphs').on('change', populateGrid);
	$('#show-extended-glyphs').on('change', populateGrid);
});