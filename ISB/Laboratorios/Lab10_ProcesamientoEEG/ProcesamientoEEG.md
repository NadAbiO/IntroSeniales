# LABORATORIO 10 - PROCESAMIENTO DE EEG

### TABLA DE CONTENIDO

1. [Objetivos](#id1)
2. [Introducción](#id2)
3. [Metodología](#id3)
   - [Adquisición de la señal](#id4)
   - [Filtrado (ICA)](#id5)
   - [Preprocesamiento](#id6)
   - [Extracción de características (Wavelet)](#id7)
4. [Resultados](#id8)
5. [Discusión](#id9)
6. [Archivos](#id10)
7. [Bibliografía](#id11)
---

## **Objetivos** <a name="id1"></a>
- Adquisición de la señal EEG mediante Ultracortex
- Aplicar Análisis de Componentes Independientes (ICA) para separar y filtrar artefactos y ruidos de la señal EEG.
- Normalizar la amplitud de las señales EEG y alinear temporalmente para asegurar una comparación precisa.
- Utilizar la Transformada Wavelet Discreta (DWT) para descomponer la señal EEG y extraer características relevantes.

---
## **Introducción** <a name="id2"></a>
<p align="justify">El electroencefalograma (EEG) es una técnica diagnóstica fundamental en la neurología que permite la medición de la actividad eléctrica del cerebro mediante electrodos situados en el cuero cabelludo. Esta técnica registra los potenciales eléctricos generados por las neuronas cerebrales, proporcionando información crítica sobre la función neuronal y la actividad cerebral [1] </p>

<p align=justify"> Se identifican cinco ondas cerebrales principales, cada una con un rango de frecuencia específico. Estas bandas de frecuencia, ordenadas de menor a mayor, se denominan delta (δ), theta (θ), alpha (α), beta (β) y gamma (γ).[2]

<p align=justify"> El EEG se utiliza ampliamente para investigar y diagnosticar trastornos neurológicos, especialmente en la evaluación de la epilepsia y otros trastornos convulsivos. También es fundamental en el diagnóstico de trastornos del sueño y encefalopatías, así como para la monitorización en cirugías cerebrales y durante la administración de anestesia .</p>

<p align=justify"> Los métodos tradicionales para eliminar artefactos del EEG suelen utilizar filtros lineales o regresiones, basándose en cuándo ocurren los artefactos o en qué rango de frecuencias se encuentran [5]. Sin embargo, filtrar en el dominio del tiempo o de la frecuencia puede llevar a una pérdida significativa de la actividad cerebral observada, debido a que las señales neurológicas y los artefactos pueden superponerse espectralmente. El análisis multirresolución con transformada wavelet discreta (DWT) es más eficaz para eliminar artefactos y preservar la estructura real de la señal EEG en el tiempo y la frecuencia [6, 7]. Por su parte, el análisis de componentes independientes (ICA) ha demostrado ser útil para separar los artefactos en componentes independientes [8].

<p align=justify"> En los últimos años, se ha implementado una técnica que combina ICA y DWT para eliminar artefactos en el EEG. Este método combinado también puede manejar diversos tipos de artefactos en EEG de múltiples canales.[4]

<p align="center">
  <img src="https://canada1.discourse-cdn.com/free1/uploads/mne/original/1X/68ff535c1fa69202b9b367218a1f8f685064032c.jpeg"  width="300" height="200"> </p>
<em><p align="center">Figura 1 Componenes ICA [9]. </p></em> 

---
## **Metodología** <a name="id3"></a>

- ### **Adquisición de la señal** <a name="id4"></a>

   <p align="justify"> La señal utilizada en este estudio fue obtenida mediante el sistema Ultracortex utilizando el sistema internacional 10-20, durante las sesiones de laboratorio. La data cuenta con 8 canales de EEG, cada uno de los cuales captura la actividad cerebral con una frecuencia de muestreo de 250 Hz. La elección del Ultracortex y del entorno de laboratorio se realizó para asegurar la calidad y consistencia de los datos recogidos, aprovechando las capacidades avanzadas del hardware de OpenBCI. Estas configuraciones permiten una resolución temporal adecuada para un análisis detallado de las ondas cerebrales y aseguran que las señales capturadas sean precisas y fiables para los propósitos del estudio.
   
<div align="center">

| Vista superior | Vista lateral |
|----------|----------|
| <img src="https://github.com/NadAbiO/IntroSeniales/assets/89549012/7363b9c8-fec1-4913-91fe-4202bf97d567" alt="superior" width="200"/> | <img src="https://github.com/NadAbiO/IntroSeniales/assets/89549012/c422a465-c922-477f-9f70-efd335f4fbf5" alt="lateral" width="200"/> |

<em><p align="center">Figura 2. Posicionamiento de Electrodos 10-20 [3]</p></em>

<div align="left">

---
- ### **Filtrado (ICA)** <a name="id5"></a>

[ICA - google Colab](https://colab.research.google.com/drive/1OVnGGGl1892MNKIAGkUj3gbo-6ZN5EDJ?usp=sharing)


---
- ### **Preprocesamiento** <a name="id6"></a>


---
- ### **Extracción de características (Wavelet)** <a name="id7"></a>


---


## **Resultados** <a name="id8"></a>


---

## **Discusión** <a name="id9"></a>


---

## **Archivos** <a name="id10"></a>

- [Señal EEG (.txt)](https://github.com/NadAbiO/IntroSeniales/blob/eabb364176c7424485a2238dc83e6cd4f13f24d7/ISB/Laboratorios/Lab10_ProcesamientoEEG/OpenBCI_GUI-v5-meditation.txt)

---


## **Bibliografía** <a name="id11"></a>

[1] D. L. Schomer and L. da S. F. Henrique, Niedermeyer’s Electroencephalography: Basic Principles, Clinical Applications, and Related Fields. New York: Oxford University Press, 2018.

[2] S. Sanei y J. A. Chambers, EEG Signal Processing. West Sussex, England: John Wiley Sons Ltd,, 2007. Accedido el 15 de junio de 2024. [En línea]. Disponible: https://doi.org/10.1002/9780470511923

[3] Bitalino (r)evolution lab guide, https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide3_EEG.pdf. Accedido el 15 de junio de 2024. 

[4] S. S. Lee, K. Lee and G. Kang, "EEG Artifact Removal by Bayesian Deep Learning & ICA," 2020 42nd Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC), Montreal, QC, Canada, 2020, pp. 932-935, doi: 10.1109/EMBC44109.2020.9175785.

[5] J. C. Woestenburg, M. N. Verbaten, and J. L. Slangen, "The removal of the eye-movement artifact from the EEG by regression analysis in the frequency domain," Biological Psychology, vol. 16, pp. 127-147, 1983.

[6] J. H. Zhang, K. Janschek, J. F. Bohme, and Y. J. Zeng, "Multi-resolution dyadic wavelet denoising approach for extraction of visual evoked potentials in the brain," IEE Proceedings - Vision, Image and Signal Processing, vol. 151, pp. 180-186, 2004.

[7] M. Mamun, M. Al-Kadi, and M. Marufuzzaman, "Effectiveness of Wavelet Denoising on Electroencephalogram Signals," Journal of Applied Research and Technology, vol. 11, pp. 156-160, 2013.

[8] M. B. Hamaneh, N. Chitravas, K. Kaiboriboon, S. D. Lhatoo, and K. A. Loparo, "Automated Removal of EKG Artifact From EEG Data Using Independent Component Analysis and Continuous Wavelet Transformation," IEEE Transactions on Biomedical Engineering, vol. 61, pp. 1634-1641, 2014.

[9] “Unusual failure mode of ICA in particular subject”. MNE Forum. Accedido el 15 de junio de 2024. [En línea]. Disponible: https://mne.discourse.group/t/unusual-failure-mode-of-ica-in-particular-subject/2924

