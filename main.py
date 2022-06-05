# https://www.youtube.com/watch?v=Q0lHb-FCATk
from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path


def pdf_to_mp3(file_path='test.pdf', language='en'):
    """ Процедура для чтения файла pdf и переобразования его в файл mp3
    :param file_path: путь до файла
    :param language: язык для озвучивания
    :return:
    """
    # Проверяем существование файла
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        
        print(f'[+] Original file: {Path(file_path).name}')
        print('[+] Processing...')

        # Читаем файл в двоичном режиме
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
        
            # ###############
            # Читаем файл pdf
            # ###############
            
            pages = [page.extract_text() for page in pdf.pages]  # перебираем все страницы
            text = ''.join(pages)  # склеиваем страницы

            # # 1.1 Пишем текст в файл с переносами строк
            # with open('text1.txt', 'w') as file:
            #     file.write(text)

            # 1.2. Пишем текст в файл без переноса строк            
            text = text.replace('\n', '')  # удаляем переносы строки, чтобы не было пауз в файле mp3

            # with open('text2.txt', 'w') as file:
            #     file.write(text)


            # ################
            # Создаем файл mp3
            # ################
            
            my_audio = gTTS(text=text, lang=language)  # формируем файл            
            file_name = Path(file_path).stem  # получаем имя файла для сохранения
            my_audio.save(f'{file_name}.mp3')

            return f'[+] {file_name}.mp3 saved successfully!\n---Have a good day!---'
    else:
        return 'File not exists, check the file path!'


def main():
    tprint('PDF>>TO>>MP3', font='bulbhead')
    file_path = input("Enter a file's path: ")
    language = input("Choose language for example 'en' or ''ru: ")
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main()
