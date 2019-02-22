# Cancelación masiva de CDFI´s
Script sencillo hecho en *Python* para realizar cancelaciones masivas de CFDI´s en el Portal de Timbrado para OPDs del Gobierno del Estado de Veracruz.

Este script realiza una petición POST al portal con los datos necesarios para cancelar cada timbre especificado.

# Requerimientos
- Acceso al Portal de Timbrado
- Archivo CSV con los datos de los timbres a cancelar con las siguentes columnas: UUID, Folio. **El archivo deberá ir sin encabezados.**

# AVISO:
---
Los timbres a cancelar deberán estar plenamente identificados, ya que el proceso es **ireversible** en el Portal de Timbrado.
La finalidad de este script es facilitarte el proceso de cancelación.
---


# Pasos
1) Accede al portal de timbrado con tus credenciales.
2) Busca el valor de JSESSIONID en las cookies. (Usar el inspector de elementos de tu navegador favorito)
3) Corre el script en tu consola con los siguentes parametros: *RFCEmisor*, *JSESSIONID*, *nombre de tu archivo*.
  ```
  #ejemplo
  > python .\cancelacion.py OPD000101XXX xxxxxxxxxxxxxxxxxxxxxxxxxxx .\cfdis_a_cancelar.csv
  ```

# Resultado
Si la **JSESSIONID** es valido, aparecerá en consola la lista de Folios seguidos de un **200**, quiere decir que la petición se realizó correctamente.

Si **JSESSIONID** ha expirado, se obtendrá algo parecido a esto:
  ```
  Failed: 401 Client Error: Unauthorized for url: http://gevportaltimbrado.veracruz.gob.mx/portalTimbrado2017/timbrado/nominas/cfdiNomina12.do
  Traceback (most recent call last):
  File ".\cancelacion.py", line 33, in <module>
    r.raise_for_status()
  File "C:\Users\cencarnacion\AppData\Roaming\Python\Python36\site-packages\requests\models.py", line 940, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
  requests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: http://gevportaltimbrado.veracruz.gob.mx/portalTimbrado2017/timbrado/nominas/cfdiNomina12.do
  ```




