# 후처리 코드 추가 (p312)
# 학습 완료 모델이 출력하는 것은 텐서 타입의 수치임
# 물체가 감지된 이미지를 작성하는데 물체를 감싸는 테두리, 색, 선두께, 라벨, 글꼴등을 이미지에 붙임

# 이미지에 붙이기 위해서 OpenCV를 이용한다.
# preparation와 preprocess는 코드가 적어서 모듈로 나누어 함수로 할 필요가 없을 수 있음.
import random

import cv2


def make_color(labels):
    """테두리 선의 색을 랜덤으로 결정"""
    colors = [[random.randint(0, 255) for _ in range(3)] for _ in labels]
    color = random.choice(colors)
    return color


def make_line(result_image):
    """테두리 선을 작성"""
    line = round(0.002 * max(result_image.shape[0:2])) + 1
    return line


def draw_lines(c1, c2, result_image, line, color):
    """테두리 선을 덧붙여 씀"""
    cv2.rectangle(result_image, c1, c2, color, thickness=line)


def draw_texts(result_image, line, c1, color, display_txt):
    """검지한 텍스트 라벨을 이미지에 덧붙여 씀"""
    # 텍스트 크기의 취득
    font = max(line - 1, 1)
    t_size = cv2.getTextSize(display_txt, 0, fontScale=line / 3, thickness=font)[0]
    c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3

    # 박싱이 안되어 코드 수정
    # y 좌표 보정 (이미지 위로 벗어나지 않게)
    x1, y1 = c1
    y1 = max(y1, t_size[1] + 5)

    # 좌상단 / 우하단 명확히 지정
    top_left = (x1, y1 - t_size[1] - 5)
    bottom_right = (x1 + t_size[0], y1)

    # 텍스트 박스의 추가
    # cv2.rectangle(result_image, c1, c2, color, -1) 박싱이 안되어 수정
    cv2.rectangle(result_image, top_left, bottom_right, color, -1)

    # 텍스트 라벨 및 텍스트 박스의 가공 박싱이 안되어 수정
    # cv2.putText(
    #     result_image,
    #     display_txt,
    #     (c1[0], c1[1] - 2),
    #     0,
    #     line / 3,
    #     [225, 255, 255],
    #     thickness=font,
    #     lineType=cv2.LINE_AA,
    # )

    cv2.putText(
        result_image,
        display_txt,
        (x1, y1 - 2),
        0,
        line / 3,
        (225, 255, 255),
        thickness=font,
        lineType=cv2.LINE_AA,
    )