import csv
cones = []

with open('cones.csv', 'w', newline="") as r:
    write_cones=csv.writer(r)

    write_cones.writerow(['cone_id', 'x', 'y', 'color'])
    write_cones.writerow(['0100', '44', '23', 'blue'])
    write_cones.writerow(['0200', '34', '86', 'yellow'])
    write_cones.writerow(['0300', '52', '89', 'blue'])
    write_cones.writerow(['0400', '24', '43', 'blue'])
    write_cones.writerow(['0500', '98', '98', 'yellow'])
    write_cones.writerow(['0600', '34', '43', 'yellow'])

    #write_cones.writerows([['cone_id', 'x', 'y', 'color'],['0100', '44', '23', 'blue'],['0200', '34', '86', 'yellow'],])

with open('cones.csv', 'r') as c:
    r = csv.reader(c)
        
    for row in r:
        if row[0].strip().lower() == "cone_id":
            continue
            
        cone_id = row[0]
        x = float(row[1])
        y = float(row[2])
        color = row[3]
        
        dist = x**2 + y**2
        cones.append((dist, cone_id, x, y, color))

cones.sort()

with open('blue_cones.csv', 'w', newline='') as bc, open('yellow_cones.csv', 'w', newline='') as yc:
    write_blue=csv.writer(bc)
    write_yellow=csv.writer(yc)

    write_blue.writerow(['cone_id', 'x', 'y', 'color'])
    write_yellow.writerow(['cone_id', 'x', 'y', 'color'])

    for row in cones:
        if row[4].strip().lower() == 'blue':
            write_blue.writerow(row[1:])
        elif row[4].strip().lower() == 'yellow':
            write_yellow.writerow(row[1:])


blue_cones_coordinates = []
yellow_cones_coordinates = []

for row in cones:
    if row[4].strip().lower() == 'blue':
        blue_cones_coordinates.append((row[2],row[3]))
    elif row[4].strip().lower() == 'yellow':
        yellow_cones_coordinates.append((row[2],row[3]))

with open('centreline.csv', 'w', newline='') as cl:
    writer = csv.writer(cl)
    writer.writerow(['x', 'y']) 
    
    for bx, by in blue_cones_coordinates:
        
        nearest_yellow = None
        min_dist_sq = float('inf')
        
        for yx, yy in yellow_cones_coordinates:
            dist_sq = (bx - yx)**2 + (by - yy)**2
            
            if dist_sq < min_dist_sq:
                min_dist_sq = dist_sq
                nearest_yellow = (yx, yy)
        
        yx, yy = nearest_yellow
        mid_x = (bx + yx) / 2
        mid_y = (by + yy) / 2
        
        writer.writerow([mid_x, mid_y])