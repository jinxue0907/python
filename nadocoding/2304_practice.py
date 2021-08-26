# 11-1 모듈
# import theater_module
# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
# theater_module.price_solider(5) # 5명이서 군인 할인 영와 보러 갔을 때

# import theater_module as mv         # theater_module 이름이 너무 길기 때문에 이름을 대신 mv로 붙여줌
# mv.price(3)
# mv.price_morning(4)
# mv.price_solider(5)

# from theater_module import *          # theater_module의 모든 함수를 가져온다
# price(3)
# price_morning(4)
# price_solider(5)

# from theater_module import price, price_morning     # theater_module의 특정 함수만 가져온다
# price(5)
# price_morning(6)

# from theater_module import price_solider as price       #theater_module에서 price_solider 함수를 가져오는데 별명을 price로 한다
# price(5)

# 11-2 패키지
# import travel.thailand          # import를 사용할 때 맨뒷부분은 항상 모듈 또는 패키만 사용할 수 있다, 함수나 클래스는 x
# trip_to = travel.thailand.TailandPackage()
# trip_to.detail()

# from travel.thailand import TailandPackage      # from에서는 맨 뒷부분에 함수나 클래스를 사용할 수 있다
# trip_to = TailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# 11-3 __all__
# from travel import *
# # trip_to = vietnam.VietnamPackage()
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# 11-5 패키지, 모듈 위치
# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))
