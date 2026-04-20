# 전처리 코드 추가 (p312)
import torchvision

# torchvision을 이용하여 데이터를 텐서 타입으로 변환
# 텐서 타입은 numpy의 nbarrat 형식 비슷
# 벡터 표현에서 행렬 표현
# 이것을 연산 GPU를 이용하는 것처럼 많은 데이터를 사용해서 계산하기 위한 데이터 타입 중 하나임
# GPU를 이용하지 않지만 PyTorch를 이용한 모델에 대응하기 위함.


def image_to_tensor(image):
    """이미지 데이터를 텐서형의 수치 데이터로 변환"""
    image_tensor = torchvision.transforms.functional.to_tensor(image)
    return image_tensor