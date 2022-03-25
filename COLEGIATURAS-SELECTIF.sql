--SELECT * FROM platzi.alumnos--

--nombre, apellido, colegiatura--

SELECT nombre, apellido, 
CASE WHEN colegiatura > 2000 THEN 'TIENE UNA COLEGIATURA MAYOR DE 2000'
WHEN colegiatura < 2000 THEN 'APLICA A LA BECA DEBIDO A QUE SU COLEGIATURA ES MENOR DE 2000'
ELSE 'SE DESCONOCE SU ESTADO'
END AS COSTO
FROM platzi.alumnos