import os

import csv

output_csv = r'/home/ben/DITT/Central_Australia_Fire_Mapping/Output_CSVs/FY_Fire_Breakdown.csv'
tbl_breakdown = open(output_csv, mode='w', newline='')
writer = csv.writer(tbl_breakdown)
writer.writerow(['Financial Year', 'Aboriginal Land', 'Pastoral Land', 'Parks', 'Other', 'CheckSum'])

aboriginal_land_path = r'/home/ben/DITT/Central_Australia_Fire_Mapping/Land_Use_Layers/Fixed/aboriginal_dissolved.gpkg'
pastoral_land_path = r'/home/ben/DITT/Central_Australia_Fire_Mapping/Land_Use_Layers/Fixed/pastoral_dissolved.gpkg'
parks_path = r'/home/ben/DITT/Central_Australia_Fire_Mapping/Land_Use_Layers/Fixed/parks_dissolved.gpkg'

aboriginal_land_lyr = QgsVectorLayer(aboriginal_land_path, 'aboriginal_land', 'ogr')
pastoral_land_lyr = QgsVectorLayer(pastoral_land_path, 'pastoral_land', 'ogr')
parks_lyr = QgsVectorLayer(parks_path, 'parks_land', 'ogr')

aboriginal_land_feat = [ft for ft in aboriginal_land_lyr.getFeatures()][0]
pastoral_land_feat = [ft for ft in pastoral_land_lyr.getFeatures()][0]
parks_feat = [ft for ft in parks_lyr.getFeatures()][0]

aboriginal_land_geom = aboriginal_land_feat.geometry()
pastoral_land_geom = pastoral_land_feat.geometry()
parks_geom = parks_feat.geometry()


firescars_folder = r'/home/ben/DITT/Central_Australia_Fire_Mapping/Sth_NT_Fire_Scars_by_FY/fixed_again'
f_names = sorted([file.name for file in os.scandir(firescars_folder) if file.name.split('.')[1] == 'gpkg'])
for file_name in f_names:
    # print(file_name)
    lyr_uri = os.path.join(firescars_folder, file_name)
    # print(lyr_uri)
    lyr_name = file_name.split('.')[0].split('_')[1]
    # print(lyr_name)
    print(f'Calculating burnt areas for {lyr_name}')
    fy_fs_lyr = QgsVectorLayer(lyr_uri, lyr_name, 'ogr')
    all_fire_geoms = []
    aboriginal_fire_geoms = []
    pastoral_fire_geoms = []
    parks_fire_geoms = []
    for ft in fy_fs_lyr.getFeatures():
        fire_geom = ft.geometry()
        if not fire_geom.isGeosValid():
            fire_geom = fire_geom.makeValid()
        all_fire_geoms.append(fire_geom)
        aboriginal_fire_geoms.append(fire_geom.intersection(aboriginal_land_geom))
        pastoral_fire_geoms.append(fire_geom.intersection(pastoral_land_geom))
        parks_fire_geoms.append(fire_geom.intersection(parks_geom))
    
    all_fires_area = sum([g.area() for g in all_fire_geoms])
    aboriginal_fires_area = sum([g.area() for g in aboriginal_fire_geoms])
    pastoral_fires_area = sum([g.area() for g in pastoral_fire_geoms])
    parks_fires_area = sum([g.area() for g in parks_fire_geoms])
    other_area = all_fires_area-sum([aboriginal_fires_area, pastoral_fires_area, parks_fires_area])

    aboriginal_pcnt = (aboriginal_fires_area/all_fires_area)*100
    pastoral_pcnt = (pastoral_fires_area/all_fires_area)*100
    parks_pcnt = (parks_fires_area/all_fires_area)*100
    other_pcnt = (other_area/all_fires_area)*100
    checksum = sum([aboriginal_pcnt, pastoral_pcnt, parks_pcnt, other_pcnt])
    # print(f'{lyr_name}---Aboriginal Land: {round(aboriginal_pcnt, 2)}%---Pastoral Land: {round(pastoral_pcnt, 2)}%---Parks: {round(parks_pcnt, 2)}%---Other: {round(other_pcnt, 2)}%')
    writer.writerow([lyr_name,
                    round(aboriginal_pcnt, 2),
                    round(pastoral_pcnt, 2),
                    round(parks_pcnt, 2),
                    round(other_pcnt, 2),
                    round(checksum)])

tbl_breakdown.close()
print('Done')