def main():
    # u_file = str(input("What is the file? "))
    # u_exct = extractor()
    # u_exct.loadString(u_file)
    # json load test

    data = characteristicsList('backend/characteristics.json')

    # Print all of the data in the category list
    for cat_name, list in data.data.items():
        # name = self.getCategoryItems(j)
        print("Category: " + cat_name)
        for i in range(len(list)):
            print(data.getCharacteristic(cat_name, i))
    print("this is working")


main()