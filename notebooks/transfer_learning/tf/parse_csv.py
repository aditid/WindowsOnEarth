import csv
import os

tags_map = {
    'Aurora': 'aurora',
    # 'Agriculture': 'agriculture',
    # 'BadBlankBlurry': 'bad_blank_blurry',
    'Clouds': 'clouds',
    'Cupola': 'cupola',
    'Day': 'day',
    # 'Deployed satellite': 'deployed_satellite',
    # 'Deployer': 'deployer',
    'Dock Undock': 'dock',
    # 'Glacier': 'glacier',
    # 'Glint': 'glint',
    # 'Harvey': 'harvey',
    'Hurricane': 'hurricane',
    # 'Inside ISS': 'inside',
    # 'Lake Balaton': 'lake_balaton',
    'Moon': 'moon',
    # 'Mt. Rainier': 'rainier',
    'Night': 'night',
    # 'Richat Structure': 'richat',
    # 'San Francisco': 'san_francisco',
    'Solar Panels': 'solar_panels',
    # 'Solar Eclipse': 'eclipse',
    'ISS Structure': 'structure',
    'Stars': 'stars',
    'Sunrise': 'sunrise',
    'Volcano': 'volcano',
    # 'Window': 'window',
    # 'Winnipeg': 'winnipeg',
}

with open('H:\BU10000Set.csv', newline='') as csvfile:
    tags = csv.reader(csvfile)
    for row in tags:
        with open(os.path.join('H:', 'BU10000SetA', 'multi_label_images', row[0] + '.txt'), 'w') as f:
            c = [tags_map[item.strip()] if item.strip() in tags_map else 'unknown' for item in row[1:]]
            f.write('\n'.join(c))
