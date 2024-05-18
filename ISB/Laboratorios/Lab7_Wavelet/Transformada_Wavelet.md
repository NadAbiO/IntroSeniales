# Laboratorio 7: Filtrado de las señales Transformada Discreta Wavelet

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
- Entender los principios básicos del filtro wavelet.
- Utilizar el filtro wavelet en señales de EMG, ECG y EEG.
- Evaluar las señales filtradas.

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
# Entregable:
En este laboratorio, se llevó a cabo una tabulación de datos con el objetivo de analizar y visualizar de manera más precisa y ordenada las señales de ECG y EEG previamente adquiridas cin BITalino. 

 [EMG (.txt)](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab7_Wavelet/EMG/Bruno.txt)

 [ECG (.txt)](https://github.com/NadAbiO/IntroSeniales/blob/6abf1eb74153f9200835076af4d8b57692140198/ISB/Laboratorios/Lab7_Wavelet/ECG/bruno_reposo.txt)
 
 [EEG (.txt)](https://github.com/NadAbiO/IntroSeniales/blob/6abf1eb74153f9200835076af4d8b57692140198/ISB/Laboratorios/Lab7_Wavelet/EEG/bruno1.txt)

## Introducción

#### ¿Qué es Transformada Discreta Wavelet?

La transformada Wavelet (WT) es una técnica comúnmente empleada para reducir el ruido y extraer características de imágenes biomédicas. La efectividad del proceso de eliminación de ruido depende en gran medida de la configuración seleccionada para el sistema WT [1].

#### Para EMG
El electromiograma (EMG) mide la actividad eléctrica de los músculos y es crucial para aplicaciones biomédicas. Las señales EMG suelen estar contaminadas por ruido, complicando su análisis. La transformada wavelet es altamente efectiva para eliminar este ruido, permitiendo una descomposición multirresolución de la señal. Usando wavelets como Daubechies (db2, db6, db8) y Meyer ortogonal, se pueden identificar y suprimir los componentes de ruido sin perder información importante. El proceso incluye la descomposición de la señal en varios niveles de resolución, la aplicación de un umbral a los coeficientes wavelet y la reconstrucción de la señal denoised. Esta técnica supera a los métodos de filtrado tradicionales, mejorando la calidad de las señales EMG para su análisis posterior. [5]

#### Para ECG
Las enfermedades cardiovasculares son una de las principales causas de muerte a nivel mundial. La monitorización diaria de las señales del electrocardiograma (ECG) es crucial para su prevención, diagnóstico y tratamiento. Sin embargo, las señales captadas por sensores portátiles son susceptibles a interferencias y ruidos. Por ello, es esencial filtrar el ruido antes de analizar las señales cardiacas, ya que afecta la precisión del sistema de detección. Existen diversas técnicas de eliminación de ruido, como el filtrado digital, la reducción adaptativa de ruido y la transformada wavelet. Esta última es especialmente efectiva para señales biomédicas no estacionarias y se ha mejorado en los últimos años para optimizar la eliminación de ruido en señales cardiacas.[2]

#### Para EEG
La electroencefalografía (EEG) registra la actividad eléctrica del cerebro y su uso en investigaciones ha aumentado con los años. Es crucial procesar eficazmente los datos de EEG para mejorar la calidad de la señal. La transformada wavelet es un método destacado para el análisis en el dominio tiempo-frecuencia, superior a la transformada de Fourier por su buena localización tiempo-frecuencia y capacidad de análisis multiresolución, lo que permite extraer eficientemente información transitoria de las señales EEG.[3]



---

## Metodología

#### Para EMG
Se utilizó un artículo en el cual se aplican distintas ondas wavelet para filtrar ruidos de la data de EMG recolectada. En el estudio, se comprobó que las ondas wavelet db2, db6 y db8 son efectivas para el análisis de señales EMG en pacientes sanos. Para determinar el umbral de los filtros, se utilizó una fórmula basada en la desviación media absoluta (usando la mediana de cada coeficiente del filtro Wavelet) y la cantidad de muestras. Además, se usó una fracción de la señal para que se observe mejor el resultado del filtro [5]

[Codigo en python](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab7_Wavelet/EMG/EMG_Filter.py)

#### Para EEG
Se utilizó un artículo en el cual usan distintas ondas wavelet para filtrar ruidos de la data de EEG recolectada. En el estudio, se comprobó que l onda wavelet db8 es la mejor para analisis de EEG en paciences sanos. 
Para la toma del umbral de los filtros se utilizó una formula en la cual se utilizó la desviación media absoluta (usando la media de cada coeficiente del filtro Wavelet) y la cantidad de muestras. [4]

[Colab muestra 1](https://colab.research.google.com/drive/1eUaBxhaQXpU8WfdU1FeMOJBCxhVQ00yy?usp=sharing)

[Colab muestra 2](https://colab.research.google.com/drive/1UXi7iKzdLzqB8rShkmAx6oaGnAhum5fr?usp=sharing)


---
## Gráficos de resultados

#### EMG
| Muestra 1 |
|--------------|
| ![](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab7_Wavelet/EMG/EMG%20wavelet%20filter.png) |


#### EEG

| Muestra 1 | Muestra 2 | 
|--------------|:------------:|
| ![w1](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab7_Wavelet/EEG/w1.png?raw=true) |  ![w4](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab7_Wavelet/EEG/w4.png?raw=true) |  

#### EMG
| Señal en reposo|
|--------------|
|![](<img src="https://github.com/NadAbiO/IntroSeniales/blob/main/Anexos/Laboratorios/ECG_wavelet.png" alt="ECG Wavelet" width="400" height="250">)|






---
## Archivos
- [ECG (.txt)](https://github.com/NadAbiO/IntroSeniales/blob/6abf1eb74153f9200835076af4d8b57692140198/ISB/Laboratorios/Lab7_Wavelet/ECG/bruno_reposo.txt)
- [EEG (.txt)](https://github.com/NadAbiO/IntroSeniales/blob/6abf1eb74153f9200835076af4d8b57692140198/ISB/Laboratorios/Lab7_Wavelet/EEG/bruno1.txt)



---
## Discusión


---
## Bibliografía 

[1] D. Vilimek et al., “Comparative analysis of wavelet transform filtering systems for noise reduction in ultrasound images”, PLOS ONE, vol. 17, n.º 7, julio de 2022, art. n.º e0270745. Accedido el 17 de mayo de 2024.[Online]. Available: https://doi.org/10.1371/journal.pone.0270745

[2] Y. KAIMIN, L. FENG, W. MINFENG, and C. WEB, “Accurate wavelet thresholding method for ECG Signals,” Computers in Biology and Medicine. Accedido el 17 de mayo de 2024.[Online]. Available: https://doi.org/10.1016/j.compbiomed.2023.107835 

[3] S. N. S. S. Daud and R. Sudirman, “Wavelet based filters for artifact elimination in Electroencephalography Signal: A review ,” SpringerLink. Accedido el 17 de mayo de 2024.[Online]. Available: https://doi.org/10.1007/s10439-022-03053-5

[4]	M. Mamun, M. Al-Kadi, y M. Marufuzzaman, “Effectiveness of wavelet denoising on electroencephalogram signals”, J. Appl. Res. Technol., vol. 11, núm. 1, pp. 156–160, 2013. Accedido el 17 de mayo de 2024.[Online]. Available: https://doi.org/10.1016/S1665-6423(13)71524-4

[5] N. M. Sobahi, "Denoising of EMG Signals Based on Wavelet Transform," Asian Transactions on Engineering (ATE ISSN: 2221-4267), vol. 1, no. 5, pp. 17-23, 2011. [Online]. Available: https://www.researchgate.net/publication/267957236_Denoising_of_EMG_Signals_Based_on_Wavelet_Transform





