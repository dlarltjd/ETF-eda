# 네이버 금융 ETF 데이터 자동 수집 및 스케줄링 안내

## 1. 개요
네이버 금융 ETF 시세 API(`https://finance.naver.com/api/sise/etfItemList.nhn`) 데이터를 **10분 마다** 수집하여 `data/` 폴더에 CSV 파일 형태로 자동 저장하는 스케줄러를 구축하였습니다.

---

## 2. 주요 파일 구성 (상대 경로)
- **`.venv/`**: `uv`로 생성된 파이썬 가상환경
- **`src/app.py`**: 실시간 네이버 금융 ETF 종합 EDA 대시보드 웹 애플리케이션
- **`src/save_etf_data.py`**: 네이버 금융 ETF API에서 시세 및 종목 목록을 가져와 `data/etf_data_YYYYMMDD_HHMMSS.csv` 및 `data/etf_data_latest.csv`로 저장하는 스크립트
- **`src/run_scheduler.py`**: 600초(10분) 간격으로 `src/save_etf_data.py`를 지속 실행하는 백그라운드 스케줄러 프로세스
- **`data/`**: 수집된 CSV 데이터 파일들이 저장되는 디렉토리
- **`docs/`**: 프로젝트 관련 명세서 및 문서가 저장되는 디렉토리

---

## 3. 데이터 저장 형식
- **파일명 형식**: `data/etf_data_YYYYMMDD_HHMMSS.csv` (예: `data/etf_data_20260722_113401.csv`)
- **최신본 파일명**: `data/etf_data_latest.csv` (항상 가장 최근 데이터로 업데이트됨)
- **인코딩**: `utf-8-sig` (Excel 및 파이썬에서 한글 깨짐 없이 정상 호환)
- **수집 데이터 항목**: `itemcode`, `itemname`, `nowVal`, `changeVal`, `changeRate`, `nav`, `marketSum`, `quant`, `amonut`, `collected_at` (수집 일시) 등

---

## 4. 실행 및 스케줄러 상태
1. **백그라운드 스케줄러 (Task ID: `task-71`)**: 백그라운드 프로세스로 `run_scheduler.py 600`이 10분 마다 주기적으로 수집을 진행하고 있습니다.
2. **시스템 Cron 스케줄러 (Task ID: `task-73`)**: `schedule` 도구를 사용하여 매 10분(`*/10 * * * *`)마다 크론 규칙이 등록되어 작동합니다.
