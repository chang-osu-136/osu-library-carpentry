#file = open("SAFI_results.csv")
#
#for line in file:
#    print(line)

with open("SAFI_results.csv") as file:
    file.readline()
    n_grass = 0
    n_mabatipitched = 0
    n_mabatisloping = 0
    unknown = 0
    for line in file:
        roof_type = line.split(",")[18] 
        # index 18: the 19th column is C01_respondent_roof_type
        if roof_type == "grass":
            n_grass = n_grass + 1
        elif roof_type == 'mabatipitched':
            n_mabatipitched += 1
        elif roof_type == 'mabatisloping':
            n_mabatisloping += 1
        else:
            unknown += 1
    print("Grass: ", n_grass, "Pitched: ", n_mabatipitched, 
          "Sloping: ", n_mabatisloping, "Unknown: ", unknown)
