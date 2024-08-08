import os
import pypdf
from datetime import datetime, timedelta


os.chdir(os.path.dirname(__file__))
# ルートディレクトリの設定
root_directory = './３年前期'

original_password = ['qC5QXHGs']
# 試行するパスワードリスト


start_date = datetime(2022, 4, 1)
end_date = datetime(2026, 4, 1)
passwords = [(start_date + timedelta(days=x)).strftime('%Y%m%d')
             for x in range((end_date - start_date).days + 1)]
passwords.append(*original_password)


def try_password(pdf_path, passwords):
    reader = pypdf.PdfReader(pdf_path)
    if not reader.is_encrypted:
        return None  # PDFが暗号化されていない場合はパスワード不要

    for password in passwords:
        try:
            if (reader.decrypt(password) > 0):
                return password
        except:
            continue
    return None


# 各講義ディレクトリを探索
for lecture in os.listdir(root_directory):
    lecture_path = os.path.join(root_directory, lecture)
    if os.path.isdir(lecture_path):
        print(lecture)
        lecture_materials_path = os.path.join(lecture_path, '講義資料')
        if os.path.isdir(lecture_materials_path):
            output_file = os.path.join(lecture_materials_path, 'password.txt')
            with open(output_file, 'w', encoding='utf-8') as f:
                # 各回の講義資料ディレクトリを探索

                for item in sorted(os.listdir(lecture_materials_path), key=lambda x: int(x[1:-1]) if x.startswith('第') and x.endswith('回') and x[1:-1].isdigit() else float('inf')):
                    item_path = os.path.join(lecture_materials_path, item)
                    if os.path.isdir(item_path) and item.startswith('第') and item.endswith('回'):
                        for filename in os.listdir(item_path):
                            if filename.endswith('.pdf'):
                                pdf_path = os.path.join(item_path, filename)
                                password = try_password(pdf_path, passwords)
                                if password:
                                    f.write(f'{item}：{password}\n')
                                    print(f'{item}の講義資料に対するパスワード：{password}')
