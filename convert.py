import os

def convert_file(file_path):
    try:
        # Читаем файл в CP1251
        with open(file_path, 'r', encoding='cp1251') as f:
            content = f.read()
        
        # Заменяем Content-Type на UTF-8 (все варианты)
        content = content.replace(
            '<meta http-equiv="Content-Type" content="text/html; charset=windows-1251">',
            '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
        ).replace(
            '<meta charset="windows-1251">',
            '<meta charset="UTF-8">'
        )
        
        # Перезаписываем файл в UTF-8
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Успех: {file_path}")
    
    except Exception as e:
        print(f"Ошибка в {file_path}: {str(e)}")

# Обрабатываем ВСЕ .htm файлы в папке и подпапках
for root, _, files in os.walk('.'):
    for file in files:
        if file.lower().endswith('.htm'):
            convert_file(os.path.join(root, file))
print("Все файлы обработаны!")