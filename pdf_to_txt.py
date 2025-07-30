#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PyPDF2
import os
import sys

def pdf_to_txt(pdf_path, output_dir="files"):
    """
    Преобразует PDF файл в TXT файл

    Args:
        pdf_path (str): Путь к PDF файлу
        output_dir (str): Папка для сохранения TXT файла
    """
    try:
        # Проверяем существование PDF файла
        if not os.path.exists(pdf_path):
            print(f"Ошибка: Файл {pdf_path} не найден")
            return False

        # Создаем папку output_dir если она не существует
        os.makedirs(output_dir, exist_ok=True)

        # Получаем имя файла без расширения
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        txt_path = os.path.join(output_dir, f"{base_name}.txt")

        print(f"Преобразование {pdf_path} в {txt_path}...")

        # Открываем PDF файл
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Извлекаем текст из всех страниц
            text_content = []
            total_pages = len(pdf_reader.pages)

            for page_num, page in enumerate(pdf_reader.pages, 1):
                print(f"Обработка страницы {page_num}/{total_pages}...")
                text = page.extract_text()
                if text.strip():  # Добавляем только непустые страницы
                    text_content.append(f"\n--- Страница {page_num} ---\n")
                    text_content.append(text)

            # Сохраняем в TXT файл
            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(''.join(text_content))

            print(f"✅ Преобразование завершено! Файл сохранен: {txt_path}")
            return True

    except Exception as e:
        print(f"Ошибка при преобразовании: {str(e)}")
        return False

if __name__ == "__main__":
    # Используем story.pdf по умолчанию, если не указан другой файл
    pdf_file = sys.argv[1] if len(sys.argv) > 1 else "story.pdf"
    pdf_to_txt(pdf_file)