# import requests
# from bs4 import BeautifulSoup
# import os

# # Get credentials from GitHub Secrets
# BOT_TOKEN = os.getenv("BOT_TOKEN")
# CHAT_ID = os.getenv("CHAT_ID")
# TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# # URL to monitor
# URL = "https://aknu.edu.in/Exams/results.php"
# DATA_FILE = "previous_results.txt"

# def send_telegram_message(message):
#     """Send a message to Telegram."""
#     requests.post(TELEGRAM_API_URL, data={"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"})

# def fetch_latest_results():
#     """Fetch the latest <p> tags inside the target div."""
#     response = requests.get(URL)
#     response.raise_for_status()

#     soup = BeautifulSoup(response.text, "html.parser")
#     div = soup.find("div", class_="col-xl-9 col-md-8")

#     if not div:
#         return []

#     p_tags = div.find_all("p")
#     return [str(p) for p in p_tags]  # Store as string for easy comparison

# def load_previous_results():
#     """Load previously stored <p> tags."""
#     if not os.path.exists(DATA_FILE):
#         return set()
    
#     with open(DATA_FILE, "r", encoding="utf-8") as file:
#         return set(file.read().split("\n"))  # Store as set for quick comparison

# def save_results(results):
#     """Save current <p> tags to the file."""
#     with open(DATA_FILE, "w", encoding="utf-8") as file:
#         file.write("\n".join(results))

# def main():
#     """Check for new <p> tags and send Telegram alerts."""
#     current_results = set(fetch_latest_results())
#     previous_results = load_previous_results()

#     new_results = current_results - previous_results  # Find new <p> tags
#     if new_results:
#         for p_tag in new_results:
#             send_telegram_message(f"New Result Published:\n{p_tag}")
#         save_results(current_results)  # Update stored results
#     else:
#         send_telegram_message("✅ No new results found.")

# if __name__ == "__main__":
#     main()











import requests
import os

# Get credentials from GitHub Secrets
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def send_telegram_message(message):
    """Send a test message to Telegram."""
    data = {"chat_id": CHAT_ID, "text": message}
    response = requests.post(TELEGRAM_API_URL, data=data)
    print("Telegram Response:", response.json())  # Print response to debug

if __name__ == "__main__":
    send_telegram_message("Test message from GitHub Actions!")


