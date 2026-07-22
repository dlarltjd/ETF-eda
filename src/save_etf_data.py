"""네이버 금융 ETF 목록 수집 및 CSV 저장 모듈.

이 모듈은 네이버 금융 API에서 국내 ETF 목록 및 시세 정보를 수집하여
지정된 폴더에 타임스탬프 기반 CSV 파일로 저장합니다.
"""

from datetime import datetime
import json
import os
from typing import Any, Dict, List, Optional
import pandas as pd
import requests


def fetch_etf_data() -> List[Dict[str, Any]]:
    """네이버 금융 API에서 ETF 목록 데이터를 요청하여 반환합니다.

    Returns:
        List[Dict[str, Any]]: ETF 항목 정보 목록 (각 항목은 딕셔너리 형태).

    Raises:
        requests.RequestException: HTTP 요청에 실패한 경우 발생.
        ValueError: JSON 응답 파싱 실패 또는 데이터 구조가 예상과 다른 경우 발생.
    """
    url = "https://finance.naver.com/api/sise/etfItemList.nhn?etfType=0&targetColumn=market_sum&sortOrder=desc"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }

    # API HTTP GET 요청 수행
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    # JSON 데이터 파싱
    data: Dict[str, Any] = response.json()

    # 데이터 검증
    if "result" in data and "etfItemList" in data["result"]:
        etf_items: List[Dict[str, Any]] = data["result"]["etfItemList"]
        return etf_items
    else:
        raise ValueError("API 응답 구조에 'etfItemList' 필드가 존재하지 않습니다.")


def save_to_csv(data_list: List[Dict[str, Any]], output_dir: str = "data") -> str:
    """수집된 ETF 데이터 목록을 CSV 파일로 저장합니다.

    Args:
        data_list (List[Dict[str, Any]]): CSV로 저장할 ETF 데이터 딕셔너리 리스트.
        output_dir (str): 저장할 대상 디렉토리 상대 경로. 기본값은 'data'.

    Returns:
        str: 생성된 CSV 파일의 상대 경로.
    """
    # 저장 폴더가 없으면 생성
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    # 현재 시간을 기준으로 파일명 생성 (YYYYMMDD_HHMMSS 형식)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"etf_data_{timestamp}.csv"
    file_path = os.path.join(output_dir, file_name)

    # pandas DataFrame 변환 후 CSV 저장 (한글 깨짐 방지를 위해 utf-8-sig 인코딩 사용)
    df = pd.DataFrame(data_list)

    # 수집 시각 컬럼 추가
    df["collected_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    df.to_csv(file_path, index=False, encoding="utf-8-sig")
    print(f"[{datetime.now()}] ETF 데이터 저장 완료: {file_path} (총 {len(df)}건)")

    # 최신 데이터 파일(latest.csv)로도 업데이트
    latest_path = os.path.join(output_dir, "etf_data_latest.csv")
    df.to_csv(latest_path, index=False, encoding="utf-8-sig")

    return file_path


def main() -> None:
    """ETF 데이터 수집 및 저장 프로세스를 실행하는 메인 함수입니다."""
    try:
        # 데이터 수집
        items = fetch_etf_data()
        # 데이터 저장
        saved_file = save_to_csv(items)
        print(f"성공적으로 데이터를 수집하고 저장했습니다: {saved_file}")
    except Exception as e:
        print(f"데이터 수집 중 오류 발생: {e}")


if __name__ == "__main__":
    main()
