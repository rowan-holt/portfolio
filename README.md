# 정우민 사진 포트폴리오

주소: https://rowan-holt.github.io/portfolio/

빌드 과정 없는 HTML, CSS, 바닐라 JS 사이트입니다. GitHub Pages의 `main` 브랜치 루트에서 배포합니다.

## 사진 추가 방법

1. 사진을 긴 변 2400px JPG로 내보냅니다. 위치정보는 제거하고, 원본은 올리지 않습니다.
2. 파일명은 영문 소문자·숫자·하이픈만 씁니다. 예: `portrait-01.jpg`
3. 저장소의 카테고리 폴더에 올립니다.

   | 폴더 | 카테고리 |
   | --- | --- |
   | `photos/portrait` | 프로필 인물 |
   | `photos/event` | 행사·보도 |
   | `photos/staged` | 연출 |
   | `photos/wedding` | 웨딩 스냅 |
   | `photos/ai` | AI·합성 |

4. `data/photos.json`에 항목을 하나 추가합니다. 다른 파일은 고치지 않아도 됩니다.

   ```json
   {
     "id": "portrait-02",
     "category": "portrait",
     "file": "assets/img/portrait/portrait-02.webp",
     "thumb": "assets/thumb/portrait/portrait-02.webp",
     "width": 1800,
     "height": 1200,
     "title": "사진 제목",
     "caption": "촬영 의도나 조명 구성",
     "year": 2026
   }
   ```

   - `category`는 위 표의 폴더 이름 중 하나입니다.
   - `file`과 `thumb`는 `/`로 시작하지 않는 상대 경로로 적습니다.
   - `width`와 `height`는 `file` 이미지의 실제 픽셀 크기입니다.

## 문구 수정

사이트의 모든 문구는 `content/ko.json`에 있습니다. 자리표시자로 남은 소개 문구, 경력, 장비, 이메일, 인스타그램을 이 파일에서 바꾸면 됩니다. 홈 대표 사진은 `home.hero_photo_id`에 사진의 `id`를 적어 지정합니다.

## 내 컴퓨터에서 보기

파일을 직접 열면 JSON을 읽지 못하므로 저장소 폴더에서 로컬 서버를 실행합니다.

```bash
python -m http.server 8765
```

그다음 브라우저에서 http://localhost:8765 를 엽니다.
