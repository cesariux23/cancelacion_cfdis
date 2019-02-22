import sys
import csv
import requests
import logging

url = 'http://gevportaltimbrado.veracruz.gob.mx/portalTimbrado2017/timbrado/nominas/cfdiNomina12.do'
modo = 'cancelarCfdi'
logger = logging.Logger('catch_all')

try:
    # recupera los parametros

    # rfc emisor
    emisor = sys.argv[1]
     # Token de autorizacion
    jsesssionid = sys.argv[2]
    # nombre del archivo csv
    csv_filename = sys.argv[3]
    with open(csv_filename) as csv_file:
        #Las colimnas deben de estar en el siguente orden:
        #uuid, folio
        cfdis = csv.reader(csv_file)
        headers = {'Content-Type' : 'application/x-www-form-urlencoded'}
        cookies = {'JSESSIONID' : jsesssionid}
        for cfdi in cfdis:
            # Se definen los parametros a utilizar
            uuid = cfdi[0]
            folio = cfdi[1]
            payload = {'modo': modo, 'rfc': emisor, 'uuid': uuid, 'dcFolio': folio}
            #Generando la petición
            r = requests.post(url, data = payload, headers=headers, cookies = cookies)
            print(str(folio) + ': ' + str(r.status_code))
            r.raise_for_status()

except Exception as e: 
    logger.exception('Failed: ' + str(e))
