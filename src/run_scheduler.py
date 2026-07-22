"""ETF 데이터 지속 수집 스케줄러 모듈.

이 모듈은 지정된 주기(기본 10분 = 600초)로 `save_etf_data.py`의 수집 로직을
지속적으로 반복 실행하는 백그라운드 루프 스케줄러입니다.
"""

from datetime import datetime
import sys
import time
try:
    from src.save_etf_data import main as run_etf_collector
except ImportError:
    from save_etf_data import main as run_etf_collector


def start_scheduler(interval_seconds: int = 600) -> None:
    """지정된 초 간격으로 ETF 수집 함수를 반복 실행합니다.

    Args:
        interval_seconds (int): 수집 주기(초). 기본값은 600초(10분).
    """
    print(f"[{datetime.now()}] ETF 수집 스케줄러 시작 (수집 주기: {interval_seconds}초 / {interval_seconds // 60}분)")

    while True:
        try:
            # ETF 수집 및 CSV 저장 실행
            run_etf_collector()
        except Exception as e:
            # 예외 발생 시 스케줄러가 멈추지 않도록 예외 처리 후 로그 출력
            print(f"[{datetime.now()}] 스케줄러 실행 중 예외 발생: {e}")

        # 지정된 주기(10분 = 600초) 대기
        time.sleep(interval_seconds)


if __name__ == "__main__":
    # 커맨드라인 인자로 수집 주기(초)를 전달받거나 기본 600초(10분) 사용
    interval = 600
    if len(sys.argv) > 1:
        try:
            interval = int(sys.argv[1])
        except ValueError:
            print(f"올바르지 않은 인자입니다. 기본 주기 {interval}초로 설정합니다.")

    start_scheduler(interval_seconds=interval)
