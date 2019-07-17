(function() {
	"use strict";

	var temp;
	
	function fvsToAxes(fvs) {
		if (!fvs) {
			return {};
		}
		if (typeof fvs === 'string') {
			fvs = fvs.split(/, */);
		}
		var axes = {};
		$.each(fvs, function(i, setting) {
			var k, v;
			if (temp = setting.match(/["'](....)['"]\s+([\-\d\.]+)/)) {
				k = temp[1];
				v = parseFloat(temp[2]);
				axes[k] = v;
			}
		});
		return axes;
	}
	
	function axesToFVS(axes) {
		var clauses = [];
		
		//workaround Safari default-opsz bug
		try {
			if ('opsz' in axes && axes.opsz == fontInfo[$('#select-font').val()].axes.opsz.default) {
				axes.opsz = fontInfo[$('#select-font').val()].axes.opsz.default + 0.1;
			}
		} catch (e) {}
		
		$.each(axes, function(k, v) {
			if (k.length !== 4) {
				return;
			}
			clauses.push('"' + k + '" ' + v);
		});
		if (clauses.length === 0) {
			return "normal";
		} else {
			return clauses.join(", ");
		}
	}

	function slidersToElement() {
		var styleEl = $('#style-general');
		var selector = '.variable-demo-target';
		
		var rules = [];
		
		var foreground = $('#foreground').length && $('#foreground').spectrum('get').toString();
		var background = $('#background').length && $('#background').spectrum('get').toString();

		rules.push('font-family: "' + $('#select-font').val() + '-VP"');
		
		if (background) {
			rules.push('background-color: ' + background);
		}

		if (foreground) {
			rules.push('color: ' + foreground);
		}
		
		// update the actual CSS
		styleEl.text('\n' 
			+ selector + ' {\n\t' + rules.join(';\n\t') + ';\n}\n'
		);
	}
	
	function doGridSize() {
		var grid = document.getElementById('proof-grid');
		var axes = fontInfo[$('#select-font').val()].axes;

		//disable the animation for a minute
		grid.style.animationName = 'none';

		//reset
		grid.style.removeProperty('font-size');
		grid.innerHTML = grid.innerHTML.replace(/<\/?div[^>]*>/g, '');

		//get the stuff as wide as possible
		var fvs = {};
		if ('wdth' in axes) {
			fvs.wdth = axes.wdth.max;
		}
		if ('wght' in axes) {
			fvs.wght = axes.wght.max;
		}
		if ('opsz' in axes) {
			fvs.opsz = axes.opsz.min;
		}
		grid.style.fontVariationSettings = axesToFVS(fvs);
		
		//shrink the font so it fits on the page
		var winHeight = window.innerHeight - 96;
		var gridHeight = grid.getBoundingClientRect().height, fontsize = parseFloat(getComputedStyle(grid).fontSize);

		while (gridHeight < winHeight) {
			fontsize *= 1.5;
			grid.style.fontSize = Math.floor(fontsize) + 'px';
			gridHeight = grid.getBoundingClientRect().height;
			if (fontsize > 144) {
				break;
			}
		}

		while (gridHeight > winHeight) {
			fontsize *= 0.9;
			grid.style.fontSize = Math.floor(fontsize) + 'px';
			gridHeight = grid.getBoundingClientRect().height;
			if (fontsize < 24) {
				break;
			}
		}
		
		var lines = [], line = [], lastX = Infinity;
		$.each(grid.childNodes, function(i, span) {
			if (!span.tagName || span.tagName !== 'SPAN') {
				return;
			}
			var box = span.getBoundingClientRect();
			if (box.width > 0) {
				if (!span.style.width) {
					//hard-code the max width so it doesn't move around
					span.style.width = (box.width / fontsize) + 'em';
				}
				if (box.left < lastX) {
					if (line && line.length) {
						lines.push(line);
					}
					line = [];
				}
				lastX = box.left;
			}
			line.push(span);
		});
		if (line && line.length) {
			lines.push(line);
		}

		lines.forEach(function(line) {
			var div = document.createElement('div');
			line.forEach(function(span) {
				div.appendChild(span);
			});
			grid.appendChild(div);
		});

		//re-enable the animation and remove the wide settings
		grid.style.removeProperty('font-variation-settings');
		grid.style.removeProperty('animation-name');
	}
	
	function calculateKeyframes(font) {
		//O(3^n)? this might get ugly
		var keyframes = [];

		//represent each frame as a trinary number: 000, 001, 002, 010, 011, 012…
		// 0 is axis default, 1 is axis min, 2 is axis max
		// some combinations might be skipped if the min/max is the default
		var axesMDM = [];
		var raxisPresent = [];
		$.each(registeredAxes, function(index, axis) {
			if (axis in font.axes) {
				raxisPresent.push(axis);
				axesMDM.push([font.axes[axis].default, font.axes[axis].min, font.axes[axis].max]);
			}
		});

		if (!raxisPresent.length) {
			return [];
		}

		var permutations = [];
		var i, maxperms, j, l;
		var raxisCount = raxisPresent.length;
		var perm, filler, prev, current;
		for (i=0, maxperms = Math.pow(3, raxisCount); i < maxperms; i++) {
			current = i.toString(3);
			filler = raxisCount - current.length;
			perm = [];
			for (j=0; j<filler; j++) {
				perm.push(axesMDM[j][0]);
			}
			for (j=0, l=current.length; j<l; j++) {
				perm.push(axesMDM[filler+j][current[j]]);
			}
			permutations.push(perm);
			// and go back to default at the end of each cycle
			if (current[j-1] == 2) {
				perm = perm.slice(0, -1);
				perm.push(axesMDM[filler+j-1][0]);
				permutations.push(perm);
			}
		}

		var fvsPerms = [];
		$.each(permutations, function(i, perm) {
			var fvs = {};
			$.each(raxisPresent, function(j, axis) {
				fvs[axis] = perm[j];
			});
			fvs = axesToFVS(fvs);
			if (fvs !== prev) {
				fvsPerms.push(fvs);
			}
			prev = fvs;
		});
		
		return fvsPerms;
	}

	var videoproofOutputInterval, videoproofActiveTarget, animationRunning = false;
	function animationUpdateOutput() {
		var output = document.getElementById('aniparams');
// 		var timestamp = $('label[for=animation-scrub]');
// 		var scrub = $('#animation-scrub')[0];
		var mode = $('#select-mode')[0];

		var css = videoproofActiveTarget ? getComputedStyle(videoproofActiveTarget) : {};
		var percent = animationRunning ? parseFloat(css.outlineOffset) : -parseFloat(css.animationDelay) / parseFloat(css.animationDuration) * 100;
		var axes = fvsToAxes(css.fontVariationSettings);
		var outputAxes = [];
		$.each(registeredAxes, function(i, axis) {
			if (axis in axes) {
				outputAxes.push(axis + ' ' + Math.floor(axes[axis]));
			}
		});
		var bits = [
			window.fontInfo[$('#select-font').val()].name,
			mode.options[mode.selectedIndex].textContent,
			outputAxes.join(' ')
// 			css ? parseFloat(css.outlineOffset) + '%' : ""
		];
		output.textContent = bits.join(": ");
// 		scrub.value = percent;
// 		timestamp.text(Math.round(percent));
		if (animationRunning && percent == 100) {
			resetAnimation();
		}
	}

	function startAnimation() {
		//just in case it had been removed
		updateAnimationParam('animation-name', null);
		$('html').removeClass('paused');
		videoproofOutputInterval = setInterval(animationUpdateOutput, 100);
		animationRunning = true;
		currentKeyframe = null;
	}
	
	function stopAnimation() {
		animationRunning = false;
		$('html').addClass('paused');
		if (videoproofOutputInterval) {
			clearInterval(videoproofOutputInterval);
			videoproofOutputInterval = null;
		}
	};

	var currentKeyframe;
	function jumpToKeyframe(index) {
		stopAnimation();
		currentKeyframe = index;
		var duration = parseFloat($('#animation-duration').val());
		var ratio = index / currentKeyframes.length;
		var kfTime = ratio * duration;

		//set "timestamp" in animation, for resuming
		updateAnimationParam('animation-delay', -kfTime + 's');
// 		$('#animation-scrub').val(Math.round(ratio * 100));

		//but the timing is imprecise, so also set the explicit FVS for the keyframe
		updateAnimationParam('animation-name', 'none');
		if (/font-variation-settings\s*:\s*([^;\}]+)/.test(currentKeyframes[index])) {
			updateAnimationParam('font-variation-settings', RegExp.$1);
		}
		setTimeout(animationUpdateOutput);
		
		//need to do a bit of extra hoop jumping for the keyframe display
		$('#keyframes-display a').css('animation-name', 'none');
		setTimeout(function() {
			$('#keyframes-display a').css('animation-name', '');
		}, 100);
	}

	function setupAnimation() {
		$('#animation-controls button.play-pause').on('click', function() {
			videoproofOutputInterval ? stopAnimation() : startAnimation();
		});
		
		$('#animation-controls').find('button.back, button.forward').on('click', function() {
			if (!videoproofActiveTarget || !currentKeyframes) {
				return;
			}			
			var toIndex;
			if (typeof currentKeyframe === 'number') {
				toIndex = $(this).hasClass('back') ? currentKeyframe - 1 : currentKeyframe + 1;
			} else {
				var css = getComputedStyle(videoproofActiveTarget);
				var percent = parseFloat(css.outlineOffset);
				var exactIndex = percent / 100 * currentKeyframes.length;
				//if we're already on an index, go to the next int
				if (Math.abs(exactIndex - Math.round(exactIndex)) > 0.01) {
					toIndex = Math[$(this).hasClass('back') ? 'floor' : 'ceil'](exactIndex);
				} else {
					toIndex = $(this).hasClass('back') ? Math.round(exactIndex) - 1 : Math.round(exactIndex) + 1;
				}
			}
			if (toIndex < 0 || toIndex >= currentKeyframes.length) {
				toIndex = 0;
			}
			jumpToKeyframe(toIndex);
		});
		
		$('#animation-controls button.beginning').on('click', resetAnimation);
		$('#animation-controls button.end').on('click', function() {
			if (!videoproofActiveTarget || !currentKeyframes) {
				return;
			}
			fakeFrame(currentKeyframes.length - 1);
		});
		
		$('#animation-duration').on('change input', function() {
			updateAnimationParam('animation-duration', this.value + 's');
		}).trigger('change');

		$('#first-play').css('cursor', 'pointer').on('click', startAnimation);
	}

	var currentKeyframes;
	function animationNameOnOff(callback) {
		updateAnimationParam('animation-name', 'none !important');
		setTimeout(function() {
			updateAnimationParam('animation-name', null);
			stopAnimation();
			setTimeout(animationUpdateOutput);
		}, 100);
	}

	function updateAnimationParam(k, v) {
		var style = $('style.' + k);
		if (!style.length) {
			$('head').append("<style class='" + k + "'></style>");
			style = $('style.' + k);
		}
		if (v === null) {
			style.empty();
		} else {
			style.text('.variable-demo-target, #keyframes-display a { ' + k + ': ' + v + '; }');
		}
	}

	function resetAnimation() {
		stopAnimation();
		
		var keyframes = currentKeyframes = calculateKeyframes(fontInfo[$('#select-font').val()]);
		var perstep = 100 / keyframes.length;
		$('#animation-duration').val(keyframes.length * 2).trigger('change');
		updateAnimationParam('animation-delay', '0');
		var stepwise = [];

		var ul = document.getElementById('keyframes-display');
		ul.textContent = "";
		keyframes.forEach(function(fvs, i) {
			var prevPercent = Math.max(0, Math.round(10*(perstep * (i-1)))/10);
			var percent = Math.round(10*(perstep * i))/10;
			var nextPercent = Math.min(100, Math.round(10*(perstep * (i+1)))/10);

			//add display listing
			var li = document.createElement('li');
			var a = document.createElement('a');
			a.textContent = fvs.replace(/"|(\.\d+)/g, '');
			a.addEventListener('click', function(evt) {
				evt.preventDefault();
				jumpToKeyframe(i);
			});
			li.appendChild(a);
			ul.appendChild(li);

			//add timeline hints
			var stepwiseName = "videoproof-hint-" + i;
			stepwise.push("@keyframes " + stepwiseName + " { 0%, " + prevPercent + '%, ' + nextPercent + '%, 100% { color:black; font-weight:400; } ' + percent + '% { color: red; font-weight: 700; } } #keyframes-display li:nth-child(' + (i+1) + ') a { animation-name: ' + stepwiseName + '; }');

			//add CSS step
			var percentOutput = (percent == 0 ? percent + '%, 100' : percent) + '%';
			keyframes[i] =  percentOutput + ' { font-variation-settings: ' + fvs + '; outline-offset: ' + percent + 'px; }';
		});
				
		document.getElementById('videoproof-keyframes').textContent = "@keyframes videoproof {\n" + keyframes.join("\n") + "}\n" + stepwise.join("\n");
		
		animationNameOnOff();
	}

	
	function handleFontChange(font) {
		var spectropts = {
			'showInput': true,
			'showAlpha': true,
			'showPalette': true,
			'showSelectionPalette': true,
			'localStorageKey': 'spectrum',
			'showInitial': true,
			'chooseText': 'OK',
			'cancelText': 'Cancel',
			'preferredFormat': 'hex'
		};

		spectropts.color = $('#foreground').attr('value');
		$('#foreground').spectrum(spectropts);

		spectropts.color = $('#background').attr('value');
		$('#background').spectrum(spectropts);
		
		$('head style[id^="style-"]').empty().removeData();
		
		resetAnimation();
	}

	function addCustomFont(fonttag, url, format, font) {
		var info = {
			'name': font.getEnglishName('fontFamily'),
			'axes': {},
			'axisOrder': [],
			'fontobj': font
		};
		if ('fvar' in font.tables && 'axes' in font.tables.fvar) {
			$.each(font.tables.fvar.axes, function(i, axis) {
				info.axes[axis.tag] = {
					'name': 'name' in axis ? axis.name.en : axis.tag,
					'min': axis.minValue,
					'max': axis.maxValue,
					'default': axis.defaultValue
				};
				info.axisOrder.push(axis.tag);
			});
		}
		
		window.font = font;

		$('head').append('<style>@font-face { font-family:"' + fonttag + '-VP"; src: url("' + url + '") format("' + format + '"); font-weight: 100 900; }</style>');

		window.fontInfo[fonttag] = info;
		var optgroup = $('#custom-optgroup');
		var option = document.createElement('option');
		option.value = fonttag;
		option.innerHTML = info.name;
		option.selected = true;
		if (!optgroup.length) {
			$('#select-font').wrapInner('<optgroup label="Defaults"></optgroup>');
			optgroup = $('<optgroup id="custom-optgroup" label="Your fonts"></optgroup>').prependTo($('#select-font'));
		}
		optgroup.append(option);

		setTimeout(function() { $('#select-font').trigger('change') });
	}

	function addCustomFonts(files) {
		$.each(files, function(i, file) {
			var reader = new FileReader();
			var mimetype, format;
			if (file.name.match(/\.[ot]tf$/)) {
				mimetype = "application/font-sfnt";
				format = "opentype";
			} else if (file.name.match(/\.(woff2?)$/)) {
				mimetype = "application/font-" + RegExp.$1;
				format = RegExp.$1;
			} else {
				alert(file.name + " not a supported file type");
				return;
			}
			var blob = new Blob([file], {'type': mimetype});
			reader.addEventListener('load', function() {
				var datauri = this.result;
				window.opentype.load(datauri, function(err, font) {
					if (err) {
						console.log(err);
						return;
					}
					var fonttag = 'custom-' + file.name.replace(/(-VF)?\.\w+$/, '');
					addCustomFont(fonttag, datauri, format, font);
				});
			});
			reader.readAsDataURL(blob);
		});
	}
	

	window.TNTools = {
		'customFonts': {},
		'clone': function(obj) { return JSON.parse(JSON.stringify(obj)); },
		'slidersToElement': slidersToElement,
		'handleFontChange': handleFontChange,
		'fvsToAxes': fvsToAxes,
		'axesToFVS': axesToFVS,
		'addCustomFonts': addCustomFonts,
		'addCustomFont': addCustomFont,
		'resetAnimation': resetAnimation,
		'doGridSize': doGridSize
	};
	
	//jquery overhead is sometimes causing window.load to fire before this! So use native events.
	document.addEventListener('DOMContentLoaded', function() {
		var controls = $('#controls');
		$('head').append("<style id='style-general'></style>");
		$('#mode-sections > sections').each(function() {
			var styleid = 'style-' + this.id;
			if ($('#' + styleid).length === 0) {
				$('head').append("<style id='" + styleid + "'></style>");
			}
		});

		$('#select-mode').on('change', function(evt) {
			var newActiveSection = $('#mode-sections > #' + this.value);
			$('#mode-sections > section').hide();
			newActiveSection.show();
			videoproofActiveTarget = newActiveSection.find('.variable-demo-target').get(0);
		});

		$('#select-font').on('change', TNTools.handleFontChange);
		$('#foreground, #background').on('move.spectrum change.spectrum hide.spectrum', function() { TNTools.slidersToElement(); });

		$('#add-your-own-button').on('click', function(evt) {
			$('#custom-fonts')[0].click();
			return false;
		});

		$('#custom-fonts').on('change', function() {
			addCustomFonts(this.files);
		});
		
		$('#foreground, #background').on('click', function() {
			//clicking color labels fires the real control and not the spectrum picker
			$(this).spectrum('toggle');
			return false;
		});
		
		var dragging = false;
		$('body').on('dragover', function(evt) {
			if (dragging) return false;
			dragging = true;
			evt.originalEvent.dataTransfer.dropEffect = 'copy';
			$('body').addClass('dropzone');
			return false;
		}).on('dragleave', function(evt) {
			if (evt.target !== document.body) {
				return;
			}
			dragging = false;
			$('body').removeClass('dropzone');
			return false;
		}).on('dragend', function(evt) {
			$('body').removeClass('dropzone');
			dragging = false;
			return false;
		}).on('drop', function(evt) {
			addCustomFonts(evt.originalEvent.dataTransfer.files);
			$(this).trigger('dragend');
			return false;
		});

		$('#grab-new-fonts').on('click', function() {
			var clocks = ['🕛','🕧','🕐','🕜','🕑','🕝','🕒','🕞','🕓','🕟','🕔','🕠','🕕','🕢','🕖','🕢','🕗','🕣','🕘','🕤','🕙','🕥','🕚','🕦'];
			var start = Date.now();
			$(this).next('span').remove();
			var spinner = $("<span style='padding-left: 0.33em'>" + clocks[0] + "</span>").insertAfter(this);
			var interval = setInterval(function() {
				var sec = (Date.now() - start) / 1000;
				spinner.text(clocks[Math.floor(sec*2)%24]);
			}, 500);
			$.ajax(this.href, {
				'complete': function(xhr) {
					clearInterval(interval);
					if (xhr.status === 200) {
						spinner.text("✅ reloading…").attr('title', xhr.responseText);
						setTimeout(function() { window.location.reload(); }, 1000);
					} else {
						spinner.text("❌").attr('title', xhr.statusText + " — call chris!");
					}
				}
			});
			return false;
		});
	});
	
	window.addEventListener('load', function() {
		//this timeout is for the sidebar load
		setTimeout(function() {
			var showSidebar = $('a.content-options-show-filters');
			if (showSidebar.is(':visible')) {
				showSidebar.click();
			}
		}, 100);
			
		setupAnimation();
		$('#select-mode').trigger('change');
		$('#select-font').trigger('change');
		var resizeTimeout;
		$(window).on('resize', function() {
			if (resizeTimeout) {
				clearTimeout(resizeTimeout);
			}
			resizeTimeout = setTimeout(TNTools.doGridSize, 500);
		}).trigger('resize');
	});
})();
