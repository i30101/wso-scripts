# woodsonscioly-scripts

This repository contains a number of coding tools for Woodson Science Olympiad events and club management. Reach out if you have any questions or concerns. 


## admin
Administrative tools for running Woodson Science Olympiad

### conflict finder
![version](https://img.shields.io/badge/release-v2.0.0-blue)
![python-versions](https://img.shields.io/badge/python-3.9_%7C_3.10_%7C_3.11-limegreen)

Finds every single conflict for each event, marginally useful for coming up with training session schedule


### dues analyzer
![version](https://img.shields.io/badge/release-v1.0.1-blue)
![python-versions](https://img.shields.io/badge/python-3.9_%7C_3.10_%7C_3.11-limegreen)

Reads and decrypts locally stored (!) email files for MySchoolBucks dues and obtains individual t-shirt preferences


### Dependencies
- Python 3.9 or newer
- PyPi `pandas` library for reading CSV files: install with `pip install pandas`

<br><br>


## cryptography
![version](https://img.shields.io/badge/release-v2.1.3-blue)
![python-versions](https://img.shields.io/badge/python-3.9_%7C_3.10_%7C_3.11-limegreen)

OP Codebusters cipher generation tool


### Depencencies
- Python 3.9 or newer
- PyPi `requests` library for quote generation: install with `pip install requests`

<br><br>



## arduino
![version](https://img.shields.io/badge/release-v1.0.0-blue)
![arduino](https://img.shields.io/static/v1?label=Arduino&message=v2.2.1&logo=arduino&logoColor=white&color=blue)

This folder contains code for events involving the Arduino platform. 

### Installation
Compiling and uploading code requires using the Arduino IDE. For Windows 11 school laptops, go to `Software Center` and install `Arduino`. For personal laptops, visit [Arduino's Software Page](https://www.arduino.cc/en/software).


### Code Setup - Robot Tour

Getting the code on your computer: 
1. Navigate to `Documents\Arduino` on your local drive
2. Create new a new folder `Robot`
3. Download `Robot.ino` from this reposity and copy to your new folder

Adding the MakeBlock library:
1. Install the MakeBlock Drive library by installing this [zip](https://codeload.github.com/Makeblock-official/Makeblock-Libraries/zip/master) file
2. This code is also in the repository
3. Unzip file and copy to `Documents\Ardunio\libraries`

Running your mBot:
1. Connect your robot to your computer via a USB-B cable
2. Select the right port/board and your board to `Ardunio Uno`
3. Hit the arrow or "upload" button to flash code to the Arduino
4. If you installed the MakeBlock library, your mBot should be up and running
<br>


### Code Setup - Detector Building

Coming soon!


