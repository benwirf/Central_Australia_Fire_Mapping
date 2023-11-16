import os

folder_path = r'/home/ben/DITT/Central_Australia_Fire_Mapping/Sth_NT_Fire_Scars_by_FY/Fixed'
save_path = r'/home/ben/DITT/Central_Australia_Fire_Mapping/Sth_NT_Fire_Scars_by_FY/fixed_again'

for file in os.scandir(folder_path):
    # print(file.name)
    if file.name.split('.')[1] == 'gpkg':
        in_path = os.path.join(folder_path, file.name)
        lyr_name = file.name.split('.')[0]
        out_path = os.path.join(save_path, f'{lyr_name}.gpkg')
        params = {'INPUT':in_path,
                'OUTPUT':out_path}
        processing.run('native:fixgeometries', params)

print('Done')