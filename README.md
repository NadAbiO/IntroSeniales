# Introducción a Señales Biomédicas
### <a name="bienvenida"></a>Bienvenidos al repositorio del grupo 5 :)
---

## Tabla de contenido:
- [Integrantes](#integrantes)
- [Proyecto](#proyecto)
- [Entregables](#entregables)

---
### Integrantes

| **Integrante** | **Correo**|
| ---------| ----------|
| Nadira Oviedo <br> <img src="Documentos/Imágenes/Nadira.jpg" alt="img_nad" height="200"/>| nadira.oviedo@upch.pe |
| Alvaro Cigarán <br> <img src="Documentos/Imágenes/Alvaro.jpg" alt="img_nad" height="200"/>| alvaro.cigaran@upch.pe |
| Kimberly Tito <br> <img src="Documentos/Imágenes/kim.jpg" alt="img_nad" height="200"/>| kimberly.tito@upch.pe |
| Bruno Tello <br> <img src="Documentos/Imágenes/br1.jpg" alt="img_nad" height="200"/>| gustavo.tello@upch.pe |
  
---
# Proyecto
### ANALIZANDO SEÑALES DE EEG
*Desarrollaremos un sistema que pueda adquirir, procesar y comparar señales de un Electroencefalograma (EEG)*

## ¿Qué es un electroencefalograma?
#### Es un estudio médico que detecta anomalías en las ondas cerebrales. Se colocan electrodos en el cuero cabelludo para medir la actividad eléctrica del cerebro. Estas señales se registran como gráficos en una pantalla de computadora o en papel [9].

<div align="center">
  <img src="https://cainvas-static.s3.amazonaws.com/media/user_data/cainvas-admin/eeg.gif" />
  <p> Photo by Lobster on Dribbble </p>
</div>


## Objetivo
<p align="justify"> El objetivo es comparar las ondas cerebrales de personas con sueño completo y de aquellas que consumen bebidas energéticas, utilizando un mismo estímulo. Se busca analizar cómo afecta el consumo de estas bebidas a la actividad cerebral en comparación con un estado de sueño normal, lo que puede tener implicaciones en el rendimiento cognitivo y en la salud mental.

---

# Entregables
<details>
<summary>  Primer entregable</summary>

# Temas a tratar:
 ## 1.- Electroencefalograma y ondas cerebrales

 ## 2.- Importancia del sueño

 ## 3.- Bebidas energéticas y estudiantes universitarios

 ## 4.- Insomnio

#### Descarga el archivo PPT -> [aquí](Documentos/Señales_problematica.pdf).

</details>


<details>
<summary> Segundo entregable</summary>

# Temas a tratar:
 ## 1.- Problemática

<p align="justify"> El sueño es una función vital para el bienestar físico y mental, especialmente en estudiantes universitarios, quienes frecuentemente enfrentan desafíos académicos y sociales que pueden afectar su calidad de sueño. La falta de sueño adecuado puede llevar a una disminución del rendimiento académico, problemas de atención y memoria, y un aumento en el riesgo de desarrollar problemas de salud mental como ansiedad y depresión. Entre los factores que influyen en el sueño, el consumo de bebidas energéticas ha ganado atención debido a su popularidad y sus posibles efectos adversos.[2][3][5]
 
Las bebidas energéticas contienen ingredientes como la cafeína y la taurina, que actúan sobre el sistema nervioso central. La cafeína tiene múltiples objetivos bioquímicos, incluyendo los receptores GABA y adenosina A1 y A2A. Bloquear estos receptores, especialmente los de adenosina A2A, se relaciona con propiedades psicoactivas como el aumento de la capacidad intelectual, alerta y reducción de la fatiga mental. Sin embargo, su consumo excesivo puede interferir con el sueño, causando insomnio, ansiedad y afectando negativamente la función cognitiva a largo plazo. Además, altas dosis de cafeína pueden aumentar el riesgo de alucinaciones y reducir el umbral convulsivo. [4][6][7]

La taurina, aunque puede tener efectos neuroprotectores, también puede impactar negativamente la función cognitiva y el comportamiento, especialmente en jóvenes adultos. La taurina afecta al sistema nervioso interactuando con neurotransmisores y regiones cerebrales, lo que sugiere un posible papel neuroprotector. Sin embargo, su suplementación podría tener efectos negativos en la función cognitiva y el comportamiento, especialmente en adolescentes y adultos jóvenes. [6][7]
El insomnio crónico tiene graves consecuencias para la calidad de vida y la salud: afecta negativamente el funcionamiento físico, emocional y social de las personas; aumenta el riesgo de accidentes, incluidos accidentes laborales; disminuye la productividad y la concentración en el trabajo; y está asociado con una mayor probabilidad de desarrollar depresión y ansiedad..[8]


 ## 2.- Propuesta de solución
 **Propuesta de Investigación:** Impacto cognitivo por mala calidad de sueño y uso de bebidas energéticas
 
**Objetivo:**

Con el uso del Ultracortex, registrar la actividad cerebral al realizar tareas cognitivas para relacionar los resultados con el uso prolongado de bebidas energéticas y mala calidad de sueño.

**Hipótesis:**

El uso prolongado de energizantes y la mala calidad del sueño afectan negativamente el rendimiento cognitivo, manifestándose en patrones específicos de actividad cerebral detectables mediante EEG.

**Metodología:**

1.- Selección de participantes

2.- Registro de datos

3.- Análisis de datos

 ## 3.- Materiales y métodos
 
### 3.1 Materiales y recursos

| **Materiales** | 
| ---------|
| Encuesta| 
| Ultracortex|
| OpenBCI GUI|
| Ambiente relajado| 
| Pruebas cognitivas| 
| Procesamiento de señales: Código en Python| 
| Análisis estadístico: Stata| 

- ### **Ondas EEG y sus frecuencias**

<p align="justify"> Las ondas del EEG pueden caracterizarse en función de su localización, amplitud, frecuencia, morfología, continuidad (rítmica, intermitente o continua), sincronía, simetría y reactividad. Sin embargo, el método más utilizado para clasificar las formas de onda del EEG es el de la frecuencia. Las formas de onda más estudiadas son [12]:

<p align="center"> 
    
| **_Tipos de Frecuencia_** | **_Frecuencia (Hz)_** |Estado del cerebro|
|:---------------------------------------------:|:---------------------:|:------------:|
|                     Delta                     |      0.50 - 4.00      |Se observa durante el sueño profundo y es prominente en las regiones frontocentrales de la cabeza.|
|                     Theta                     |      4.00 - 7.00      |Asociado con somnolencia y las primeras etapas del sueño. |
|                     Alpha                     | 8.00 - 12.00          |Característico en registros de EEG normales despiertos en la región occipital.|
|                      Beta                     | 13.00 - 30.00         |Más prominente en regiones frontal y central.|

</p>

- ### **Uso del Ultracortex**
  
  - ***¿Para qué sirve?***
        <p align="justify"> El Ultracortex Mark IV es un casco modular que permite la colocación de electrodos en el cuero cabelludo de manera precisa y cómoda. Registra la actividad eléctrica  de hasta 16 canales de EEG y  permite ver dichas señales a través de su interfaz OpenBCI.

<p align="center">
  <img src="https://github.com/NadAbiO/IntroSeniales/assets/89549012/6751155f-23d8-4c8e-96d8-2d27ee3c0d34"  width="400" height="300"> </p>
<em><p align="center">Photo by OpenBCI Documentation [13]</p></em> 

  <p align="justify"> Es un tipo de Non-Invasive Brain Computer Interfaces lo cual significa que los electrodos se colocan en la superficie del cráneo para registrar los cambios de estado del EEG.
    
  - - ***Ubicación de los electrodos***
      <p align="justify"> Las ubicaciones de los nodos Ultracortex se basan en el sistema 10-20, que es el estándar aceptado internacionalmente para la colocación de electrodos en el contexto del EEG. [13]
      <p align="justify"> En nuestro caso nos enfocaremos en los lóbulo Frontal y temporal por lo que la posición de los electrodos que nos interesan son [14]:
      
      <p align="center">
      
      | **Lóbulo** | **Electrodos**|
      | ---------| ----------|
      | Frontal| Fz, Fp1, Fp2, F3, F4, F7, F8 |
      | Temporal| T3, T4, T5, T6 |
      | Referencia | pinzas para orejas |

      </p>

      <p align="center">
        <img src="https://github.com/NadAbiO/IntroSeniales/assets/89549012/e8e5d13f-bb79-4916-a7a9-7ccb6533e2e0"  width="400" height="300"> </p>
      <em><p align="center">Photo by BITalino (r)evolution Lab Guide [14]</p></em> 


  - - ***OPENBCI GUI***
      
      <p align="justify"> 
      Para seleccionar los canales correspondientes a los lóbulos frontal y temporal en OpenBCI, luego de conectar los electrodos al dispositivo OpenBCI, seguiremos estos pasos:
      
      1. **Conectamos y configuramos nuestro dispositivo OpenBCI**
         
      2. **Seleccionamos los canales de interés:**
         En la interfaz del software de OpenBCI, veremos una lista de todos los canales disponibles. Estos canales estarán etiquetados según la configuración de nuestro dispositivo y los electrodos que hayamos conectado.

      3. **Identificamos los canales correspondientes a los lóbulos frontal y temporal:**
         Basándonos en la colocación de nuestros electrodos, identificamos los canales que registran la actividad en los lóbulos frontal y temporal. 
         
      4. **Realizamos la adquisición de datos:**
         Una vez que hayamos seleccionado los canales de interés y estemos visualizando las señales, podemos comenzar la adquisición de datos. Esto registrará la actividad eléctrica en los lóbulos frontal y temporal según la colocación de nuestros electrodos.
  

###  3.2 Preparación del grupo de estudio

- **Participantes objetivo**: Se buscó estudiantes universitarios entre 19-25 años, con diferentes niveles de consumo de bebidas energéticas y calidad de sueño. Que sean no fumadoras y que no consuman ninguna sustancia psicoactiva o psicotrópica.
- **Cuestionarios**: Se administraron cuestionarios para evaluar el consumo de bebidas energéticas y la calidad del sueño de los participantes.
  
### 3.3 Procedimiento

 - ***Reclutamiento de participantes***
Se reúne a estudiantes universitarios que cumplan con los criterios de elegibilidad. Se les explica el estudio y se asegura que todos los participantes firmen un formulario de consentimiento informado, detallando el propósito del estudio y los procedimientos. Se les clasifica en grupos según su consumo de cafeína y calidad de sueño.

- ***Colocación de los electrodos***
Los electrodos se colocaron según el sistema internacional 10/20. Todas las impedancias de los electrodos se mantuvieron por debajo de 5 kΩ.

- ***Configuración del Ambiente***
Se realiza la adquisición de las señales en un ambiente controlado, libre de ruidos y distracciones.

- ***Instrucciones a los Participantes***
Se les da instrucciones claras sobre las tareas a realizar y se asegura de que los participantes comprendan los procedimientos.

- ***Registro Basal***
Obtener un registro basal de EEG con el participante en reposo (ojos cerrados y ojos abiertos) durante 5 minutos cada uno.

***Tareas Cognitivas***
Se realiza la adquisición de EEG mientras los participantes completan las tareas cognitivas seleccionadas. Según lo encontrado en la literatura, se seleccionaron las siguientes tareas cognitivas a realizar:

- **Visual event-related potential (ERP)**: En la tarea se empleó el paradigma oddball, el cual consiste en que los sujetos distingan los estímulos objetivo (infrecuentes) de los no objetivo o estándar (frecuentes). Este paradigma es especialmente útil para investigar los Potenciales Relacionados con Eventos (ERP) en el cerebro, particularmente el componente P300, que es conocido por su sensibilidad a la novedad y la relevancia de los estímulos [16].
- **Reaction Time**: Consiste en un experimento que mide cuánto tardan los sujetos en presionar un botón de un joystick después de un estímulo objetivo, utilizado como un indicador del rendimiento motor de los individuos [16].
- **Stroop Test**: El test de Stroop evalúa la atención focalizada y examina la capacidad integrativa de los mecanismos cognitivos para tomar decisiones basadas en información proveniente de dos modalidades diferentes (léxica y perceptual). En la primera parte del test, se pide a los sujetos que lean los nombres de diferentes colores. Luego, deben nombrar el color de impresión de una palabra que denota un color diferente; por ejemplo, leer la palabra "azul" impresa en verde, lo que crea una interferencia color-palabra. Se instruye a los sujetos para que realicen la tarea tan rápido y precisamente como sea posible [16].
- **Digit Span**: La prueba de Amplitud de Dígitos es parte de la Escala de Inteligencia para Adultos de Wechsler (WAIS-III) y se utiliza para medir la memoria a corto plazo y la memoria operativa. Esta prueba consta de dos subcomponentes: Amplitud de Dígitos Hacia Adelante y Amplitud de Dígitos Hacia Atrás. En el primero, se pide a los sujetos que repitan una serie de números en orden creciente después de que el examinador los lea en voz alta. En el subtest de Amplitud de Dígitos Hacia Atrás, los sujetos deben repetir la secuencia en orden inverso [16].

## 4.- Análisis de datos

- **Preprocesamiento**: Se filtrarán las señales EEG para la eliminación del ruido, se utilizará un filtro pasa banda Butterworth, el cual es una de las opciones que se encontró en la literatura [17].
- **Análisis de Frecuencia**: Realizamos un análisis espectral para evaluar las bandas de frecuencia alfa, beta, theta y delta.

## 5.- Análisis estadístico 
Los datos del estudio se analizarán estadísticamente mediante el software STATA para Windows. Se realizará una prueba de análisis de varianza (ANOVA) para comparar los resultados obtenidos en las distintas tareas cognitivas entre los grupos que se clasificaron en la investigación.


### Descarga el archivo PPT -> [Segundo_entregable_grupo_5.pdf](https://github.com/NadAbiO/IntroSeniales/files/15367578/Segundo_entregable_grupo_5.pdf)
### Accede al video -> https://youtu.be/hr92DlsCNKE 

</details>


<details>
<summary> Bibliografía </summary>
  
[1] E. A. S. E. Niripil, “ONDAS CEREBRALES, CONCIENCIA Y COGNICIÓN”, Researchgate.net. [En línea]. Disponible en: https://www.researchgate.net/profile/Eduardo-Alfredo-Sciotto/publication/326056524_ONDAS_CEREBRALES_CONCIENCIA_Y_COGNICION/links/5b358f71aca2720785f48880/ONDAS-CEREBRALES-CONCIENCIA-Y-COGNICION.pdf. [Consultado: 01-abr-2024].

[2] J. I. Bazan-Olaya, J. M. Campos-Pastelin, N. V. Gutiérrez-Moguel, y L. González-Montiel, “Frecuencia y Razones de Consumo de Bebidas Energéticas en Jóvenes Universitarios”, Revista Salud y Administración, vol. 6, núm. 17, pp. 17–26, 2019.

[3] A. M. Rivera Ruiz y D. M. Vasquez Monsalve, “Asociación entre consumo de bebidas energizantes y calidad de sueño en estudiantes de medicina humana de una universidad privada - 2021”, Universidad Señor de Sipán, 2024.

[4] C. R. Mahoney et al., “Intake of caffeine from all sources and reasons for use by college students”, Clin. Nutr., vol. 38, núm. 2, pp. 668–675, 2019.

[5] J. M. Schmickler, S. Blaschke, R. Robbins, y F. Mess, “Determinants of sleep quality: A cross-sectional study in university students”, Int. J. Environ. Res. Public Health, vol. 20, núm. 3, p. 2019, 2023.

[6] I. M. Nadeem, A. Shanmugaraj, S. Sakha, N. S. Horner, O. R. Ayeni, y M. Khan, “Energy drinks and their adverse health effects: A systematic review and meta-analysis”, Sports Health, vol. 13, núm. 3, pp. 265–277, 2021.

[7] N. de referencia: AESAN-, “Informe del Comité Científico de la Agencia Española de Seguridad Alimentaria y Nutrición (AESAN) sobre los riesgos asociados al consumo de bebidas energéticas”, Gob.es. [En línea]. Disponible en: https://www.aesan.gob.es/AECOSAN/docs/documentos/seguridad_alimentaria/evaluacion_riesgos/informes_comite/BEBIDAS_ENERGETICAS.pdf. [Consultado: 01-abr-2024].

[8] T. Roth, “Insomnia: Definition, prevalence, etiology, and consequences”, Journal of Clinical Sleep Medicine : JCSM : official publication of the American Academy of Sleep Medicine, vol. 3, núm. 5 Suppl, p. S7, 2007.

[9] “Electroencephalogram (EEG)”, Stanfordchildrens.org. [En línea]. Disponible en: https://www.stanfordchildrens.org//es/topic/default?id=electroencephalogram-eeg-92-P09193. [Consultado: 01-abr-2024].
Bibliografía

[10]	Reinmar, “Data sets”, Bnci-horizon-2020.eu. [En línea]. Disponible en: https://bnci-horizon-2020.eu/database/data-sets. [Consultado: 01-abr-2024].

[11]	G. Seguimiento y P. De comunicación, “EEG ANALYSIS AND CLASSIFICATION - file exchange - MATLAB CentralFile exchange - MATLAB central”, Mathworks.com, 27-ene-2016. [En línea]. Disponible en: https://la.mathworks.com/matlabcentral/fileexchange/55112-eeg-analysis-and-classification. [Consultado: 01-abr-2024].

[12] C. S. Nayak and A. C. Anilkumar, “EEG Normal Waveforms,” Nih.gov, Jan. 21, 2023. https://www.ncbi.nlm.nih.gov/books/NBK539805/#:~:text=However%2C%20the%20most%20frequently%20used,beta%20(13%20to%2030Hz) (accessed May.17, 2024).

[13] “Ultracortex Mark III Nova and Supernova: Openbci documentation,” OpenBCI Documentation RSS, https://docs.openbci.com/Deprecated/UltracortexMark3_NovaDep/ (accessed May 18, 2024). 

[14] G. Xavier, A. Su Ting, and N. Fauzan, “Exploratory study of brain waves and corresponding brain regions of fatigue on-call doctors using quantitative electroencephalogram,” OUP Academic, https://doi.org/10.1002/1348-9585.12121 (accessed May 18, 2024). 

[15] Bitalino (r)evolution lab guide, https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide3_EEG.pdf (accessed May. 17, 2024).

[16] A. Deslandes et al., “Effects of Caffeine on Electrophysiological and Neuropsychological Indices after Sleep Deprivation,” Neuropsychobiology, vol. 54, no. 2, pp. 126–133, 2006, doi: https://doi.org/10.1159/000098263.
‌

[17] A. Jain, R. Raja, S. Srivastava, Prakash Chandra Sharma, Jayesh Gangrade, and Manoj R, “Analysis of EEG signals and data acquisition methods: a review,” Computer methods in biomechanics and biomedical engineering. Imaging & visualization, pp. 1–26, Feb. 2024, doi: https://doi.org/10.1080/21681163.2024.2304574.


</details>
