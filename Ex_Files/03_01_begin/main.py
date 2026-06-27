import csv
from pprint import pprint

# EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'

# EINSTEIN = {
#     "birthplace": "Germany",
#     "name": "Albert",
#     "surname": "Einstein",
#     "born": "1879-03-14",
#     "category": "physics",
#     "motivation": "for his services to Theoretical Physics...",
# }

# with open("laureates.csv", "r") as f:
#     reader = csv.DictReader(f)
#     laureates = list(reader)

# pprint(reader)

# for laureate in laureates:
#     if laureate["surname"] == "Einstein":
#         pprint(laureate)
#         break

with open("laureates.csv", "r") as f:
    file = csv.DictReader(f)
    Legends  = list(file)

Surnames = ["Curie", "Kahneman", "Sen", "Fleming"]
Filtered_list  = [i for i in Legends if i["surname"] in Surnames]

for genius in Legends:
    if genius["surname"] in Filtered_list:
        pprint(genius)
        break
        
pprint(Filtered_list)