# Ukol: projdete si nize uvedeny kod a doplnte komentare k jednotlivym castem, tak aby bylo jednoznacne, co dane casti delaji (viz prechozi priklady)
# lze vyuzit oficialni napovedu: https://pro.arcgis.com/en/pro-app/latest/arcpy/data-access/searchcursor-class.htm

# nasledne kod upravte tak, aby se kolem bodu vytvarel buffer o velikosti urcene nasledujicim zpusobem:
#   pokud je vyska bodu mensi nez 445, bude buffer siroky 100 m
#   pokud je vyska bodu vetsi nez 445, bude buffer siroky 200 m

import arcpy
arcpy.env.workspace = r"U:\2024-25\GIS_4\automatizace_python\autom_python\zabaged_horni-bezdekov\zabaged_horni-bezdekov.gdb"

in_fc = 'KotovanyBod'

with arcpy.da.SearchCursor(in_fc, ['vyska', 'SHAPE@XY', 'SHAPE@']) as cur:
    for row in cur:
        print(f"XY = {row[1]}Z = {row[0]}")
        arcpy.Buffer_analysis(row[2], f'buff_{int(row[0])}', f"{int(row[0])} Meters")