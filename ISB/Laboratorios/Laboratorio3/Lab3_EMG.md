# Laboratorio 3 - Adquisición señales EMG

## **Tabla de contenidos**
1. [Introducción](#id1)
2. [Objetivos](#id2)
3. [Metodología](#id3)\
     3.1 [Fotos de la conexión](#id4)\
     3.2 [Guía electromiográfica](#id5)
4. [Resultados](#id6)\
     4.1 [Video de la señal y Ploteo de la señal en OpenSignal](#id7)\
     4.2 [Ploteo de la señal en Python](#id8)\
     4.3 [Archivos](#id9)

## **Introducción** <a name="id1"></a>
Las señales biomédicas como la electromiografía (EMG) y el electrocardiograma (ECG) son fundamentales para mejorar el diagnóstico médico y mejorar el tratamiento. El laboratorio tiene como objetivo avanzar en la comprensión y el control de estas señales biomédicas utilizando tecnologías avanzadas que permitan una captura y análisis eficientes. Este informe describe el proceso de adquisición de señales EMG utilizando el sistema BiTalino, un dispositivo versátil y fácil de usar diseñado para aplicaciones biomédicas.


## **Objetivos** <a name="id2"></a>
- Adquirir señales biomédicas de EMG y ECG.
- Hacer una correcta configuración de BiTalino.
- Extraer la información de las señales EMG y ECG del software OpenSignals (r)evolution


## **Metodología** <a name="id3"></a>
### **Fotos de la conexión** <a name="id4"></a>
Se utilizó la conexión EMG en la placa Bitalino utilizando el sensor EMG de 3 electrodos como se muestra a continuación.

<p align="center">
  <img width="460" height="300" src="https://github.com/NadAbiO/IntroSeniales/blob/04b4b318e89baa6323d34983073915a5d99de282/Anexos/Laboratorios/BITalino.jpeg">
</p> 
<em><p align="center">Conexión en BiTalino</p></em>

1. Conexión BITalino por medio de Bluetooth.
2. Se colocaron dos electrodos, uno positivo y otro negativo, en el bíceps braquial izquierdo.
3. Luego, se colocó un electrodo de referencia en una área con poca actividad muscular, como el codo, para minimizar interferencias.
4. Inició la captura de la señal estando en reposo.
7. Se realizó un ciclo de contracción y liberación del músculo, seguido de un período de descanso, cinco veces consecutivas.
8. Finalmente se detuvo la grabación y se guardaron los datos obtenidos.


### **Guía electromiográfica** <a name="id5"></a>

Como referencia para la colocación de los electrodos y buenas prácticas durante la toma de datos utilizamos la siguiente guía:

- BITalino (r)evolution Lab Guide
  https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide1_EMG.pdf

Una consideración importante es que el paciente se encuentre en una posición cómoda y relajada, sin objetos metálicos que interfieran. Además, al colocar los electrodos sobre la piel, es fundamental asegurar que la zona esté limpia. Asimismo, es necesario seguir las guías para garantizar la correcta ubicación de los electrodos positivo, negativo y de referencia en sus respectivas áreas.

## **Resultados** <a name="id6"></a>
### **Video de la señal y Ploteo de la señal en OpenSignal** <a name="id7"></a>


|<video src="https://github.com/NadAbiO/IntroSeniales/blob/1580db42e4102d9f0211767390ac96dc52d5835e/Anexos/Laboratorios/Se%C3%B1al_Alvaro.mp4">|<video src="https://github.com/NadAbiO/IntroSeniales/blob/d0aabcc28630d5eeb89ba88f1ce359d80de15abe/Anexos/Laboratorios/Se%C3%B1al_Bruno.mp4">|
|--------------------------|--------------------------|

|<video src="https://github.com/NadAbiO/IntroSeniales/blob/49c08082e671159f89028ce6481f36c2898f7b36/Anexos/Laboratorios/Se%C3%B1al_Kim.mp4">|

### **Ploteo de la señal en Python** <a name="id8"></a>
#### Prueba 1 (Álvaro Cigarán)
<p align="center">
  <img width="460" height="300" src="https://github.com/NadAbiO/IntroSeniales/blob/d89ea89b08f120aeae8d22b9aafe5de57bfd7395/ISB/Laboratorios/Laboratorio3/Se%C3%B1ales_EMG/Alvaro.png">
</p> 
<em><p align="center">DESCRIPCIÓN DE IMAGEN</p></em>

#OLA COMENTEN LO QUE VEN Y PONGAN DESCRIPCIÓN EN LA FOTO
#### Prueba 2 (Bruno Tello)

<p align="center">
  <img width="460" height="300" src="https://github.com/NadAbiO/IntroSeniales/blob/7ffa4febc457ecbf7bccf107111b8ec98c56bbc7/ISB/Laboratorios/Laboratorio3/Se%C3%B1ales_EMG/Bruno.png">
</p> 
<em><p align="center">DESCRIPCIÓN DE IMAGEN</p></em>
#OLA COMENTEN LO QUE VEN Y PONGAN DESCRIPCIÓN EN LA FOTO

#### Prueba 3 (Kimberly Tito)

<p align="center">
  <img width="460" height="300" src="https://github.com/NadAbiO/IntroSeniales/blob/27c27fcf60a2edf8676019d2ac410a710b6506e7/ISB/Laboratorios/Laboratorio3/Se%C3%B1ales_EMG/Kim.png">
</p> 
<em><p align="center">DESCRIPCIÓN DE IMAGEN</p></em>
#OLA COMENTEN LO QUE VEN Y PONGAN DESCRIPCIÓN EN LA FOTO

### **Archivos** <a name="id9"></a>

- [Documentos (.txt)](https://github.com/NadAbiO/IntroSeniales/tree/d3b35c0b271c22b37876451e3511eb8a77f34da4/ISB/Laboratorios/Laboratorio3/Se%C3%B1ales_EMG)

- [Ploteo de la señal (.py)](https://github.com/NadAbiO/IntroSeniales/blob/315d3a861240fa3999442cdf8c89407ae29e8ad6/ISB/Laboratorios/Laboratorio3/adq_senial.py)
