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
- Utilizar el filtro wavelet en señales de ECG y EEG.
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

 [ECG (.txt)](https://github.com/NadAbiO/IntroSeniales/blob/6abf1eb74153f9200835076af4d8b57692140198/ISB/Laboratorios/Lab7_Wavelet/ECG/bruno_reposo.txt)
 
 [EEG (.txt)](https://github.com/NadAbiO/IntroSeniales/blob/6abf1eb74153f9200835076af4d8b57692140198/ISB/Laboratorios/Lab7_Wavelet/EEG/bruno1.txt)

## Introducción

#### ¿Qué es Transformada Discreta Wavelet?

La transformada Wavelet (WT) es una técnica comúnmente empleada para reducir el ruido y extraer características de imágenes biomédicas. La efectividad del proceso de eliminación de ruido depende en gran medida de la configuración seleccionada para el sistema WT [1].

#### Para ECG
Las enfermedades cardiovasculares son una de las principales causas de muerte a nivel mundial. La monitorización diaria de las señales del electrocardiograma (ECG) es crucial para su prevención, diagnóstico y tratamiento. Sin embargo, las señales captadas por sensores portátiles son susceptibles a interferencias y ruidos. Por ello, es esencial filtrar el ruido antes de analizar las señales cardiacas, ya que afecta la precisión del sistema de detección. Existen diversas técnicas de eliminación de ruido, como el filtrado digital, la reducción adaptativa de ruido y la transformada wavelet. Esta última es especialmente efectiva para señales biomédicas no estacionarias y se ha mejorado en los últimos años para optimizar la eliminación de ruido en señales cardiacas.[2]

#### Para EEG
La electroencefalografía (EEG) registra la actividad eléctrica del cerebro y su uso en investigaciones ha aumentado con los años. Es crucial procesar eficazmente los datos de EEG para mejorar la calidad de la señal. La transformada wavelet es un método destacado para el análisis en el dominio tiempo-frecuencia, superior a la transformada de Fourier por su buena localización tiempo-frecuencia y capacidad de análisis multiresolución, lo que permite extraer eficientemente información transitoria de las señales EEG.[3]
---

## Metodología


---
## Gráficos de resultados



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

