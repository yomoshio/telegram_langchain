# English Prompts
SUMMARY_PROMPT_EN = """
Content: {content}

Instructions:
Generate an extensive workbook-style summary of the provided book content in markdown format, styled as a professional marketing workbook with rich, detailed content, visual elements, and interactive components. The output **must** be 6000-7000 words (~20-25 pages at 250-300 words/page), ensuring a dense, interactive workbook like a professional marketing resource. Strictly enforce this word count, completing all 8 modules fully with no truncation. Use concrete book examples (e.g., Miller’s bulimia recovery, Diana Nyad’s swim) and tie to themes like BRIDGE, Good Grit, and psychological safety. Follow this structure exactly:

# Summary Workbook: [Book Title]

## Module 1: Introduction to Key Concepts
- **Learning Objectives**: List 7 objectives tied to book themes (100-150 words).
- **Key Concepts**: Define 7 concepts in a table, each with a book example (250-300 words):
  | Concept | Description | Book Example |
  |---------|-------------|--------------|
  | [Concept] | [Detailed description] | [Specific example] |
- **Why It Matters**: Explain importance with 3 book examples and real-world context (250-300 words).
- **Quick Quiz**: 5 multiple-choice questions with 4 options each (150-200 words).
- **Links**: 5 external resources (e.g., `[WOOP](https://woopmylife.org)`) with descriptions (150-200 words).
- **Image**: `![Key Concepts Diagram](images/concepts_diagram.png)`.

---

## Module 2: Core Themes and Insights
- **Theme 1**: Describe with 3 book examples, linking to BRIDGE framework (300-350 words).
  - **Case Study**: Real-world application with data/outcomes (250-300 words).
  - **Links**: 3 resources (e.g., `[HBR](https://hbr.org)`) (100-150 words).
- **Theme 2**: Describe with 3 book examples, focusing on gender/cultural nuances (300-350 words).
  - **Case Study**: Real-world application (250-300 words).
  - **Links**: 3 resources (100-150 words).
- **Theme 3**: Describe with 3 book examples, emphasizing resilience (300-350 words).
  - **Case Study**: Real-world application (250-300 words).
  - **Links**: 3 resources (100-150 words).
- **Quick Activity**: Mini-exercise to apply themes (150-200 words).
- **Image**: `![Themes Overview](images/themes.png)`.

---

## Module 3: Practical Application
- **Exercise 1: WOOP Planning**: Instructions with template (300-350 words).
  - Table: | Step | Description | Your Response |
- **Exercise 2: Bias Audit**: Track decisions with mitigation strategies (300-350 words).
  - Table: | Decision | Bias | Mitigation | Outcome |
- **Exercise 3: Network Mapping**: Identify catalysts/naysayers (250-300 words).
  - Table: | Contact | Role | Support Level | Action |
- **Exercise 4: Goal Prioritization**: Rank goals with rationale (250-300 words).
  - Table: | Goal | Priority | Rationale | Timeline |
- **Exercise 5: Resilience Checklist**: Build Good Grit (250-300 words).
  - Table: | Checkpoint | Status | Action | Deadline |
- **Exercise 6: Feedback Loop Design**: Create feedback mechanisms (250-300 words).
  - Table: | Goal | Feedback Source | Frequency | Notes |
- **Exercise 7: Psychological Safety Plan**: Foster safe environments (250-300 words).
  - Table: | Action | Stakeholder | Impact | Timeline |
- **Self-Reflection Questions**: 7 questions tied to book themes (150-200 words).
- **Evaluation Criteria**: 6 criteria in a table (200-250 words):
  | Criteria | Description | Example |
- **Links**: 5 resources (e.g., `[Positive Psychology](https://positivepsychology.com)`) (150-200 words).
- **Image**: `![Exercise Toolkit](images/toolkit.png)`.

---

## Module 4: Case Studies and Examples
- **Case Study 1**: Application with book tie-in and outcomes (350-400 words).
- **Case Study 2**: Application with data/metrics (350-400 words).
- **Case Study 3**: Application with cultural/gender focus (350-400 words).
- **Case Study 4**: Application with resilience focus (350-400 words).
- **Case Study 5**: Application with team/organizational focus (350-400 words).
- **Quick Activity**: Scenario-based exercise tied to case studies (200-250 words).
- **Links**: 5 resources (e.g., `[TED](https://www.ted.com)`) (150-200 words).
- **Image**: `![Case Studies](images/case_studies.png)`.

---

## Module 5: Templates and Tools
- **Template 1: BRIDGE Framework Worksheet**: Instructions and table (300-350 words).
  - Table: | Step | Description | Your Plan |
- **Template 2: Decision-Making Checklist**: Instructions and table (250-300 words).
  - Table: | Checkpoint | Status | Notes |
- **Template 3: Weekly Goal Tracker**: Instructions and table (250-300 words).
  - Table: | Week | Goal | Progress | Next Steps |
- **Template 4: Relationship Audit**: Instructions and table (250-300 words).
  - Table: | Contact | Support Type | Frequency | Action |
- **Links**: 4 resources (e.g., `[MindTools](https://mindtools.com)`) (100-150 words).
- **Image**: `![Templates](images/templates.png)`.

---

## Module 6: Reflection and Growth
- **Reflection Activity**: Guided journaling with 5 prompts (250-300 words).
  - Table: | Prompt | Response |
- **Self-Assessment Quiz**: 7 questions to evaluate progress (200-250 words).
- **Growth Plan**: Create a 6-month plan with table (250-300 words).
  - Table: | Month | Goal | Action | Metric |
- **Links**: 4 resources (e.g., `[Greater Good](https://greatergood.berkeley.edu)`) (100-150 words).
- **Image**: `![Growth Plan](images/growth_plan.png)`.

---

## Module 7: Summary and Next Steps
- **Key Takeaways**: 7 bullet points summarizing book insights (250-300 words).
- **Next Steps**: 7 actionable steps in a table (250-300 words):
  | Step | Action | Timeline | Resource |
- **Final Reflection**: 5 questions to consolidate learning (150-200 words).
- **Additional Resources**: 7 resources with descriptions (200-250 words).
- **Image**: `![Roadmap](images/roadmap.png)`.

---

## Module 8: Glossary and References
- **Glossary**: Define 10 key terms from the book (200-250 words).
  - Table: | Term | Definition |
- **References**: List 10 sources cited in the book or related (150-200 words).
- **Links**: 5 resources (e.g., `[Google Scholar](https://scholar.google.com)`) (100-150 words).
- **Image**: `![Glossary](images/glossary.png)`.

**Formatting Instructions**:
- Use markdown syntax (#, ##, ###, -, |, etc.).
- Include 10-12 image placeholders (e.g., `images/concepts_diagram.png`), 4x2.5 inches.
- Use tables with light blue headers (`#ADD8E6`), grey grids (`#D3D3D3`), alternating row colors.
- Add section breaks (`---`) for pagination (~250-300 words/page).
- Include 25-30 external links (e.g., `[WOOP](https://woopmylife.org)`) with descriptions, formatted as `[Title](URL)`.
- Use professional styling: navy 22pt titles, dark blue 18pt/14pt headings with grey background, black 11pt body in Helvetica.
- Ensure actionable tone with specific book examples and data (e.g., “30% revenue increase”).
- **Strictly enforce 6000-7000 words** across all 8 modules.

**DeepSeek Instructions**:
- Generate the full 6000-7000 words in a single response if possible.
- If split into files, generate two parts: Part 1 (Modules 1-4, ~3000-3500 words), Part 2 (Modules 5-8, ~3000-3500 words). Ensure continuity and combine for 6000-7000 words total.
- If chunking within a part, assign specific modules (e.g., Chunk 1: Modules 1-2, Chunk 2: Modules 3-4) and combine for a cohesive output.
- Ensure each module is fully completed with all components (e.g., tables, exercises).
- Prioritize key chapters if content is large.
- Output must be in markdown, ready for PDF generation.
"""

