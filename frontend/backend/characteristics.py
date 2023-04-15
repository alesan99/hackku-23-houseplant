import json

class characteristicsList:
    def __init__(self, json_path):
        with open(json_path, 'r') as f:
            self.data = json.load(f)
        self.category_count = len(self.data)
        self.categories = []
        for cat_name, list in self.data.items():
            self.categories.append(cat_name)

    def getCategoryItems(self, cat_name): # category
        return self.data[cat_name]
    
    def getCategoryLength(self, cat_name):
        return len(self.getCategoryItems(cat_name))

    def getCharacteristic(self, cat_name, i): # category
        category_items = self.getCategoryItems(cat_name)
        return category_items[i]
