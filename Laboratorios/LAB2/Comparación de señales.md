# Laboratorio 2 - Adquisición de señales y graficación en Arduino
***

## Objetivos
- Capturar señales identificadas como formas cuadradas, triangulares, sinusoidales, rampas y más.
- Entender los elementos que determinan la selección de la frecuencia de muestreo adecuada.
- Operar y calibrar de manera eficiente dispositivos como una fuente de poder ajustable, un multímetro digital, un generador de funciones y un osciloscopio digital.
---

## Generación de señales
El generador de señales es útil para producir señales eléctricas con diferentes parámetros como frecuencia y amplitud. Se configura para generar la señal deseada, luego se visualiza con un osciloscopio. En este laboratorio, generamos 3 señales distintas y comparamos las gráficas obtenidas mediante el  osciloscopio con las señales graficadas por el Arduino Nano 33 IoT.

**Carácterísticas y comparación:**

### Onda sinusoidal
Frecuencia= 1KHz
Forma= sinusoidal
Vpp=5V, offset= 0V

<p align="center">
  <img width="460" height="300" src="https://github.com/NadAbiO/IntroSeniales/blob/18924b64c18a5a575f808ad1ba2b23f68c9aa4f3/Anexos/sinusoidal.jpeg">
</p>

                                    Onda sinusoidal en el Serial Plotter de Arduino IDE:
<p align="center">
  <img width="460" height="300" src="https://github.com/NadAbiO/IntroSeniales/blob/30ac0878deb48294ac68e9ac71535bad82cd66d4/Anexos/sin_arduino.png">
</p>


### Onda cuadrada
Frecuencia= 1KHz
Forma= cuadrada
Vpp=5V, offset= 0V

<p align="center">
  <img width="460" height="300" src="https://github.com/NadAbiO/IntroSeniales/blob/dd1901ce6a8aa4b74cd673735fe22a586e1d77fb/Anexos/cuadrada.jpeg">
</p>


### Onda triangular
Frecuencia= 1KHz
Forma= cuadrada
Vpp=5V, offset= 0V

<p align="center">
  <img width="460" height="300" src="https://github.com/NadAbiO/IntroSeniales/blob/cf2ed693fc405f83ca6400063f5dac8086353eac/Anexos/triangular.jpeg">
</p>

***
## Código Arduino
```
const int analogPin = A0; // Define la constante analogPin como el pin A0, 
//que será utilizado para leer la señal analógica.

unsigned long lastMsg = 0; //almacenar el tiempo en milisegundos del último mensaje enviado.
float F=1;                      // 1 hz
double Fs = 10*F;               // 10 hz
double Ts_ms = (1/Fs)*1000;     //  100 ms  

void setup() {
  Serial.begin(9600); //Inicia la comunicación serial
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

```
***
##   Ploteo de señales en Arduino

***

## Conclusiones
En resumen, este experimento nos proporcionó una comprensión más profunda sobre cómo trazar señales en Arduino IDE procedentes de un generador de señales. Se evidenció que el cable BNC, con una atenuación de x10, tuvo un impacto significativo en la visualización de la señal. Además, la inclusión del condensador en el circuito actuó como un filtro, disminuyendo efectivamente el ruido presente en la señal deseada.
