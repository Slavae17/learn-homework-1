"""
Домашнее задание №1
Цикл for: Продажи товаров
* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

slovar = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def main(slovar):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    obshee_kol_vo = 0
    kol_vo_vseh = 0
    
    for x in slovar:  
        kol_vo_items_sold = 0   
         
              
        for item in x['items_sold']:     
            kol_vo_items_sold += item  
            srednee_kol_odnogo = round(kol_vo_items_sold / len(x['items_sold']),1)
        
        print(f''' Cуммарное количество продаж для {x['product']} -  {kol_vo_items_sold},  Среднее количество продаж для {x['product']} - {srednee_kol_odnogo}''')
        obshee_kol_vo += kol_vo_items_sold
        kol_vo_vseh += len(x['items_sold'])
        srednee_kol_prod = obshee_kol_vo / kol_vo_vseh
        
    print(f'Cуммарное количество продаж всех товаров  - {obshee_kol_vo} , Cреднее количество продаж всех - {srednee_kol_prod}' )
                      

if __name__ == "__main__":
    main(slovar)