WORKSHEET_PROMPT_EN = """
Content: {content}

Instructions:
Generate an extensive workbook with exercises based on the book content in markdown, styled as a professional marketing workbook. Target 4000-5000 words (~15-20 pages at 250-300 words/page), ensuring interactive, actionable content. Use this structure:

# Workbook: [Book Title] Exercises

## Module 1: Comprehension Exercises
- 7 questions with detailed instructions in a table (200-250 words each):
  | Question | Instructions | Response |
- **Links**: 3 resources (e.g., `[Positive Psychology](https://positivepsychology.com)`) (100-150 words).
- **Image**: `![Questions](images/questions.png)`.

## Module 2: Analytical Tasks
- 5 tasks with detailed instructions and tables (250-300 words each):
  | Task | Instructions | Response |
- **Links**: 3 resources (100-150 words).
- **Image**: `![Tasks](images/tasks.png)`.

## Module 3: Creative Prompts
- 4 prompts with instructions and tables (250-300 words each):
  | Prompt | Instructions | Response |
- **Links**: 3 resources (100-150 words).
- **Image**: `![Prompts](images/prompts.png)`.

## Module 4: Application Scenarios
- 3 scenarios with exercises and tables (250-300 words each):
  | Scenario | Instructions | Response |
- **Links**: 3 resources (100-150 words).
- **Image**: `![Scenarios](images/scenarios.png)`.

## Module 5: Answer Keys
- Guidelines for all exercises in tables (150-200 words each):
  | Exercise | Guideline | Example |
- **Links**: 3 resources (100-150 words).
- **Image**: `![Answer Key](images/answer_key.png)`.

## Module 6: Self-Reflection
- 7 questions with response table (150-200 words):
  | Question | Response |
- 6 evaluation criteria in a table (150-200 words):
  | Criteria | Description | Example |
- **Links**: 3 resources (100-150 words).
- **Image**: `![Reflection](images/reflection.png)`.

**Formatting Instructions**:
- Use markdown (#, ##, ###, -, |).
- Include 8-10 image placeholders (e.g., `images/questions.png`), 4x2.5 inches.
- Use tables with light blue headers (`#ADD8E6`), grey grids (`#D3D3D3`).
- Add section breaks (`---`) for pagination (~250-300 words/page).
- Include 15-20 links with descriptions.
- Use professional styling: navy 22pt titles, dark blue 18pt/14pt headings, black 11pt body in Helvetica.
- Ensure actionable tone with book examples (e.g., Miller’s recovery).
- Target 4000-5000 words, no truncation.

**DeepSeek Instructions**:
- Generate full 4000-5000 words in a single response.
- If split, generate as one file or combine parts seamlessly.
- Prioritize module completion if truncated.
- Use book themes (BRIDGE, Good Grit).
"""

