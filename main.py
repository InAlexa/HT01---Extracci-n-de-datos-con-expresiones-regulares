import pandas as pd
import re
from PyPDF2 import PdfReader

rutaArch = "C:\\Users\\danie\\OlsneDrive\\Escritorio\\compiladores\\Analisis Anual 2018 ETAS.pdf"
documento = PdfReader(rutaArch)
x=len(documento.pages)
pagina = documento.pages[4]
texto = pagina.extract_text()
print(texto)

"""
patron = r'\n(\w+\s*\w+\s*\w*)\s+(\d+)\s+(\d+.\d+)\s+(\d+)\s+(\d+.\d+)'

datos = re.findall(patron, texto)
print(datos)

etas = pd.DataFrame(datos, columns = ['No.', 'SE','Área de Salud, 'ETA reportada', 'Tasas 2018'])
print(etas)"""