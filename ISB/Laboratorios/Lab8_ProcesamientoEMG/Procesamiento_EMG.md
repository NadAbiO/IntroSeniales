# LABORATORIO 8 - PROCESAMIENTO DE EMG

### TABLA DE CONTENIDO

1. [Objetivos](#id1)
2. [Introducción](#id2)
3. [Metodología](#id3)
   - [Adquisición de la señal](#id4)
   - [Filtrado](#id5)
   - [Segmentación](#id6)
   - [Extracción de características](#id7)
4. [Resultados](#id8)
5. [Discusión](#id9)
6. [Archivos](#id10)
7. [Bibliografía](#id11)
---


## **Objetivos** <a name="id1"></a>
- Recopilar estudios científicos sobre el procesamiento de datos electromiográficos (EMG).
- Utilizar métodos de filtrado para mejorar y acondicionar las señales EMG recolectadas.
- Desarrollar un sistema para segmentar las señales EMG.
---

## **Introducción** <a name="id2"></a>
---
La señal de electromiografía (EMG) es una representación eléctrica de la actividad neuromuscular asociada con un músculo en contracción. Esta señal es extremadamente compleja y está influenciada por las propiedades anatómicas y fisiológicas de los músculos, el sistema de control del sistema nervioso periférico y las características de la instrumentación utilizada para su detección y monitoreo. Muchas de las relaciones entre la señal EMG y las propiedades de un músculo en contracción que se utilizan comúnmente se han desarrollado de manera fortuita. La falta de una representación adecuada de la señal EMG es probablemente el factor más significativo que ha impedido el desarrollo de la EMG como un campo especializado [4].

En términos generales, el proceso de análisis de la señal EMG incluye etapas como la adquisición de datos, el procesamiento de la señal, la extracción y clasificación de características de la señal, y las funciones de predicción. Cada una de estas etapas varía según los parámetros de diseño, tales como el costo de producción y el porcentaje de precisión.

## **Metodología EMG** <a name="id3"></a>

- ### **Adquisición de la señal** <a name="id4"></a>
   <p align="justify"> La obtención de señales biomédicas es esencial para la evaluación de pacientes que presentan afecciones médicas. Desde un enfoque que considera aspectos de la fisiología y biomecánica, la aplicación de electromiografías (EMG) ha facilitado el estudio del funcionamiento muscular. Esto abarca desde actividades diarias hasta movimientos específicos, como caminar, subir escaleras, manejar objetos, saltar, lanzar, correr, entre otros.[1]

   En otro aspecto, la electromiografía (EMG) se destaca por su importancia tanto en el ámbito teórico como clínico, donde su procesamiento y análisis son fundamentales. En este sentido, muchas investigaciones se centran en analizar la variación temporal de la señal electromiográfica, utilizando los cambios en la amplitud mioeléctrica como un indicador clave para describir la actividad muscular.[1]

   En la adqusición de las señales de sEMG, se pueden identificar varios pasos distintos: pre-amplificación, filtrado y la etapa de conversión de analógico a digital. 
La señal proveniente de la etapa de pre-amplificación contiene una mezcla de señales biológicas y ruido del ambiente, es por esta razón que se requiere depurar o filtrar la información. La extracción de características consiste en obtener información relevante de la señal de sEMG mediante una transformación de los datos originales. [2]

</p>

<p align="center">
  <img src="https://github.com/NadAbiO/IntroSeniales/assets/89549012/42be6c03-eb21-43e3-99c3-3785d83aa594"  width="500" alt="image"> </p>
<em><p align="center">Principales etapas implicadas en la adquisición de la señal, preprocesamiento, y extracción de características de señales de EMG registrados a partir de una fibra muscular [3]</p></em> 

- ### **Filtrado** <a name="id5"></a>

Para identificar el mejor filtro para una señal EMG, se siguió una metodología que involucró el uso de tres tipos diferentes de filtros: el filtro Wavelet, el filtro FIR (Finite Impulse Response) y el filtro IIR (Infinite Impulse Response). Se evaluó la efectividad de estos filtros utilizando la métrica de la Signal to Noise Ratio (SNR) de la señal filtrada frente a la señal original.
<p align="center">
  <img src="https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab8_ProcesamientoEMG/Signals.png" alt="image"> </p>
<em><p align="center">Comparacion de filtros en la señal EMG</p></em> 
<p align="center">
  <img src="https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab8_ProcesamientoEMG/SNRmiau.png" alt="image"> </p>
<em><p align="center"> Valores SNR obtenidos de la comparacion </p></em> 

En base a los resultados obtenidos de la comparacion, se eligio al filtro wavelet como el mejor para realizar la segmentacion y posterior extraccion de caracteristicas. El filtro Wavelet implementado se hizo en base a un estudio que certifico que las ondas wavelet db2, db6 y db8 son efectivas para el análisis de señales EMG en pacientes sanos. Para determinar el umbral de los filtros, se utilizó una fórmula basada en la desviación media absoluta (usando la mediana de cada coeficiente del filtro Wavelet) y la cantidad de muestras. Además, se usó una fracción de la señal para que se observe mejor el resultado del filtro[5]

- ### **Segmentación** <a name="id6"></a>
El artículo titulado "Comparison of the Techniques Used for Segmentation of EMG Signals" explora las metodologías para segmentar señales de EMG específicamente en el contexto de diagnósticos neuromusculares. El documento identifica y compara tres técnicas principales de segmentación utilizadas para extraer potenciales de acción de unidades motoras (MUAPs) de las señales EMG. Los MUAPs, son el resultado de la suma de los potenciales de acción de las fibras musculares individuales dentro de una unidad motora y son fundamentales para entender la actividad muscular [6].

Técnicas de segmentación utilizadas: 
Identificación de picos de MUAPs: Esta técnica segmenta la señal detectando los picos de los MUAPs utilizando un umbral basado en el valor máximo y el valor medio absoluto de la señal EMG [6].

Identificación de puntos de inicio y fin: El BEP (Beginning Extraction Point) y el EEP (Ending Extraction Point) marcan el inicio y el final, respectivamente, de un MUAP. Utilizamos un filtro de paso alto y ventanas deslizantes para identificar los puntos de inicio y fin de los MUAPs basándose en umbrales específicos de amplitud [6].

Transformada de Wavelet Discreta (DWT): Esta técnica descompone la señal EMG utilizando wavelets, en este caso, Daubechies4 (db4), para identificar los picos de los MUAPs.


- ### **Extracción de caracteríticas** <a name="id7"></a>
La extracción de características en señales EMG implica transformar los datos brutos de la señal en una estructura de datos relevante, eliminando el ruido y resaltando la información esencial. Dentro de este contexto, se identifican tres tipos principales de características: las del dominio del tiempo, las del dominio de la frecuencia y las del dominio tiempo-frecuencia [7]. 

Para la extracción de características en nuestras señales, optaremos por métodos en el dominio del tiempo. Estas técnicas son ampliamente utilizadas en el reconocimiento de patrones EMG debido a su simplicidad y rapidez de cálculo, puesto que no requieren de transformaciones adicionales. Las características en el dominio del tiempo se calculan directamente a partir de la amplitud de las señales entrantes [7].

La técnica para evaluar en el tiempo es la raíz cuadrada media (RMS), ofrece una mejor representación de las fluctuaciones observadas en las contracciones de fuerza constante [7].

Además en el Biosignals Notebooks, para Análisis de las señales EMG, se recomienda las siguientes técnicas: Detección de señales de activación, en el dominio de la frecuencia: Median Frecuency, Maximum power frecuency. También consideraremos la detección de las contracciones musculares. 


--- 


## **Resultados** <a name="id8"></a>
---
1. **Segmentación**

- **Identificación de picos de MUAPs**
  <div align="center">
  <img src="https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab8_ProcesamientoEMG/Imagenes/peak_detection.png"  width="700" height="500"> 
  </div>

- **Identificación de puntos de inicio y fin**
  <div align="center">
  <img src="https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab8_ProcesamientoEMG/Imagenes/bep.png"  width="700" height="500"> 
  </div>

- **Transformada de Wavelet Discreta (DWT)**
  <div align="center">
  <img src="https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab8_ProcesamientoEMG/Imagenes/dwt_segmentation.png"  width="700" height="500"> 
  </div>
  
   
2. **Extracción de características**

- **Detección de contracciones musculares**
  <div align="center">
  <img src="https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab8_ProcesamientoEMG/Imagenes/contracciones%20musculares.png"  width="700" height="500"> 
  </div>
  
- **Detección de señales de activación**
  <div align="center">
  <img src="https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab8_ProcesamientoEMG/Imagenes/se%C3%B1ales_de_activacion.png"  width="700" height="500"> 
  </div>
  
- **RMS**
  <div align="center">
  <img src="https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab8_ProcesamientoEMG/Imagenes/RMS.png"  width="700" height="500"> 
  </div>
  
- **Valores obtenidos**
  - Maximum Muscular Activation Duration: 1.925
  - Minimum Muscular Activation Duration: 0.234
  - Average Muscular Activation Duration: 1.05
  - Standard Deviation Sample Value: 68.79
  - RMS EMG: 68.7923
  - Median Frequency': 50.78125
  - Maximum Power Frequency: 35.15625



## **Discusión** <a name="id9"></a>

---
## **Archivos** <a name="id10"></a>
---
[Código Procesamiento EMG](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab8_ProcesamientoEMG/Procesamiento_EMG_code.ipynb)

## **Referencias** <a name="id11"></a>

[1] O. Valencia, C. De La Fuente, R. Guzmán-Venegas, R. Salas, and A. Weinstein, “Propuesta de Flujo de Procesamiento utilizando Python para ajustar la Señal Electromiográfica Funcional a la Contracción Voluntaria Máxima,” vol. 40, no. 3, pp. 171–175, 2021, Available: https://repositoriobibliotecas.uv.cl/bitstream/handle/uvscl/7565/Valencia_Pro2021.pdf?sequence=1&isAllowed=y. [Accessed: May. 25, 2024]

[2] “Item 1009/743 | Repositorio INAOE,” Repositorioinstitucional.mx, 2023, doi: http://inaoe.repositorioinstitucional.mx/jspui/handle/1009/743. [Accessed: May. 25, 2024]

[3] J. J. G. Murillo, A. Ilzarbe, y S. Osuna, «Procesado de señales EMG en Trastornos Neuromusculares», 2013, doi: 10.13140/2.1.4902.9445. [Accessed: May. 25, 2024]

[4] C. J. De Luca, "Electromyography," in Encyclopedia of Medical Devices and Instrumentation, 2006. [Accessed: May. 25, 2024]

[5] N. M. Sobahi, "Denoising of EMG Signals Based on Wavelet Transform," Asian Transactions on Engineering (ATE ISSN: 2221-4267), vol. 1, no. 5, pp. 17-23, 2011. [Online]. Available: https://www.researchgate.net/publication/267957236_Denoising_of_EMG_Signals_Based_on_Wavelet_Transform [Accessed: May. 25, 2024]

[6] Comparison of the techniques used for segmentation of EMG Signals. Available at: https://www.researchgate.net/publication/228977464_Comparison_of_the_techniques_used_for_segmentation_of_EMG_signals (Accessed: 26 May 2024).
Se adjunta el artículo:

[PDF](https://github.com/NadAbiO/IntroSeniales/blob/main/ISB/Laboratorios/Lab8_ProcesamientoEMG/Referencia/Comparison_of_the_techniques_used_for_segmentation.pdf)

[7] C. Spiewak, “A Comprehensive Study on EMG Feature Extraction and Classifiers,” Open Access Journal of Biomedical Engineering and Biosciences, vol. 1, no. 1, Feb. 2018, doi: https://doi.org/10.32474/oajbeb.2018.01.000104.
‌

---
