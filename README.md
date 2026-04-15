# marketplace-card-maker

Каркас Python + Streamlit проекта для внутреннего инструмента генерации карточек товаров для Ozon и Wildberries.

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Запуск приложения

```bash
streamlit run app.py
```

После запуска откроется минимальный экран с описанием, что это каркас v1.

## Как сразу применить изменения локально и в GitHub

1. Откройте терминал в папке проекта:

```bash
cd C:\Users\User\Desktop\marketplace-card-maker
```

2. Проверьте, что есть привязка к GitHub:

```bash
git remote -v
```

Если `origin` не задан, добавьте его:

```bash
git remote add origin https://github.com/islentev/marketplace-card-maker.git
```

3. Заберите изменения из репозитория в локальную папку:

```bash
git pull origin main
```

4. Если вы сделали локальные правки, отправьте их в GitHub:

```bash
git add .
git commit -m "chore: sync local changes"
git push origin main
```

## Простая схема работы по шагам (для вас)

Ниже самый простой цикл после каждого моего шага.

### 1) Забрать мои изменения из GitHub в локальную папку

Откройте терминал в папке проекта и выполните:

```bash
cd C:\Users\User\Desktop\marketplace-card-maker
git pull origin main
```

### 2) Запустить проект локально

```bash
pip install -r requirements.txt
streamlit run app.py
```

### 3) Проверить, что всё открылось

- в браузере откроется страница Streamlit;
- если всё хорошо — пишете мне следующий шаг.

### 4) Если терминал пишет ошибку

Просто скопируйте текст ошибки и отправьте мне — я дам готовую команду, что нажать и куда вставить.

---

## Коротко: какие команды нужны чаще всего

```bash
cd C:\Users\User\Desktop\marketplace-card-maker
git pull origin main
streamlit run app.py
```

## Как обновить файлы в GitHub (очень просто)

Если я написал, что шаг готов, сделайте так:

```bash
cd C:\Users\User\Desktop\marketplace-card-maker
git pull origin main
```

Если вы сами меняли файлы и хотите отправить их в GitHub:

```bash
git add .
git commit -m "update: local changes"
git push origin main
```

---

## Как сделать новый PR от свежего `main`

Ниже безопасный шаблон команд (копировать по порядку):

```bash
cd C:\Users\User\Desktop\marketplace-card-maker

git checkout main
git pull origin main

git checkout -b feature/my-next-step

# внесли изменения в файлы

git add .
git commit -m "feat: your next step"
git push -u origin feature/my-next-step
```

После этого в GitHub появится кнопка **Compare & pull request**.
Нажимаете ее и создаете PR.

## Если появился Merge conflict (что делать)

Это нормально, если `main` изменился, пока ветка была открыта.

### Быстрый способ (рекомендую)

1. Закройте старый конфликтный PR.
2. Создайте новую ветку от свежего `main` и перенесите только нужные изменения.

```bash
cd C:\Users\User\Desktop\marketplace-card-maker
git checkout main
git pull origin main
git checkout -b fix/new-clean-pr

# внесите нужные правки

git add .
git commit -m "fix: clean PR from fresh main"
git push -u origin fix/new-clean-pr
```

Откройте новый PR из `fix/new-clean-pr` в `main`.

### Если хотите исправить текущую ветку

```bash
cd C:\Users\User\Desktop\marketplace-card-maker
git checkout <ваша-ветка>
git fetch origin
git rebase origin/main
```

Если Git попросит решить конфликт:

```bash
# исправляете конфликтные файлы

git add .
git rebase --continue
```

Когда rebase завершится:

```bash
git push --force-with-lease
```

Если запутались — просто отправьте мне скрин/текст ошибки, я дам точные команды под ваш случай.
