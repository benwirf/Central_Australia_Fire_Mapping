import matplotlib.pyplot as plt
import numpy as np
import os
import csv

output_bar_charts = r'C:/Users/qw2/Desktop/Central_Australia_Fire_Mapping/Output_CSVs/Bar_Charts'

def make_bar_chart(fy, val_list):
    plt.clf()
    y = np.array([round(float(v)) for v in val_list])
    print(y)
    clr_aboriginal_land = '#fdbf6f'
    clr_pastoral_land = '#b2df8a'
    clr_parks_land = '#b57c66'
    colours = [clr_aboriginal_land, clr_pastoral_land, clr_parks_land]
    x = [f'Aboriginal ({round(float(val_list[0]), 1)}%)',
        f'Pastoral ({round(float(val_list[1]), 1)}%)',
        f'Parks ({round(float(val_list[2]), 1)}%)']
    bars = plt.bar(x, y)
    bars[0].set_color(clr_aboriginal_land)
    bars[1].set_color(clr_pastoral_land)
    bars[2].set_color(clr_parks_land)
    plt.ylim(0, 50)
    plt.ylabel('% Burnt')
    plt.title(f"Percentage of Land Tenure Burnt {fy}")
    plt.tight_layout()
    # plt.show()
    chart_name = f'pcnt_burnt_by_land_tenure_{fy}.png'
    save_path = os.path.join(output_bar_charts, chart_name)
    plt.savefig(save_path, dpi=1000, bbox_inches='tight')

# fy = '2000-2001'
# vals = [26.6, 7.8, 7.7]
# make_bar_chart(fy, vals)

breakdown_csv = r'C:/Users/qw2/Desktop/Central_Australia_Fire_Mapping/Output_CSVs/Land_Use_Burnt_by_FY.csv'
csv_file = open(breakdown_csv, mode='r', newline='')
reader = csv.reader(csv_file, delimiter=',')

row_count = 0

for row in reader:
    if row_count > 0:
        fy = row[0]
        vals = row[1:4]
        # print(f'{fy}--{vals}')
        make_bar_chart(fy, vals)
    row_count+=1

csv_file.close()
print('Done')