project = QgsProject.instance()
extent_lyr = project.mapLayersByName('Reprojected')[0]# Extent layer reprojected to 9473
aboriginal_lyr = project.mapLayersByName('aboriginal_dissolved')[0]
pastoral_lyr = project.mapLayersByName('pastoral_dissolved')[0]
parks_lyr = project.mapLayersByName('parks_dissolved')[0]

extent_area = sum([ft.geometry().area() for ft in extent_lyr.getFeatures()])
aboriginal_area = sum([ft.geometry().area() for ft in aboriginal_lyr.getFeatures()])
pastoral_area = sum([ft.geometry().area() for ft in pastoral_lyr.getFeatures()])
parks_area = sum([ft.geometry().area() for ft in parks_lyr.getFeatures()])
other_area = extent_area - sum([aboriginal_area, pastoral_area, parks_area])

aboriginal_pcnt = (aboriginal_area/extent_area)*100
pastoral_pcnt = (pastoral_area/extent_area)*100
parks_pcnt = (parks_area/extent_area)*100
other_pcnt = (other_area/extent_area)*100

print(round(aboriginal_pcnt, 1))
print(round(pastoral_pcnt, 1))
print(round(parks_pcnt, 1))
print(round(other_pcnt, 1))

print(f'Checksum: {sum([49.3, 43.4, 1.5, 5.8])}')