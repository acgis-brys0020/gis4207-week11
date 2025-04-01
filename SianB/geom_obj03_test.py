import geom_obj03 as g3
import os

def test_get_stop_id_to_da_data(capsys):
    stops_workspace = r'..\..\..\..\data\Stops'
    stop_name = "GLADSTONE"
    stop_id_fc = os.path.join(stops_workspace,'Stops_UTM.shp')
    dissemination_area_fc = r'..\..\..\..\data\OttawaDA_UTM\OttawaDA_UTM.shp'
    da_population_field = "POP_2016"
    
    g3.get_stop_id_to_da_data(stops_workspace, stop_name, stop_id_fc, dissemination_area_fc,da_population_field)
    captured = capsys.readouterr()
    assert len(captured.out.split('\n')) == 152