'''
Quiz5-1. 모듈이란?
함수 정의나 클래스 등의 파이썬 문장을 담고 있는 파일을 모듈이라 한다.

Quiz5-2. 패키지란?
모듈들을 모아놓은 집합. 하나의 디렉토리에 여러 모듈 파일을 갖다넣은 것을 패키지라 한다.

Quiz5-3. theater_module.py 모듈(파일)의 price 함수를 p학번 라는 이름으로 호출 하도록 import문을 작성하세요
from theater_module import price as p

Quiz5-4. __all__의 역할은?
패키지 안에 포함된 것들 중에서 import 되기를 원하는 것만 공개를 한다

Quiz5-5. 지금 파이썬 파일을 직접실행할 때만 실행되고, 다른 모듈에서 import할 때는 실행되지 않도록 하는 제어문은?
if __name__ == "__main__":

Quiz5-6. travel 패키지(폴더) 안에 vietnam.py 모듈(파일) 안의 ThailandPackage 클래스를 생성하고 detail 함수를 호출하는 < 가 >, < 나 >, < 다 > 에 들어갈 각 방법은?
import travel.vietnam
< 가 >
trip_to = travel.vietnam.TailandPackage()
trip_to.detail()

from travel import vietnam
< 나 >
trip_to = vietnam.TailandPackage()
trip_to.detail()

from travel.vietnam import ThailandPackage
< 다 >
trip_to = TailandPackage()
trip_to.detail()
'''