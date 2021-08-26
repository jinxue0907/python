class TailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
    trip_to = ThailandPackage()
    trip_to.detail()                     # thailand 파일 자체에서 실행 될 때 호출
else:
    print("Thailand 외부에서 모듈 호출")    # practice(외부)에서 thailand 파일을 실행 될 때 호출