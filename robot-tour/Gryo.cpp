#pragma region VEXcode Generated Robot Configuration
// Make sure all required headers are included.
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include <string.h>


#include "vex.h"

using namespace vex;

// Brain should be defined by default
brain Brain;


// START IQ MACROS
#define waitUntil(condition)                                                   \
  do {                                                                         \
    wait(5, msec);                                                             \
  } while (!(condition))

#define repeat(iterations)                                                     \
  for (int iterator = 0; iterator < iterations; iterator++)
// END IQ MACROS


// Robot configuration code.
motor MotorGroup1MotorA = motor(PORT1, false);
motor MotorGroup1MotorB = motor(PORT12, true);
motor_group MotorGroup1 = motor_group(MotorGroup1MotorA, MotorGroup1MotorB);

motor MotorGroup7MotorA = motor(PORT7, true);
motor MotorGroup7MotorB = motor(PORT6, false);
motor_group MotorGroup7 = motor_group(MotorGroup7MotorA, MotorGroup7MotorB);

gyro Gyro5 = gyro(PORT5);

#pragma endregion VEXcode Generated Robot Configuration

/* ---------------- CONSTANTS ---------------- */
double RPM = 0;
double turnRPM = 15;
int targetDirection = 0;
double turnTime = 0;
double timeToTurn = 4;
bool GYRO_ENABLED = true;


/* ---------------- AUXILIARY METHODS ---------------- */
void printReading() {
  Brain.Screen.newLine();
  Brain.Screen.print("rotation: %f", Gyro5.rotation());
}

void setSpeed(double v) {
  MotorGroup1MotorA.setVelocity(v, rpm);
  MotorGroup1MotorB.setVelocity(v, rpm);
  MotorGroup7MotorA.setVelocity(v, rpm);
  MotorGroup7MotorB.setVelocity(v, rpm);
}

void turnRightTo();
void turnLeftTo();

void turnRightTo() {
  setSpeed(turnRPM);
  if (GYRO_ENABLED) {
    while (fabs(targetDirection - Gyro5.rotation()) > 0.5) {
      MotorGroup1MotorA.spin(forward);
      MotorGroup1MotorB.spin(reverse);
      MotorGroup7MotorA.spin(reverse);
      MotorGroup7MotorB.spin(forward);
      wait(1, msec);
      if (Gyro5.rotation() < targetDirection - 5) {
        turnLeftTo();
        break;
      }
    }
  } else {
    MotorGroup1MotorA.spin(forward);
    MotorGroup1MotorB.spin(reverse);
    MotorGroup7MotorA.spin(reverse);
    MotorGroup7MotorB.spin(forward);
    wait(timeToTurn, seconds);
  }
  MotorGroup1.stop();
  MotorGroup7.stop();
  setSpeed(RPM);
  wait(500, msec);
}

void turnLeftTo() {
  setSpeed(turnRPM);
  if (GYRO_ENABLED) {
    while (fabs(targetDirection - Gyro5.rotation()) > 0.5) { 
      MotorGroup1MotorA.spin(reverse);
      MotorGroup1MotorB.spin(forward);
      MotorGroup7MotorA.spin(forward);
      MotorGroup7MotorB.spin(reverse);
      wait(1, msec);
      if (Gyro5.rotation() > targetDirection + 5) {
        turnRightTo();
        break;
      }
    }
  } else {
    MotorGroup1MotorA.spin(reverse);
    MotorGroup1MotorB.spin(forward);
    MotorGroup7MotorA.spin(forward);
    MotorGroup7MotorB.spin(reverse);
    wait(timeToTurn, seconds);
  }
  MotorGroup1.stop();
  MotorGroup7.stop();
  setSpeed(RPM);
  wait(500, msec);
}



/* ---------------- MOVEMENT CONTROL ---------------- */
struct Movement {int movement; double units; };
Movement movements[100] = {};
int currentIndex = 0;
double totalDistance = 0;

void addMovement(int movement, double units, double dist) {
  movements[currentIndex] = {movement, units};
  currentIndex++;
  if (movement == 4 || movement == 5) {
    turnTime += (units * timeToTurn);
  }
  totalDistance += dist;
}

void goForward(double spaces) { addMovement(0, spaces, 50.0 * spaces); }
void goBack(double spaces) { addMovement(1, spaces, 50.0 * spaces); }
void goRight(double spaces) { addMovement(2, spaces, 50.0 * spaces); }
void goLeft(double spaces) { addMovement(3, spaces, 50.0 * spaces); }
void turnRight(int times) { addMovement(4, times, 0); }
void turnLeft(int times) { addMovement(5, times, 0); }

void run(double targetTime) {
  double travelTime = targetTime - turnTime;
  double rotations = totalDistance / 20.0;
  RPM = (rotations / travelTime) * 60.0;

  Brain.Screen.clearScreen();
  Brain.Screen.print("total distance: %f", totalDistance);
  Brain.Screen.newLine();
  Brain.Screen.print("RPM: %f", RPM);
  Brain.Screen.newLine();
  Brain.Screen.print("turnTime: %f", turnTime);

  setSpeed(RPM);
  for (auto &m : movements) {
    switch (m.movement) {
      case 0:
        MotorGroup7.spinFor(forward, m.units * 2.5, turns);
        break;
      case 1:
        MotorGroup7.spinFor(reverse, m.units * 2.5, turns);
        break;
      case 2: 
        MotorGroup1.spinFor(forward, m.units * 2.5, turns);
        break;
      case 3:
        MotorGroup1.spinFor(reverse, m.units * 2.5, turns);
        break;
      case 4:
        targetDirection -= (90 * m.units);
        turnRightTo();
        break;
      case 5:
        targetDirection += (90 * m.units);
        turnLeftTo();
        break;
      default:
        Brain.Screen.clearScreen();
        Brain.Screen.print("error");
        break;
    }
  }
}



int main() {
  Brain.Screen.print("Calibrating!");
  Gyro5.calibrate(calNormal);

  goForward(3.76);
  goLeft(1);
  goBack(1);
  goLeft(1);
  goBack(2);
  turnLeft(1);
  goForward(0.6);
  goBack(0.6);
  turnRight(1);
  goForward(3);
  turnLeft(1);
  goForward(0.6);
  goBack(0.6);
  turnRight(1);
  goBack(1.26);

  /* ---------------- MUST REVIEW BEFORE RUNNING! ---------------- */
  GYRO_ENABLED = true;
  run(60);
}