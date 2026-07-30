# 🚀 Daily Python Backend Upskill & Git Push Repository

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Build Status](https://img.shields.io/badge/tests-passing-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Streak Tracker](https://img.shields.io/badge/daily--streak-active-orange.svg)

> **Level up your Python Backend Engineering skills every single day.** Solve real-world backend engineering challenges, test your solutions using automated Pytest suites, track your daily streaks via an interactive terminal CLI, and build a green contribution graph on GitHub!

---

## 🎯 Why This Repository?

Consistency is key to mastering backend software engineering. This repository is structured into daily hands-on challenges across **6 essential backend engineering domains**:

1. ⚡ **Core Python Mastery**: Advanced Decorators, Generators, AsyncIO Concurrency, Context Managers, Pydantic V2.
2. 🏗️ **System Design & Algorithms**: $O(1)$ LRU Cache, Rate Limiters, Design Patterns (Factory, Strategy, Observer).
3. 🗄️ **Database & ORM Deep-Dive**: SQLAlchemy 2.0 models, raw SQL indexing, transaction ACID bounds, Redis Caching.
4. 🌐 **API Engineering & Security**: FastAPI production design, JWT Auth, Custom Middleware, API Rate Limiting.
5. 🔄 **Async Queues & Realtime**: Celery background workers, Async task queues, WebSockets stream logic.
6. 🛠️ **Production & DevOps**: Pytest fixtures/mocking, structured logging, Prometheus metrics, CI pipelines.

---

## ⚡ Quickstart & Daily Workflow

### 1. Installation
Clone the repository and install the lightweight requirements:
```bash
# Install dependencies
pip install -r requirements.txt
```

### 2. View Progress Dashboard
Run the top-level tracker CLI to view your current streak and available challenges:
```bash
python daily_push.py --status
```

### 3. Work on Today's Challenge
Navigate to the day's challenge directory under `challenges/`:
- Read `README.md` for concept theory, scenario requirements, and acceptance criteria.
- Open `starter.py` and write your implementation.

### 4. Run Automated Tests
Verify your code against the Pytest test suite:
```bash
python daily_push.py --test 1
```

### 5. Mark Complete & Push to GitHub 🚀
Once tests pass, run `--complete` to update your daily streak in `.progress.json`, automatically format a conventional commit message, and push your changes to GitHub (`git push`):
```bash
python daily_push.py --complete 1
```

---

## 📚 30-Day Curriculum Roadmap

| Day | Module | Challenge Title | Concept Learned |
| :---: | :--- | :--- | :--- |
| **01** | Core Python | **Decorators & Telemetry** | Timing, Retry logic, Metadata preservation, Custom decorator attributes |
| **02** | Core Python | **Generators & Log Streaming** | Memory-efficient $O(1)$ file parsing, Generator pipelines |
| **03** | Core Python | **AsyncIO Concurrency** | `asyncio.gather`, `asyncio.Semaphore` rate limiting, Error isolation |
| **04** | Core Python | **Context Managers** | `__enter__`/`__exit__`, Resource guards, Transaction rollback |
| **05** | Core Python | **Pydantic V2 Validation** | EmailStr, custom `@field_validator`, DTO mapping |
| **06** | System Design | **$O(1)$ LRU Cache** | Doubly Linked List + Hash Map, MRU/LRU eviction |
| **07** | System Design | **Sliding Window Rate Limiter** | Timestamp logs, sliding window boundary calculation |
| **08** | System Design | **Factory & Strategy Patterns** | Decoupled payment gateway processors, abstract interfaces |
| **09** | System Design | **Observer & Pub/Sub Pattern** | Event driven domain event dispatchers |
| **10** | Database & ORM | **Connection Pooling Guard** | Pool starvation prevention & connection checkout |
| **11** | Database & ORM | **SQLAlchemy 2.0 Models** | Async sessions, relations, cascade deletes |
| **12** | Database & ORM | **Query Optimization** | Indexing strategies, avoiding N+1 query problems |
| **13** | Database & ORM | **ACID Transactions** | Isolation levels, optimistic vs pessimistic locking |
| **14** | Database & ORM | **Redis Cache Strategy** | Cache-aside pattern, TTL expiration, invalidation |
| **15+**| API Engineering | **FastAPI, JWT, Middleware & CI** | Production security, background tasks, monitoring |

---

## 🖥️ CLI Commands Cheat Sheet

| Command | Action |
| :--- | :--- |
| `python daily_push.py` | Open interactive progress dashboard & streak status |
| `python daily_push.py --status` | Display total completed days, streak, and challenge list |
| `python daily_push.py --test <day>` | Execute pytest for a specific day challenge (e.g. `--test 1`) |
| `python daily_push.py --complete <day>` | Test, update streak stats, commit with formatted message & git push |
| `python daily_push.py --all-tests` | Run pytest across all repository test suites |

---

## 🛠️ Repository Directory Structure

```
.
├── .github/
│   └── workflows/
│       └── python_daily_ci.yml      # GitHub Actions CI matrix auto-testing every push
├── challenges/
│   ├── week1_core_mastery/          # Week 1: Core Python Deep Dive
│   │   ├── day01_decorators_logging/
│   │   ├── day02_generators_memory/
│   │   ├── day03_asyncio_concurrency/
│   │   ├── day04_context_managers/
│   │   └── day05_dataclasses_pydantic/
│   └── week2_system_design_patterns/ # Week 2: System Design & Patterns
│       ├── day06_lru_cache/
│       ├── day07_rate_limiter/
│       └── day08_factory_strategy_pattern/
├── tracker/                         # CLI & Git Automation Engine
│   ├── cli.py
│   ├── streak_manager.py
│   └── git_helper.py
├── tests/
│   └── test_cli.py                  # Unit tests for tracker engine
├── daily_push.py                    # Top-level CLI entry point
├── requirements.txt                 # Project dependencies
├── .gitignore                       # Python & progress ignore rules
└── README.md                        # Master repository documentation
```

---

## 🤝 Contribution & License

This project is licensed under the MIT License - feel free to fork, customize, and build your own daily learning routine!

*Happy Coding & Keep That GitHub Contribution Graph Green!* 🟢
