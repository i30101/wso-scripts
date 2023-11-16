/**
 * @author Andrew Kim
 * @version 1.0.0
 * @date 9 November 2023
 * @brief MakeBlock mBot driver for Robot Tour
 */

#include "MeOrion.h"

MeDCMotor leftMotor(M1);
MeDCMotor rightMotor(M2);

// speed of the robot, between -255 and 255
uint8_t speed = 250;

// whether the robot should wait after each action
bool wait = true;

// duration of waiting time
int waitTime = 500;

// time a motor should be run to turn 90 degrees
int turnTime = 1000;


/**
 * Moves robot desired distance forward
 * @note MUST CALIBRATE!
 * @param meters the distance the robot should travel
 */
void forward(double centimeter) {
  // run motors
  leftMotor.run(-speed);
  rightMotor.run(speed);
  double secondsPerCentimeter = 1.0/44;
  Serial.println(centimeter * secondsPerCentimeter);
  delay(centimeter * secondsPerCentimeter * 1000);

  // stop motors
  leftMotor.stop();
  rightMotor.stop();

  // wait if wanted by user
  if(wait) {
    delay(waitTime);
  }
}


/**
 * Moves robot desired distance backward
 * @note MUST CALIBRATE!
 * @param meters the distance the robot should travel
 */
void backward(double meters) {
  // run motors
  leftMotor.run(speed);
  rightMotor.run(-speed);
  delay(meters * 1000);

  // stop motors
  leftMotor.stop();
  rightMotor.stop();

  // wait if wanted by user
  if(wait) {
    delay(waitTime);
  }
}


/**
 * Turns robot to the right
 * @note MUST CALIBRATE!
 */
void right() {
  // run left motor to turn right
  leftMotor.run(-speed);
  rightMotor.run(-speed);
  delay(turnTime / 2);
  
  // stop motor
  leftMotor.stop();
}


/**
 * Turns robot to the left
 * @note MUST CALIBRATE!
 */
void left() {
  // run right motor to turn left
  leftMotor.run(speed);
  rightMotor.run(speed);
  delay(turnTime / 2);

  // stop motor
  rightMotor.stop();
}


/**
 * Turns robot 180 degrees
 * @note MUST CALIBRATE!
 */
void uTurn() {
  leftMotor.run(speed);
  rightMotor.run(speed);
  delay(turnTime);

  // stop motors
  leftMotor.stop();
  rightMotor.stop();
}





// program setup
void setup() {
  // nothing to set up
  Serial.begin(9600);
  delay(1000);
  forward(100);
}


// main loop
void loop() {
}