QUIZ_PROMPT_EN = """
Content: {content}

Instructions:
Generate a comprehensive questionnaire based on the book content in markdown, styled as a professional workbook. Target 2500-3000 words (~10-12 pages at 250-300 words/page), ensuring engaging, structured content. Use this structure:

# Quiz: [Book Title]

## Instructions
- Explain quiz purpose and format (100-150 words).
- 25 multiple-choice questions in tables (100-150 words each):
  | Question | A | B | C | D | Answer |
- **Links**: 4 resources (e.g., `[HBR](https://hbr.org)`) (150-200 words).
- **Image**: `![Quiz](images/quiz.png)`.

## Answer Key
- Explanations for all answers (150-200 words each):
  | Question | Correct Answer | Explanation |
- **Links**: 4 resources (150-200 words).
- **Image**: `![Answer Key](images/answer_key.png)`.

**Formatting Instructions**:
- Use markdown (#, ##, ###, -, |).
- Include 4-6 image placeholders (e.g., `images/quiz.png`), 4x2.5 inches.
- Use tables with light blue headers (`#ADD8E6`), grey grids (`#D3D3D3`).
- Add section breaks (`---`) for pagination (~250-300 words/page).
- Include 8-12 links with descriptions.
- Use professional styling: navy 22pt titles, dark blue 18pt/14pt headings, black 11pt body in Helvetica.
- Ensure questions tie to book themes (BRIDGE, Good Grit).
- Target 2500-3000 words, no truncation.

**DeepSeek Instructions**:
- Generate full 2500-3000 words in a single response.
- If split, generate as one file or combine parts.
- Prioritize question completion if truncated.
- Use book examples (e.g., Diana Nyad’s swim).
"""

