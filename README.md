---

# 🧩 개인 알고리즘 풀이 저장소

백준 & 프로그래머스 문제 풀이 개인 저장소입니다.

## 💡 만든 이유

코딩 스터디 레포에 풀이를 올릴 때, 루트에 바로 커밋되는 게 아니라 **내 이름의 폴더 안에만** 올라갔으면 했습니다. 백준허브는 레포 루트에 커밋하는 구조라 직접 경로를 지정할 수 없어서, GitHub Actions를 활용해 자동 동기화하는 방식으로 해결했습니다.

## ⚙️ 동작 방식

```
백준허브 자동 커밋
    ↓
개인 레포
    ↓ GitHub Actions 트리거
스터디 레포/{본인이름}/
```

1. 백준허브 크롬 확장프로그램이 채점 통과 시 개인 레포에 자동 커밋
2. 커밋이 감지되면 GitHub Actions 워크플로우 실행
3. 개인 레포 전체가 스터디 레포의 `{본인이름}/` 폴더로 자동 동기화

## 🛠️ 동일하게 세팅하는 법

### 1. 개인 레포 생성
백준허브를 연결할 개인 레포를 생성하고 백준허브 확장프로그램에서 연결합니다.

### 2. Personal Access Token 발급
`GitHub Settings` → `Developer settings` → `Fine-grained tokens`
- 스터디 레포 선택
- `Contents`: Read and write 권한 부여

### 3. 개인 레포 Secret 등록
개인 레포 `Settings` → `Secrets and variables` → `Actions`
- Name: `{토큰이름}`
- Value: 발급받은 토큰

### 4. 스터디 레포 Actions 권한 설정
스터디 레포 `Settings` → `Actions` → `General` → `Workflow permissions`
- `Read and write permissions` 선택

### 5. 워크플로우 파일 추가
개인 레포에 `.github/workflows/sync.yml` 파일을 생성하고 아래 내용을 붙여넣은 뒤 주석을 참고해 본인에 맞게 수정하세요.

```yaml
name: Sync to algolog
on:
  push:
    branches:
      - main  # 본인 기본 브랜치 이름으로 변경
jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - name: 개인 레포 체크아웃
        uses: actions/checkout@v3
      - name: 스터디 레포 체크아웃
        uses: actions/checkout@v3
        with:
          repository: {스터디레포주인계정}/{스터디레포이름}
          token: ${{ secrets.{토큰이름} }}
          path: shared-repo
      - name: 파일 복사
        run: |
          rsync -av --exclude='.git' --exclude='.github' --exclude='README.md' --exclude='shared-repo' ./ shared-repo/{본인이름}/
      - name: 스터디 레포에 push
        run: |
          cd shared-repo
          git config user.name "{GitHub유저네임}"
          git config user.email "{GitHub유저네임}@users.noreply.github.com"
          git add .
          git diff --cached --quiet || git commit -m "sync: $(git -C $GITHUB_WORKSPACE log --format=%s -1 HEAD)"
          git push
```

---
