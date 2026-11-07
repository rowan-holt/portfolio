# 서울 호텔 판정 (MVP)

주소: https://rowan-holt.github.io/portfolio/ (zh-TW) · 검토용 한국어: /ko/

빌드 도구 없는 정적 사이트. `data/hotels.json` 하나만 고치고 `python3 build.py`를 돌리면
`index.html`, `about.html`, `hotels/*.html`, `ko/…`, `sitemap.xml`, `style.css`가 다시 만들어진다.
생성된 HTML도 커밋한다 (GitHub Pages가 main 루트를 그대로 배포).

## 데이터 규칙
- 사실 항목: `status`는 `ok`(공식 출처로 확인) 또는 `unverified`(미확인). `source`(URL)와 `checked`(확인일) 필수.
- 욕조/분리 값: `yes` / `no` / `unlisted`(공식 설비 목록에 없음) / `unverified`.
- 추측으로 채우지 않는다. 확인 못 하면 `unverified`.

## 판정 넣는 법 (`verdicts` 배열)
```json
{
  "topic": {"zh": "隔音差", "ko": "방음이 약하다"},
  "verdict": "structural",
  "summary": {"zh": "…", "ko": "…"},
  "evidence": {"zh": "…", "ko": "…"},
  "date": "2026-11-10"
}
```
`verdict`: `isolated`(일부 사례) / `structural`(구조적 문제) / `mixed`(객실·시기에 따라 다름)

## 예약 링크
`booking`의 `agoda`, `trip`, `klook`에 제휴 링크를 넣으면 버튼이 생긴다 (빈 값이면 버튼 없음).