ANALYSIS_PROMPT_EN = """
Content: {content}

Instructions:
Generate an extensive workbook-style literary analysis of the book in markdown, styled as a professional marketing workbook. Target 4000-5000 words (~15-20 pages at 250-300 words/page), ensuring deep, structured insights. Use this structure:

# Literary Analysis: [Book Title]

## Introduction
- Overview with book context and analysis purpose (300-350 words).
- **Links**: 3 resources (e.g., `[Google Scholar](https://scholar.google.com)`) (100-150 words).
- **Image**: `![Book Cover](images/book_cover.png)`.

## Module 1: Narrative Style
- Analysis with 3 book examples (350-400 words).
- **Links**: 2 resources (75-100 words).
- **Image**: `![Narrative](images/narrative.png)`.

## Module 2: Themes
- Analysis with 3 book examples (350-400 words).
- **Links**: 2 resources (75-100 words).
- **Image**: `![Themes](images/themes.png)`.

## Module 3: Character Development
- Analysis with 3 book examples (350-400 words).
- **Links**: 2 resources (75-100 words).
- **Image**: `![Characters](images/characters.png)`.

## Module 4: Cultural Context
- Analysis with 3 book examples (350-400 words).
- **Links**: 2 resources (75-100 words).
- **Image**: `![Context](images/context.png)`.

## Module 5: Psychological Insights
- Analysis with 3 book examples (350-400 words).
- **Links**: 2 resources (75-100 words).
- **Image**: `![Insights](images/insights.png)`.

## Module 6: Conclusion
- Summary and insights (250-300 words).
- **Links**: 2 resources (75-100 words).
- **Image**: `![Conclusion](images/conclusion.png)`.

## Self-Reflection
- 7 questions with response table (150-200 words):
  | Question | Response |
- **Links**: 3 resources (100-150 words).
- **Image**: `![Reflection](images/reflection.png)`.

## Resources
- 7 resources with descriptions (200-250 words).

**Formatting Instructions**:
- Use markdown (#, ##, ###, -, |).
- Include 6-8 image placeholders (e.g., `images/book_cover.png`), 4x2.5 inches.
- Use tables with light blue headers (`#ADD8E6`), grey grids (`#D3D3D3`).
- Add section breaks (`---`) for pagination (~250-300 words/page).
- Include 15-20 links with descriptions.
- Use professional styling: navy 22pt titles, dark blue 18pt/14pt headings, black 11pt body in Helvetica.
- Ensure analysis ties to book themes (BRIDGE, psychological safety).
- Target 4000-5000 words, no truncation.

**DeepSeek Instructions**:
- Generate full 4000-5000 words in a single response.
- If split, generate as one file or combine parts.
- Prioritize module completion if truncated.
- Use book examples (e.g., Miller’s recovery).
"""

