import os

import csv

output_csv = r'/home/ben/DITT/Central_Australia_Fire_Mapping/Output_CSVs/Land_Use_Burnt_by_FY.csv'
tbl_land_use = open(output_csv, mode='w', newline='')
writer = csv.writer(tbl_land_use)
writer.writerow(['Financial Year', '% Aboriginal Land Burnt', '% Pastoral Land Burnt', '% Parks Land Burnt'])

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


firescars_folder = r'/home/ben/DITT/Central_Australia_Fire_Mapping/Sth_NT_Fire_Scars_by_FY/Fixed'
f_names = sorted([file.name for file in os.scandir(firescars_folder) if file.name.split('.')[1] == 'gpkg'])
for file_name in f_names:
    # print(file_name)
    lyr_uri = os.path.join(firescars_folder, file_name)
    # print(lyr_uri)
    lyr_name = file_name.split('.')[0].split('_')[1]
    # print(lyr_name)
    print(f'Calculating burnt areas for {lyr_name}')
    fy_fs_lyr = QgsVectorLayer(lyr_uri, lyr_name, 'ogr')
    ###ABORIGINAL LAND###
    aboriginal_burnt_areas = []
    for ft in fy_fs_lyr.getFeatures():
        fire_on_aboriginal_land = ft.geometry().intersection(aboriginal_land_geom)
        aboriginal_burnt_areas.append(fire_on_aboriginal_land.area())
    total_area_burnt_on_aboriginal_land = sum(aboriginal_burnt_areas)
    pcnt_of_aboriginal_land_burnt = (total_area_burnt_on_aboriginal_land/aboriginal_land_geom.area())*100
    # print(f'{lyr_name}-{round(pcnt_of_aboriginal_land_burnt, 5)}%')
    ###PASTORAL LAND###
    pastoral_burnt_areas = []
    for ft in fy_fs_lyr.getFeatures():
        fire_on_pastoral_land = ft.geometry().intersection(pastoral_land_geom)
        pastoral_burnt_areas.append(fire_on_pastoral_land.area())
    total_area_burnt_on_pastoral_land = sum(pastoral_burnt_areas)
    pcnt_of_pastoral_land_burnt = (total_area_burnt_on_pastoral_land/pastoral_land_geom.area())*100
    # print(f'{lyr_name}-{round(pcnt_of_pastoral_land_burnt, 5)}%')
    ###NATIONAL PARKS###
    parks_burnt_areas = []
    for ft in fy_fs_lyr.getFeatures():
        fire_on_parks_land = ft.geometry().intersection(parks_geom)
        parks_burnt_areas.append(fire_on_parks_land.area())
    total_area_burnt_on_parks_land = sum(parks_burnt_areas)
    pcnt_of_parks_land_burnt = (total_area_burnt_on_parks_land/parks_geom.area())*100
    # print(f'{lyr_name}-{round(pcnt_of_parks_land_burnt, 5)}%')
    writer.writerow([lyr_name, round(pcnt_of_aboriginal_land_burnt, 5), round(pcnt_of_pastoral_land_burnt, 5), round(pcnt_of_parks_land_burnt, 5)])

tbl_land_use.close()
print('Done')
    