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
        print("Usage:  geom_obj01.py in_txt out_shp")
        sys.exit()
    in_txt = sys.argv[1]
    out_shp = sys.argv[2]

    create_polyline(in_txt, out_shp)

def create_polyline(in_txt, out_shp):
    sr = arcpy.SpatialReference(4326)
    fc = arcpy.management.CreateFeatureclass(outpath, out_shp, "POLYLINE", spatial_reference= sr)
    array = arcpy.Array()
    
    with open(in_txt, 'r') as txt, arcpy.da.InsertCursor(fc, "SHAPE@") as cursor:
        next(txt)
        for i in txt:
            i = i.rstrip()
            parts = i.split()
            if len(parts) == 1:
                polyline = arcpy.Polyline(array, sr)
                cursor.insertRow([polyline])
                array = arcpy.Array()
                continue
            else:
                x = float(parts[0])
                y = float(parts[1])
                array.add(arcpy.Point(x, y))
        polyline = arcpy.Polyline(array, sr)
        cursor.insertRow([polyline])
    
if __name__ == '__main__':
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(end_time - start_time)