# Russian Prompts
SUMMARY_PROMPT_RU = """
Content: {content}

Instructions:
Сгенерируйте обширный конспект в стиле рабочей тетради на основе содержания книги в формате markdown, оформленный как профессиональная маркетинговая рабочая тетрадь с насыщенным, детализированным содержимым, визуальными элементами и интерактивными компонентами. Выходной текст **должен** быть 6000–7000 слов (~20–25 страниц при 250–300 словах/страница), обеспечивая плотную, интерактивную рабочую тетрадь. Строго соблюдайте этот объем, полностью завершая все 8 модулей без усечения. Используйте конкретные примеры из книги (например, восстановление Миллер, плавание Дианы Няд) и связывайте с темами BRIDGE, Good Grit и психологическая безопасность. Следуйте этой структуре:

# Конспект: [Название книги]

## Модуль 1: Введение в ключевые концепции
- **Цели обучения**: Перечислите 7 целей, связанных с темами книги (100–150 слов).
- **Ключевые концепции**: Определите 7 концепций в таблице, каждая с примером из книги (250–300 слов):
  | Концепция | Описание | Пример из книги |
  |----------|----------|-----------------|
  | [Концепция] | [Детальное описание] | [Конкретный пример] |
- **Почему это важно**: Объясните значимость с 3 примерами из книги и реальным контекстом (250–300 слов).
- **Короткая викторина**: 5 вопросов с множественным выбором, по 4 варианта ответа (150–200 слов).
- **Ссылки**: 5 внешних ресурсов (например, `[WOOP](https://woopmylife.org)`) с описаниями (150–200 слов).
- **Изображение**: `![Диаграмма ключевых концепций](images/concepts_diagram.png)`.

---

## Модуль 2: Основные темы и выводы
- **Тема 1**: Опишите с 3 примерами из книги, связанными с рамкой BRIDGE (300–350 слов).
  - **Кейс**: Реальное применение с данными или результатами (250–300 слов).
  - **Ссылки**: 3 ресурса (например, `[HBR](https://hbr.org)`) с описаниями (100–150 слов).
- **Тема 2**: Опишите с 3 примерами из книги, с акцентом на гендерные/культурные нюансы (300–350 слов).
  - **Кейс**: Реальное применение (250–300 слов).
  - **Ссылки**: 3 ресурса (100–150 слов).
- **Тема 3**: Опишите с 3 примерами из книги, с акцентом на устойчивость (300–350 слов).
  - **Кейс**: Реальное применение (250–300 слов).
  - **Ссылки**: 3 ресурса (100–150 слов).
- **Короткое задание**: Мини-упражнение для применения тем (150–200 слов).
- **Изображение**: `![Обзор тем](images/themes.png)`.

---

## Модуль 3: Практическое применение
- **Упражнение 1: Планирование WOOP**: Подробные инструкции с шаблоном (300–350 слов).
  - Таблица: | Шаг | Описание | Ваш ответ |
- **Упражнение 2: Аудит предубеждений**: Отслеживание решений с стратегиями устранения (300–350 слов).
  - Таблица: | Решение | Предубеждение | Устранение | Результат |
- **Упражнение 3: Карта связей**: Определите катализаторы/противники (250–300 слов).
  - Таблица: | Контакт | Роль | Уровень поддержки | Действие |
- **Упражнение 4: Приоритизация целей**: Ранжируйте цели с обоснованием (250–300 слов).
  - Таблица: | Цель | Приоритет | Обоснование | Сроки |
- **Упражнение 5: Чек-лист устойчивости**: Создание Good Grit (250–300 слов).
  - Таблица: | Пункт | Статус | Действие | Срок |
- **Упражнение 6: Дизайн обратной связи**: Создание механизмов обратной связи (250–300 слов).
  - Таблица: | Цель | Источник обратной связи | Частота | Заметки |
- **Упражнение 7: План психологической безопасности**: Создание безопасной среды (250–300 слов).
  - Таблица: | Действие | Заинтересованная сторона | Влияние | Сроки |
- **Вопросы для саморефлексии**: 7 вопросов, связанных с темами книги (150–200 слов).
- **Критерии оценки**: 6 критериев в таблице (200–250 слов):
  | Критерий | Описание | Пример |
- **Ссылки**: 5 ресурсов (например, `[Positive Psychology](https://positivepsychology.com)`) (150–200 слов).
- **Изображение**: `![Набор инструментов](images/toolkit.png)`.

---

## Модуль 4: Кейсы и примеры
- **Кейс 1**: Детальное применение с привязкой к книге и результатами (350–400 слов).
- **Кейс 2**: Применение с данными или метриками (350–400 слов).
- **Кейс 3**: Применение с акцентом на культуру/гендер (350–400 слов).
- **Кейс 4**: Применение с акцентом на устойчивость (350–400 слов).
- **Кейс 5**: Применение с акцентом на команду/организацию (350–400 слов).
- **Короткое задание**: Упражнение на основе сценария, связанное с кейсами (200–250 слов).
- **Ссылки**: 5 ресурсов (например, `[TED](https://www.ted.com)`) (150–200 слов).
- **Изображение**: `![Кейсы](images/case_studies.png)`.

---

## Модуль 5: Шаблоны и инструменты
- **Шаблон 1: Рабочий лист BRIDGE**: Инструкции и таблица (300–350 слов).
  - Таблица: | Шаг | Описание | Ваш план |
- **Шаблон 2: Чек-лист принятия решений**: Инструкции и таблица (250–300 слов).
  - Таблица: | Пункт | Статус | Заметки |
- **Шаблон 3: Еженедельный трекер целей**: Инструкции и таблица (250–300 слов).
  - Таблица: | Неделя | Цель | Прогресс | Следующие шаги |
- **Шаблон 4: Аудит отношений**: Инструкции и таблица (250–300 слов).
  - Таблица: | Контакт | Тип поддержки | Частота | Действие |
- **Ссылки**: 4 ресурса (например, `[MindTools](https://mindtools.com)`) (100–150 слов).
- **Изображение**: `![Шаблоны](images/templates.png)`.

---

## Модуль 6: Рефлексия и рост
- **Рефлексивное задание**: Ведение дневника с 5 вопросами (250–300 слов).
  - Таблица: | Вопрос | Ответ |
- **Викторина для самооценки**: 7 вопросов для оценки прогресса (200–250 слов).
- **План роста**: Создание плана на 6 месяцев с таблицей (250–300 слов).
  - Таблица: | Месяц | Цель | Действие | Метрика |
- **Ссылки**: 4 ресурса (например, `[Greater Good](https://greatergood.berkeley.edu)`) (100–150 слов).
- **Изображение**: `![План роста](images/growth_plan.png)`.

---

## Модуль 7: Резюме и следующие шаги
- **Ключевые выводы**: 7 пунктов, суммирующих выводы книги (250–300 слов).
- **Следующие шаги**: 7 действенных шагов в таблице (250–300 слов):
  | Шаг | Действие | Сроки | Ресурс |
- **Финальная рефлексия**: 5 вопросов для закрепления знаний (150–200 слов).
- **Дополнительные ресурсы**: 7 ресурсов с описаниями (200–250 слов).
- **Изображение**: `![Дорожная карта](images/roadmap.png)`.

---

## Модуль 8: Глоссарий и ссылки
- **Глоссарий**: Определите 10 ключевых терминов из книги (200–250 слов).
  - Таблица: | Термин | Определение |
- **Ссылки**: Перечислите 10 источников, цитируемых в книге или связанных (150–200 слов).
- **Ссылки**: 5 ресурсов (например, `[Google Scholar](https://scholar.google.com)`) (100–150 слов).
- **Изображение**: `![Глоссарий](images/glossary.png)`.

**Инструкции по форматированию**:
- Используйте синтаксис markdown (#, ##, ###, -, |, и т.д.).
- Включите 10–12 заполнителей для изображений (например, `images/concepts_diagram.png`), каждый 4x2.5 дюйма.
- Используйте таблицы с голубыми заголовками (`#ADD8E6`), серой сеткой (`#D3D3D3`), чередующимися строками.
- Добавьте разделители (`---`) для разбивки на страницы (~250–300 слов/страница).
- Включите 25–30 внешних ссылок (например, `[WOOP](https://woopmylife.org)`) с описаниями, отформатированными как `[Название](URL)`.
- Используйте профессиональное оформление: темно-синие заголовки 22pt, темно-синие подзаголовки 18pt/14pt с серым фоном, черный текст 11pt в шрифте Helvetica.
- Обеспечьте действенный тон с конкретными примерами и данными (например, «рост дохода на 30%»).
- **Строго соблюдайте 6000–7000 слов** для всех 8 модулей.

**Инструкции для DeepSeek**:
- Сгенерируйте полные 6000–7000 слов в одном ответе, если возможно.
- Если разделяется на файлы, сгенерируйте две части: Часть 1 (Модули 1-4, ~3000–3500 слов), Часть 2 (Модули 5-8, ~3000–3500 слов). Обеспечьте непрерывность и объедините для 6000–7000 слов.
- Если используется чанкинг внутри части, назначьте конкретные модули (например, Чанк 1: Модули 1-2, Чанк 2: Модули 3-4) и объедините для связного вывода.
- Убедитесь, что каждый модуль полностью завершен со всеми компонентами (например, таблицы, упражнения).
- Приоритет ключевым главам, если контент велик.
- Вывод должен быть в markdown, готов для генерации PDF.
"""

