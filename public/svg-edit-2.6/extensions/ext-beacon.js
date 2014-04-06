/* Extension that adds a button to draw iBeacons on canvas.
 */
svgEditor.addExtension("iBeacon", function() {

		return {
			name: "iBeacon",
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
			},
			{
				// Must match the icon ID
				id: "isave", 
				type: "context", 
				panel: "editor_panel",
				title: "Save file.",
				
				// Events
				events: {
					'click': function() {
						console.log(svgCanvas.getSvgString())
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
							"stroke-width": "1",
							"fill":"#0000ff",
							"stroke-dasharray": "null",
							"stroke-linejoin": "null",
							"stroke-linecap": "null",
							"d": "m-25.97835,1.78687c-0.55082,-7.64931 2.31107,-15.47559 7.70132,-20.93505c0.73638,-0.71526 2.02457,-0.62195 2.69944,0.13269c0.81713,0.69314 0.83154,2.08116 0.03547,2.79641c-4.49609,4.67028 -6.92742,11.26406 -6.44382,17.73857c0.34608,5.37861 2.66286,10.58915 6.37356,14.49211c0.35477,0.34713 0.64599,0.79036 0.67109,1.30074c0.14996,1.27856 -1.18638,2.46096 -2.43699,2.18515c-0.44901,-0.07777 -0.82291,-0.36632 -1.12189,-0.696c-4.37502,-4.5692 -7.06197,-10.70354 -7.47818,-17.01463l0,0zm7.50135,0.18931c-0.63742,-5.86036 1.52269,-11.94563 5.71023,-16.09279c0.74023,-0.64798 1.95064,-0.56722 2.61589,0.15276c0.80359,0.65667 0.89385,1.98034 0.16524,2.72448c-2.61769,2.65521 -4.27985,6.2448 -4.55194,9.96703c-0.37496,4.52017 1.34012,9.13854 4.52497,12.357c0.78458,0.74222 0.69519,2.12458 -0.1394,2.79269c-0.6796,0.71998 -1.92263,0.77967 -2.6426,0.08864c-3.19162,-3.18982 -5.22197,-7.50334 -5.6824,-11.9898l0,0zm7.40121,-0.86619c-0.36726,-3.69833 1.0489,-7.52156 3.72722,-10.09502c0.73346,-0.70463 1.99568,-0.623 2.67434,0.11921c0.81339,0.67394 0.86818,2.02457 0.10582,2.75709c-1.48912,1.45061 -2.43023,3.45986 -2.54366,5.54019c-0.16822,2.36105 0.76433,4.74997 2.42355,6.42652c0.46336,0.41234 0.74795,1.02473 0.67396,1.65158c-0.10206,1.45542 -2.04484,2.46587 -3.21094,1.46325c-2.19577,-2.02444 -3.55609,-4.89992 -3.85029,-7.86281l0,0zm6.91115,-0.57002c-0.39991,-2.38317 1.56802,-4.80193 3.98469,-4.87885c2.36971,-0.22103 4.61827,1.87077 4.56629,4.24904c0.07409,2.13803 -1.69961,4.11942 -3.82606,4.30696c-2.23227,0.30474 -4.46747,-1.44111 -4.72492,-3.67715l0,0zm30.23208,-2.42523c0.5507,7.64921 -2.31119,15.47554 -7.70126,20.93493c-0.7365,0.71526 -2.02463,0.62208 -2.69938,-0.13263c-0.81719,-0.6932 -0.83167,-2.08116 -0.03559,-2.7966c4.49603,-4.67009 6.9273,-11.26402 6.44369,-17.73844c-0.34595,-5.37875 -2.66285,-10.58916 -6.37355,-14.49212c-0.35477,-0.34713 -0.64599,-0.7903 -0.67109,-1.30074c-0.15002,-1.2785 1.18631,-2.46102 2.43705,-2.18509c0.44894,0.07784 0.82297,0.3662 1.12189,0.69593c4.37508,4.56927 7.06197,10.70354 7.47824,17.01475l0,0zm-7.50129,-0.18941c0.63742,5.86036 -1.52276,11.94549 -5.7103,16.09271c-0.74029,0.64798 -1.95064,0.56728 -2.61583,-0.15282c-0.80365,-0.65661 -0.89398,-1.98034 -0.1653,-2.72442c2.61769,-2.65515 4.27991,-6.24483 4.55187,-9.96706c0.37496,-4.52027 -1.34006,-9.13852 -4.52498,-12.35704c-0.78458,-0.74215 -0.69513,-2.12452 0.13946,-2.79268c0.6796,-0.71998 1.92263,-0.77961 2.6426,-0.08846c3.19156,3.18976 5.22197,7.50328 5.68247,11.98976zm-7.40128,0.86619c0.36726,3.69823 -1.04884,7.5216 -3.72723,10.095c-0.73346,0.70463 -1.9957,0.62301 -2.67435,-0.11927c-0.81339,-0.67388 -0.86818,-2.0245 -0.10582,-2.75712c1.48911,-1.45061 2.43024,-3.45987 2.54368,-5.54019c0.16822,-2.36105 -0.7642,-4.74996 -2.42356,-6.42652c-0.46336,-0.41244 -0.74795,-1.0247 -0.67396,-1.65162c0.10207,-1.45542 2.04484,-2.46568 3.21095,-1.46312c2.19565,2.02457 3.55596,4.89993 3.85029,7.86283l0,0z",
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

