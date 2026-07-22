# 📈 Naver ETF Real-time EDA Dashboard & Data Pipeline

네이버 금융 실시간 ETF API 데이터를 수집하여 20년차 데이터 분석가 관점의 **종합 탐색적 데이터 분석(EDA) 대시보드**를 제공하며, **GitHub Pages** 정적 웹 호스팅 및 **GitHub Actions** 자동 데이터 파이프라인을 구축한 프로젝트입니다.

---

## 🌟 주요 특징 (Key Features)

- **⚡ 0.1초 초고속 정적 웹 대시보드**: 별도의 백엔드 파이썬 서버 없이 **Pure Modern HTML5 + Vanilla JS + Plotly.js** 환경으로 0.1초 만에 즉시 반응형 렌더링됩니다.
- **🔄 CORS 우회 JSONP 동적 수신**: 브라우저에서 CORS 보안 제한 없이 100% 최신 실시간 네이버 ETF 시세 데이터 수신 (네트워크 단절 시 `./data/etf_latest.json` 자동 Fallback).
- **⏱️ 5분 주기 GitHub Actions 데이터 파이프라인**: GitHub Actions 스케줄러가 5분 마다 최신 ETF 시세 데이터를 자동으로 수집하여 `data/` 폴더 내에 저장 및 커밋합니다.
- **📊 8개 다각도 EDA 분석 탭 & 10개+ Plotly 인터랙티브 차트**:
  1. 📌 **개요 & 메타데이터**: 데이터 타입, 유효 데이터 수, 결측 비율, 고유값 메타표
  2. 📊 **기술통계 분석**: 수치형 변수(평균, 표준편차, 사분위수 25/50/75, 최소/최대값) 종합 통계표
  3. 💰 **시가총액 & 거래대금**: Top 15 시가총액/거래대금, Log Scale 산점도
  4. 📈 **수익률 & 등락률**: 일일 등락률 히스토그램, 3개월 수익률 Top/Bottom 8
  5. ⚖️ **NAV & 괴리율**: 괴리율 분포 히스토그램, 절대 괴리율 상위 15개
  6. 🏢 **브랜드 & 카테고리**: 자산운용사별 시가총액 도넛 차트, 카테고리별 거래대금 바 차트
  7. 🔗 **상관관계 & 이상치**: 주요 수치형 변수 상관관계 Heatmap
  8. 📋 **Raw Data 탐색 & CSV 다운로드**: 필터링된 원천 데이터 조회 및 UTF-8 BOM CSV 저장

---

## 📂 프로젝트 구조 (Directory Structure)

```text
ETF-eda/
├── index.html                  # GitHub Pages 정적 EDA 대시보드 (Vanilla JS + Plotly.js)
├── requirements.txt            # 파이썬 의존성 패키지 목록
├── .gitignore                  # Git 무시 항목 설정
├── .github/
│   └── workflows/
│       └── deploy.yml          # 5분 주기 자동 데이터 수집 GitHub Actions 워크플로우
├── src/
│   ├── save_etf_data.py        # 네이버 ETF 데이터 수집 및 data/ 폴더 저장 모듈
│   ├── app.py                  # Streamlit 로컬 대시보드 모듈
│   └── run_scheduler.py        # 로컬 스케줄러 구동 모듈
├── data/
│   ├── etf_latest.json         # 최신 ETF 시세 데이터셋 (JSON)
│   └── etf_data_*.csv          # 타임스탬프 기반 수집 데이터 파일
└── docs/
    └── walkthrough.md          # 프로젝트 구현 및 배포 완료 보고서
```

---

## 🚀 GitHub Pages 배포 가이드 (Deployment)

1. 저장소를 푸시한 후 GitHub 리포지토리의 **Settings** 탭으로 이동합니다.
2. 좌측 메뉴 **Pages** 선택 후 **Build and deployment**의 Source를 `Deploy from a branch`로 설정합니다.
3. Branch를 `main` 및 `/ (root)` 폴더로 지정하고 **Save** 버튼을 누릅니다.
4. 약 1~2분 뒤 생성되는 `https://<username>.github.io/ETF-eda/` URL을 통해 정적 EDA 대시보드에 접근할 수 있습니다.