WORKSHEET_PROMPT_RU = """
Content: {content}

Instructions:
Сгенерируйте обширную рабочую тетрадь с упражнениями на основе содержания книги в формате markdown, оформленную как профессиональная маркетинговая рабочая тетрадь. Цель — 4000–5000 слов (~15–20 страниц при 250–300 словах/страница), обеспечивая интерактивный, действенный контент. Используйте следующую структуру:

# Рабочая тетрадь: [Название книги]

## Модуль 1: Упражнения на понимание
- 7 вопросов с подробными инструкциями в таблице (200–250 слов каждое):
  | Вопрос | Инструкции | Ответ |
- **Ссылки**: 3 ресурса (например, `[Positive Psychology](https://positivepsychology.com)`) (100–150 слов).
- **Изображение**: `![Вопросы](images/questions.png)`.

## Модуль 2: Аналитические задания
- 5 заданий с подробными инструкциями и таблицами (250–300 слов каждое):
  | Задание | Инструкции | Ответ |
- **Ссылки**: 3 ресурса (100–150 слов).
- **Изображение**: `![Задания](images/tasks.png)`.

## Модуль 3: Креативные задания
- 4 задания с инструкциями и таблицами (250–300 слов каждое):
  | Задание | Инструкции | Ответ |
- **Ссылки**: 3 ресурса (100–150 слов).
- **Изображение**: `![Креативные задания](images/prompts.png)`.

## Модуль 4: Сценарии применения
- 3 сценария с упражнениями и таблицами (250–300 слов каждое):
  | Сценарий | Инструкции | Ответ |
- **Ссылки**: 3 ресурса (100–150 слов).
- **Изображение**: `![Сценарии](images/scenarios.png)`.

## Модуль 5: Ключи к ответам
- Руководства для всех упражнений в таблицах (150–200 слов каждое):
  | Упражнение | Руководство | Пример |
- **Ссылки**: 3 ресурса (100–150 слов).
- **Изображение**: `![Ключи к ответам](images/answer_key.png)`.

## Модуль 6: Саморефлексия
- 7 вопросов с таблицей для ответов (150–200 слов):
  | Вопрос | Ответ |
- 6 критериев оценки в таблице (150–200 слов):
  | Критерий | Описание | Пример |
- **Ссылки**: 3 ресурса (100–150 слов).
- **Изображение**: `![Рефлексия](images/reflection.png)`.

**Инструкции по форматированию**:
- Используйте markdown (#, ##, ###, -, |).
- Включите 8–10 заполнителей для изображений (например, `images/questions.png`), 4x2.5 дюйма.
- Используйте таблицы с голубыми заголовками (`#ADD8E6`), серой сеткой (`#D3D3D3`).
- Добавьте разделители (`---`) для страниц (~250–300 слов/страница).
- Включите 15–20 ссылок с описаниями.
- Используйте профессиональное оформление: темно-синие заголовки 22pt, темно-синие подзаголовки, черный 11pt текст в Helvetica.
- Обеспечьте действенный тон с примерами из книги (например, восстановление Миллер).
- Цель — 4000–5000 слов, без усечения.

**Инструкции для DeepSeek**:
- Сгенерируйте полные 4000–5000 слов в одном ответе.
- Если разделяется, сгенерируйте как один файл или объедините части.
- Приоритет завершения модулей, если усекается.
- Используйте темы книги (BRIDGE, Good Grit).
"""

