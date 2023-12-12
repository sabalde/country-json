import json

# Read data from each file
with open('country-by-population.json', 'r') as f1:
    data1 = json.load(f1)

with open('country-by-yearly-average-temperature.json', 'r') as f2:
    data2 = json.load(f2)

with open('country-by-capital-city.json', 'r') as f3:
    data3 = json.load(f3)


with open('country-by-calling-code.json', 'r') as f4:
    data4 = json.load(f4)


with open('country-by-continent.json', 'r') as f5:
    data5 = json.load(f5)


with open('country-by-currency-code.json', 'r') as f6:
    data6 = json.load(f6)


with open('country-by-government-type.json', 'r') as f7:
    data7 = json.load(f7)


with open('country-by-independence-date.json', 'r') as f8:
    data8 = json.load(f8)


with open('country-by-life-expectancy.json', 'r') as f9:
    data9 = json.load(f9)


with open('country-by-population-density.json', 'r') as f10:
    data10 = json.load(f10)


with open('country-by-population.json', 'r') as f11:
    data11 = json.load(f11)


with open('country-by-religion.json', 'r') as f12:
    data12 = json.load(f12)


with open('country-by-surface-area.json', 'r') as f13:
    data13 = json.load(f13)
    

with open('country-by-avg-male-height.json', 'r') as f14:
    data14 = json.load(f14)


# Merge the data
merged_data = []
for item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13 , item14 in zip(data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14):
    merged_item = {
        "country": item1["country"],
        "population": item1["population"],
        "temperature": item2["temperature"],
        "city": item3["city"],
        "calling_code": item4["calling_code"],
        "continent": item5["continent"],
        "currency_code": item6["currency_code"],
        "government": item7["government"],
        "independence": item8["independence"],
        "expectancy": item9["expectancy"],
        "density": item10["density"],
        "population": item11["population"],
        "religion": item12["religion"],
        "area": item13["area"],
        "height": item14["height"]
    }
    merged_data.append(merged_item)

# Write merged data to a new JSON file
with open('countries_merged_data.json', 'w') as merged_file:
    json.dump(merged_data, merged_file, indent=4)




