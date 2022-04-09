# counties_dict = {"Arapahoe":422829, "Denver":463353, "Jefferson":432438}
# for county, voters in counties_dict.items():
#     if county == "Arapahoe":
#         print(county, "County has", voters, "registered voters.")
#     elif county == "Denver":
#         print(county, "County has", voters, "registered voters.")
#     else:
#         print(county, "County has", voters, "registered voters.")

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")


for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")