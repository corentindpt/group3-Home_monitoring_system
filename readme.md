<h1>Home monitoring system</h1>

In order to facilitate access for house residents, a pi camera is placed near the front door, pointing to people wanting to enter.

<img src="pictures/Project_presentation_1.png" alt="Project_presentation_1" />

The faces of all the resident of the house are registered beforehand.

<img src="pictures/Project_presentation_2.png" alt="Project_presentation_2" />

Thanks to the Raspberry and the Pi camera, the video stream is analyzed. If the person is recognized by the system and is allowed to enter, the door is unlocked via the Arduino.

<img src="pictures/Project_presentation_3.png" alt="Project_presentation_3" />

 If the person is not recognized by the system or is not allowed to enter in the house, a doorbell rings to notify the residents of a guest coming in thanks to the Arduino. 

<img src="pictures/Project_presentation_4.png" alt="Project_presentation_4" />

Furthermore, a picture of the guest is sent to the resident by mail, saved into the Raspberry Pi and displayed on a screen inside the house.

<img src="pictures/Project_presentation_5.png" alt="Project_presentation_5" />

In the event that is dark, and a person is detected by the Raspberry, the outside light is switched on by the Arduino. After a few seconds, the light is switched off.

<img src="pictures/Project_presentation_6.png" alt="Project_presentation_6" />

<hr>
<h2><u>Summary</u></h2>
<ul>
  <li><strong>Getting started</strong></li>
  <li><strong>Start the program</strong></li>
  <li><strong>Contributing</strong></li>
  <li><strong>Authors</strong></li>
</ul>
<hr>
<h2><u>Getting started</u></h2>
<h3>prerequisite</h3>
<h4>Material list</h4>
<img src="pictures/Material_list.jpeg" alt="Material_list" />
<h3>Configuration of the Raspberry Pi 4</h3>
<ol>
	<li>Connect your Raspberry to a network via Wifi or via Ethernet</li>
	<li>Enable the ssh on the Rapsberry Pi to access to the terminal from your pc</li>
	<ul>
		<li>Enter <code>"sudo raspi-config"</code> in the terminal window</li>
		<li>Select "Interfacing Options"</li>
		<li>Navigate to and select "SSH"</li>
		<li>Choose "Yes"</li>
		<li>Select "Ok"</li>
		<li>Choose "Finish"</li>
	</ul>
	<li>Enable the Pi Camera</li>
</ol>
<h3>Installing</h3>

<hr>
<h2><u>Start the program</u></h2>

<hr>
<h2><u>Contributing</u></h2>

<hr>
<h2><u>Authors</u></h2>
<ul>
  <li><strong>Goffin Gerome</strong></li>
  <li><strong>Dupont Corentin</strong></li>
  <li><strong>Josis Arnaud</strong></li>
</ul>
