"""
file operation modes:
1. 'r' -> open text file for reading text
2. 'w' -> open text file for writing text
3. 'a' -> open text file for appending text
3. '+' -> open text file for updating (both reading & writing)
"""

# Writing data into the file
# file = open("some_file.txt", "w")
# try:
#     file.write("this is some data")
# except Exception as e:
#     print(e)
# finally:
#     file.close()

# ------------------------------------------------------------------
# lines = [
#     "Students are learning python",
#     "Yug has given his end semester exams",
#     "Khilav is attending session at ahmedabad branch"
# ]

# with open("somefile.txt", "w") as f:
#     for line in lines:
#         f.write(line)
#         f.write("\n")

# ------------------------------------------------------------------
# with open("somefile.txt", "w") as f:
#     # f.writelines(lines)
#     f.write('\n'.join(lines))

# ------------------------------------------------------------------
# dialogue = "偶然だよ。それに裏が出ても、表が出るまで何度でも投げ続けようと思ってたから"

# with open("anime.txt", "w", encoding="utf-8") as f:
#     f.write(dialogue)

# with open("docs/somefile.txt", 'x') as f:
#     pass

# f.close()
# ------------------------------------------------------------------

# check if the file already exists
# from os.path import exists

# file_exists = exists("anime.txt")
# print(file_exists)

# import os
# print(os.path.exists('anime.txt'))

# from os.path import exists as file_exists
# print(file_exists('docs/somefile.txt'))

# from pathlib import Path

# rasto = Path('anime.txt')
# print(rasto.is_file())
# ------------------------------------------------------------------


# reading data from the file
# ------------------------------------------------------------------

# with open('somefile.txt', 'a') as file:
#     file.write("\nthis is another line of text data")

# with open('somefile.txt', 'r') as file:
#     lines = file.readlines()

# print(lines)
# ------------------------------------------------------------------

# with open('somefile.txt', 'r') as f:
#     contents = f.read()
#     print(contents)
# ------------------------------------------------------------------

# with open('somefile.txt', 'r') as f:
#     [print(line.strip()) for line in f.readlines()]

# ------------------------------------------------------------------

# with open('somefile.txt') as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         print(line.strip())

# ------------------------------------------------------------------

with open('anime_dialogues.txt', encoding='utf-8') as f:
    for line in f:
        print(line.strip())