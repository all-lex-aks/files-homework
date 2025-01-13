def read_cook_book():
    cook_book = {}
    with open('recipes.txt', 'r', encoding='utf-8') as f:
       data_list = f.readlines()
    dish_list = []
    for line in data_list:
        if line != "\n":
            if len(line.strip()) > 2 and "|" not in line:
                dish_name = line.strip()
            elif "|" in line:
                dict = {'ingredient_name': list(line.strip().split(" | "))[0],
                        'quantity': int(list(line.strip().split(" | "))[1]),
                        'measure': list(line.strip().split(" | "))[2]}
                dish_list.append(dict)
            else:
                continue
            cook_book[dish_name] = dish_list
        else:
            dish_list = []
    return cook_book

print(read_cook_book())
print()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list_by_dishes = {}
    ingredients_list = []
    quantity_list = []
    quantity_dict = {}
    cook_book = read_cook_book()
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredients_list.append(ingredient['ingredient_name'])
    ingredients_list = list(set(ingredients_list))
    shop_list_by_dishes = dict.fromkeys(ingredients_list)
    for ingredient_name in ingredients_list:
        for dish in dishes:
            for ingredient in cook_book[dish]:
                if ingredient_name == ingredient['ingredient_name']:
                    quantity_list.append([ingredient['ingredient_name'], ingredient['quantity'] * person_count])
    quantity_count = 0
    for ingredient_name in ingredients_list:
        for ingredient_with_quantity in quantity_list:
            if ingredient_name == ingredient_with_quantity[0]:
                quantity_count += ingredient_with_quantity[1]
            else:
                quantity_count
            quantity_dict[ingredient_name] = quantity_count
        quantity_count = 0
    for dish in dishes:
        for ingredient in cook_book[dish]:
            for ingredient_name in ingredients_list:
                if ingredient_name == ingredient['ingredient_name']:
                    shop_list_by_dishes[ingredient_name] = {'measure': ingredient['measure'], 'quantity': quantity_dict[ingredient_name]}
    return shop_list_by_dishes

print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))
print()

def write_file(file_name_1, file_name_2, file_name_3):
    file_1 = file_name_1
    file_2 = file_name_2
    file_3 = file_name_3
    data_list = []
    with open(file_1, 'r', encoding='utf-8') as f:
       data_list=[[int(len(f.readlines())), file_1]]
    with open(file_2, 'r', encoding='utf-8') as f:
       data_list.append([int(len(f.readlines())), file_2])
    with open(file_3, 'r', encoding='utf-8') as f:
       data_list.append([int(len(f.readlines())), file_3])
    sorted_list = sorted(data_list)
    with open('result.txt', 'w', encoding='utf-8') as f:
       f.write('')
    for element in sorted_list:
        with open(element[1], 'r', encoding='utf-8') as f:
            data = f.read()
        with open('result.txt', 'a', encoding='utf-8') as f:
            f.write(element[1])
            f.write('\n')
            f.write(str(element[0]))
            f.write('\n')
            f.write(data)
            f.write('\n')
    return f'Файл result.txt сформирован.'

print(write_file('1.txt', '2.txt', '3.txt'))
print()