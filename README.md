# Вычислитель отличий (QA Python)

[![hexlet-check](https://github.com/oxiliu66/qa-auto-engineer-python-project-241/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/oxiliu66/qa-auto-engineer-python-project-241/actions)

Консольная утилита, которая сравнивает два плоских файла JSON или YAML и выводит разницу в трёх форматах. Проект стоит в профессии тестировщика, поэтому основная работа идёт над тестами. Вы пишете их на pytest, сверяете вывод утилиты с эталонными файлами и задаёте порог покрытия, при просадке которого падает сборка в GitHub Actions.

Учебный проект Хекслета: https://ru.hexlet.io/programs/qa-auto-engineer-python
Как это должно работать: https://asciinema.org/a/Pe6QypnLEmFWssNAjCOJN1iii

## Стек

- Python

## Установка

install:
	uv sync

build:
	uv build

update:
	uv lock --upgrade
	uv sync



```bash
git clone https://github.com/oxiliu66/qa-auto-engineer-python-project-241.git
cd qa-auto-engineer-python-project-241
```

## Использование

[![asciicast](https://asciinema.org/a/wK9WKfckJtSjFS9A.svg)](https://asciinema.org/a/wK9WKfckJtSjFS9A)

---

<details>
<summary>Автоматические тесты Хекслета</summary>

Тесты запускаются на каждый коммит. За запуск отвечает файл `.github/workflows/hexlet-check.yml` — не удаляйте и не переименовывайте ни его, ни репозиторий.

</details>

## О Хекслете

[Хекслет](https://ru.hexlet.io/) — школа программирования: авторские программы обучения с практикой, поддержкой наставников и реальными проектами, которые остаются в резюме. Этот репозиторий — один из таких проектов.
