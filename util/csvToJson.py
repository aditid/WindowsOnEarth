import csv

approvedTags = [
    'Atmosphere',
    'Clouds',
    'Day',
    'Night',
    'Hurricane',
    'Movie',
    'Inside ISS',
    'ISS Structure',
    'Sunrise Sunset',
    'Dragon',
    'Dock Undock',
    'Cupola',
    'Moon',
    'Spacewalk',
    'Spacecraft',
    'Glacier',
    'Surface',
    'Cities',
    'Soyuz',
    'Aurora',
    'Volcano',
    'Surface',
    'Rivers'
]

unapprovedTags = [
    '',
    '#EarthPhoto',
    '#WinEarthFavs',
    'Astronaut Favs',
    'BUSpark',
    'ISS Astronauts Photograph Earth',
    'Richard Garriott',
    'Windows on Earth',
    '#EarthArt',
    'C Panoramic',
    'Maine',
    'North America',
    'Portsmouth',
    'United States',
    'geo',
    'Irma',
    '#Astronaut',
    '#ISS',
    'Reid Wiseman tweet',
    'Partners',
    'SSASummer2014',
    '#CASIS ISS Conf',
    'C Panoramic Fav',
    'Africa',
    'Morocco',
    'Mystery images',
    'WinEarthTweet',
    'Florida',
    'Florida Keys',
    'National Parks'
]

def removeUnhelpfulTags(tags):
    imageTags = []
    for tag in approvedTags:
        if tag in tags:
            imageTags.append(tag)
    return imageTags

def removeUnapprovedTags(tags):
    imageTags = []
    for tag in tags:
        if tag not in unapprovedTags:
            imageTags.append(tag)
    return imageTags

imageTags = {}
tagImages = {}
file = open('tags.csv', "r")
reader = csv.reader(file)
for row in reader:
    tags = removeUnhelpfulTags(row)
    if len(tags) > 1:
        tags.pop(0)
        imageName = row[0]
        imageTags[imageName] = tags
        for tag in tags:
            if tagImages.get(tag,None) is None:
                tagImages[tag] = []
            tagImages[tag].append(imageName)
print(tagImages)
