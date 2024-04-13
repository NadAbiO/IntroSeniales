# Laboratorio 3 - Adquisición señales EMG

## **Tabla de contenidos**
1. [Introducción](#id1)
2. [Objetivos](#id2)
3. [Metodología](#id3)\
     3.1 [Fotos de la conexión](#id4)\
     3.1 [Guías electromiográficas](#id5)
4. [Resultados](#id6)\
     3.1 [Video de la señal y Ploteo de la señal en OpenSignal](#id7)\
     3.2 [Ploteo de la señal en Python](#id8)\
     3.3 [Archivos](#id9)

## **Introducción** <a name="id1"></a>
Las señales biomédicas como la electromiografía (EMG) y el electrocardiograma (ECG) son fundamentales para mejorar el diagnóstico médico y mejorar el tratamiento. El laboratorio tiene como objetivo avanzar en la comprensión y el control de estas señales biomédicas utilizando tecnologías avanzadas que permitan una captura y análisis eficientes. Este informe describe el proceso de adquisición de señales EMG utilizando el sistema BiTalino, un dispositivo versátil y fácil de usar diseñado para aplicaciones biomédicas.


## **Objetivos** <a name="id2"></a>
- Adquirir señales biomédicas de EMG y ECG.
- Hacer una correcta configuración de BiTalino.
- Extraer la información de las señales EMG y ECG del software OpenSignals (r)evolution


## **Metodología** <a name="id3"></a>
Se utilizó la conexión EMG en la placa Bitalino utilizando el sensor EMG de 3 electrodos como se muestra a continuación.

<p align="center">
  <img width="460" height="300" src="https://github.com/NadAbiO/IntroSeniales/blob/04b4b318e89baa6323d34983073915a5d99de282/Anexos/Laboratorios/BITalino.jpeg">
</p> 

1. Conexión BITalino por medio de Bluetooth.
2. Se colocaron dos electrodos, uno positivo y otro negativo, en el bíceps braquial izquierdo.
3. Luego, se colocó un electrodo de referencia en una área con poca actividad muscular, como el codo, para minimizar interferencias.
4. Inició la captura de la señal estando en reposo.
7. Se realizó un ciclo de contracción y liberación del músculo, seguido de un período de descanso, cinco veces consecutivas.
8. Finalmente se detuvo la grabación y se guardaron los datos obtenidos.

