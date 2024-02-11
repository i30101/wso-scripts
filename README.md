# woodsonscioly-scripts

This repository contains a number of coding tools for Woodson Science Olympiad events and club management. Sensitive files have been hidden for security reasons. Reach out via LinkedIn if you have questions or concerns. 

<br><br>

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
![version](https://img.shields.io/badge/release-v3.1.0-blue)
![python-versions](https://img.shields.io/badge/python-3.9_%7C_3.10_%7C_3.11-limegreen)

OP Codebusters cipher generation tool able to create test questions for the following ciphers: 
- Fractionated Morse
- Complete Columnar Transposition
- Columnar Transportation
- Porta
- Hill 2x2
- Hill 3x3
- Nihilist


### Depencencies
- Python 3.9 or newer
- PyPi `requests` library for quote generation: install with `pip install requests`

<br><br>



## arduino
![version](https://img.shields.io/badge/release-v1.0.0-blue)
![arduino](https://img.shields.io/static/v1?label=Arduino&message=v2.2.1&logo=arduino&logoColor=white&color=blue)

This folder contains code for events involving the Arduino platform. 

### Installation
Compiling and uploading code requires using the Arduino IDE. For Windows 11 school laptops, go to `Software Center` and install `Arduino`. For personal laptops, visit [Arduino's Software Page](https://www.arduino.cc/en/software) and install the latest IDE.


### Code Setup - Robot Tour

Getting the code on your computer: 
- Navigate to `Documents\Arduino` on your local drive
- Create new a new folder `Robot`
- Download `Robot.ino` from this reposity and copy to your new folder

Adding the MakeBlock library:
- Install the MakeBlock Drive library by installing this [zip](https://codeload.github.com/Makeblock-official/Makeblock-Libraries/zip/master) file
- Unzip file and copy entire file to `Documents\Ardunio\libraries`

Running your mBot:
- Connect your robot to your computer via a USB-B cable
- Select the right port/board and your board to `Ardunio Uno`
- Hit the arrow or "upload" button to flash code to the Arduino
- If you installed the MakeBlock library, your mBot should be up and running


### Code Setup - Detector Building

Ignore the LiquidCrystal library if you are 

