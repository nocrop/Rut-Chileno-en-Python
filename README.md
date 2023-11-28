# Validador de RUN (Mejor conocido a la Chilena como RUT) en Python


<img align="right" src="https://media.giphy.com/media/ehOmuAGboX837Dx9LR/giphy.gif" width="300"/>

## Descripción
Hola, este pequeño codigo te permite validar si un RUT (Run) (Rol Unico Tributario) chileno es válido. 
El validador no solo comprueba el dígito verificador, sino que también verifica que el número se encuentre dentro de un rango realista para descartar RUTs obviamente falsos.
Esto es super util si quieres añadirlo en algun proyecto para darle un plus de validacion. 

## ¿Comó lo hago funcionar?
El script solicita al usuario que ingrese un RUT. Luego, realiza dos verificaciones:
1. **Formato y Rango**: Verifica que el RUT tenga un formato adecuado y que el número se encuentre dentro de un rango realista (por defecto, de 1.000.000 a 25.000.000).
2. **Dígito Verificador**: Calcula y verifica el dígito verificador según el algoritmo oficial para los RUTs chilenos.

## Requisitos
- Python
- Un editor para ejecutarlo
- Café

## No se requiere instalación adicional de bibliotecas para ejecutar este script. Simplemente clona el repositorio y ejecuta el script principal. 
No necesitas dar creditos, ni nada, pero si puedes dejame un comentario para saber que lo estas usando. 