QUIZ_PROMPT_RU = """
Content: {content}

Instructions:
Сгенерируйте обширную анкету на основе содержания книги в формате markdown, оформленную как профессиональная рабочая тетрадь. Цель — 2500–3000 слов (~10–12 страниц при 250–300 словах/страница), обеспечивая увлекательный, структурированный контент. Используйте следующую структуру:

# Анкета: [Название книги]

## Инструкции
- Объясните цель и формат анкеты (100–150 слов).
- 25 вопросов с множественным выбором в таблицах (100–150 слов каждый):
  | Вопрос | A | B | В | Г | Ответ |
- **Ссылки**: 4 ресурса (например, `[HBR](https://hbr.org)`) (150–200 слов).
- **Изображение**: `![Анкета](images/quiz.png)`.

## Ключи к ответам
- Объяснения для всех ответов (150–200 слов каждое):
  | Вопрос | Правильный ответ | Объяснение |
- **Ссылки**: 4 ресурса (150–200 слов).
- **Изображение**: `![Ключи к ответам](images/answer_key.png)`.

**Инструкции по форматированию**:
- Используйте markdown (#, ##, ###, -, |).
- Включите 4–6 заполнителей для изображений (например, `images/quiz.png`), 4x2.5 дюйма.
- Используйте таблицы с голубыми заголовками (`#ADD8E6`), серой сеткой (`#D3D3D3`).
- Добавьте разделители (`---`) для страниц (~250–300 слов/страница).
- Включите 8–12 ссылок с описаниями.
- Используйте профессиональное оформление: темно-синие заголовки 22pt, темно-синие подзаголовки, черный 11pt текст в Helvetica.
- Обеспечьте вопросы, связанные с темами книги (BRIDGE, Good Grit).
- Цель — 2500–3000 слов, без усечения.

**Инструкции для DeepSeek**:
- Сгенерируйте полные 2500–3000 слов в одном ответе.
- Если разделяется, сгенерируйте как один файл или объедините части.
- Приоритет завершения вопросов, если усекается.
- Используйте примеры из книги (например, плавание Няд).
"""

