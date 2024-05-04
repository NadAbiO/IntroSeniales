# Laboratorio 7: DISEÑO DE FILTROS IIR y FIR

## Tabla de contenidos:
* [Objetivos](#objetivos)
* [Materiales y equipos](#materiales-y-equipos)
* [Entregable](#entregable)
  * [Introducción](#introducción)
  * [Metodología](#metodología)
  * [Gráficos de resultados](#gráficos-de-resultados)
  * [Resumen y explicación final](#resumen-y-explicación-final)
  * [Archivos](#archivos)
* [Conclusiones](#conclusiones)
* [Bibliografía](#bibliografía)

## Objetivos:
  * Diseños de filtros IIR y FIR.
  * Filtrar las señales EMG para eliminar ruido y artefactos, y aislar la actividad muscular efectiva.
  * Filtrar señales EEG para reducir el ruido y extraer características de interés como ondas cerebrales específicas.
  * Filtrar señales ECG para eliminar el ruido.

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

  - #### *FIR*:

  - #### *IIR*:

### Metodología
#### EEG


### Gráficos de resultados
#### EEG
| | 1er Reposo | Pestañeo | 2do Reposo | Resolución de ejercicios |
| ------------ | ------------ | ------------ | ------------ | ------------ |
| FIR | ![fir1](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab6_Filtros/EEG/img/ej1_FIR.png?raw=true) | ![fir2](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab6_Filtros/EEG/img/ej2_FIR.png?raw=true) | ![fir3](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab6_Filtros/EEG/img/ej3_FIR.png?raw=true) | ![fir4](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab6_Filtros/EEG/img/ej4_FIR.png?raw=true) | 
| IIR | ![iir1](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab6_Filtros/EEG/img/ejercicio1_IIR.png?raw=true) | ![iir2](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab6_Filtros/EEG/img/ejercicio2_IIR.png?raw=true) | ![iir3](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab6_Filtros/EEG/img/ejercicio3_IIR.png?raw=true) | ![iir4](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab6_Filtros/EEG/img/ejercicio4_IIR.png?raw=true) | 

### Resumen y explicación final
#### EEG

### Archivos
#### EEG

## Bibliografía 
[1] J. M. Marín de la Rosa. “FUNDAMENTOS TEÓRICOS”. Test Page for the HTTP Server on Red Hat Enterprise Linux. [En línea]. Disponible: https://biblus.us.es/bibing/proyectos/abreproy/11375/fichero/MEMORIA%2FFundamentos+teoricos.pdf

