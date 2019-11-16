import csv

def createTemplate(features, target): 
    temp = []
    for item in features: 
        temp.append(item)
    
    temp.append(target)
    temp.append("Percentage")

    csvData = [temp]

    with open('template.csv', 'w') as csvfile: 
        writer = csv.writer(csvfile)
        writer.writerows(csvData)

    csvfile.close()


createTemplate(['a', 'b', 'c'], 'd')