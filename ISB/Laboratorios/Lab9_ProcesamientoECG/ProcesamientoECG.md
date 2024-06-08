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

- ### **Adquisición de la señal** <a name="id4"></a>
- ### **Filtrado** <a name="id5"></a>
Para el filtrado de la señal se usó un filtro IRR pasabajas simple, ya que al evaluar el espectrograma de la señal se obtuvo que las frecuencias con mayor magnitud eran las que se encontraban por debajo de 5hz.
Para la detección de picos R se usó el código elaborado en la referencia [1] en la cuál usan una una seno para correlacionarla con la señal ECG (previamente filtrada) en la cual se evidencia que los piceos de interés tiene una correlación alta con la onda seno. A partir de dicho filtro se puede hallar fácilmente los picos R y determinar la frecuencia con la que se encuentran.
Como se muestra en el código, se encontraron parámetros de dichos picos.

- ### **Cálculo del HRV** <a name="id6"></a>

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


---

## **Discusión** <a name="id8"></a>

sdfs

---

## **Archivos** <a name="id9"></a>

dsfcs

---

## **Bibliografía** <a name="id10"></a>
[1]	B. Kulas, HRV_ECG_analysis.ipynb at master · kulasbart/ECG-processing_HRV.

[2] Chandra S, Sharma A, Singh GK. Feature extraction of ECG signal. J Med Eng Amp Technol [Internet]. Disponible en: https://doi.org/10.1080/03091902.2018.1492039

[3] Malgina O, Milenkovic J, Plesnik E, Zajc M, Tasic JF. ECG signal feature extraction and classification based on R peaks detection in the phase space. En: 2011 IEEE GCC Conference and Exhibition (GCC) [Internet]; 19-22 de febrero de 2011; Dubai, United Arab Emirates. Disponible en: https://doi.org/10.1109/ieeegcc.2011.5752545

[4] Gholam-Hosseini H, Nazeran H. Detection and extraction of the ECG signal parameters. En: 20th Annual International Conference of the IEEE Engineering in Medicine and Biology Society. Vol.20 Biomedical Engineering Towards the Year 2000 and Beyond [Internet]; Hong Kong, China. Disponible en: https://doi.org/10.1109/iembs.1998.745846

[5] Akhter N, Gite H, Tharewal S, Kale KV. Computer based RR-Interval detection system with ectopy correction in HRV data. En: 2015 International Conference on Advances in Computing, Communications and Informatics (ICACCI) [Internet]; 10-13 de agosto de 2015; Kochi, India. Disponible en: https://doi.org/10.1109/icacci.2015.7275844

[6] “Heart Rate Variability Training - SimpliFaster”. SimpliFaster. [En línea]. Disponible: https://simplifaster.com/articles/heart-rate-variability-training/



