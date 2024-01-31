#include <LiquidCrystal_I2C.h>
#include <Wire.h>


#define RED_PIN 5
#define GREEN_PIN 6
#define BLUE_PIN 7
#define POT_PIN A0


LiquidCrystal_I2C lcd(0x27, 16, 2);


/**
 * @return voltage value ranging from 0 to 5000
 */
int getPotReading() {
  float input = analogRead(POT_PIN);
  return int(input * 5000.0 / 1024.0);
}

int getRawADC() {
  return analogRead(A3);
}

void red() {
  digitalWrite(RED_PIN, HIGH);
}

void green() {
  digitalWrite(GREEN_PIN, HIGH);
}

void blue() {
  digitalWrite(BLUE_PIN, HIGH);
}

void clear() {
  digitalWrite(RED_PIN, LOW);
  digitalWrite(GREEN_PIN, LOW);
  digitalWrite(BLUE_PIN, LOW);
}

void setup() {
  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);
  pinMode(POT_PIN, INPUT);
  Serial.begin(9600);

  // lcd.init();
  // lcd.backlight();

  // set up ADC for pin 14
  // analogReadResolution(14);
}

void loop() {
  int reading = getRawADC();
  Serial.println(reading);
  red();
  green();
  blue();
  clear();

  // if (reading < 2048) {
  //   clear();
  // } else if (reading < 4096) {
  //   clear();
  //   red();
  // } else if (reading < 6144) {
  //   clear();
  //   green();
  // } else if (reading < 8192) {
  //   clear();
  //   blue();
  // } else if (reading < 10240) {
  //   clear();
  //   green();
  //   red();
  // } else if (reading < 12288) {
  //   clear();
  //   blue();
  //   green();
  // } else if (reading < 14336) {
  //   clear();
  //   red();
  //   green();
  // } else {
  //   clear();
  //   red();
  //   green();
  //   blue();
  // // }
  lcd.clear();
  lcd.setCursor(9, 0);
  lcd.print(9);
  // delay(100);
}