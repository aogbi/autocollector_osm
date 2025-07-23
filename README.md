Here’s a clear and concise `README.md` for your **Auto Collector** script:

---

# 🛠️ Auto Collector for Online Soccer Manager

This Python script automates the process of collecting Boss Coins by simulating video ad watches and claiming rewards on [Online Soccer Manager (OSM)](https://web-api.onlinesoccermanager.com).

## 🚀 Features

* Authenticates using OSM credentials
* Sends periodic API requests to simulate video ad views
* Automatically collects rewards (Boss Coins)
* Handles common errors and API wait times
* Runs continuously until stopped by the user

## ⚙️ Requirements

* Python 3.x
* `requests` library

Install dependencies:

```bash
pip install requests
```

## 📄 Configuration

The script uses hardcoded credentials. Make sure to replace these with your own:

```python
username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
```

> ⚠️ **Warning:** Avoid sharing or uploading the script with your credentials to public platforms. Consider using environment variables for security.

## 🧠 How It Works

1. Authenticates with the OSM API using a `Bearer` token.
2. Sends a `watched` request to simulate watching an ad.
3. Extracts the reward ID from the response.
4. Sends a `consumereward` request to collect Boss Coins.
5. Waits between requests to mimic human behavior.
6. Repeats the process in a loop.

## 📝 Usage

Run the script:

```bash
python3 auto_collector.py
```

To stop the script, press `Ctrl + C`.

## 🧩 API Endpoints Used

* `POST /api/token` – for authentication
* `POST /api/v1.1/user/videos/watched` – to simulate ad views
* `POST /api/v1/user/bosscoinwallet/consumereward` – to collect rewards

## ❗ Disclaimer

This script interacts with OSM's private APIs and simulates user actions. Use at your own risk. Your account may be subject to limitations or bans if automated behavior is detected.

## 📄 License

This project is for **educational purposes only** and is not affiliated with or endorsed by OSM.

---

Let me know if you'd like a version with environment variable support or `.env` file integration for safer use.
