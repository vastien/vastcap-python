# vastcap-python

**A fast, minimal, and easy-to-use Python wrapper for the [Vast Captcha API](https://captcha.vast.sh), supporting both asynchronous and synchronous solving!**
---

## ✨ Features

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
    TurnstileTask
)

def main() -> None:
    client = Vast(api_key="vastCap_...")
    
    task = TurnstileTask(
        website_url="...",
        website_key="...",
    )
    
    solution: str = client.solve(task)
    print(f"Response token: {solution.turnstile_response}")
    
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
            is_invisible=True,
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

**All** errors are derived from `VastCapException`, but you can catch more specific errors and handle them as you please. You can find more information about these errors in the API docs.

```python
from vastcap import VastCapException # broad
from vastcap import InvalidAPIKeyError # specific to api key error
```

Check `status`, `errorCode`, and `errorDescription` in API docs or via raised exceptions.

Docs: https://docs.vast.sh

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

<a href="https://github.com/vastien/vastcap-python/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=vastien/vastcap-python&preview=true&max=&columns=" />
</a>

---

## ⚖ License

![License](https://img.shields.io/badge/License-MIT-blue.svg)

Copyright © 2025 [vastien](https://github.com/vastien)
