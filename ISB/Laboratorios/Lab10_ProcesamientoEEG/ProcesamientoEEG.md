# LABORATORIO 10 - PROCESAMIENTO DE EEG

### TABLA DE CONTENIDO

1. [Objetivos](#id1)
2. [Introducción](#id2)
3. [Metodología](#id3)
   - [Adquisición de la señal](#id4)
   - [Filtrado (ICA)](#id5)
   - [Preprocesamiento](#id6)
   - [Feature extraction (Wavelet)](#id7)
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


<p align="center">
  <img src=""  width="300" height="200"> </p>
<em><p align="center">Figura 1. </p></em> 

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
- ### **Feature extraction (Wavelet)** <a name="id7"></a>


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


