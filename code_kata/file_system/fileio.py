'''
file I/O
'''

import os
sample_file_name = 'sample.txt'
sample_text_file = os.path.join( os.path.dirname(os.path.realpath(__file__)), sample_file_name )

'''
파일객체 = open(파일이름, 파일모드)         # 파일 열기
파일객체.close()                       # 파일 객체 닫기
 
with open(파일이름, 파일모드) as 파일객체:    # 파일을 사용한 뒤 자동으로 파일 객체를 닫아줌
    코드
'''
with open(sample_text_file, 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    s = file.read()                     # 파일에서 문자열 읽기
    print(s)                            # Hello, world!


'''
# file read
'''
print("# readline으로 파일의 내용 읽기")
with open(sample_text_file, 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    lines = file.readlines()
    print(lines)

print("# readline으로 파일의 내용을 줄 단위로 읽기")
with open(sample_text_file, 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    line = None    # 변수 line을 None으로 초기화
    while line != '':
        line = file.readline()
        print(line.strip('\n'))    # 파일에서 읽어온 문자열에서 \n 삭제하여 출력

print("# for 반복문으로 파일의 내용을 줄 단위로 읽기")
with open(sample_text_file, 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    for line in file:    # for에 파일 객체를 지정하면 파일의 내용을 한 줄씩 읽어서 변수에 저장함
        print(line.strip('\n'))    # 파일에서 읽어온 문자열에서 \n 삭제하여 출력

'''
# 파일 객체는 이터레이터

파일 객체는 이터레이터이다.
따라서 변수 여러 개에 저장하는 언패킹(unpacking)도 가능하다.
'''

'''
# with-statement

https://docs.python.org/3/reference/compound_stmts.html#the-with-statement

with A() as a, B() as b:
    SUITE

is semantically equivalent to:

with A() as a:
    with B() as b:
        SUITE

with (
    A() as a,
    B() as b,
):
    SUITE

def test():
    with open("input.txt") as fi, open("output.txt") as fo:
        data = fi.read()
        # do something
'''