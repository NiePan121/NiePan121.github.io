#food item
class food_item:
    def __init__(self,name,calories,protein,carbs,fat):#the unit of calories is kcal, and others' units are all gram.
        self.name=name
        self.calories=calories
        self.protein=protein
        self.carbs=carbs
        self.fat=fat
apple=food_item("Apple",60,0.3,15,0.5)
banana = food_item("Banana", 89, 1.1, 23, 0.3)
orange = food_item("Orange", 47, 0.9, 12, 0.1)
rice = food_item("Rice", 130, 2.7, 28, 0.3)
bread = food_item("Bread", 265, 8, 49, 3)
egg = food_item("Egg", 70, 6, 0.5, 5)
milk = food_item("Milk", 150, 8, 12, 8)
yogurt = food_item("Yogurt", 100, 4, 12, 3)
chicken = food_item("Chicken", 165, 31, 0, 3.6)
beef = food_item("Beef", 250, 26, 0, 15)
chocolate = food_item("Chocolate", 546, 5, 52, 30)
potato_chip = food_item("Potato Chips", 536, 7, 53, 33)
#calculate total nutrition
def calculate_total_nutrition(food_list):
    total_cal=0.0
    total_pro=0.0
    total_car=0.0
    total_fat=0.0
    for food in food_list:
        total_cal = total_cal + food.calories
        total_pro = total_pro + food.protein
        total_car = total_car + food.carbs
        total_fat = total_fat + food.fat
    print("24 Hours Total Nutrition")
    print("Total Calories:", total_cal)
    print("Total Protein:", total_pro)
    print("Total Carbs:", total_car)
    print("Total Fat:", total_fat)
    if total_cal > 2500:
        print("Warning: Calories are too high (exceed 2500 kcal)!")
    if total_fat > 90:
        print("Warning: Fat is too high (exceeds 90 g)!")
#example
if __name__ == "__main__":
    print("\n-----Example -----")
    print("Input Example:apple, egg, milk, chicken, rice")
    daily_food = [apple, egg, milk, chicken, rice]
    calculate_total_nutrition(daily_food)
#user input
    user_input = input("\nPlease enter your own daily food list: ")
    food_list = [eval(name.strip()) for name in user_input.split(",")]
    result = calculate_total_nutrition(food_list)