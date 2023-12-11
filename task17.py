from pathlib import Path

dir_path = Path('files')
if dir_path.exists():
    print('Dir exists.')
else:
   dir_path = dir_path.mkdir()

file_path = Path('files/first.txt')
with file_path.open('a') as f:
    f.write('vhvhwgfsv sfdgsgdsw\n')
    f.write('hdgsgsh sdgshg\n')
file_path1 = Path('files/second.txt')
with file_path1.open('a') as f1:
    f1.write('gdgvv fgshgfgwh et w\n')
    f1.write('vdhv bbwgef 35476tfshs \n')
    f1.write('sgvvx gut7623t tf shdf e2 \n')

with open('files/first.txt') as test_file:
    print(test_file.read())

with open('files/second.txt') as test_file1:
    lines = test_file1.readlines()
    for line in lines:
        print(line)
file_path.unlink()
file_path1.unlink()
dir_path.rmdir()