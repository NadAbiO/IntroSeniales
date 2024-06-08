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

gvdsg

---

## **Introducción** <a name="id2"></a>
fdbdf

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
[1]	B. Kulas, HRV_ECG_analysis.ipynb at master · kulasbart/ECG-processing_HRV. .