ANALYSIS_PROMPT_RU = """
Content: {content}

Instructions:
Сгенерируйте обширный литературный анализ в стиле рабочей тетради на основе книги в формате markdown, оформленный как профессиональная маркетинговая рабочая тетрадь. Цель — 4000–5000 слов (~15–20 страниц при 250–300 словах/страница), обеспечивая глубокие, структурированные инсайты. Используйте следующую структуру:

# Литературный анализ: [Название книги]

## Введение
- Обзор с контекстом и целью анализа книги (300–350 слов).
- **Ссылки**: 3 ресурса (например, `[Google Scholar](https://scholar.google.com)`) (100–150 слов).
- **Изображение**: `![Обложка книги](images/book_cover.png)`.

## Модуль 1: Нарративный стиль
- Анализ с 3 примерами из книги (350–400 слов).
- **Ссылки**: 2 ресурса (75–100 слов).
- **Изображение**: `![Нарратив](images/narrative.png)`.

## Модуль 2: Темы
- Анализ с 3 примерами из книги (350–400 слов).
- **Ссылки**: 2 ресурса (75–100 слов).
- **Изображение**: `![Тематика](images/themes.png)`.

## Модуль 3: Развитие персонажей
- Анализ с 3 примерами из книги (350–400 слов).
- **Ссылки**: 2 ресурса (75–100 слов).
- **Изображение**: `![Персонажи](images/characters.png)`.

## Модуль 4: Культурный контекст
- Анализ с 3 примерами из книги (350–400 слов).
- **Ссылки**: 2 ресурса (75–100 слов).
- **Изображение**: `![Контекст](images/context.png)`.

## Модуль 5: Психологические инсайты
- Анализ с 3 примерами из книги (350–400 слов).
- **Ссылки**: 2 ресурса (75–100 слов).
- **Изображение**: `![Инсайты](images/insights.png)`.

## Модуль 6: Заключение
- Резюме и выводы (250–300 слов).
- **Ссылки**: 2 ресурса (75–100 слов).
- **Изображение**: `![Заключение](images/conclusion.png)`.

## Саморефлексия
- 7 вопросов с таблицей для ответов (150–200 слов):
  | Вопрос | Ответ |
- **Ссылки**: 3 ресурса (100–150 слов).
- **Изображение**: `![Рефлексия](images/reflection.png)`.

## Ресурсы
- 7 ресурсов с описаниями (200–250 слов).

**Инструкции по форматированию**:
- Используйте markdown (#, ##, ###, -, |).
- Включите 6–8 заполнителей для изображений (например, `images/book_cover.png`), 4x2.5 дюйма.
- Используйте таблицы с голубыми заголовками (`#ADD8E6`), серой сеткой (`#D3D3D3`).
- Добавьте разделители (`---`) для страниц (~250–300 слов/страница).
- Включите 15–20 ссылок с описаниями.
- Используйте профессиональное оформление: темно-синие заголовки 22pt, темно-синие подзаголовки, черный 11pt текст в Helvetica.
- Обеспечьте анализ, связанный с темами книги (BRIDGE, психологическая безопасность).
- Цель — 4000–5000 слов, без усечения.

**Инструкции для DeepSeek**:
- Сгенерируйте полные 4000–5000 слов в одном ответе.
- Если разделяется, сгенерируйте как один файл или объедините части.
- Приоритет завершения модулей, если усекается.
- Используйте примеры из книги (например, восстановление Миллер).
"""