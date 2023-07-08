# create a list of products as text
prod1 = "PHILIPS_Boiler_HD4646_2020_09_21_C_1"
prod2 = "KENWOOD_KitchenMachine_KVL8300S_2015_09_22_C_3"
prod3 = "BOSCH_Blender_MMB65G5M_2016_05_07_C_3"
prod4 = "WHIRLPOOL_Microwave_MCP345WH_2019_01_15_C_1"
prod5 = "ROSENLEW_Freezer_RPP2330_2017_01_29_C_2"
prod6 = "ELECTROLUX_Fridge_ERF4114AOW_2017_11_07_C_2"
# split each products details
parts1 = prod1.split("_")
parts2 = prod2.split("_")
parts3 = prod3.split("_")
parts4 = prod4.split("_")
parts5 = prod5.split("_")
parts6 = prod6.split("_")
# all products in one places
products = [parts1, parts2, parts3, parts4, parts5, parts6]
# Categories of appliances.
categories = ["Other", "Small electronics", "Appliances", "Blenders"]
# loop all the products
# and print everything
for parts in products:
    parts[7] = int(parts[7])
    c = categories[parts[7] - 1]

    print()
    print(f"Brand:{parts[0]}")
    print(f"Name and model: {parts[2]} ({parts[3]})")
    print(f"Category: {c}")
    print(f"Additin date: {parts[5]}.col{parts[4]}.{parts[5]}")
