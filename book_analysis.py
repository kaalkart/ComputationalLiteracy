import re
with open(r"./Tanizaki_4II.txt", "r", encoding='utf-8') as file:
    text=file.read()
pattern = r"【.*?】|（.*?）|［.*?］|＜.*?＞"
cleaned_text=re.sub(pattern, "", text)
with open(r"./Tanizaki_texts_final.txt", "w", encoding='utf-8') as output_file:
    output_file.write(cleaned_text)