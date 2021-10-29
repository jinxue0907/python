# 파이썬 객체 그대로 저장하자
import pickle

class Person:
    def __init__(self, name, music):
        self.name = name
        self.music = music

    def __str__(self):
        return f'이름: {self.name}\t나이: {self.music}'

if __name__ == '__main__':
    번호1 = Person('공도윤', '곰세마리')
    번호4 = Person('김설', 'stay(저스틴비버)')
    절친 = [번호1, 번호4]

with open('object.bin', 'wb') as f:
    pickle.dump(절친, f)
with open('object.bin', 'wb') as f:
    data = pickle.load(f)
print(f'load한 데이터: {data}')