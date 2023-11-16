import matplotlib.pyplot as plt
import numpy as np
import os
import csv

breakdown_csv = r'C:/Users/qw2/Desktop/Central_Australia_Fire_Mapping/Output_CSVs/Land_Use_Burnt_by_FY.csv'
csv_file = open(breakdown_csv, mode='r', newline='')
reader = csv.reader(csv_file, delimiter=',')

row_count = 0

f_yrs = []
aboriginal_land_data = []
pastoral_land_data = []
parks_land_data = []

for row in reader:
    if row_count > 0:
        fy = row[0]
        f_yrs.append(fy)
        aboriginal_land_pcnt = round(float(row[1]), 1)
        aboriginal_land_data.append(aboriginal_land_pcnt)
        pastoral_land_pcnt = round(float(row[2]), 1)
        pastoral_land_data.append(pastoral_land_pcnt)
        parks_land_pcnt = round(float(row[3]), 1)
        parks_land_data.append(parks_land_pcnt)
    row_count+=1
csv_file.close()
#print(f_yrs)
#print(aboriginal_land_data)
#print(pastoral_land_data)
#print(parks_land_data)
plt.clf()
clr_aboriginal_land = '#fdbf6f'
clr_pastoral_land = '#b2df8a'
clr_parks_land = '#b57c66'

plt.plot(f_yrs, aboriginal_land_data, label='Aboriginal', color=clr_aboriginal_land, linewidth=1.5)
plt.plot(f_yrs, pastoral_land_data, label='Pastoral', color=clr_pastoral_land, linewidth=1.5)
plt.plot(f_yrs, parks_land_data, label='Parks', color=clr_parks_land, linewidth=1.5)

plt.title('Percentage Burnt by Land Tenure 2000-2023')
plt.legend(fontsize=10)
plt.xticks(fontsize=6, rotation=90)
plt.yticks(np.arange(0, 50, step=10), fontsize=12)
plt.gca().yaxis.grid(linestyle='dashed')
#plt.show()
save_path = r'C:/Users/qw2/Desktop/Central_Australia_Fire_Mapping/Output_CSVs/Pcnt_All_FYs.png'
plt.savefig(save_path, dpi=1000, bbox_inches='tight')

print('Done')