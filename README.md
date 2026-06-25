# loz-whook 🚀

A lightweight, handy Python library that monitors system errors (tracebacks), tracks events (custom logs), and sends instant notifications directly to your **Discord Webhook** using beautiful Embeds. Perfect for monitoring when developing Discord Bots or background applications (Cronjobs, VPS, etc.).

Developed by **MinhSangGD**

📧 Email: [minhsanggd@mscrew.io.vn](mailto:minhsanggd@mscrew.io.vn)  
🌐 GitHub: [https://github.com/MinhSangGD/loz-whook](https://github.com/MinhSangGD/loz-whook)

---

## ✨ Key Features
* **Plug and Play:** Just set up your `.env` file, no verbose configuration code needed.
* **Auto Locator:** Intelligently locates the `.env` file in the execution directory (works flawlessly on Termux, Docker, Linux, Windows).
* **Decorator `@monitor`:** Automatically captures any exception raised inside a function and forwards it to Discord with just a single line of code.
* **Flexible Customization:** Supports changing the sender's name (Username) and Profile Picture (Avatar) for the Webhook dynamically.
* **Anti-Flood Logging:** Smart character limitation to prevent Discord API `400 Bad Request` errors when the Traceback is too long.

---

## ⚙️ Installation & Configuration

### 1. Installation
You can install the library directly from PyPI or via GitHub:
```bash
pip install loz-whook

```
### 2. Environment Variables Configuration
Create a file named .env in the root directory of your project (in the same folder as your main executable script) and fill in the following information:
```env
# (REQUIRED) The Webhook URL of the Discord channel where you want to receive logs (please set your channel to private if you dont want your error logs to be exposed)
LOZ_WHOOK_URL=https://discord.com/api/webhooks/xxxxxx/xxxxxx

# (OPTIONAL) Sender name for the webhook. Defaults to "loz-whook" if left blank
LOZ_WHOOK_NAME=System Monitor Bot

# (OPTIONAL) Direct link to the avatar image (.png, .jpg). Defaults to webhook's original avatar if left blank
LOZ_WHOOK_AVATAR=https://i.imgur.com/example.png

```
## 🚀 Usage Guide
Import the library into your code and use it in 3 extremely simple ways:
### Method 1: Automatic Error Tracking (Most Convenient)
Add the `@monitor` decorator on top of your function. If an error occurs inside the function, it will automatically send the full traceback to Discord while still printing the error to the Terminal as usual.
```python
from loz_whook import monitor

@monitor
def connect_database():
    # Simulate a ZeroDivisionError
    return 100 / 0

# When calling this function, the ZeroDivisionError will automatically fly to your Webhook!
connect_database() 

```
### Method 2: Custom Log (Event Tracking)
If you want to track a specific event (bot starting, user logged in, backup successful...), it only takes one line of code:
```python
from loz_whook import log

# Custom log with your own title, message, and color (Decimal color code)
log(
    message="Bot has successfully started and connected to the Database!", 
    title="✅ System Info", 
    color=5763719
)

```
### Method 3: Manual Error Handling with Try-Except
Best suited for cases where you want to catch specific exceptions without interrupting the application's workflow.
```python
from loz_whook import log_error

try:
    # Code that might raise an exception
    x = int("this_string_will_cause_an_error")
except Exception as e:
    # Send detailed error report to your webhook with contextual information
    log_error(e, context="Error during data type casting from API response")

```
## 💡 Complete Example Project
Here is a full demonstration of how to configure and structure your project using loz-whook.
### 1. File .env
```env
# Real URL from your Discord channel
LOZ_WHOOK_URL=https://discord.com/api/webhooks/123456789/AbCdEfGhIjKlMnOp

# Change the sender's display name
LOZ_WHOOK_NAME=System Auto Bot

# Add a custom avatar)
LOZ_WHOOK_AVATAR=https://mingsengbot.vercel.app/assets/avatar.jpg

```
### 2. File app.py
```python
import time
from loz_whook import log, log_error, monitor

# --- FEATURE 1: CUSTOM LOG ---
def startup():
    print("[1] Starting system...")
    # Notify Discord when the app successfully starts running
    log(
        message="🚀 The `DemoLozWhook` system has successfully started and is ready for commands!",
        title="🟢 System Online",
        color=3066993 # Green color code
    )
    time.sleep(1)

# --- FEATURE 2: MANUAL ERROR TRACKING (TRY-EXCEPT) ---
def process_data():
    print("\n[2] Processing input data...")
    try:
        # Intentionally create an error: Casting a non-numeric string to integer
        junk_data = "not_a_number"
        amount = int(junk_data)
    except Exception as e:
        print("    -> ⚠️ Data processing error detected! Report sent to Discord.")
        # Push error to Discord with context to help developers debug easily
        log_error(e, context="Error in `process_data` function - User entered invalid amount format.")
    time.sleep(1)

# --- FEATURE 3: AUTOMATIC ERROR TRACKING VIA DECORATOR ---
# Just put @monitor at the top; if the function fails, Discord receives it instantly
@monitor
def connect_critical_server():
    print("\n[3] Connecting to central server...")
    time.sleep(1)
    # Intentionally create a critical error: Division by zero
    result = 100 / 0
    return result

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    startup()
    
    process_data()
    
    print("\nPreparing to run a critical function that will crash the app...")
    connect_critical_server()
    
    # This line will NEVER be reached because the function above raises an unhandled exception
    print("Code executed successfully!")

```
## 📄 License
This project is distributed under the [MIT License](https://github.com/MinhSangGDVN/loz-whook/blob/main/LICENSE). Feel free to use, modify, and distribute it for both personal and commercial projects!
