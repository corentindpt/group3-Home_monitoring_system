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
	<li>Connect your Raspberry to a power supply and a network via Wifi or via Ethernet</li>
	<li>Enable the ssh on the Rapsberry Pi to control it from your pc</li>
	<ul>
		<li>Enter <code>sudo raspi-config</code> in the terminal window on the Raspberry Pi 4</li>
		<li>Select <code>Interfacing Options</code></li>
		<li>Navigate to and select <code>SSH</code></li>
		<li>Choose <code>Yes</code></li>
		<li>Select <code>Ok</code></li>
		<li>Choose <code>Finish</code></li>
	</ul>
	<li>Connect and enable the Pi Camera</li>
	<b>Be carefull !</b> Disconnect the power of the Raspberry Pi 4 before connect the Pi Camera.
		<ul>
			<li>Enter <code>sudo raspi-config</code> in the terminal</li>
			<li>Select <code>Interfacing Options</code></li>
			<li>Navigate to and select <code>Pi Camera</code></li>
			<li>Choose <code>Yes</code></li>
			<li>Select <code>Ok</code></li>
			<li>Choose <code>Finish</code></li>
		</ul>
	After the restart of the Raspberry, you can test the camera via the command <code>raspistill -o testImage.jpeg</code> or if the camera is upside down <code>raspistill -vf -hf -o testImage.jpeg</code>. There are others parameters for the command, check <a href=https://www.raspberrypi.org/documentation/raspbian/applications/camera.md> here</a>.
	You can also try a python test program, <a href=https://github.com/corentindpt/group3-Home_monitoring_system/tree/master/Programs/TestCamera> see /Programs/TestCamera</a>.
	<li>Update the Raspberry Pi 4 os and the installed packages</li>
		<ul>
			<li>Enter <code>sudo apt update</code> in the terminal</li>
			<li>Enter <code>sudo apt full-upgrade</code> in the terminal</li>
		</ul>	
</ol>
<h3>Installing</h3>
<ol>
	Here is the list of the needed libraries:
	<ul>
		<li>Numpy (version : 1.18.3)</li>
		<li>Matplotlib (version : 3.2.1)</li>
		<li>imutils (version : )</li>
		<li>Scipy (version : 1.4.1)</li>
		<li>Keras (version : 2.3.1)</li>
		<li>TensorFlow (version : 1.14.0)</li>
		<li>Pickle (version : 4.0)</li>
		<li>Dlib (version : 19.19.0)</li>
	</ul>
	<li>Install numpy library</li>
		<ul>
			<li>Enter <code>pip install numpy</code> in the terminal</li>
		</ul>	
	<li>Install matplotlib library</li>
		<ul>
			<li>Enter <code>pip install matplotlib</code> in the terminal</li>
		</ul>	
	<li>Install imutils library</li>
		<ul>
			<li>Enter <code>pip install imutils</code> in the terminal</li>
		</ul>	
	<li>Install scipy library</li>
		<ul>
			<li>Enter <code>pip install scipy</code> in the terminal.
				This step takes a long time (2-3 hours). You can revise your SI course during this period :-).
			</li>
		</ul>	
	<li>Install keras library</li>
		<ul>
			<li>Enter <code>pip install keras</code> in the terminal.</li>
		</ul>	
	<li>Install tensorflow library</li>
		<ul>
			<li>Enter <code>pip install tensorflow</code> in the terminal.</li>
		</ul>		
	<li>Install pickle library</li>
		<ul>
			<li>Normally, pickle is already installed on the raspberry. If not,
				enter <code>pip install pickle</code> in the terminal.</li>
		</ul>
	<li>Install dlib library</li>
		<ul>
			We have installed dlib with GPU support.
			<li>Enter <code>git clone https://github.com/davisking/dlib.git</code> in the terminal.</li>
			<li>Enter <code>cd dlib</code> in the terminal.</li>
			<li>Enter <code>mkdir build</code> in the terminal.</li>
			<li>Enter <code>cd build</code> in the terminal.</li>
			<li>Enter <code>cmake .. -DDLIB_USE_CUDA=1 -DUSE_AVX_INSTRUCTIONS=1</code> in the terminal.</li>
			<li>Enter <code>cmake --build</code> in the terminal.</li>
			<li>Enter <code>cd ..</code> in the terminal.</li>
			<li>Enter <code>python setup.py install --yes USE_AVX_INSTRUCTIONS --yes DLIB_USE_CUDA</code> in the terminal.</li>
			if it doesn’t works, you can try the installing without the GPU support :
			<li>Enter <code>pip install dlib</code> in the terminal.</li>
		</ul>				
</ol>	

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
