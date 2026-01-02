def define_three_most_popular_food_ingredients(data):
    """
    Computes the three most popular ingredients from recipe data.

    Args:
        data (list): List of food recipes.

    Returns:
        list: Top three ingredients with counts as a list of tuples.
    """

    # WRITE YOUR CODE HERE
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

print(define_three_most_popular_food_ingredients(
    [
        [53010, 'Lamb Tzatziki Burgers', 'Greek', 'Bulgur Wheat, Lamb Mince, Cumin, Coriander, Paprika, Garlic, Olive Oil, Bun, Cucumber, Greek Yogurt, Mint'], 
        [52909, 'Tarte Tatin', 'French', 'Puff Pastry, Plain Flour, Braeburn Apples, Caster Sugar, Butter, Creme Fraiche'], 
        [52871, 'Yaki Udon', 'Japanese', 'Udon Noodles, Sesame Seed Oil, Onion, Cabbage, Shiitake Mushrooms, Spring Onions, Mirin, Soy Sauce, Caster Sugar, Worcestershire Sauce'], 
        [52875, 'Chicken Ham and Leek Pie', 'British', 'Chicken Stock, Chicken Breast, Butter, Leek, Garlic, Plain Flour, Milk, White Wine, Double Cream, Ham, Sea Salt, Pepper, Plain Flour, Butter, Free-range Egg, Beaten, Cold Water, Free-range Egg, Beaten'], 
        [53019, 'Pierogi (Polish Dumplings)', 'Polish', 'Butter, Chopped Onion, Sauerkraut, Butter, Chopped Onion, Potatoes, Eggs, Sour Cream, Flour, Salt, Baking Powder']
    ]))
''' Should print:
[('butter', 5), ('plain flour', 3), ('beaten', 2)]
'''

print(define_three_most_popular_food_ingredients(
    [
        [52849, 'Spinach & Ricotta Cannelloni', 'Italian', 'Olive Oil, Garlic, Caster Sugar, Red Wine Vinegar, Chopped Tomatoes, Basil Leaves, Mascarpone, Milk, Parmesan, Mozzarella, Spinach, Parmesan, Ricotta, Nutmeg, Cannellini Beans'], 
        [52924, 'Nanaimo Bars', 'Canadian', 'Custard, Caster Sugar, Cocoa, Egg, Digestive Biscuits, Desiccated Coconut, Almonds, Butter, Double Cream, Custard Powder, Icing Sugar, Dark Chocolate, Butter'], 
        [52838, 'Venetian Duck Ragu', 'Italian', 'Olive Oil, Duck Legs, Onions, Garlic, Cinnamon, Plain Flour, Red Wine, Chopped Tomatoes, Chicken Stock Cube, Rosemary, Bay Leaves, Sugar, Milk, Paccheri Pasta, Parmesan Cheese'], 
        [52987, 'Lasagna Sandwiches', 'American', 'Sour Cream, Chopped Onion, Dried Oregano, Salt, Bread, Bacon, Tomato, Mozzarella, Butter'], 
        [53008, 'Stuffed Lamb Tomatoes', 'Greek', 'Tomatoes, Sugar, Olive Oil, Onion, Garlic Clove, Lamb, Cinnamon, Tomato Puree, Rice, Chicken Stock, Dill, Chopped Parsley, Mint'], 
        [53022, 'Polskie Naleniki (Polish Pancakes)', 'Polish', 'Flour, Eggs, Milk, Water, Salt, Sugar, Butter'], 
        [52765, 'Chicken Enchilada Casserole', 'Mexican', 'Enchilada sauce, shredded Monterey Jack cheese, corn tortillas, chicken breasts']
    ]))
''' Should print:
[('butter', 4), ('milk', 3), ('olive oil', 3)]
'''

