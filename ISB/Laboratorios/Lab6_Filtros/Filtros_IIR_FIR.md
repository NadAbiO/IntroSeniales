# Laboratorio 7: DISEÑO DE FILTROS IIR y FIR

## Tabla de contenidos:
* [Objetivos](#objetivos)
* [Materiales y equipos](#materiales-y-equipos)
* [Entregable](#entregable)
  * [Introducción](#introducción)
  * [Metodología](#metodología)
  * [Gráficos de resultados](#gráficos-de-resultados)
  * [Archivos](#archivos)
* [Discusión](#discusión)
* [Bibliografía](#bibliografía)

## Objetivos:
  * Diseños de filtros IIR y FIR.
  * Filtrar las señales EMG para eliminar ruido y artefactos, y aislar la actividad muscular efectiva.
  * Filtrar señales EEG para reducir el ruido y extraer características de interés como ondas cerebrales específicas.
  * Filtrar señales ECG para eliminar el ruido.
---
## Materiales y equipos:
1. Adquisición de señales en laboratoiros anteriores:

|Cantidad|Material o equipo|
|:-----:|:-----:|
|1|Kit BITalino (R)EVOLUTION|
|1|OpenSignals (R)EVOLUTION |
|3|Electrodos|
|1|Laptop|

2. Procesamiento de señales:

|Cantidad|Material o equipo|Uso|
|:-----------:|:-----:|:-------:|
|1|Laptop|Visualización y procesamiento de las señales con lenguaje de programación|
---
## Entregable:
<p align="justify">En laboratorios pasados, obtuvimos las señales ECG, EMG y EEG a las que se le aplicarán los filtros diseñados.

### Introducción
#### ¿ Qué es un filtro?
Un filtro es un dispositivo, ya sea implementado en hardware o software, que se aplica a un conjunto de datos ruidosos con el objetivo de extraer información relevante sobre una cantidad específica. En el contexto de señales, el filtrado es un proceso mediante el cual se altera el contenido espectral de una señal para resaltar o eliminar ciertas frecuencias de interés. [1]

Existen distintos tipos de filtros, se pueden clasificar en si filtros analógicos o digitales, según su aplicación. En el caso de los filtros analógicos, podemos diferenciar entre dos categorías:

- Filtros Analógicos Pasivos:
  Estos filtros están construidos exclusivamente con componentes pasivos, como resistencias, capacitores e inductores. Un
  ejemplo común es el filtro en escalera RLC.
  No incorporan elementos activos, como amplificadores u operacionales.
- Filtros Analógicos Activos:
  Además de los componentes pasivos, estos filtros incluyen elementos activos, como amplificadores operacionales (OPAMPS) o
  transistores.
  Los OPAMPS y transistores permiten una mayor flexibilidad en el diseño y ajuste de las características del filtro.[1]

Un filtro digital es un sistema que, al ser lineal e invariante en el tiempo (LTI), altera el espectro de frecuencia de una señal de entrada X(w) de acuerdo con su respuesta en frecuencia H(w). Como resultado, se genera una señal de salida con un espectro Y(w) = H(w) * X(w).[1]

Los sistemas LTI se dividen en dos categorías principales[1]:
|FIR|IIR|
|:-----------:|:-----:|
|Este filtro tiene una respuesta finita al impulso y que se caracterizan por ser sistemas no recursivos. |Un filtro IIR es aquel que tiene una respuesta infinita al impulso y que se caracterizan por tener una retroalimentación de la señal de salida. |       
---
## Metodología
#### EEG
Para el filtrado de señales provenientes del electroencefalograma realizado tras distintas actividades (resposo, parpadeo, razonamiento matemático), se tomó como base los filtros vistos en clase.
Para la definición de las frecuencias de corte, primero se obtuvo la gráfica de las magnitudes vs frecuencia de cada señal; asumiendo que la frecuencia con mayor mayor magnitud es la de interés, se filtraron las demás frecuencias.

#### EMG
Para el filtrado de las seales electromiográficas, se utilizaron las señales adquiridas en laboratorios anteriores.
Además, se diseñaron filtro IIR y FIR de acuerdo a lo visto en clase.

#### ECG
Para el filtrado de las señales de electrocardiograma, se utilizaron las señales obtenidas en laboratorios pasados, las cuales fueron tomadas en tres estados distintos (reposo, respiración y post ejercicio). Se diseñaron filtros IIR y FIR, usando de base las características de diseño sugeridas en clase, utilizamos la bibliografía para la selección del tipo de ventana para los filtros FIR y también para la selección del tipo de filtro IIR.

---
## Gráficos de resultados
#### EEG
| | 1er Reposo | Pestañeo | 2do Reposo | Resolución de ejercicios |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| FIR | ![fir1](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab6_Filtros/EEG/img/ej1_FIR.png?raw=true) | ![fir2](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab6_Filtros/EEG/img/ej2_FIR.png?raw=true) | ![fir3](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab6_Filtros/EEG/img/ej3_FIR.png?raw=true) | ![fir4](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab6_Filtros/EEG/img/ej4_FIR.png?raw=true) | 
| IIR | ![iir1](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab6_Filtros/EEG/img/ejercicio1_IIR.png?raw=true) | ![iir2](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab6_Filtros/EEG/img/ejercicio2_IIR.png?raw=true) | ![iir3](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab6_Filtros/EEG/img/ejercicio3_IIR.png?raw=true) | ![iir4](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab6_Filtros/EEG/img/ejercicio4_IIR.png?raw=true) | 

#### EMG

| | SEÑAL| 
| ------------ | ------------ | 
|Señal cruda| <img width="927" alt="sin filtro" src="https://github.com/NadAbiO/IntroSeniales/assets/89549012/8cc9fd7e-6423-45ca-b339-e12476e124c8"> | 
| FIR|  <img width="920" alt="FILTRO_FIR" src="https://github.com/NadAbiO/IntroSeniales/assets/89549012/1ec61161-6f2f-4a59-b00c-5deab0c3bbce"> |  
| IIR |  <img width="932" alt="filtro_IIR" src="https://github.com/NadAbiO/IntroSeniales/assets/89549012/8ba5275c-4fb5-4a08-9cce-ba441eef4b69"> | 

#### ECG
Para una mejor visualización de las gráficas, entrar al archivo "ECG_filter.ipynb" que se encuentra en la sección de archivos.

|| Campo | Señal cruda | Filtro IIR | Filtro FIR Ventana Hamming|Filtro FIR Ventana Rectangular |
| ------------ | ------------ | ------------ | ------------ | ------------ |------------ |
|| Reposo |<img width="927" alt="sin filtro" src="https://github.com/NadAbiO/IntroSeniales/blob/main/Anexos/Laboratorios/ecg_reposo.png"> | <img width="927" alt="sin filtro" src="https://github.com/NadAbiO/IntroSeniales/blob/main/Anexos/Laboratorios/ecg_IIR_II.png">|<img width="927" alt="sin filtro" src="https://github.com/NadAbiO/IntroSeniales/blob/main/Anexos/Laboratorios/ecg_FIR_hamming_II.png">|<img width="927" alt="sin filtro" src="https://github.com/NadAbiO/IntroSeniales/blob/main/Anexos/Laboratorios/ecg_FIR_rectangular_II.png">|
| |Respiración |<img width="927" alt="sin filtro" src="https://github.com/NadAbiO/IntroSeniales/blob/main/Anexos/Laboratorios/ecg_aguantando_respiracion.png"> | <img width="927" alt="sin filtro" src="https://github.com/NadAbiO/IntroSeniales/blob/main/Anexos/Laboratorios/ecg_respiracion_IIR.png">|<img width="927" alt="sin filtro" src="https://github.com/NadAbiO/IntroSeniales/blob/main/Anexos/Laboratorios/ecg_respiracion_hamming.png">|<img width="927" alt="sin filtro" src="https://github.com/NadAbiO/IntroSeniales/blob/main/Anexos/Laboratorios/ecg_respiracion_rectangular.png">|
| |Post Ejercicio |<img width="927" alt="sin filtro" src="https://github.com/NadAbiO/IntroSeniales/blob/main/Anexos/Laboratorios/ecg_post_ejercicio.png"> | <img width="927" alt="sin filtro" src="https://github.com/NadAbiO/IntroSeniales/blob/main/Anexos/Laboratorios/ecg_post_iir.png">|<img width="927" alt="sin filtro" src="https://github.com/NadAbiO/IntroSeniales/blob/main/Anexos/Laboratorios/ecg_post_hamming.png">|<img width="927" alt="sin filtro" src="https://github.com/NadAbiO/IntroSeniales/blob/main/Anexos/Laboratorios/ecg_post_rectangular.png">|


---
## Archivos
#### EEG
|FIR|IIR|
|:-----------:|:-----:|
|[Abrir filtro FIR (Google Collab)](https://colab.research.google.com/drive/10l-gRCAlV1tx8irrjU6R-cUOdud9RAXe?usp=sharing) | [Abrir filtro IIR (Google Collab)](https://colab.research.google.com/drive/1DYxeyBe8zKtgBCG9q7QG4aXB8l4qfcVC?usp=sharing)|

#### EMG
- [Ploteo de la señal (.py)](https://github.com/NadAbiO/IntroSeniales/blob/e98997f596b04235cb52582e697b4858334fdf60/ISB/Laboratorios/Lab6_Filtros/EMG_filtered.py)

#### ECG
- [Ploteo de la señales y aplicación de los filtros](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab6_Filtros/ECG_filter.ipynb)
  
---
## Discusión
#### EEG
Como se observa en las imágenes de los resultados, al aplicar filtros IIR, la representación de la señal filtrada en el dominio del tiempo es mejor que la señal filtrada con filtro FIR; sin embargo, debido al escaso procesamiento de laseñal, dichas representaciones pueden ser información no útil o distorcionada.
Como se sabe, el filtro IIR no tiene una fase lineal, por lo cual puede desfasar la señal y alterar los resultados; además, para el filtrado  de señales en este laboratorio no se tomó en cuenta todos los factores que pueden afectar a la obtención de la señal, ni se evaluó a modo detallado los filtros usados.
Para un correcto procesamiento de señales de EEG se tiene que tomar en cuenta el rango de frecuencias de ondas a evaluar (alfa, betha, etc), los ruidos provenientes de movimiento muscular o de la impedancia de los electrodos, el ruido de la corriente eléctrica, entre otro tipo de distorcionadores de señal.
Para un correcto procesamiento se requieren distintas etapas y conocimiento acerca de las limitantes del mismo electroencefalógrafo.

![procedimiento](https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRhx6_dI5JR4Cnmw2S2_I317l-QK8k12f2rJhBZSNJtkyqAKJCM)

#### EMG
En la investigación, realizada por **Roger G. T. Mello, Liliam F. Oliveira y Jurandir Nadal**, presentan un filtro digital (Butterworth) diseñado específicamente para delimitar la banda de frecuencias de los electromiogramas de superficie (EMG) y eliminar el ruido de red y sus armónicos. El enfoque se centra en el análisis de la señal durante la actividad muscular reducida [3].

**Resultados Clave:**
- El filtro demostró una eficaz eliminación de los componentes de ruido de red, con atenuaciones superiores al 96,6%.
- La atenuación selectiva a frecuencias inferiores a 15 Hz y a 60 Hz causó solo una pequeña reducción en la potencia total, preservando así el espectro original.
- Dada su eficacia, el filtro resulta adecuado para la aplicación propuesta.
  
Además, la correcta supresión de la fluctuación de la línea de base (BLF) es un aspecto crucial al registrar señales EMG, ya que su omisión puede afectar negativamente la calidad de la señal y distorsionar tanto el análisis cualitativo como el cuantitativo. Para ello se diseñó un filtro FIR que logre atenuar el BLF.[4]

#### ECG
En la investigación llevada a cabo por Priyanka y Gurjit Kaur, se exploró la eliminación de ruido en señales de ECG mediante el uso de diversas técnicas de ventanas en filtros FIR. Se enfocaron en reducir varios tipos de ruido, como la interferencia de línea eléctrica, ruido muscular y ruido EMG. Utilizaron diferentes métodos de ventanas, tales como Kaiser, Rectangular, Hamming, Hanning y Welch, y evaluaron los resultados con base en parámetros de rendimiento como el Mean Square Error (MSE), la Signal to Noise Ratio (SNR), Positive Peak y Total Harmonic Distortion (THD). Un filtro bien diseñado debería mejorar el SNR, reducir el MSE y minimizar el THD. El estudio concluyó que la ventana Kaiser ofrece el mejor rendimiento en la eliminación de ruido, seguido por la ventana rectangular. La ventana Hamming también mostró una efectividad notable, particularmente en la eliminación de ruido muscular en las señales de ECG, aunque su rendimiento generalmente no alcanza el de las ventanas Kaiser o Rectangular, pero aun así presenta resultados satisfactorios [5]. 

Para el diseño de nuestro filtro, optamos por utilizar un filtro FIR empleando ventanas Rectangular y Hamming. Según la literatura revisada, estas ventanas son efectivas para atenuar el ruido en señales de ECG. Aunque la ventana Kaiser fue identificada como la mejor opción para este propósito, no fue considerada porque no estaba dentro de las opciones disponibles. Al analizar los gráficos resultantes de nuestro proceso de filtrado, es evidente que el filtro FIR con ventana rectangular reduce el ruido de manera más significativa en comparación con el uso de la ventana Hamming.

Con respecto al diseño del filtro IIR, se encontró el estudio "Suppression of Noise in ECG Signal Using Low pass IIR Filters" realizado por Mohandas Choudhary y Ravindra Pratap Narwaria, se investiga la eliminación de ruido en señales ECG a través del uso de filtros IIR de paso bajo. Los autores evalúan y comparan la eficacia de tres tipos de filtros: Butterworth, Chebyshev Tipo I y Chebyshev Tipo II. Sus hallazgos indican que el filtro Butterworth de paso bajo sobresale en la reducción de ruido, en comparación con los filtros Chebyshev Tipo I y Tipo II [6]. Por ello, basado en la literatura revisada, se diseñó un filtro IIR Butterworth low pass para el filtrado de las señales ECG en los distintos estados. 

---
## Bibliografía 
[1] J. M. Marín de la Rosa. “FUNDAMENTOS TEÓRICOS”. Test Page for the HTTP Server on Red Hat Enterprise Linux. [En línea]. Disponible: https://biblus.us.es/bibing/proyectos/abreproy/11375/fichero/MEMORIA%2FFundamentos+teoricos.pdf

[2] A. de Cheveigné y I. Nelken, “Filters: When, why, and how (not) to use them”, Neuron, vol. 102, núm. 2, pp. 280–293, 2019. DOI: https://doi.org/10.1016/j.neuron.2019.02.039

[3] Mello, R. G. T., Oliveira, L. F., & Nadal, J. (2007). "Digital Butterworth filter for subtracting noise from low magnitude surface electromyogram". Computer Methods and Programs in Biomedicine, 87(1), 28–35. https://doi.org/10.1016/j.cmpb.2007.04.004.

[4] Rodríguez-Carreño, I., Malanda-Trigueros, A., Gila-Useros, L., Navallas-Irujo, J., & Rodríguez-Falces, J. (2006). Filter design for cancellation of baseline-fluctuation in needle EMG recordings. Computer Methods and Programs in Biomedicine, 81(1), 79–93. https://doi.org/10.1016/j.cmpb.2005.11.002. 

[5] “Noise Removal in ECG Signal using Windowing Technique and its Optimization,” Advances in Biotechnology & Microbiology, vol. 6, no. 1, Aug. 2017, doi: https://doi.org/10.19080/aibm.2017.06.555676.

[6] C. Mohandas, “Suppression of Noise in ECG Signal Using Low pass IIR Filters ,” International Journal of Electronics and Computer Science Engineering, vol. 1, no. 4, Available: https://citeseerx.ist.psu.edu/document?repid=rep1&amp;type=pdf&amp;doi=a361a547eedcc1f37ac007cc03ad7b93073aaf3a


