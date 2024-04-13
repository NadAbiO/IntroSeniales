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
5. [Discusión](#id9)
6. [Archivos](#id10)
***
## **Introducción** <a name="id1"></a>
Las señales biomédicas como la electromiografía (EMG) y el electrocardiograma (ECG) son fundamentales para mejorar el diagnóstico médico y mejorar el tratamiento. El laboratorio tiene como objetivo avanzar en la comprensión y el control de estas señales biomédicas utilizando tecnologías avanzadas que permitan una captura y análisis eficientes. Este informe describe el proceso de adquisición de señales EMG utilizando el sistema BiTalino, un dispositivo versátil y fácil de usar diseñado para aplicaciones biomédicas.

***
## **Objetivos** <a name="id2"></a>
- Adquirir señales biomédicas de EMG y ECG.
- Hacer una correcta configuración de BiTalino.
- Extraer la información de las señales EMG y ECG del software OpenSignals (r)evolution

***
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
***
## **Resultados** <a name="id6"></a>
### **Video de la señal y Ploteo de la señal en OpenSignal** <a name="id7"></a>

En la prueba 1 (Alvaro Cigarán) se tomaron señales del reposo y contraccion del brazo, realizando un total de 5 contracciones intentando mantener el mismo nivel de intensidad<video src="https://github.com/NadAbiO/IntroSeniales/assets/89696355/fc7d09d6-4187-4c49-ad28-0e2f5665a451">

En la prueba 2 (Bruno Tello) se tomaron señales del reposo y contraccion del brazo, realizando un total de 4 contracciones, las 2 iniciales siendo leves y posteriormente 2 con mayor intensidad <video src="https://github.com/NadAbiO/IntroSeniales/assets/89696355/342fb4fb-9379-489e-8dab-4b2a8ff090d1">

En la prueba 3 (Kimberly Tito) se tomaron señales del reposo y contraccion del brazo, realizando un total de 4 contracciones intercalando el nivel de intensidad entre estas <video src="https://github.com/NadAbiO/IntroSeniales/assets/89696355/b20587c5-c154-42e3-ab5c-d82674526e56">


### **Ploteo de la señal en Python** <a name="id8"></a>
#### Prueba 1 (Álvaro Cigarán)
<p align="center">
  <img width="460" height="300" src="https://github.com/NadAbiO/IntroSeniales/blob/d89ea89b08f120aeae8d22b9aafe5de57bfd7395/ISB/Laboratorios/Laboratorio3/Se%C3%B1ales_EMG/Alvaro.png">
</p> 
<em><p align="center">1era Prueba: 5 Contracciones leves</p></em>

La señal fluctúa entre períodos de menor y mayor actividad eléctrica, reflejando diferentes intensidades en la contracción del músculo.

#### Prueba 2 (Bruno Tello)

<p align="center">
  <img width="460" height="300" src="https://github.com/NadAbiO/IntroSeniales/blob/7ffa4febc457ecbf7bccf107111b8ec98c56bbc7/ISB/Laboratorios/Laboratorio3/Se%C3%B1ales_EMG/Bruno.png">
</p> 
<em><p align="center">2da Prueba: 2 contracciones leves y 2 contracciones fuertes</p></em>
En comparación con la Prueba 1, las contracciones tienen una mayor amplitud, indicando una contracción más fuerte o una mayor respuesta del músculo.

#### Prueba 3 (Kimberly Tito)

<p align="center">
  <img width="460" height="300" src="https://github.com/NadAbiO/IntroSeniales/blob/27c27fcf60a2edf8676019d2ac410a710b6506e7/ISB/Laboratorios/Laboratorio3/Se%C3%B1ales_EMG/Kim.png">
</p> 
<em><p align="center">3ra Prueba: 4 Contracciones leves y fuertes intercaladas</p></em>
Incluyen picos altos similares a los de la Prueba 2, con algunos periodos de actividad más constante, demostrando una mezcla de contracciones fuertes y leves.

***
## **Discusión** <a name="id9"></a>


Para comprender a fondo la electromiografía, es esencial explicar primero qué constituye una unidad motora. Esta unidad representa el componente más básico y pequeño de un músculo e incluye una única neurona motora y todas las fibras musculares que esta inerva. Durante un electromiograma, se mide la actividad eléctrica que generan estas unidades motoras al activarse durante una contracción muscular. A través del EMG, podemos visualizar la representación bioeléctrica de dicha actividad, conocida como potenciales de unidad motora (PUM). Cada vez que una unidad motora emite un impulso eléctrico, las fibras musculares correspondientes se contraen y generan un potencial eléctrico mensurable. En los registros de PUM, una deflexión hacia arriba indica una polaridad negativa, mientras que una deflexión hacia abajo muestra una polaridad positiva. La forma y polaridad de estos potenciales son cruciales para diagnosticar diversas condiciones neuromusculares.

<p align="center">
  <img width="460" height="300" src="https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Laboratorio3/Se%C3%B1ales_EMG/Analisis_de_signal.png?raw=true">
</p> 
<em><p align="center">Análisis de EMG</p></em>


***
### **Archivos** <a name="id10"></a>

- [Documentos (.txt)](https://github.com/NadAbiO/IntroSeniales/tree/d3b35c0b271c22b37876451e3511eb8a77f34da4/ISB/Laboratorios/Laboratorio3/Se%C3%B1ales_EMG)

- [Ploteo de la señal (.py)](https://github.com/NadAbiO/IntroSeniales/blob/315d3a861240fa3999442cdf8c89407ae29e8ad6/ISB/Laboratorios/Laboratorio3/adq_senial.py)

