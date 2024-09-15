#define RED_PIN 10
#define GREEN_PIN 8
#define BLUE_PIN 7
#define IN_PIN A3

const int delayTime = 2;
const int numReadings = 1000;
int readings[numReadings];

int getRawADC() { return analogRead(IN_PIN); }

void red() {digitalWrite(RED_PIN, HIGH); }
void green() {digitalWrite(GREEN_PIN, HIGH); }
void blue() {digitalWrite(BLUE_PIN, HIGH); }

void clear() {
  digitalWrite(RED_PIN, LOW);
  digitalWrite(GREEN_PIN, LOW);
  digitalWrite(BLUE_PIN, LOW);
}

void setup() {
  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);

  // configure input
  pinMode(A3, INPUT);
  analogReadResolution(14);

  Serial.begin(9600);
}

void loop() {
  
  int sum = 0;
  for (int i = 0; i < numReadings; i++) {
    readings[i] = analogRead(A3);
    sum += readings[i];
    delay(delayTime);
  }

  // calculate average raw ADC value
  double average = sum / numReadings;

  Serial.println("\nTAKING READING");

  // print average raw ADC value
  Serial.println("Average raw: " + String(average));

  // print voltage
  Serial.println("Voltage: " + String(average * 5.0 / 16383));

  float ppm = 13.42 * average - 6884.3;

  // print concentration in PPM
  Serial.println("PPM: " + String (ppm));

  // change LED status
  if ((ppm > 625 && ppm < 2500) || (ppm > 4375)) {
    clear();
    red();
  } else if ((ppm < 1875) || (ppm > 2500 && ppm < 3125)) {
    clear();
    green();
  } else {
    blue();
  }
}
