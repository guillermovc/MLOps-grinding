# Proyecto Machine Learning con datos de molienda SAG

Este proyecto forma parte de la materia de Machine Learning de la Maestría en Ciencia de Datos de la Universidad de Sonora. Se utilizan los datos de un molino SAG, los cuales fueron escalados.

**Integrantes del equipo**
* Misael Gonzalez Soria
* Guillermo Velazquez Coronado
* Viowio MCD

**¿Que problema se plantea resolver?**

Para optimizar el control del nivel de llenado del molino, las variables controlables actuales necesitan ser complementadas con mediciones de variables externas a través de sensores inteligentes. Esto permitirá evitar que el molino opere con cargas extremadamente bajas o altas, lo que puede comprometer su eficiencia y seguridad.

El objetivo de este trabajo es identificar las relaciones entre estas variables adicionales para determinar los puntos de ajuste ideales. Estos puntos de ajuste asegurarán que el molino mantenga una presión óptima según lo deseado por el operador, mejorando así su rendimiento y prolongando su vida útil.

**¿Porqué es un problema importante para la institución/organización/empresa?**

El adecuado funcionamiento del molino SAG es crucial para la empresa minera debido a su significativo consumo energético. Cualquier mejora en su eficiencia o reducción en su uso se traduce en ahorros significativos para la compañía. Por lo tanto, resolver el problema de control del nivel de llenado del molino no solo optimiza su rendimiento, sino que también impacta directamente en los costos operativos de la minera.

**¿Cuales son las métricas para medir el impacto de la solución una vez obtenida?**

Las métricas para medir el impacto de la solución incluyen el Error Absoluto Medio (MAE), el cual se espera que sea de alrededor de 3 en una escala de datos escalados. Además, se establece un límite de error de 4 como máximo aceptable. Es importante tener en cuenta que estas métricas pueden resultar ambiciosas dada la calidad variable de algunas variables. No obstante, también se considerará positivo si se logra obtener una tendencia clara entre la presión predicha y la presión real.

**¿Que problema de aprendizaje implica resolver?**

El problema de aprendizaje que se está abordando es de regresión. El objetivo es desarrollar un modelo que, a partir de datos históricos de variables de proceso y datos proporcionados por sensores inteligentes, pueda generar una función que mapee estas variables a la presión promedio en el molino SAG.

**¿Qué metricas permiten medir la calidad del modelo de aprendizaje? ¿Cuales son sus valores deseables?**

Las métricas principales para medir la calidad del modelo de aprendizaje son el Error Absoluto Medio (MAE) y el Error Absoluto Medio Puntual (pMAE). En este caso, se enfatiza en el pMAE, buscando no exceder un umbral de error de 4. Es decir, se espera que el error absoluto medio en cada predicción individual no supere el valor de 4.
