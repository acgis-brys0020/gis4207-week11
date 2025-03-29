import arcpy
import os
import time
import sys

#Setup
outpath = r'..\..\..\..\data\outputs\polyline'
if not os.path.exists(outpath):
    os.makedirs(outpath)
arcpy.env.overwriteOutput = True

def main():
        if len(sys.argv) != 3:
            print("Usage:  geom_obj02.py in_txt out_shp")
            sys.exit()
        in_txt = sys.argv[1]
        out_shp = sys.argv[2]
        create_polyline(in_txt, out_shp)

def create_polyline(in_txt, out_shp):    
    sr = arcpy.SpatialReference(4326)
    fc = arcpy.management.CreateFeatureclass(outpath, "poly2.shp", "POLYLINE", spatial_reference= sr)

    with open(in_txt, 'r') as txt, arcpy.da.InsertCursor(fc, "SHAPE@") as cursor:
        import re
        next(txt)
        points = []
        for i in txt:
            i = i.rstrip()
            parts = i.split()
            if len(parts) == 1:  
                linestring = f'LINESTRING ({points})'
                linestring = re.sub("[\[\]'']","", string = linestring)
                polyline = arcpy.FromWKT(linestring, sr)
                cursor.insertRow([polyline])
                points = []
                continue
            else:
                points.append(i)
        polyline = arcpy.FromWKT(linestring, sr)
        cursor.insertRow([polyline])

if __name__ == '__main__':
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(end_time - start_time)