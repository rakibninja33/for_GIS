# Batch Conversion- GPX to Feature Class

import arcpy

# make sure to put the file path in inverted commas              # 'D:\\z_input'
# make sure to put double slash after output folder link         # 'D:\\z_output\\'


arcpy.env.workspace = input('Input Folder Path: ')
out_folder = input('Output Folder Path: ')

for gps in arcpy.ListFiles():
    outgps = out_folder + arcpy.Describe(gps).baseName + '.shp'
    arcpy.GPXtoFeatures_conversion(gps, outgps)
