class FoodItem:
    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):
        self.name=name
        self.fat=fat
        self.carbs=carbs
        self.protein=protein
    def get_calories(selfself, num_servings):
        calories = ((self.fat*9)+(self.carbs*4)+(self.protein*4)) *num_servings;
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('Fat: {:.2f} g'.format(self.fat))
        print('Carbohydrates: {:.2f} g'.format(self.carbs))
        print('Protein: {:.2f} g'.format(self.protein))

if __name__ == "__main__":
    food_item1 = FoodItem()

    item_name = input("Enter the Item name: ")
    amount_fat = float(input("Enter the Fat Amount: "))
    amount_carbs = float(input("Enter the Carbs Amount: "))
    amount_protein = float(input("Enter the Protein Amount: "))

    food_item2 = FoodItem(item_name,amount_fat,amount_carbs,amount_protein)

    num_servings = float(input('Enter the number of serving: '))

    food_item1.print.info()
    print('Number of calories for {:.2f} serving(s):{:.2f}'.format(num_servings, food_item1.get_calories(num_servings)))

    print()

    food_item2.print.info()
    print('Number of calories for {:.2f} serving(s):{:.2f}'.format(num_servings, food_item2.get_calories(num_servings)))