print(define_three_most_popular_food_ingredients(
    [
        [52943, 'Oxtail with broad beans', 'Jamaican', 'Oxtail, Onion, Spring Onions, Garlic, Ginger, Scotch Bonnet, Soy Sauce, Fresh Thyme, Vegetable Oil, Water, Broad Beans, Corn Flour, Water'], 
        [52794, 'Vegan Chocolate Cake', 'American', 'self raising flour, coco sugar, cacao, baking powder, flax eggs, almond milk, vanilla, water'], 
        [52920, 'Chicken Marengo', 'French', 'Olive Oil, Mushrooms, Chicken Legs, Passata, Chicken Stock Cube, Black Olives, Parsley'], 
        [52975, 'Tuna and Egg Briks', 'Tunisian', 'Olive Oil, Spring Onions, Spinach, Filo Pastry, Tuna, Eggs, Hotsauce, Tomatoes, Cucumber, Lemon Juice, Apricot Jam'], 
        [52793, 'Sticky Toffee Pudding Ultimate', 'British', 'Medjool dates, water, vanilla extract, self-raising flour, bicarbonate of soda, eggs, butter, demerara sugar, black treacle, milk, ice cream, muscovado sugar, butter, double cream, black treacle'], 
        [52783, 'Rigatoni with fennel sausage sauce', 'Moroccan', 'olive oil, Italian fennel sausages, onion, fennel bulb, smoky paprika, garlic, fennel seeds, red wine, chopped tomatoes, caster sugar, pitted black olives, rigatoni, pecorino, anchovy fillet, garlic, olive oil, basil leaves'], 
        [52884, 'Lancashire hotpot', 'British', 'Butter, Lamb, Lamb Kidney, Onions, Carrots, Plain Flour, Worcestershire Sauce, Chicken Stock, Bay Leaves, Potatoes'], 
        [52896, 'Full English Breakfast', 'British', 'Sausages, Bacon, Mushrooms, Tomatoes, Black Pudding, Eggs, Bread, Baked Beans'], 
        [52949, 'Sweet and Sour Pork', 'Chinese', 'Pork, Egg, Water, Salt, Sugar, Soy Sauce, Starch, Tomato Puree, Vinegar, Coriander'], 
        [52863, 'Vegetarian Casserole', 'British', 'Rapeseed Oil, Onion, Garlic, Paprika, Cumin, Thyme, Carrots, Celery, Red Pepper, Yellow Pepper, Tomato, Vegetable Stock Cube, Courgettes, Thyme, Lentils']
    ]))
''' Should print:
[('water', 5), ('garlic', 4), ('olive oil', 4)]
'''

