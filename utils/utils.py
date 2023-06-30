import os

def get_abs_path(relative_path):
    """
    현재 스크립트의 경로를 기반으로 상대 경로의 절대 경로를 반환합니다.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, relative_path)