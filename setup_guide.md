# Настройка manimlib
1. `pip3 install manimlib`
2. Добавить в папку _manimlib_ файл __russian_tex_template.tex__, чтоб компилировать тех с русскими символами
3. Добавить в файл __constants.py__ строчки <br/>
   ```python
   language = 'russian'
   if language == 'english':
       tex_template = "tex_template.tex"
   if language == 'russian':
       tex_template = "russian_tex_template.tex"
   ```
   чтобы выбирался нужный template
3. Добавить в папку _manimlib_ файл __\_\_main\_\_.py__ с тем же содержанием, что и __\_\_init\_\_.py__, чтобы запускать библиотеку как модуль в PyCharm-e
4. Run configuration parameters:<br/>
    ```
    [Scene_name]
    --video_dir
    /home/user/PycharmProjects/[your_project_name]/videos
    --tex_dir
    /home/user/PycharmProjects/[your_project_name]/Tex
    ```
5. Interpreter options: `-m manimlib`
