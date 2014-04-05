/* Extension that adds a button to draw iBeacons on canvas.
 */
svgEditor.addExtension("iBeacon", function() {

		return {
			name: "Hello World",
			svgicons: "extensions/ibeacon-icon.xml",
			
			buttons: [{
				// Must match the icon ID
				id: "ibeacon", 
				
				// This indicates that the button will be added to the "mode"
				// button panel on the left side
				type: "mode", 
				
				// Tooltip text
				title: "Add an iBeacon.", 
				
				// Events
				events: {
					'click': function() {
						// The action taken when the button is clicked on.
						// For "mode" buttons, any other button will 
						// automatically be de-pressed.
						svgCanvas.setMode("ibeacon");
					}
				}
			}],
			// This is triggered when the main mouse button is pressed down 
			// on the editor canvas (not the tool panels)
			mouseDown: function() {
				// Check the mode on mousedown
				if(svgCanvas.getMode() == "ibeacon") {
				
					// The returned object must include "started" with 
					// a value of true in order for mouseUp to be triggered
					return {started: true};
				}
			},
			
			// This is triggered from anywhere, but "started" must have been set
			// to true (see above). Note that "opts" is an object with event info
			mouseUp: function(opts) {
				// Check the mode on mouseup
				// Diego: This should be started && svgC... For some reason,
				// it breaks the button.
				if(svgCanvas.getMode() == "ibeacon") {
					var zoom = svgCanvas.getZoom();
					var canv = svgEditor.canvas;
					
					// Get the actual coordinate by dividing by the zoom value
					var x = opts.mouse_x / zoom;
					var y = opts.mouse_y / zoom;
					
					var cur_shape = canv.addSvgElementFromJson({
						"element": "path",
						"curStyles": true,
						"attr": {
							// Spawn at correct coordinates
							"transform": "translate(" +x +"," +y +")",
							"stroke": "#000000",
							"stroke-width": "5",
							"stroke-dasharray": "null",
							"stroke-linejoin": "null",
							"stroke-linecap": "null",
							"d": "m-30,0c0,-16.57458 13.42542,-30 30,-30c16.57458,0 30,13.42542 30,30c0,16.57458 -13.42542,30 -30,30c-16.57458,0 -30,-13.42542 -30,-30z",
							"id": canv.getNextId()
						}
					});
					
					return {
						keep: true,
						element: cur_shape,
						started: false
					}
				}
			}
		};
});

