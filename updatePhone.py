# Telefonların güncellenmesi / Updating phones
# Adem ÖZİPEK

import logging
import pprint
from lxml import etree
import zeep
import requests
import urllib3
from requests.auth import HTTPBasicAuth

#Değişkenler / Variables
CUCM_SERVER_IP_ADDRESS = "1.1.1.1"
CUCM_AXL_USERNAME = "admin" #Kullanıcı AXL erişim yetkisine sahip olmalı / The user must access the AXL service
CUCM_AXL_PASSWORD = "C1sco123"
#AXLAPI.wsdl ve AXLSoap.xsd dosyalarının CUCM üzerinden indirilip yolunun belirtilmesi gerekiyor.
#Defining path AXLAPI.wsdl and AXLSOAP.xsd files downloaded from CUCM
AXL_WSDL_FILE = "AXLAPI.wsdl"

#Oturum başlatıyoruz. /  Starting session.
session = requests.Session()
#SSL Sertifikası kullanmak istemiyorsanız. / Avoid using an SSL certificate.
session.verify = False
#Güvensiz istekler uyarısını atlamak için / Ignores Insecure request warning.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#Kimlik doğrulama / Authentication
session.auth = requests.auth.HTTPBasicAuth(CUCM_AXL_USERNAME,CUCM_AXL_PASSWORD)
#Hata Ayıklama / Debugging
history = zeep.plugins.HistoryPlugin()
#Zeep client oluşturuyoruz / Create an instance of the zeep.
client = zeep.Client(wsdl=AXL_WSDL_FILE, transport=zeep.Transport(session=session), plugins=[history])
#AXL servisini oluşturuyoruz / Create the AXL service
service = client.create_service('{http://www.cisco.com/AXLAPIService/}AXLAPIBinding',
                                f'https://' + CUCM_SERVER_IP_ADDRESS + ':8443/axl/')

#Güncellenecek telefon bilgileri / Fields to update
update_phone_data = {
    'name' : 'A1B2C3D4B5C6', #Arama kriteri / Search Criteria
    'description': 'Adem SIP Device'
}

#Sorguyu çalıştırıyoruz / Executing query
response = service.updatePhone(**update_phone_data)

#Info seviyesindeki logları görüntülemek için / Setting log severity
logging.getLogger().setLevel(logging.INFO)
#Sonuçlar/Results
logging.info('Sorgu/Query:\n %s', etree.tostring(history.last_sent["envelope"], encoding="unicode", pretty_print=True))
logging.info('Cevap/Response:\n %s', etree.tostring(history.last_received["envelope"], encoding="unicode", pretty_print=True))
logging.info('Biçimlendirilmiş/Parsed:\n %s', pprint.pformat(response))
