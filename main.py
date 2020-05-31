from pprint import pprint
def empty_lines(file):                          #Нахождение количества блюд в файле
        a = 1
        for line in file:
                if line.strip() == '':
                        a += 1
        file.seek(0)
        return a

def add_dish(file):                             # Добавление блюда
        dish = file.readline().strip()
        file.readline()     # Убирает количество ингридиентов за ненадобностью
        list_ingrs = []
        cook_book[dish] = []
        for line in file:
                if line.strip() == '':
                        break
                list_ingrs.append(line.strip())
        for ingrs in list_ingrs:
                ingr = ingrs.split('|')
                a = ingr[0]
                a = a.strip()
                b = ingr[1]
                b = b.strip()
                c = ingr[2]
                c = c.strip()
                dict_ingrs = {'ingridient_name' : a, 'quantity' : int(b), 'measure': c}
                cook_book[dish].append(dict_ingrs)


def get_shop_list_by_dishes(dishes, persons):
        ingridients = {}
        for dish in dishes:
                for ingrs in cook_book[dish]:
                        if ingridients.get(ingrs['ingridient_name']) != None:
                                ingridients[ingrs['ingridient_name']]['quantity'] += int(ingrs['quantity']) * persons
                        else:
                                ingridients[ingrs['ingridient_name']] = {'quantity': ingrs['quantity'] * persons, 'measure': ingrs['measure']}

        pprint(f'Список ингридиентов на {persons} человек: {ingridients}')

def create_cook_book():
        for i in range(empty_lines(file_recepts)):
                add_dish(file_recepts)
        pprint(cook_book)

with open('recepts.txt', encoding="utf-8") as file_recepts:
        cook_book = {}
        create_cook_book()
        dishes = ['Фахитос', 'Запеченный картофель']
        get_shop_list_by_dishes(dishes, 2)
