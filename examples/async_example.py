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
