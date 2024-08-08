import os
import mojimoji

from scraping_course import get_courses

LECUTURE_NUM = 15
LECUTURE_MATERIALS = '講義資料'
DIR_PATH = "３年前期"

def create_lecuture_dir(dir_path, dir_name):
    dir = os.path.join(dir_path, dir_name)
    if not os.path.exists(dir):
        
        os.makedirs(dir)
    

                
def make_lecture_dirs(dir_path):
    
    courses = get_courses()
    
    for course in courses:
        create_lecuture_dir(dir_path, course)

    dirlist = []
    
    dirs = os.listdir(dir_path)



    for dirname in dirs:
        if os.path.isdir(os.path.join(dir_path, dirname)):
            dirlist.append(dirname)


    for dir in dirlist:
        dir = os.path.join(dir_path, dir)
        if not os.path.exists(os.path.join(dir, LECUTURE_MATERIALS)):

            create_lecuture_dir(dir, LECUTURE_MATERIALS)
            
            for i in range(1, LECUTURE_NUM + 1):
                dir_name = f"第{mojimoji.han_to_zen(str(i))}回"
                create_lecuture_dir(dir, dir_name)
                create_lecuture_dir(os.path.join(dir, LECUTURE_MATERIALS), dir_name)
            
    print("完了しました。")
    

if __name__ == "__main__":
    make_lecture_dirs(DIR_PATH)