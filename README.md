# 🧠 vastcap-python

**A Python wrapper for the [Vast Captcha API](https://captcha.vast.sh)**  
Supports both sync and async solving of many captcha challenges. Fast, minimal, and easy to use.

![License](https://img.shields.io/badge/License-MIT-blue.svg)

---

## ✨ Features

- ✅ Sync (`Vast`) and Async (`AsyncVast`) clients
- ✅ Supports ReCaptcha v2 and hCaptcha tasks
- ✅ Easy `solve()` method with built-in polling
- ✅ Typed error handling & result objects
- ✅ Tiny, no-bloat dependency footprint

---

## 📦 Installation

```bash
pip install vastcap
````

---

## 🔐 Authentication

Pass your API key via `Vast(api_key=...)` or `AsyncVast(api_key=...)`.

---

## 🧪 Example Usage

### Synchronous

```python
from vastcap import (
    Vast,
    RecaptchaV2Task,
    HCaptchaTask
)

def main() -> None:
    client = Vast(api_key="vastCap_...")
    
    task = RecaptchaV2Task(
        website_url="...",
        website_key="...",
        is_invisible=False
    )
    
    solution: str = client.solve(task)
    print(f"Response token: {solution.grecaptcha_response}")
    
    balance: int | float = client.get_balance()
    print(f"Current balance: ${balance:.2f}")
  
if __name__ == "__main__":
    main()
```

### Asynchronous

```python
from vastcap import AsyncVast, HCaptchaTask
import asyncio

async def main() -> None:
    async with AsyncVast(api_key="vastCap_...") as client:
        task = HCaptchaTask(
            website_url="https://discord.com/register",
            website_key="a9b5fb07-92ff-493f-86fe-352a2803b3df",
            enterprise=True,
            proxy="user:pass@ip:port"
        )
    
        solution: str = await client.solve(task)
        print(f"Response token: {solution.hcaptcha_response}")
    
        balance: int | float = await client.get_balance()
        print(f"Current balance: ${balance:.2f}")

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🧩 Task Types

```python
from vastcap import TaskType
```

* `RecaptchaV2Task`
* `RecaptchaV3Task`
* `HCaptchaTask`
* `TurnstileTask`
* `FunCaptchaTask`

Each task must define:

* `website_url`: the page with the captcha
* `website_key`: the sitekey for the captcha provider
* (Optional) task-specific flags like `is_invisible`

---

## 💥 Errors

Errors are raised as `VastCapException` or mapped subclasses via:

```python
from vastcap.exceptions import ERROR_MAPPING
```

Check `status`, `errorCode`, and `errorDescription` in API docs or via raised exceptions.

---

## 🧱 Structure

* `client.py` – Sync & Async client classes
* `types.py` – Typed definitions for tasks, results, statuses
* `exceptions.py` – Custom exception mapping
* `examples/` – Working usage examples

---

## 🛠️ Contributing

PRs and issues welcome!

```bash
git clone https://github.com/vastien/vastcap-python
cd vastcap-python
pip install -e .[dev]
```

---

## ⚖ License

MIT © [vastien](https://github.com/vastien)
