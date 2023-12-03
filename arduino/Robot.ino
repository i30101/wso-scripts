/**
 * @author Andrew Kim
 * @version 1.0.0
 * @date 9 November 2023
 * @brief MakeBlock mBot driver for Robot Tour
 * 
 * WOODSON SCIENCE OLYMPIAD CALLISTO + IO ROBOT TOUR DRIVER
 * How the code works:
 * 1. You type out the following in setup:
 *    a. The target time given by the event supervisor
 *    b. The path of the robot 
 * 2. The code optimizes the speed and travel times of the robot
 * 
 *
 * 
 * How the robot works:
 * 1. The robot can only move forwards or backwards in 25cm intervals (half of a grid box)
 * 2. The robot can turn right, left, or do a u-turn
 * 3. Start the robot by pressing on the small black button on the top of the board
 */



#include "MeOrion.h"

MeDCMotor leftMotor(M1);
MeDCMotor rightMotor(M2);



// whether the robot should wait after each action
bool wait = true;

// duration of waiting time
int waitTime = 500;

// time a motor should be run to turn 90 degrees
int turnTime = 1000;


/**
 * TARGET TIME GIVEN BY EVENT SUPERVISOR
 * @note unit is seconds
 */
int time = 0;


/**
 * SPEED AT WHICH ROBOT SHOULD RUN TO MATCH GIVEN TIME
 * @note should be an int
 * @note range is -255 to 255
 */
uint8_t speed = 250;


/**
 *
 */
float runTime = 0;


/**
 * 
 */
void setSpeed() {
  // placeholder value
  speed = 255;
}


/**
 * Moves robot desired distance forward
 * @note MUST CALIBRATE!
 * @param meters the distance the robot should travel
 */
void forward(double seconds) {
  // run motors
  leftMotor.run(-speed);
  rightMotor.run(speed);
  delay(seconds * 1000);

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
 * Slows the robot down before stopping to turn
 * Intended for greater precision of movement
 * @pre speeds of motors are negative of the other
*/
void slowDown() {
  uint8_t tempSpeed = speed;
  
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
  forward(2);
}


// main loop
void loop() {
}

