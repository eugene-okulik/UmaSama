PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_list = {item.split()[0]: int(item.split()[1].rstrip('р'))
            for item in PRICE_LIST.strip().split('\n')}

print(new_list)
