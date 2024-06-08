# LABORATORIO 9 - PROCESAMIENTO DE ECG

### TABLA DE CONTENIDO

1. [Objetivos](#id1)
2. [Introducción](#id2)
3. [Metodología](#id3)
   - [Adquisición de la señal](#id4)
   - [Filtrado](#id5)
   - [Cálculo del HRV](#id6)
4. [Resultados](#id7)
5. [Discusión](#id8)
6. [Archivos](#id9)
7. [Bibliografía](#id10)
---

## **Objetivos** <a name="id1"></a>

- Utilizar el filtro más apropiado para procesar la señal ECG.
- Obtener características particulares de la señal ECG.
- Estudiar la variación en la frecuencia cardíaca (HRV).
- Contrastar los resultados obtenidos con aquellos de métodos convencionales.

---

## **Introducción** <a name="id2"></a>

El electrocardiograma (ECG) es esencial para evaluar la función cardíaca, registrando la actividad eléctrica del corazón. Las señales de ECG, generadas a través de un transductor que convierte las vibraciones mecánicas del corazón en señales eléctricas, son propensas a diversos tipos de interferencias y ruidos, como los artefactos de movimiento, la interferencia de la línea de alimentación y el ruido muscular. Para interpretar estas señales con precisión, se aplican técnicas de filtrado como el filtrado con la transformada wavelet, que es especialmente efectiva por su capacidad de resolución múltiple [2].

La onda del ECG se compone de las ondas P, Q, R, S y T, cada una reflejando diferentes aspectos de la actividad eléctrica del corazón, lo que facilita el diagnóstico de diversas condiciones cardíacas . Particularmente, la detección precisa del pico R es crucial, ya que sirve como referencia para medir la frecuencia cardíaca y calcular la variabilidad de la frecuencia cardíaca (HRV) [2]. El intervalo R-R, que es la duración entre dos picos R consecutivos, indica la frecuencia cardíaca, con un rango normal entre 60 y 100 latidos por minuto. Valores fuera de este rango se conocen como bradicardia (menos de 60 latidos por minuto) o taquicardia (más de 100 latidos por minuto) [2,4].

<p align="center">
  <img src="https://simplifaster.com/wp-content/uploads/2016/12/R-R-Interval-for-Heart-Rate-Variability.jpg"  width="300" height="200"> </p>
<em><p align="center">Figura 1. HRV [6]</p></em> 

---


## **Metodología** <a name="id3"></a>


- ### **Filtrado** <a name="id5"></a>
Para el filtrado de la señal se usó un filtro IRR pasabajas simple, ya que al evaluar el espectrograma de la señal se obtuvo que las frecuencias con mayor magnitud eran las que se encontraban por debajo de 5hz.
Para la detección de picos R se usó el código elaborado en la referencia [1] en la cuál usan una una seno para correlacionarla con la señal ECG (previamente filtrada) en la cual se evidencia que los piceos de interés tiene una correlación alta con la onda seno. A partir de dicho filtro se puede hallar fácilmente los picos R y determinar la frecuencia con la que se encuentran.
Como se muestra en el código, se encontraron parámetros de dichos picos.

- ### **Cálculo del HRV** <a name="id6"></a>
La variabilidad de la frecuencia cardíaca (HRV, por sus siglas en inglés) es una herramienta no invasiva utilizada para evaluar la salud cardíaca y el equilibrio cardiovascular [7]. Para analizar la HRV, se emplean métodos lineales que calculan diversos índices en el dominio del tiempo y el dominio de la frecuencia [7]. Uno de los recursos disponibles para este propósito es el "hrv module", una herramienta de Python que es sencilla, de código abierto, y que incluye técnicas comunes para filtrar, eliminar tendencias y extraer información [7]. Otra opción para la investigación y desarrollo de aplicaciones en HRV es la caja de herramientas de código abierto pyHRV [8].

En nuestro caso, analizamos la HRV utilizando la biblioteca pyHRV y codificamos en Google Colab. Seguimos la guía de codificación proporcionada en la documentación de pyHRV [9]. Esta documentación menciona el uso de los intervalos normal a normal (NNI), que miden los intervalos entre los picos R detectados en un ECG [8]. Basándonos en la literatura, seleccionamos los siguientes parámetros según el dominio [7] [8]:

### **Dominio del tiempo:**

**Desviación típica de intervalos sucesivos de NN (SDNN)**
La SDNN mide la variabilidad total de la HRV, generada por las ramas parasimpática y simpática del sistema nervioso autónomo [7]. La desviación estándar (DE) es una métrica común para cuantificar la dispersión en un conjunto de datos. En este contexto, la SDNN mide la variabilidad en las duraciones de los NNI alrededor de su valor medio [8].

**Media cuadrática de las diferencias sucesivas (RMSSD)**
La RMSSD es la raíz cuadrada de la media de las diferencias al cuadrado entre intervalos NN sucesivos. Esta métrica mide las variaciones a corto plazo en los intervalos NN y proporciona información sobre la actividad del sistema nervioso parasimpático [8].

**Desviación típica de las diferencias sucesivas (SDSD)**
La SDSD es la desviación estándar de las diferencias entre intervalos NN consecutivos, similar al parámetro RMSSD. La principal diferencia entre SDSD y RMSSD radica en su dependencia de las características estacionarias de la serie de intervalos NN, lo que significa que cada una puede ser más útil en diferentes contextos de análisis de la variabilidad de la frecuencia cardíaca [8].

### **Dominio de la frecuencia:**

El análisis en el dominio de la frecuencia mide cómo cada componente de frecuencia contribuye a la fluctuación total de la frecuencia cardíaca. Los componentes principales son VLF (frecuencia muy baja; < 0,04 Hz), LF (frecuencia baja; 0,04-0,15 Hz) y HF (frecuencia alta; 0,15-0,40 Hz) [7].
El análisis en el dominio de la frecuencia implica calcular el contenido de energía espectral de cada componente de frecuencia mediante la estimación de la densidad espectral de potencia (PSD) [7]. El periodograma de Welch es un método no paramétrico basado en la transformada de Fourier que se obtiene promediando varias estimaciones de la PSD en diferentes segmentos de la señal [7].

### **Parámetros no lineales:**

Los parámetros no lineales buscan resaltar las características no lineales e imprevisibles de las series de intervalos NNI. El gráfico de Poincaré es una herramienta gráfica en la que un intervalo NNIj se traza frente a su sucesor NNIj+1, proporcionando una representación visual del HRV en un conjunto de datos de NNI. Este gráfico permite realizar una evaluación rápida del estado de salud de un sujeto y visualizar HRV global [8]. En el gráfico de Poincaré, el valor de SD1 refleja las fluctuaciones a corto plazo de la frecuencia cardíaca, mientras que SD2 refleja tanto las fluctuaciones a corto como a largo plazo [7].



---



## **Resultados** <a name="id7"></a>


| ECG de la muestra | ECG filtrado|
|-----------|-----------|
| ![ecg_muestra](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab9_ProcesamientoECG/img/ecg_muestra.png?raw=true)  | ![ecg_filtrado](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab9_ProcesamientoECG/img/ecg_filtrado.png?raw=true)   | 

| Sine filter | ECG filtrado (sine filter) |
|-----------|-----------|
| ![sine_fil](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab9_ProcesamientoECG/img/sine_filter.png?raw=true)    | ![ecg_sine_fil](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab9_ProcesamientoECG/img/ecg_sine_filter.png?raw=true)     |

#### Picos R de la muestra de ECG
![r_peaks](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab9_ProcesamientoECG/img/R_peaks.png?raw=true)

### Análisis del HRV

#### Dominio del tiempo
![tiempo](https://github.com/NadAbiO/IntroSeniales/blob/main/Anexos/Laboratorios/tiempo.png)

#### Dominio de la frecuencia
<img src="https://github.com/NadAbiO/IntroSeniales/blob/main/Anexos/Laboratorios/frecuencia.png" width="700" height="500">

#### Parámetros no lineales
<img src="https://github.com/NadAbiO/IntroSeniales/blob/main/Anexos/Laboratorios/poincare.png" width="500" height="500">


---

## **Discusión** <a name="id8"></a>

sdfs

---

## **Archivos** <a name="id9"></a>

[Código cálculo HRV](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab9_ProcesamientoECG/HRV_calculations.ipynb)

Se adjunta el archivo de la referencia [7] en PDF:
[PDF](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab9_ProcesamientoECG/PDF_bibliografia/Pythonic_package_for_HRV.pdf)

Se adjunta el archivo de la referencia [8] en PDF:
[PDF](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab9_ProcesamientoECG/PDF_bibliografia/Development_of_Open_Source_Python_Toolbox.pdf)

---

## **Bibliografía** <a name="id10"></a>
[1]	B. Kulas, HRV_ECG_analysis.ipynb at master · kulasbart/ECG-processing_HRV.

[2] Chandra S, Sharma A, Singh GK. Feature extraction of ECG signal. J Med Eng Amp Technol [Internet]. Disponible en: https://doi.org/10.1080/03091902.2018.1492039

[3] Malgina O, Milenkovic J, Plesnik E, Zajc M, Tasic JF. ECG signal feature extraction and classification based on R peaks detection in the phase space. En: 2011 IEEE GCC Conference and Exhibition (GCC) [Internet]; 19-22 de febrero de 2011; Dubai, United Arab Emirates. Disponible en: https://doi.org/10.1109/ieeegcc.2011.5752545

[4] Gholam-Hosseini H, Nazeran H. Detection and extraction of the ECG signal parameters. En: 20th Annual International Conference of the IEEE Engineering in Medicine and Biology Society. Vol.20 Biomedical Engineering Towards the Year 2000 and Beyond [Internet]; Hong Kong, China. Disponible en: https://doi.org/10.1109/iembs.1998.745846

[5] Akhter N, Gite H, Tharewal S, Kale KV. Computer based RR-Interval detection system with ectopy correction in HRV data. En: 2015 International Conference on Advances in Computing, Communications and Informatics (ICACCI) [Internet]; 10-13 de agosto de 2015; Kochi, India. Disponible en: https://doi.org/10.1109/icacci.2015.7275844

[6] “Heart Rate Variability Training - SimpliFaster”. SimpliFaster. [En línea]. Disponible: https://simplifaster.com/articles/heart-rate-variability-training/

[7]  R. Bartels and T. Peçanha, “HRV: a Pythonic package for Heart Rate Variability Analysis,” Journal of Open Source Software, vol. 5, no. 51, p. 1867, Jul. 2020, doi: https://doi.org/10.21105/joss.01867.

[8]  P. M. C. Gomes, "Development of an Open-Source Python Toolbox for Heart Rate Variability (HRV)", Tesis de Maestría, Departamento de Ingeniería Biomédica, Univ. of Appl. Sci. Hamburg, Hamburg, Alemania, 2018.

[9] “Highlights — pyHRV - OpenSource Python Toolbox for Heart Rate Variability 0.4 documentation,” pyhrv.readthedocs.io. https://pyhrv.readthedocs.io/en/latest/index.html (accessed Jun. 08, 2024).




