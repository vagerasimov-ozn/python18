# сегодня мы с вами попробуем выступить в роли детектива
# у нас есть множество людей, которые пользуется машиной той же марки, которую пользуется убийца
# есть множество людей, которые живут недалеко от мест преступления
# и множество людей, у которых и работа недалеко от мест преступления

#имена обычно значения неуникальные, но предплоложим, это были бы номер соц страховок
shevrole_owner = {'sam', 'edit', 'semen', 'petr'}

work_near = {'konstantin', 'vladislav', 'sam', 'petr', 'edit'}

live_near = {'john', 'vladislav', 'olga', 'mike', 'grant', 'covid', 'bilbo' }

#  д/з объединить множество людей, которые живут и работают рядом
# вывести множество людей, которые и владеют авто нужной марки, и живут и работают рядом

new_set = {}
    input = live_near | work_near


# new_mnog = ['petr','semen','sasha']
# new_mnog = set(new_mnog)
# print(new_mnog)