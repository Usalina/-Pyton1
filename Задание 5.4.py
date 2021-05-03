from translate import Translator

f_obj = open('new_file1.txt', 'w')

with open('file_4.txt') as f:
    for line in f:
        translator = Translator(form_lang="English", to_lang="Russian")
        translation = translator.translate(line)
        f_obj.write(translation)
        f_obj.write('\n')
        print(translation)

f_obj.close()
