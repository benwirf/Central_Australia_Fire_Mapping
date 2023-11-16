lyr = iface.activeLayer()
for ft in lyr.getFeatures():
    print(ft.geometry().area())
    is_problem = False
    if ft.geometry().isEmpty():
        print(f'Geometry for feature {ft.id()} is empty')
        if not is_problem:
            is_problem = True
    if not ft.geometry().isGeosValid():
        print(f'Geometry for feature {ft.id()} is invalid')
        if not is_problem:
            is_problem = True
            
if not is_problem:
    print('There are no problems')
else:
    print('There are GEOMETRY PROBLEMS')