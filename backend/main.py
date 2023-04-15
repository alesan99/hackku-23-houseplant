import json

class characteristicsList:
    def __init__(self, json_path):
        with open(json_path, 'r') as f:
            self.data = json.load(f)
        self.category_count = len(self.data)

    def getCategoryItems(self, cat_name): # category
        return self.data[cat_name]
    
    def getCategoryLength(self, cat_name):
        return len(self.getCategoryItems(cat_name))

    def getCharacteristic(self, cat_name, i): # category
        category_items = self.getCategoryItems(cat_name)
        return category_items[i]

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