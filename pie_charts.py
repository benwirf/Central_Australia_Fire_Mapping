import matplotlib.pyplot as plt
import numpy as np
import os
import csv

output_pie_charts = r'Central_Australia_Fire_Mapping/Output_CSVs/Pie_Charts/JPEGS'

def make_pie_chart(fy, val_list):
    plt.clf()
    y = np.array(val_list)
    clr_aboriginal_land = '#fdbf6f'
    clr_pastoral_land = '#b2df8a'
    clr_parks_land = '#b57c66'
    clr_other_land = '#fbd8fe'
    colours = [clr_aboriginal_land, clr_pastoral_land, clr_parks_land, clr_other_land]
    lbls = [f'Aboriginal ({val_list[0]}%)', f'Pastoral ({val_list[1]}%)', f'Parks ({val_list[2]}%)', f'Other ({val_list[3]}%)']
    patches, texts = plt.pie(y, colors = colours)
    plt.title(f"Central Australian Fires by Land Tenure {fy}")
    plt.legend(patches, lbls, bbox_to_anchor=[0, 0, 0.2, 0.2], loc='lower right')
    plt.tight_layout()
    chart_name = f'land_tenure_breakdown_{fy}.jpg'
    save_path = os.path.join(output_pie_charts, chart_name)
    plt.savefig(save_path, dpi=1000, bbox_inches='tight')

# fy = '2000-2001'
# vals = [71.64, 18.55, 0.63, 9.19]
# make_pie_chart(fy, vals)

breakdown_csv = r'Central_Australia_Fire_Mapping/Output_CSVs/FY_Fire_Breakdown.csv'
csv_file = open(breakdown_csv, mode='r', newline='')
reader = csv.reader(csv_file, delimiter=',')

row_count = 0

for row in reader:
    if row_count > 0:
        fy = row[0]
        vals = row[1:5]
        # print(f'{fy}--{vals}')
        make_pie_chart(fy, vals)
    row_count+=1

csv_file.close()
print('Done')
