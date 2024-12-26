import csv 
def load_data(file_name):
    data = []
    with open(file_name, "r") as file:
        file.readline()  # Skip header
        for row in file:
            Date, Crop, Region, Production, Price = row.strip().split(',')
            data.append((Date, Crop, Region, float(Production), float(Price)))
    return data

# 1. Total Yield by Crop Type
def total_yield_by_crop(data):
            yield_by_crop = {}
            for row in data:
                crop = row[1]
                        if crop not in yield_by_crop:
                            yield_by_crop[crop] = 0
                yield_by_crop[crop] += row[3]
            return yield_by_crop

# 2. Average Price by Crop Type
def average_price_by_crop(data):
    price_sum = {}
    count = {}
    for row in data:
        crop = row[1]
        if crop not in price_sum:
            price_sum[crop] = 0
            count[crop] = 0
        price_sum[crop] += row[4]
        count[crop] += 1
    average_price = {crop: price_sum[crop] / count[crop] for crop in price_sum}
    return average_price

# 3. Identify High-Yield Crops by Region
def high_yield_crops_by_region(data):
    yield_by_region = {}
    for row in data:
        region = row[2]
        crop = row[1]
        if region not in yield_by_region:
            yield_by_region[region] = {}
        if crop not in yield_by_region[region]:
            yield_by_region[region][crop] = 0
        yield_by_region[region][crop] += row[3]
    high_yield_crops = {}
    for region in yield_by_region:
        max_crop = None
        max_yield = 0
        for crop, yield_value in yield_by_region[region].items():
            if yield_value > max_yield:
                max_yield = yield_value
                max_crop = crop
        high_yield_crops[region] = (max_crop, max_yield)
    return high_yield_crops

# 4. Calculate Total Revenue by Region
def total_revenue_by_region(data):
    revenue_by_region = {}
    for row in data:
        region = row[2]
        revenue = row[3] * row[4]
        if region not in revenue_by_region:
            revenue_by_region[region] = 0
        revenue_by_region[region] += revenue
    return revenue_by_region

# 5. Most Profitable Crop in Each Region
def most_profitable_crop_by_region(data):
    profit_by_region = {}
    for row in data:
        region = row[2]
        crop = row[1]
        revenue = row[3] * row[4]
        if region not in profit_by_region:
            profit_by_region[region] = {}
        if crop not in profit_by_region[region]:
            profit_by_region[region][crop] = 0
        profit_by_region[region][crop] += revenue
    most_profitable = {}
    for region in profit_by_region:
        max_crop = None
        max_profit = 0
        for crop, profit_value in profit_by_region[region].items():
            if profit_value > max_profit:
                max_profit = profit_value
                max_crop = crop
        most_profitable[region] = (max_crop, max_profit)
    return most_profitable

# 6. Region with Highest Total Yield
def region_with_highest_total_yield(data):
    yield_by_region = {}
    for row in data:
        region = row[2]
        if region not in yield_by_region:
            yield_by_region[region] = 0
        yield_by_region[region] += row[3]
    highest_region = max(yield_by_region, key=yield_by_region.get)
    return highest_region, yield_by_region[highest_region]

# 7. Summarize Yearly Production for a Crop
def yearly_production_summary(data, crop_name):
    production_by_year = {}
    for row in data:
        if row[1] == crop_name:
            year = row[0].split('-')[-1]
            if year not in production_by_year:
                production_by_year[year] = 0
            production_by_year[year] += row[3]
    return production_by_year

# 8. Sort Regions by Average Price
def sort_regions_by_average_price(data):
    price_sum = {}
    count = {}
    for row in data:
        region = row[2]
        price = row[4]
        if region not in price_sum:
            price_sum[region] = 0
            count[region] = 0
        price_sum[region] += price
        count[region] += 1
    average_price = {region: price_sum[region] / count[region] for region in price_sum}
    sorted_regions = sorted(average_price.items(), key=lambda x: x[1], reverse=True)
    return sorted_regions

# 9. Add New Crop Data
def add_new_crop_data(data, date, crop, region, production, price): 
    new_entry = (date, crop, region, float(production), float(price))
    data.append(new_entry)
    with open("agri.txt", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_entry)
    return new_entry

# Optional Questions
# 10. Find Highest and Lowest Prices for a Crop
def highest_lowest_prices_for_crop(data, crop_name):
    prices = [row[4] for row in data if row[1] == crop_name]
    return max(prices), min(prices)

# 11. Identify Underperforming Crops
def underperforming_crops(data, yield_threshold):
    yield_by_crop = total_yield_by_crop(data)
    return {crop for crop, total_yield in yield_by_crop.items() if total_yield < yield_threshold}

# Main execution with user menu
file_name = "agri.txt"
agriculture_data = load_data(file_name)
while True:
    print("Menu")
    print("""
    1. Total Yield by Crop Type
    2. Average Price by Crop Type
    3. Identify High-Yield Crops by Region
    4. Calculate Total Revenue by Region
    5. Most Profitable Crop in Each Region
    6. Region with Highest Total Yield
    7. Summarize Yearly Production for a Crop
    8. Sort Regions by Average Price
    9. Add New Crop Data
    10. Find Highest and Lowest Prices for a Crop
    11. Identify Underperforming Crops
    0. Exit
    """)
    choice = int(input("Enter your choice: "))
    if choice == 0:
        print("Exiting...")
        break
    elif choice == 1:
        print(total_yield_by_crop(agriculture_data))
    elif choice == 2:
        print(average_price_by_crop(agriculture_data))
    elif choice == 3:
        print(high_yield_crops_by_region(agriculture_data))
    elif choice == 4:
        print(total_revenue_by_region(agriculture_data))
    elif choice == 5:
        print(most_profitable_crop_by_region(agriculture_data))
    elif choice == 6:
        print(region_with_highest_total_yield(agriculture_data))
    elif choice == 7:
        crop_name = input("Enter crop name: ")
        print(yearly_production_summary(agriculture_data, crop_name))
    elif choice == 8:
        print(sort_regions_by_average_price(agriculture_data))
    elif choice == 9:
        date = input("Enter date: ")
        crop = input("Enter crop: ")
        region = input("Enter region: ")
        production = input("Enter production: ")
        price = input("Enter price: ")
        print(add_new_crop_data(agriculture_data, date, crop, region, production, price))
    elif choice == 10:
        crop_name = input("Enter crop name: ")
        print(highest_lowest_prices_for_crop(agriculture_data, crop_name))
    elif choice == 11:
        threshold = float(input("Enter yield threshold: "))
        print(underperforming_crops(agriculture_data, threshold))
