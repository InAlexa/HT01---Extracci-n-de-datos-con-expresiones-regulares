import pandas as pd
import re
from PyPDF2 import PdfReader

rutaArch = "C:\\Users\\danie\\OneDrive\\Escritorio\\compiladores\\Analisis Anual 2018 ETAS.pdf"
documento = PdfReader(rutaArch)
x=len(documento.pages)
pagina = documento.pages[4]
texto = pagina.extract_text()
print(texto)

patron = r'\n(\d+){1,2}\s{1}(\d+){1,2}\s{1}([\s\S]*?(?=  |\d))(?:\s{2})(.*?(?=  ))(?:\s{2})(.*?(?=\d))(\d{1,})'

datos = re.findall(patron, texto)
print(datos)

etas = pd.DataFrame(datos, columns = ['No.', 'SE', 'Área de Salud', 'ETA reportada', 'Fuente de Contagio', 'Número de Casos'])
print(etas)