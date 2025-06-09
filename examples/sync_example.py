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
    
    solution = client.solve(task)
    print(f"Response token: {solution.grecaptcha_response}")
    
    balance = client.get_balance()
    print(f"Current balance: ${balance:.2f}")
  
if __name__ == "__main__":
  main()
