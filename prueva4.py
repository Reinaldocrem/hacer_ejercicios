import os
import shutil

# Directorio de origen para el archivo nombres.xlsx
directorio_origen_xlsx = "./compartir_con_gregor"
nombre_archivo_xlsx = "nombres.xlsx"
ruta_origen_xlsx = os.path.join(directorio_origen_xlsx, nombre_archivo_xlsx)

# Renombrar el archivo nombres.xlsx si existe
if os.path.exists(ruta_origen_xlsx):
    nuevo_nombre_xlsx = "nuevo_nombre.xlsx"
    ruta_destino_xlsx = os.path.join(directorio_origen_xlsx, nuevo_nombre_xlsx)
    os.rename(ruta_origen_xlsx, ruta_destino_xlsx)
    print(f"El archivo {nombre_archivo_xlsx} ha sido renombrado a {nuevo_nombre_xlsx} en {directorio_origen_xlsx}.")

    # Copiar el archivo renombrado a la carpeta 'carpetica'
    directorio_destino = "./carpetica"
    if not os.path.exists(directorio_destino):
        os.makedirs(directorio_destino)
    
    ruta_destino_xlsx_carpetica = os.path.join(directorio_destino, nuevo_nombre_xlsx)
    shutil.copy(ruta_destino_xlsx, ruta_destino_xlsx_carpetica)
    print(f"El archivo renombrado ha sido copiado a la carpeta 'carpetica'.")

# Directorio de origen para archivos PDF
directorio_origen_pdf = r"C:\Users\Usuario\Desktop\pd_exc\compartir_con_gregor\ARCHIVOS"

# Renombrar y copiar todos los archivos PDF en el directorio de origen a la carpeta 'carpetica'
for nombre_archivo_pdf in os.listdir(directorio_origen_pdf):
    if nombre_archivo_pdf.lower().endswith(".pdf"):
        nuevo_nombre_pdf = "prefijo_" + nombre_archivo_pdf
        ruta_origen_pdf = os.path.join(directorio_origen_pdf, nombre_archivo_pdf)
        ruta_destino_pdf_carpetica = os.path.join(directorio_destino, nuevo_nombre_pdf)
        
        # Renombrar el archivo PDF
        os.rename(ruta_origen_pdf, ruta_destino_pdf_carpetica)
        print(f"El archivo {nombre_archivo_pdf} ha sido renombrado a {nuevo_nombre_pdf} en {directorio_origen_pdf}.")

        # No es necesario copiar el archivo renombrado a la carpeta 'carpetica' después de renombrarlo
        print(f"El archivo renombrado no necesita ser copiado a la carpeta 'carpetica'.")