print(define_three_most_popular_food_ingredients(
    [
        [52845, 'Turkey Meatloaf', 'British', 'Olive Oil, Onion, Garlic, Worcestershire Sauce, Tomato Puree, Turkey Mince, Eggs, Breadcrumbs, Barbeque Sauce, Cannellini Beans, Parsley'], 
        [53025, 'Ful Medames', 'Egyptian', 'Broad Beans, Parsley, Olive Oil, Lemons, Garlic Clove, Cumin'], 
        [52788, 'Christmas Pudding Flapjack', 'British', 'salted butter, dark soft brown sugar, golden syrup, orange, rolled oats, Christmas pudding'], 
        [52902, 'Parkin Cake', 'British', 'Butter, Egg, Milk, Golden Syrup, Black Treacle, Brown Sugar, Oatmeal, Self-raising Flour, Ground Ginger'], 
        [52809, 'Recheado Masala Fish', 'Indian', 'Mackerel, Red Chili, Ginger, Garlic, Pepper, Cumin, Turmeric, Cinnamon stick, Clove, Cardamom, Sugar, Tamarind ball, Vinegar, Oil'], 
        [52930, 'Pate Chinois', 'Canadian', 'Potatoes, Butter, Milk, Minced Beef, Onion, Creamed Corn, Paprika, Parsley, Salt, Pepper'], 
        [52972, 'Tunisian Lamb Soup', 'Tunisian', 'Lamb Mince, Garlic, Onion, Spinach, Tomato Puree, Cumin, Chicken Stock, Harissa Spice, Chickpeas, Lemon Juice, Macaroni, Salt, Pepper'], 
        [52849, 'Spinach & Ricotta Cannelloni', 'Italian', 'Olive Oil, Garlic, Caster Sugar, Red Wine Vinegar, Chopped Tomatoes, Basil Leaves, Mascarpone, Milk, Parmesan, Mozzarella, Spinach, Parmesan, Ricotta, Nutmeg, Cannellini Beans'], 
        [52807, 'Baingan Bharta', 'Indian', 'Aubergine, Onion, Tomatoes, Garlic, Green Chili, Red Chili Powder, Oil, Coriander Leaves, salt'], 
        [52968, 'Mbuzi Choma (Roasted Goat)', 'Kenyan', 'Goat Meat, Corn Flour, Tomatoes, Salt, Onion, Green Chilli, Coriander Leaves'], 
        [52781, 'Irish stew', 'Irish', 'whole wheat, lamb loin chops, olive oil, shallots, carrots, turnips, celeriac, charlotte potatoes, white wine, caster sugar, fresh thyme, oregano, chicken stock'], 
        [52904, 'Beef Bourguignon', 'French', 'Goose Fat, Beef Shin, Bacon, Challots, Chestnut Mushroom, Garlic Clove, Bouquet Garni, Tomato Puree, Red Wine, Celeriac, Olive Oil, Thyme, Rosemary, Bay Leaf, Cardamom'], 
        [52814, 'Thai Green Curry', 'Thai', 'potatoes, green beans, sunflower oil, garlic, Thai green curry paste, coconut milk, Thai fish sauce, Sugar, Chicken, lime, basil, Rice'], 
        [52780, 'Potato Gratin with Chicken', 'Unknown', 'Potatoes, Onions, Olive Oil, Chicken Stock, Creme Fraiche, Parmesan, Chicken Breasts, Bacon, Spinach, Peas'], 
        [52782, 'Lamb tomato and sweet spices', 'Moroccan', 'olive oil, ginger, garlic, tomatoes, lemon juice, caster sugar, vine leaves, fennel bulb, lamb mince, onion, potato, basmati rice, chopped parsley, coriander, lemon juice, garlic, clove, cinnamon, tomatoes'], 
        [52827, 'Massaman Beef curry', 'Thai', 'Peanuts, Coconut cream, Massaman curry paste, Beef, Potatoes, Onion, Lime, Cinnamon stick, Tamarind paste, Brown sugar, Fish Sauce, chilli, Jasmine Rice'], 
        [53009, 'Lamb and Lemon Souvlaki', 'Greek', 'Garlic, Sea Salt, Olive Oil, Lemon, Dill, Lamb Leg, Pita Bread'], 
        [52914, 'Boulangre Potatoes', 'French', 'Onions, Thyme, Olive Oil, Potatoes, Vegetable Stock'], 
        [52887, 'Kedgeree', 'British', 'Smoked Haddock, Bay Leaves, Milk, Eggs, Parsley, Coriander, Vegetable Oil, Onion, Coriander, Curry Powder, Rice'], 
        [52850, 'Chicken Couscous', 'Moroccan', 'Olive Oil, Onion, Chicken Breast, Ginger, Harissa Spice, Dried Apricots, Chickpeas, Couscous, Chicken Stock, Coriander'], 
        [52770, 'Spaghetti Bolognese', 'Italian', 'onions, olive oil, garlic, lean minced beef, mushrooms, dried oregano, tomatoes, hot beef stock, tomato puree, worcestershire sauce, spaghetti, parmesan'], 
        [53008, 'Stuffed Lamb Tomatoes', 'Greek', 'Tomatoes, Sugar, Olive Oil, Onion, Garlic Clove, Lamb, Cinnamon, Tomato Puree, Rice, Chicken Stock, Dill, Chopped Parsley, Mint'], 
        [52775, 'Vegan Lasagna', 'Italian', 'green red lentils, carrot, onion, zucchini, coriander, spinach, lasagne sheets, vegan butter, flour, soya milk, mustard, vinegar'], 
        [52961, 'Budino Di Ricotta', 'Italian', 'Ricotta, Eggs, Flour, Sugar, Cinnamon, Lemons, Dark Rum, Icing Sugar'], 
        [52771, 'Spicy Arrabiata Penne', 'Italian', 'penne rigate, olive oil, garlic, chopped tomatoes, red chile flakes, italian seasoning, basil, Parmigiano-Reggiano'], 
        [52810, 'Osso Buco alla Milanese', 'Italian', 'Veal, Flour, Olive Oil, Butter, Onion, Carrot, Celery, Fennel, Garlic, Orange Zest, Marjoram, Bay Leaf, Dry White Wine, Chicken Stock, Tomatoes, Parsley, Garlic, Lemon Zest'], 
        [52928, 'BeaverTails', 'Canadian', 'Water, Yeast, Sugar, Milk, Butter, Eggs, Salt, Flour, Oil, Lemon, Sugar, Cinnamon'], 
        [52975, 'Tuna and Egg Briks', 'Tunisian', 'Olive Oil, Spring Onions, Spinach, Filo Pastry, Tuna, Eggs, Hotsauce, Tomatoes, Cucumber, Lemon Juice, Apricot Jam'], 
        [52875, 'Chicken Ham and Leek Pie', 'British', 'Chicken Stock, Chicken Breast, Butter, Leek, Garlic, Plain Flour, Milk, White Wine, Double Cream, Ham, Sea Salt, Pepper, Plain Flour, Butter, Free-range Egg, Beaten, Cold Water, Free-range Egg, Beaten'], 
        [52891, 'Blackberry Fool', 'British', 'Hazlenuts, Butter, Caster Sugar, Lemon, Plain Flour, Baking Powder, Blackberrys, Sugar, Caster Sugar, Lemon Juice, Double Cream, Yogurt, Mint'], 
        [52841, 'Creamy Tomato Soup', 'British', 'Olive Oil, Onions, Celery, Carrots, Potatoes, Bay Leaf, Tomato Puree, Sugar, White Vinegar, Chopped Tomatoes, Passata, Vegetable Stock Cube, Whole Milk'], 
        [52859, 'Key Lime Pie', 'American', 'Digestive Biscuits, Butter, Condensed Milk, Egg Yolks, Lime, Double Cream, Icing Sugar, Lime'], 
        [52844, 'Lasagne', 'Italian', 'Olive Oil, Bacon, Onion, Celery, Carrots, Garlic, Minced Beef, Tomato Puree, Chopped Tomatoes, Honey, Lasagne Sheets, Creme Fraiche, Mozzarella Balls, Parmesan Cheese, Basil Leaves'], 
        [52953, 'Shrimp Chow Fun', 'Chinese', 'Rice Stick Noodles, Prawns, Egg, Pepper, Sesame Seed Oil, Cornstarch, Oil, Minced Garlic, Ginger, Onion, Bean Sprouts, Spring Onions, Cooking wine, Oyster Sauce, Sugar, Vinegar, Soy Sauce'], 
        [53024, 'Rogaliki (Polish Croissant Cookies)', 'Polish', 'Butter, Egg Yolks, Cream Cheese, Baking Powder, Flour, Jam'], 
        [52915, 'French Omelette', 'French', 'Eggs, Butter, Parmesan, Tarragon, Parsley, Chives, Gruyre'], 
        [52918, 'Fish Stew with Rouille', 'French', 'Prawns, Olive Oil, Dry White Wine, Fish Stock, Fennel, Onion, Garlic, Potatoes, Orange, Star Anise, Bay Leaf, Harissa Spice, Tomato Puree, Chopped Tomatoes, Mussels, White Fish, Thyme, Bread'], 
        [52765, 'Chicken Enchilada Casserole', 'Mexican', 'Enchilada sauce, shredded Monterey Jack cheese, corn tortillas, chicken breasts'], 
        [52993, 'Honey Balsamic Chicken with Crispy Broccoli & Potatoes', 'American', 'Potatoes, Broccoli, Garlic, Chicken Breast, Balsamic Vinegar, Honey, Chicken Stock, Butter, Vegetable Oil, Olive Oil'], 
        [52872, 'Spanish Tortilla', 'Spanish', 'Onion, Olive Oil, Butter, Potatoes, Garlic, Eggs, Parsley, Baguette, Vine Tomatoes, Olive Oil'], 
        [52907, 'Duck Confit', 'French', 'Sea Salt, Bay Leaf, Garlic, Thyme, Duck Legs, White Wine'], 
        [52936, 'Saltfish and Ackee', 'Jamaican', 'Salt Cod, Ackee, Onion, Paprika, Curry Powder, Jerusalem Artichokes, Hotsauce, Red Pepper, Yellow Pepper, Tomatoes, Salt, Pepper, Self-raising Flour, Suet, Salt, Olive Oil'], 
        [52940, 'Brown Stew Chicken', 'Jamaican', 'Chicken, Tomato, Onions, Garlic Clove, Red Pepper, Carrots, Lime, Thyme, Allspice, Soy Sauce, Cornstarch, Coconut Milk, Vegetable Oil'], 
        [52886, 'Spotted Dick', 'British', 'Self-raising Flour, Salt, Suet, Currants, Caster Sugar, Lemon, Orange, Milk, Custard'], 
        [52959, 'Baked salmon with fennel & tomatoes', 'British', 'Fennel, Parsley, Lemon, Cherry Tomatoes, Olive Oil, Salmon, Black Olives'], 
        [52843, 'Lamb Tagine', 'Moroccan', 'Olive Oil, Onion, Carrots, Lamb Leg, Garlic, Cumin, Ginger, Saffron, Cinnamon, Honey, Apricot, Vegetable Stock Cube, Butternut Squash, Couscous, Parsley'], 
        [52894, 'Battenberg Cake', 'British', 'Butter, Caster Sugar, Self-raising Flour, Almonds, Baking Powder, Eggs, Vanilla Extract, Almond Extract, Butter, Caster Sugar, Self-raising Flour, Almonds, Baking Powder, Eggs, Vanilla Extract, Almond Extract, Pink Food Colouring, Apricot, Marzipan, Icing Sugar'], 
        [52951, "General Tso's Chicken", 'Chinese', 'Chicken Breast, Plain Flour, Egg, Starch, Baking Powder, Salt, Onion Salt, Garlic Powder, Water, Chicken Stock, Duck Sauce, Soy Sauce, Honey, Rice Vinegar, Sesame Seed Oil, Gochujang, Starch, Garlic, Spring Onions, Ginger'], 
        [53026, 'Tamiya', 'Egyptian', 'Broad Beans, Spring Onions, Garlic Clove, Parsley, Cumin, Baking Powder, Cayenne Pepper, Flour, Vegetable Oil'], 
        [52966, 'Chocolate Caramel Crispy', 'British', 'Mars Bar, Butter, Rice Krispies, Milk Chocolate']
    ]))
''' Should print:
[('olive oil', 24), ('garlic', 21), ('onion', 18)]
'''

##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q3.py