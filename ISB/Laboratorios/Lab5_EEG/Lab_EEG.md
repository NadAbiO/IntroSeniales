# Laboratorio 5: Procedimiento de registro EEG

1. [Contexto](#context)
2. [Marco teórico](#marco)
3. [Objetivos](#obj)
4. [Materiales y equipos](#mat)
5. [Procedimiento](#proc)\
     5.1 [Registro de EEG con Bitalino](#regBit)\
     5.2 [Registro de EEG con Ultracortex](#regUlt)
6. [Resultados](#resul)\
     6.1 [Fotos y videos del protocolo seguido](#senal)\
     6.2 [Ploteo de la señal en Python](#plote)\
     6.3 [Archivos](#arch)
7. [Discusión](#conclu)
8. [Referencias](#ref)

## **Contexto** <a name="context"></a>
---
<p align="justify">El electroencefalograma (EEG) es una técnica diagnóstica fundamental en la neurología que permite la medición de la actividad eléctrica del cerebro mediante electrodos situados en el cuero cabelludo. Esta técnica registra los potenciales eléctricos generados por las neuronas cerebrales, proporcionando información crítica sobre la función neuronal y la actividad cerebral [1] </p>

<p align=justify"> El EEG se utiliza ampliamente para investigar y diagnosticar trastornos neurológicos, especialmente en la evaluación de la epilepsia y otros trastornos convulsivos. También es fundamental en el diagnóstico de trastornos del sueño y encefalopatías, así como para la monitorización en cirugías cerebrales y durante la administración de anestesia .</p>

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:741/1*vd7YUOZFzdT7QMu0vcDfIQ.jpeg"  width="300" height="200"> </p>
<em><p align="center">Figura 1. Señales del EEG [2]</p></em> 


## **Marco Teorico** <a name="marco"></a>
<p align="justify"> El electroencefalograma (EEG) es un procedimiento que analiza la actividad eléctrica del cerebro. Esta actividad es generada por la interacción de las neuronas y se manifiesta como señales electroquímicas. Los distintos estados del cerebro indican diversos patrones de ondas cerebrales. Estas ondas cerebrales dan diferentes estados del cerebro como los sentimientos, las emociones, el estado de ánimo o cualquier posición mental.[5]

TIPOS DE ONDAS CEREBRALES CON RANGO DE FRECUENCIAS:

<p align="center"> 
    
| **_Tipos de Frecuencia_** | **_Frecuencia (Hz)_** |Estado del cerebro|
|:---------------------------------------------:|:---------------------:|:------------:|
|                     Delta                     |      0.50 - 4.00      |Dormir|
|                     Theta                     |      4.00 - 8.00      |Relajamiento profundo y enfoque |
|                     Alpha                     | 8.00 - 13.00          |Muy relajado y atento|
|                      Beta                     | 13.00 - 22.00         |Ansioso,activo|
|                     Gamma                     | 22.00 - 30.00         |Concentrado|

</p>

1. **Delta**:
    - Se observa durante el sueño profundo y es prominente en las regiones frontocentrales de la cabeza.
    - En casos de encefalopatía generalizada y disfunción cerebral focal, puede presentarse incluso durante la vigilia.

2. **Theta**:
    - Asociado con somnolencia y las primeras etapas del sueño (N1 y N2).
    - Más prominente en las regiones frontocentrales y reemplaza el ritmo alfa debido a la somnolencia temprana.
    - Estados emocionales elevados también pueden aumentar el ritmo theta frontal.
    - La actividad theta focal durante la vigilia sugiere disfunción cerebral focal.

3. **Alfa**:
    - Característico en registros de EEG normales despiertos en la región occipital.
    - Definitorio del ritmo de fondo en adultos.
    - Persiste hasta la vejez en individuos sanos.
    - Ralentización del alfa puede indicar disfunción cerebral generalizada.

4. **Beta**:
    - Común en adultos y niños normales.
    - Más prominente en regiones frontal y central.
    - Amplitud típica: 10-20 microvoltios.

5. **Gamma**:
    - Ondas de alta frecuencia.
    - Importantes para funciones cognitivas.
    - Pueden ayudar en la detección temprana de desmielinización y otros trastornos corticales.[6]
      
<p align="center"> <img src="https://i0.wp.com/neurodoza.com/wp-content/uploads/2023/05/tipos_de_ondas_cerebrales_6440_600-webp-600%C3%97400-.png?resize=368%2C286&ssl=1" width="60%" /> </p>
<p align="center"> Figura 2. Ondas cerebrales.</p>
   

---

## **Objetivos** <a name="obj"></a>
---
- Capturar señales biomédicas mediante el uso de EEG y configurar correctamente los dispositivos BiTalino y Ultracortex Mark IV.
- Extraer y analizar la información obtenida de estas señales utilizando el software OpenBCI GUI y Open Signal.

### **Materiales y equipos** <a name="mat"></a>
---
|  **Modelo**  | **Descripción** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| (R)EVOLUTION |   Kit BITalino  |       1      |
|       -      |      Ultracortex Mark IV EEG    |       1      |
|       -      |      Electrodos    |       3      |
|       -      |      Cable de 3 derivaciones    |       1      |
|       -      |      Laptop    |       1      |

## **Procedimiento** <a name="proc"></a>
---
### **Registro de EEG con Bitalino** <a name="regBit"></a>
Como referencia para la colocación de los electrodos y buenas prácticas durante la toma de datos utilizamos la guía proporcionada por el mismo sitio web de Bitalino [3]:

<p align="center">
  <img src="https://github.com/NadAbiO/IntroSeniales/blob/main/Anexos/Laboratorios/LabEEG/ReferenciaBitalito.png">
</p> 
<em><p align="center">Figura 3. Posicionamiento de Electrodos en posicion FP1 [3]</p></em>

<p align="center">
  <img width="300" height="400" src="https://github.com/NadAbiO/IntroSeniales/blob/main/Anexos/Laboratorios/LabEEG/BruConexion.jpg">
</p> 
<em><p align="center">Figura 4. Conexion final en Integrante</p></em>

Posterior a la conexion se realizo la toma de medicion utilizando la siguiente metodologia:

1. Registrar una línea base de señal con poco ruido y sin movimientos (respiración normal,sin movimientos oculares/ojos cerrados) 
durante 30 segundos.
2. Repetir un ciclo de OJOS ABIERTOS - OJOS CERRADOS cinco veces, manteniendo ambasfases durante cinco segundos.
3. Registre otra fase de referencia de 30 segundos (paso 1).
4. Un integrante del grupo lea en voz alta una serie de ejercicios matemáticos (verindicaciones abajo) y resolver cada uno de 
ellos mentalmente enfocando la mirada en un punto específico para evitar artefactos.
5. Detener la grabación y guardar los datos

Para el punto 4 se realizaron la siguientes preguntas[4]:

| Categoría           | Ejemplo                                                                                                                                                       |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ejemplo Sencillo    | - Hay 3 pájaros en un árbol; Llegan 7 más. ¿Cuántas aves hay ahora?     |                                                                                      
|                     | - Jonas tiene 5 manzanas y Mary tiene 4. ¿Cuántas manzanas tienen en total?    |                                                                                    
|                     | - Hanna tiene 9 dólares pero gastó 4. ¿Cuántos dólares le quedan?            |                                                                                  
| Ejemplo Complejo    | - John anotó 45 puntos para su equipo; 10 más que José. Marie anotó 13 puntos más que John y Joseph juntos. ¿Cuántos puntos obtuvieron en total?              |
|                     | - El Grupo A tiene 24 estudiantes; 13 menos que el grupo B. El grupo C tiene 12 estudiantes más que los grupos A y B combinados. ¿Cuál es el número total de estudiantes? |
|                     | - Una tienda vendía 21 refrescos por la mañana y 13 más que por la tarde. Por la noche vendió 10 más que por la mañana y por la tarde juntas. ¿Cuántos refrescos se vendieron en total?               |

### **Registro de EEG con Ultracortex** <a name="regUlt"></a>

<p align="justify"> El sistema internacional 10-20 es ampliamente reconocido para describir las posiciones de los electrodos en el cuero cabelludo. Se basa en distancias proporcionales entre puntos clave, como el nasion y el inion. Cada posición se identifica con una letra y un número que describen la ubicación en los lóbulos cerebrales y el hemisferio. Los números impares se refieren al hemisferio izquierdo (en rojo), mientras que los pares al derecho (en azul). La línea media se representa con la letra "z" de cero (en negro).[3]

<div align="center">

| Vista superior | Vista lateral |
|----------|----------|
| <img src="https://github.com/NadAbiO/IntroSeniales/assets/89549012/7363b9c8-fec1-4913-91fe-4202bf97d567" alt="superior" width="200"/> | <img src="https://github.com/NadAbiO/IntroSeniales/assets/89549012/c422a465-c922-477f-9f70-efd335f4fbf5" alt="lateral" width="200"/> |

<em><p align="center">Figura 5. Posicionamiento de Electrodos 10-20 [3]</p></em>

<div align="left">


<p align="center">
  <img width="300" height="400" src="https://github.com/NadAbiO/IntroSeniales/assets/89549012/8db0a778-d73c-43a5-9ec4-5445f65c9cf9">
</p> 
<em><p align="center">Figura 6. Conexión final en Integrante</p></em>


## **Resultados** <a name="resul"></a>
---
### **Fotos y videos del protocolo seguido** <a name="senal"></a>

Los resultados del registro de EEG con el Bitalino fueron los siguientes 
|                 **Paso**                 | **Registro del Bitalino** |
|:------------------------------------------:|:---------:|
|**1. Línea base de señal con poco ruido y sin movimientos** | <video src="https://github.com/NadAbiO/IntroSeniales/assets/89696355/a5db2a9f-8574-4e26-a086-f40897bcbabd">
|**2. Ciclo de OJOS ABIERTOS - OJOS CERRADOS cinco veces** | <video src="https://github.com/NadAbiO/IntroSeniales/assets/89696355/10e379ed-d79f-4410-a6ea-10499f0e65c0">
|**3. Otra fase de referencia** | <video src="https://github.com/NadAbiO/IntroSeniales/assets/89696355/6d01ed8f-d07c-4c07-86b0-509114b743ce"> 
|**4. Serie de ejercicios matemáticos** | <video src="">


Estos pasos se repitieron para el UltraCortex y los resultados fueron los siguientes
|                 **Paso**                 | **Registro del UltraCortex** |
|:------------------------------------------:|:---------:|
|**1. Fase de referencia inicial** | <img width="680" height="460" src="https://github.com/NadAbiO/IntroSeniales/blob/main/Anexos/Laboratorios/LabEEG/ReposoEEg.jpg">
|**2. Ciclo de OJOS ABIERTOS - OJOS CERRADOS cinco veces** | <img src="https://github.com/NadAbiO/IntroSeniales/blob/main/Anexos/Laboratorios/LabEEG/CicloEEg.jpg"> 
|**4. Serie de ejercicios matemáticos** | <video src="https://github.com/NadAbiO/IntroSeniales/assets/89696355/6b05e323-6197-4621-a14b-f3e10a6a1e63">

### **Ploteo de la señal en Python** <a name="plote"></a>
#### Prueba 1 (Bruno Tello)
<p align="center">
  <img width="460" height="300" src="https://github.com/NadAbiO/IntroSeniales/blob/446698ff298e360f24d8ca553e308076eaa7cf19/ISB/Laboratorios/Lab5_EEG/Lab5_EEG/Se%C3%B1ales_EEG/bruno1.png">
</p> 
<em><p align="center">Figura 7. Ojos cerrados</p></em>

#### Prueba 2 (Bruno Tello)
<p align="center">
  <img width="460" height="300" src="https://github.com/NadAbiO/IntroSeniales/blob/446698ff298e360f24d8ca553e308076eaa7cf19/ISB/Laboratorios/Lab5_EEG/Lab5_EEG/Se%C3%B1ales_EEG/bruno2.png">
</p> 
<em><p align="center">Figura 8. Ciclo Ojos cerrados - Ojos abiertos</p></em>

#### Prueba 3 (Bruno Tello)
<p align="center">
  <img width="460" height="300" src="https://github.com/NadAbiO/IntroSeniales/blob/446698ff298e360f24d8ca553e308076eaa7cf19/ISB/Laboratorios/Lab5_EEG/Lab5_EEG/Se%C3%B1ales_EEG/bruno3.png">
</p> 
<em><p align="center">Figura 9. Ojos cerrados </p></em>

#### Prueba 4 (Bruno Tello)
<p align="center">
  <img width="460" height="300" src="https://github.com/NadAbiO/IntroSeniales/blob/446698ff298e360f24d8ca553e308076eaa7cf19/ISB/Laboratorios/Lab5_EEG/Lab5_EEG/Se%C3%B1ales_EEG/bruno4.png">
</p> 
<em><p align="center">Figura 10. Preguntas </p></em>

### **Archivos** <a name="arch"></a>
***
- [Documentos (.txt)](https://github.com/NadAbiO/IntroSeniales/tree/059ca0ee345fdd8a566c558e600a6609b48ffcaf/ISB/Laboratorios/Lab5_EEG/Lab5_EEG/Se%C3%B1ales_EEG)

  **Código para el ploteo de la señal:**
- [Ploteo de la señal (.py)](https://github.com/NadAbiO/IntroSeniales/blob/059ca0ee345fdd8a566c558e600a6609b48ffcaf/ISB/Laboratorios/Lab5_EEG/Lab5_EEG/adq_ECG.py)

***
## **Discusión** <a name="conclu"></a>

## **Referencias** <a name="ref"></a>
---
[1] D. L. Schomer and L. da S. F. Henrique, Niedermeyer’s Electroencephalography: Basic Principles, Clinical Applications, and Related Fields. New York: Oxford University Press, 2018. <br>
[2] S. Liu, “Generating simulated EEG signals and data,” Medium, https://selinnaaliu.medium.com/generating-simulated-eeg-signals-and-data-b755363fcc3 (accessed Apr. 26, 2024). <br>
[3] Bitalino (r)evolution lab guide, https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide3_EEG.pdf (accessed Apr. 26, 2024). <br>
[4] J. M. del R&iacute;o, M. A. Guevara, M. H. Gonz&aacute;lez, R. M. H. Aguirre, and M. A. C. Aguilar, “EEG correlation during the solving of simple and complex logical–mathematical problems - cognitive, affective, & behavioral neuroscience,” SpringerLink, https://link.springer.com/article/10.3758/s13415-019-00703-5/tables/1 (accessed Apr. 26, 2024). <br>
[5] J. M. Kumar and V. K. Mittal, "EEG Data Acquisition System and Analysis of EEG Signals," 2021 2nd International Conference for Emerging Technology (INCET), Belagavi, India, 2021, pp. 1-5, doi: 10.1109/INCET51464.2021.9456431. (accessed Apr. 26, 2024). <br>
[6] C. S. Nayak and A. C. Anilkumar, “EEG Normal Waveforms,” Nih.gov, Jan. 21, 2023. https://www.ncbi.nlm.nih.gov/books/NBK539805/#:~:text=However%2C%20the%20most%20frequently%20used,beta%20(13%20to%2030Hz) (accessed Apr. 26, 2024).<br>

