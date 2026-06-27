import csv
from datetime import datetime
from pprint import pprint
from pathlib import Path

EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

csv_path = Path(__file__).parent / "laureates.csv"
if not csv_path.exists():
    raise FileNotFoundError(
        f"Could not find laureates.csv at expected location: {csv_path}\n"
        "If you're running from a different working directory, either run the script from its folder or provide the correct path."
    )

with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

# for laureate in laureates:
#     if laureate["surname"] == "Einstein":
#         pprint(laureate)
#         print("============")
#         year_date = datetime.strptime(laureate["year"], "%Y")
#         born_date = datetime.strptime(laureate["born"], "%Y-%m-%d")
#         print("age", year_date.year - born_date.year)
#         break


for legend in laureates:
    if legend["surname"] == "Curie":
        # pprint(legend)
        # print("============")
        year_date = datetime.strptime(legend["year"], "%Y")
        born_date = datetime.strptime(legend["born"], "%Y-%m-%d")
        #print(legend.keys())
        print(f"The Legend {legend['name']}'s age At the time they won their Nobel Prize is", year_date.year - born_date.year,"\n")
        #break