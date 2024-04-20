# Laboratorio 4 - Adquisición señales ECG

## **Tabla de contenidos**
- [Introducción](#id1)
- [Objetivos](#id2)
- [Metodología](#id3)
  - [Materiales y equipos](#id13)
  - [Fotos de la conexión](#id4)
  - [Guía electrocardiográfica](#id5)
- [Resultados](#id6)
  - [Video de la señal y Ploteo de la señal en OpenSignal](#id7)
  - [Archivos](#id8)
  - [Ploteo de la señal en Python](#id9) <br>
  - [Señal del Promsim4](#id10) <br>
- [Discusión](#id11)
- [Referencias](#id12)
***
## **Introducción** <a name="id1"></a>
Las señales biomédicas como la electromiografía (EMG) y el electrocardiograma (ECG) son fundamentales para mejorar el diagnóstico médico y mejorar el tratamiento. El laboratorio tiene como objetivo avanzar en la comprensión y el control de estas señales biomédicas utilizando tecnologías avanzadas que permitan una captura y análisis eficientes. Este informe describe el proceso de adquisición de señales ECG utilizando el sistema BiTalino, un dispositivo versátil y fácil de usar diseñado para aplicaciones biomédicas.

### La señal de ECG
La señal del electrocardiograma (ECG) resulta crucial ya que ofrece datos significativos sobre el rendimiento del corazón del paciente. Este examen, no intrusivo, registra la actividad eléctrica cardíaca mediante electrodos adosados a la piel. Su utiliza habitualmente en la detección y diagnóstico de diversas afecciones cardíacas, incluyendo arritmias, infarto de miocardio, hipertrofia ventricular, y otros problemas que influyen en la función cardiaca [1].

En un electrocardiograma (ECG) normal, los latidos del corazón se reflejan a través de variaciones en la línea de base, representadas por ángulos, segmentos, ondas e intervalos. Estos elementos forman una imagen característica que se repite de manera regular a lo largo de todo el registro. Un ECG típico muestra una sucesión de deflexiones, conocidas como ondas, que se alternan con la línea basal. Al leer el ECG de izquierda a derecha, se identifican la onda P, el segmento P-R, el complejo QRS, el intervalo QT, el segmento ST y, finalmente, la onda T. Esta disposición puede apreciarse en la imagen adjunta [2].

<p align="center">
  <img width="460" height="300" src="https://github.com/NadAbiO/IntroSeniales/blob/e3dd6f5f0a621e8a486cf26a2decd3816548c45b/Anexos/Laboratorios/ECG.png">

</p> 
<em><p align="center">Figura 1. Ondas e Intervalos [2]</p></em>

<div align="center">

|  **Onda/Segmento**  | **Descripción** |
|:------------:|:---------------:|
| Onda P | Representa la despolarización de las aurículas, estas se están contrayendo y enviando sangre hacia los ventrículos. La duración normal es menor de 0.10 s y una amplitud máxima de 0.25 mV. Es positiva en casi todas las derivaciones [2]. |
|Intervalo PR | Distancia entre el inicio de despolarización de la onda P y el inicio del complejo QRS. En condiciones normales, dura entre 0,10 y 0,20 segundos [2].   |
|Segmento PR   | Es el tramo de la línea basal entre el final de la onda p y el inicio del complejo QRS. Las aurículas terminan de vaciarse y se produce una desaceleración en la transmisión de la corriente eléctrica a través del corazón, justo antes del inicio de la contracción de los ventrículos [2].    |
| Complejo QRS | Representa la despolarización ventricular. Los ventrículos se contraen y expulsan su contenido sanguíneo, no debe exceder en duración más de dos cuadrados pequeños [2].  |
|  Segmento ST | Representa la despolarización completa del miocardio ventricular. La variación en la posición con respecto a la línea de basal puede sugerir la presencia de ciertas enfermedades [2].    |
|     Onda T   |  Representa la repolarización de los ventrículos. Generalmente es de menor amplitud que el complejo QRS [2].   |

<div align="left">

## **Objetivos** <a name="id2"></a>
- Adquirir señales biomédicas de ECG.
- Hacer una correcta configuración de BiTalino.
- Extraer la información de las señales ECG del software OpenSignals (r)evolution
- Graficar la información usando python

***
## **Metodología** <a name="id3"></a>

### **Materiales y equipos** <a name="id13"></a>
|  **Modelo**  | **Descripción** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| (R)EVOLUTION |   Kit BITalino  |       1      |
|       -      |      Laptop     |       1      |

### **Fotos de la conexión** <a name="id4"></a>
Se utilizó la conexión ECG en la placa Bitalino utilizando el sensor ECG de 3 electrodos como se muestra a continuación.

<p align="center">
  <img width="460" height="300" src="https://github.com/NadAbiO/IntroSeniales/blob/04b4b318e89baa6323d34983073915a5d99de282/Anexos/Laboratorios/BITalino.jpeg">
</p> 
<em><p align="center">Figura 2. Conexión en BiTalino</p></em>

1. Conexión BITalino por medio de Bluetooth.
2. Se colocaron dos electrodos, uno positivo y otro negativo, en el brazo izquierdo y brazo derecho respectivamente.
3. Luego, se colocó un electrodo de referencia en la cresta iliaca (se tomaron los puntos de referencia de la guía de BITalino).
4. Se capturaron señales en distintas condiciones de actividad corporal.
7. Los usuarios realizaron ejercicio físico y de respiración.
8. Se detuvo la grabación y se guardaron los datos obtenidos.
9. Con el programa python se graficó las imágenes en las cuales se pueden observar diferencias significativas.

### **Guía electrocardigráfica** <a name="id5"></a>

Como referencia para la colocación de los electrodos y buenas prácticas durante la toma de datos utilizamos la siguiente guía [3]:

<div align="center">

| Posición electrodos | Posición electrodos  |
|----------|----------|
| <img src="ruta/a/imagen1.png" alt="Bruno Tello" width="200"/> | <img src="https://github.com/NadAbiO/IntroSeniales/blob/c6e77fb34350850608bde48b88fe8e13443ee5f6/Anexos/Laboratorios/BITalino_ECG.jpg" alt="Alvaro Cigarán" width="200"/> |

<div align="left">


Una consideración importante es que el paciente se encuentre en una posición cómoda y relajada, sin objetos metálicos que interfieran. Además, al colocar los electrodos sobre la piel, es fundamental asegurar que la zona esté limpia. Asimismo, es necesario seguir las guías para garantizar la correcta ubicación de los electrodos positivo, negativo y de referencia en sus respectivas áreas.
***
## **Resultados** <a name="id6"></a>
### **Video de la señal y Ploteo de la señal en OpenSignal** <a name="id7"></a>

Para la captura de señales, se seleccionaron dos integrantes del grupo: Bruno Tello (Sujeto 1) y Alvaro Cigarán (Sujeto 2). A ambos se les realizó la medición de la señal ECG en dos diferentes estados:
  * Estado reposo: Evaluamos cuando los sujetos se encuentra en un estado de inactividad.
  * Luego de Actividad física: Evaluamos la señal luego de que hayan realizando ejercicios anaeróbicos, específicamente burpees durante dos minutos.
  
#### Sujeto 1 (Bruno Tello) 

|                 **Modelo**                 | **Video** |
|:------------------------------------------:|:---------:|
|                **Estado Reposo**             |<video src="https://github.com/NadAbiO/IntroSeniales/blob/main/Anexos/Laboratorios/LabECG/Burpees.mp4">
|         **Luego de Actividad física**        |<video src="" ></video>|

#### Sujeto 2 (Alvaro Cigarán) 

|                 **Modelo**                 | **Video** |
|:------------------------------------------:|:---------:|
|                **Estado Reposo**             |<video src="" ></video>|
|         **Luego de Actividad física**        |<video src="" ></video>|


### **Archivos** <a name="id8"></a>

- [Documentos (.txt/.png)](https://github.com/NadAbiO/IntroSeniales/tree/062579d29b1ff90dda9f222c8a9d4834159bf05e/ISB/Laboratorios/Lab4_ECG/Se%C3%B1ales_ECG)
  
- [Código para el ploteo de la señal (.py)](https://github.com/NadAbiO/IntroSeniales/blob/062579d29b1ff90dda9f222c8a9d4834159bf05e/ISB/Laboratorios/Lab4_ECG/adq_ECG.py)


### **Ploteo de la señal en Python** <a name="id9"></a>
Se han graficado las señales en Python para analizar segmentos de tiempo específicos que permiten identificar las ondas características de un ECG, así como para evaluar la frecuencia cardíaca.

#### Sujeto 1 (Bruno Tello) 

A continuación, se presenta el ECG del sujeto 1, visualizado mediante Python. Las gráficas muestran un intervalo de tres segundos en dos estados diferentes: en reposo y después de realizar actividad física. 
<div align="center">

| En reposo |Luego de actividad física |
|----------|----------|
| <img src="https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab4_ECG/Se%C3%B1ales_ECG/bruno_reposo.png" alt="Reposo" width="800"/> | <img src="https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab4_ECG/Se%C3%B1ales_ECG/bruno_ejercicio.png" alt="Act física" width="800"/> |

<div align="left">


Ahora mostraremos las ondas características en la señal: 
<div align="center">

| En reposo |Luego de actividad física |
|----------|----------|
| <img src="https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab4_ECG/Se%C3%B1ales_ECG/En_reposo_RR.png"/> | <img src="https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab4_ECG/Se%C3%B1ales_ECG/Analisis_Onda_ejercicio.png" alt="Act física" width="800"/> |

<div align="left">

La identificación de los complejos QRS es esencial en la interpretación de un ECG. El intervalo RR, definido como el periodo entre dos ondas R sucesivas, es un indicador del ritmo cardíaco. Para calcular la frecuencia cardíaca, se mide la duración del intervalo RR y se establece la cantidad de estos intervalos que se presentan en un lapso de un minuto.(XA)

Al examinar la imagen del ECG tomada en un estado de reposo, se observa que la cantidad de intervalos RR dentro del período de tiempo analizado es inferior en comparación con el número observado después de realizar actividad física. Esto es coherente con la respuesta fisiológica del cuerpo durante la actividad física, en los cuales se incrementa la frecuencia cardíaca para satisfacer la elevada demanda de oxígeno y energía requerida por los músculos.
  
#### Sujeto 2 (Alvaro Cigarán)

<div align="center">

| En reposo |Luego de actividad física |
|----------|----------|
| <img src="https://github.com/NadAbiO/IntroSeniales/blob/adf04d42ebb891f3f3b926e116f092bfe72e73dd/ISB/Laboratorios/Lab4_ECG/Se%C3%B1ales_ECG/Alvaro_reposo.png" alt="Reposo" width="800"/> | <img src="https://github.com/NadAbiO/IntroSeniales/blob/adf04d42ebb891f3f3b926e116f092bfe72e73dd/ISB/Laboratorios/Lab4_ECG/Se%C3%B1ales_ECG/Alvaro_ejercicio.png" alt="Act física" width="800"/> |

<div align="left">

En los electrocardiogramas obtenidos se observa una cantidad considerable de ruido. Sospechamos que las causas podrían ser interferencias electromagnéticas o posibles fallos en los electrodos empleados. Se necesita  realizar una investigación más profunda para determinar con precisión la fuente del problema. En general, el ruido compromete la claridad de una señal ECG, lo que obstaculiza su correcta interpretación.

### **Señal del Promsim4 (dispositivo de metrología que genera una señal patrón)** <a name="id10"></a>

Adicionalmente se uso el dispositivo Promsim4 para generar señales que simulaban las etapas de un paro cardiaco, estas fueron leidas por el Bitalino y mostradas como referencia
<p align="center">
  <img width="460" height="300" src="https://github.com/NadAbiO/IntroSeniales/blob/main/Anexos/Laboratorios/LabECG/mecg.jpg">
</p> 
<em><p align="center> Dispositivo de metrologia: Promsim4 </p></em>

<div align="center">

|                 **Simulación**                 | **Toma** |
|:------------------------------------------:|:---------:|
|**Simulación etapa 2** | <video src="https://github.com/NadAbiO/IntroSeniales/assets/89696355/781acdce-e37e-46b7-8329-2d68bbd1109d" width="300" height="300">
|**Simulación etapa 3** | <video src="https://github.com/NadAbiO/IntroSeniales/assets/89696355/1c40b38d-92b5-4957-87d6-8a93d2566241" width="300" height="300">
|**Simulación etapa 4** | <video src="https://github.com/NadAbiO/IntroSeniales/assets/89696355/9cc65281-9d91-4709-a5df-5906f4033834" width="300" height="300"> 
|**Simulación etapa 5** | <video src="https://github.com/NadAbiO/IntroSeniales/assets/89696355/36ea7989-d1b4-41e2-8d4f-1f8fc71f8317" width="300" height="300">

<div align="left">

* Etapa 2: Actividad electrica sin pulso
  
  La Actividad Eléctrica sin Pulso (AESP) representa el 20% de los casos de paro cardíaco y es el ritmo más común en paros cardiorrespiratorios observados en pacientes hospitalizados.(XB)
* __Etapa 3:__  Taquicardia ventricular
  
* __Etapa 4:__  Fibración ventricular
* __Etapa 5:__  Asistolia
## **Discusión** <a name="id11"></a>

La electrocardiografia es una herramienta eficiente y usualmente usada para evaluacion cardivascular. Es una herramienta que ayuda a observar el potencial electrico del corazón y poder diagnosticar, si fuera el caso, cualquier anomalía  en el corazón.
La contacción muscular rítmica de debe a la despolarización y repolarización de las células del miocardio los cuales son originados por movimiento de iones cargados al interior o exterior de la membrana célular (Na+, Ca 2+, K+).
Dicho movimiento de iones cargados genera corriente electroca cuantificable por un electrocardiografo.
El marcapasos natural es el nódulo sinoauricular que inicia la despolarización auricular. El impulso se propaga hasta el nódulo auriculoventricular para posteriormente viajar por el has de His y finalmente llegar a las fibras de Purkinje.

<p align="center">
  <img height="300" src="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1122339/bin/ecg01.f1.jpg">
</p> 
<em><p align="center">Figura 3. El sistema de conducción His-Purkinje [4] </p></em>


***
## **Referencias** <a name="id12"></a>
[1] Rafie, Nikita, Anthony H. Kashou, and Peter A. Noseworthy. "ECG Interpretation: Clinical Relevance, Challenges, and Advances." Hearts 2.4 (2021): 505-513. https://www.mdpi.com/2673-3846/2/4/39

[2] Farré Antonio López and C. M. Miguel, Libro de la Salud cardiovascular del hospital clínico san carlos Y la fundación BBVA. Barcelona: Fundación BBVA, 2009.

[3] M. Proença, & K. Mrotzeck. (2021, 15 de febrero). EXPERIMENTAL GUIDES TO MEET & LEARN YOUR BIOSIGNALS. Support PLUX Biosignals official – Official PLUX support and biosignals knowledge base. https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf

[4] S. Meek, “ABC of clinical electrocardiography: Introduction. I---Leads, rate, rhythm, and cardiac axis”, BMJ, vol. 324, núm. 7334, pp. 415–418, 2002.


