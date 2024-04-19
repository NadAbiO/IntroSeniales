# Laboratorio 3 - Adquisición señales EMG

## **Tabla de contenidos**
1. [Introducción](#id1)
2. [Objetivos](#id2)
3. [Metodología](#id3)\
     3.1 [Fotos de la conexión](#id4)\
     3.2 [Guía electromiográfica](#id5)
4. [Resultados](#id6)\
     4.1 [Video de la señal y Ploteo de la señal en OpenSignal](#id7)\
     4.2 [Ploteo de la señal en Python](#id8) <br>
     4.3 [Señal del Promsim4](#id13) <br>
6. [Discusión](#id9)
7. [Archivos](#id10)
8. [Referencias](#id11)
***
## **Introducción** <a name="id1"></a>
Las señales biomédicas como la electromiografía (EMG) y el electrocardiograma (ECG) son fundamentales para mejorar el diagnóstico médico y mejorar el tratamiento. El laboratorio tiene como objetivo avanzar en la comprensión y el control de estas señales biomédicas utilizando tecnologías avanzadas que permitan una captura y análisis eficientes. Este informe describe el proceso de adquisición de señales ECG utilizando el sistema BiTalino, un dispositivo versátil y fácil de usar diseñado para aplicaciones biomédicas.

### La señal de ECG
La señal del electrocardiograma (ECG) resulta crucial ya que ofrece datos significativos sobre el rendimiento del corazón del paciente. Este examen, no intrusivo, registra la actividad eléctrica cardíaca mediante electrodos adosados a la piel. Su utiliza habitualmente en la detección y diagnóstico de diversas afecciones cardíacas, incluyendo arritmias, infarto de miocardio, hipertrofia ventricular, y otros problemas que influyen en la función cardiaca [1].

En un electrocardiograma (ECG) normal, los latidos del corazón se reflejan a través de variaciones en la línea de base, representadas por ángulos, segmentos, ondas e intervalos. Estos elementos forman una imagen característica que se repite de manera regular a lo largo de todo el registro. Un ECG típico muestra una sucesión de deflexiones, conocidas como ondas, que se alternan con la línea basal. Al leer el ECG de izquierda a derecha, se identifican la onda P, el segmento P-R, el complejo QRS, el intervalo QT, el segmento ST y, finalmente, la onda T. Esta disposición puede apreciarse en la imagen adjunta [2].

<p align="center">
  <img width="460" height="300" src="https://github.com/NadAbiO/IntroSeniales/blob/e3dd6f5f0a621e8a486cf26a2decd3816548c45b/Anexos/Laboratorios/ECG.png">

</p> 
<em><p align="center">Figura 1. Ondas e Intervalos</p></em>


***
## **Objetivos** <a name="id2"></a>
- Adquirir señales biomédicas de ECG.
- Hacer una correcta configuración de BiTalino.
- Extraer la información de las señales ECG del software OpenSignals (r)evolution
- Graficar la información usando python

***
## **Metodología** <a name="id3"></a>
### **Fotos de la conexión** <a name="id4"></a>
Se utilizó la conexión ECG en la placa Bitalino utilizando el sensor ECG de 3 electrodos como se muestra a continuación.

<p align="center">
  <img width="460" height="300" src="IntroSeniales\Anexos\triangular.jpeg">

</p> 
<em><p align="center">Conexión en BiTalino</p></em>

1. Conexión BITalino por medio de Bluetooth.
2. Se colocaron dos electrodos, uno positivo y otro negativo, en el brazo izquierdo y brazo derecho respectivamente.
3. Luego, se colocó un electrodo de referencia en la cresta iliaca (se tomaron los puntos de referencia de la guía de BITalino).
4. Se capturaron señales en distintas condiciones de actividad corporal.
7. Los usuarios realizaron ejercicio físico y de respiración.
8. Se detuvo la grabación y se guardaron los datos obtenidos.
9. Con el programa python se graficó las imágenes en las cuales se pueden observar diferencias significativas.

### **Guía electrocardiografía** <a name="id5"></a>

Como referencia para la colocación de los electrodos y buenas prácticas durante la toma de datos utilizamos la siguiente guía [1]:

- BITalino (r)evolution Lab Guide
  https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide2_ECG.pdf

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

### **Señal del Promsim4 (dispositivo de metrología que genera una señal patrón)** <a name="id13"></a>

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

</div>


***
## **Discusión** <a name="id9"></a>

La electrocardiografia es una herramienta eficiente y usualmente usada para evaluacion cardivascular. Es una herramienta que ayuda a observar el potencial electrico del corazón y poder diagnosticar, si fuera el caso, cualquier anomalía  en el corazón.
La contacción muscular rítmica de debe a la despolarización y repolarización de las células del miocardio los cuales son originados por movimiento de iones cargados al interior o exterior de la membrana célular (Na+, Ca 2+, K+).
Dicho movimiento de iones cargados genera corriente electroca cuantificable por un electrocardiografo.
El marcapasos natural es el nódulo sinoauricular que inicia la despolarización auricular. El impulso se propaga hasta el nódulo auriculoventricular para posteriormente viajar por el has de His y finalmente llegar a las fibras de Purkinje.

<p align="center">
  <img height="300" src="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1122339/bin/ecg01.f1.jpg">
</p> 
<em><p align="center">El sistema de conducción His-Purkinje [a] </p></em>





***
## **Archivos** <a name="id10"></a>

- [Documentos (.txt)](https://github.com/NadAbiO/IntroSeniales/tree/d3b35c0b271c22b37876451e3511eb8a77f34da4/ISB/Laboratorios/Laboratorio3/Se%C3%B1ales_EMG)

  **Código para el ploteo de la señal:**
- [Ploteo de la señal (.py)](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Laboratorio4/adq_ECG.py)


***
## **Referencias** <a name="id11"></a>
[1] Rafie, Nikita, Anthony H. Kashou, and Peter A. Noseworthy. "ECG Interpretation: Clinical Relevance, Challenges, and Advances." Hearts 2.4 (2021): 505-513. https://www.mdpi.com/2673-3846/2/4/39

[2] Farré Antonio López and C. M. Miguel, Libro de la Salud cardiovascular del hospital clínico san carlos Y la fundación BBVA. Barcelona: Fundación BBVA, 2009.

[a] S. Meek, “ABC of clinical electrocardiography: Introduction. I---Leads, rate, rhythm, and cardiac axis”, BMJ, vol. 324, núm. 7334, pp. 415–418, 2002.

[] BITalino (r)evolution Lab Guide
  https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide1_EMG.pdf 
  
[] Medicosis Perfectionalis. Electromyography (EMG) Basics, Muscle Hypertrophy, Denervation, Rigor Mortis | Muscle Physiology. (20 de septiembre de 2021). [Video en línea]. Disponible: https://www.youtube.com/watch?v=sK065oV8_4w
