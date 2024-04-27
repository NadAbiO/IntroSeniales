# Laboratorio 5: Procedimiento de registro EEG

1. [Contexto](#context)
2. [Marco teórico](#marco)
3. [Objetivos](#obj)
4. [Materiales y equipos](#mat)
5. [Procedimiento](#proc)<br>
     5.1 [Registro de EEG con Bitalino](#regBit)<br>
     5.2 [Registro de EEG con Ultracortex](#regUlt)<br>
6. [Resultados](#resul)\
     6.1 [Fotos y videos del protocolo seguido](#senal)\
     6.2 [Ploteo de la señal en OpenBCI GUI](#plot)\
     6.3 [Archivos](#arch)\
     6.4 [Ploteo de la señal en Python](#plote)
7. [Conclusiones](#conclu)
8. [Referencias](#ref)

## **Contexto** <a name="context"></a>
---
<p align="justify">El electroencefalograma (EEG) es una técnica diagnóstica fundamental en la neurología que permite la medición de la actividad eléctrica del cerebro mediante electrodos situados en el cuero cabelludo. Esta técnica registra los potenciales eléctricos generados por las neuronas cerebrales, proporcionando información crítica sobre la función neuronal y la actividad cerebral [1] </p>

<p align=justify"> El EEG se utiliza ampliamente para investigar y diagnosticar trastornos neurológicos, especialmente en la evaluación de la epilepsia y otros trastornos convulsivos. También es fundamental en el diagnóstico de trastornos del sueño y encefalopatías, así como para la monitorización en cirugías cerebrales y durante la administración de anestesia .</p>

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:741/1*vd7YUOZFzdT7QMu0vcDfIQ.jpeg"  width="300" height="200"> </p>
<em><p align="center">Figura 1. Señales del EEG [2]</p></em> 


## **Marco Teorico** <a name="marco"></a>
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
<em><p align="center">Figura 2. Posicionamiento de Electrodos en posicion FP1 [3]</p></em>

<p align="center">
  <img width="300" height="400" src="https://github.com/NadAbiO/IntroSeniales/blob/main/Anexos/Laboratorios/LabEEG/BruConexion.jpg">
</p> 
<em><p align="center">Figura 3. Conexion final en Integrante</p></em>

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




## **Referencias** <a name="ref"></a>
---
[1] D. L. Schomer and L. da S. F. Henrique, Niedermeyer’s Electroencephalography: Basic Principles, Clinical Applications, and Related Fields. New York: Oxford University Press, 2018. <br>
[2] S. Liu, “Generating simulated EEG signals and data,” Medium, https://selinnaaliu.medium.com/generating-simulated-eeg-signals-and-data-b755363fcc3 (accessed Apr. 26, 2024). <br>
[3] Bitalino (r)evolution lab guide, https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide3_EEG.pdf (accessed Apr. 26, 2024). <br>
[4] J. M. del R&iacute;o, M. A. Guevara, M. H. Gonz&aacute;lez, R. M. H. Aguirre, and M. A. C. Aguilar, “EEG correlation during the solving of simple and complex logical–mathematical problems - cognitive, affective, & behavioral neuroscience,” SpringerLink, https://link.springer.com/article/10.3758/s13415-019-00703-5/tables/1 (accessed Apr. 26, 2024). 

