/*************************************
 Course: ISB-UPCH
 Date: 29/03/2023
 Autor: Moises Meza

**************************************/
const int analogPin = A0; 

unsigned long lastMsg = 0;
float F=1;                      // 1 hz
double Fs = 10*F;               // 10 hz
double Ts_ms = (1/Fs)*1000;     //  100 ms  

void setup() {
  Serial.begin(9600);
  while (!Serial);
  //Serial.println("R1:,R2:,");
  pinMode(analogPin, INPUT);
}

void loop() {

  unsigned long now = millis();

  if (now - lastMsg > Ts_ms) {
    
    lastMsg = now;

    int r1 = analogRead(analogPin);

    Serial.print("Señal1:");
    Serial.println(r1);

  }

}