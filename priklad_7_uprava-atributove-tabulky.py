# Ukol: projdete si nize uvedeny kod
# S jeho vyuzitim nasledne napiste jednoduchy skript, ktery doplni do vrstvy kotovanych bodu v databazi zabaged_horni-bezdekov.gdb nove pole "vyska_kategorie"
# toto pole bude vyplneno podle vysky bodu:
    # mensi nez 410 - hodnota atributu bude 1
    # 410 - 450 - hodnota atributu bude 2
    # vice nez 450 - hodnota atributu bude 3

import arcpy

fc = 'c:/data/base.gdb/well'
fields = ['WELL_YIELD', 'WELL_CLASS']

# Create update cursor for feature class 
with arcpy.da.UpdateCursor(fc, fields) as cursor:
    # For each row, evaluate the WELL_YIELD value (index position 
    # of 0), and update WELL_CLASS (index position of 1)
    for row in cursor:
        if (row[0] >= 0 and row[0] <= 10):
            row[1] = 1
        elif (row[0] > 10 and row[0] <= 20):
            row[1] = 2
        elif (row[0] > 20 and row[0] <= 30):
            row[1] = 3
        elif (row[0] > 30):
            row[1] = 4

        # Update the cursor with the updated list
        cursor.updateRow(row)