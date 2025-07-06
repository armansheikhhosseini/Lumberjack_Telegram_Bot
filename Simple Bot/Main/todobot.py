"""
Simple Telegram Todo Bot

A Telegram bot that helps users manage their todo lists.
Users can add items by sending text messages and remove items using inline keyboards.

Author: Arman Sheikhhosseini
Requirements: requests, sqlite3

Setup:
1. Get a bot token from @BotFather on Telegram
2. Update the token in config.py
3. Run this script
"""

import json
import requests
import time
import urllib.parse
import logging
from dbhelper import DBHelper
from config import tootiBOtToken

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Initialize database helper
db = DBHelper()

# Bot configuration
TOKEN = tootiBOtToken
URL = f"https://api.telegram.org/bot{TOKEN}/"


def get_url(url):
    """
    Make a GET request to the specified URL.
    
    Args:
        url (str): The URL to request
        
    Returns:
        str: Response content as string
    """
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.content.decode("utf8")
    except requests.RequestException as e:
        logger.error(f"Error making request to {url}: {e}")
        return None


def get_json_from_url(url):
    """
    Get JSON response from a URL.
    
    Args:
        url (str): The URL to request
        
    Returns:
        dict: Parsed JSON response or None if error
    """
    content = get_url(url)
    if content:
        try:
            return json.loads(content)
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing JSON: {e}")
    return None


def get_updates(offset=None):
    """
    Get updates from Telegram API.
    
    Args:
        offset (int): Update offset for long polling
        
    Returns:
        dict: Updates from Telegram API
    """
    url = URL + "getUpdates"
    if offset:
        url += f"?offset={offset}"
    return get_json_from_url(url)


def get_last_update_id(updates):
    """
    Get the ID of the last update.
    
    Args:
        updates (dict): Updates response from Telegram API
        
    Returns:
        int: Last update ID
    """
    if not updates or "result" not in updates or not updates["result"]:
        return None
        
    update_ids = [int(update["update_id"]) for update in updates["result"]]
    return max(update_ids)


def handle_updates(updates):
    """
    Process incoming updates from Telegram.
    
    Args:
        updates (dict): Updates from Telegram API
    """
    if not updates or "result" not in updates:
        return
        
    for update in updates["result"]:
        try:
            if "message" not in update:
                continue
                
            message = update["message"]
            if "text" not in message or "chat" not in message:
                continue
                
            text = message["text"]
            chat_id = message["chat"]["id"]
            
            # Get user's current items
            items = db.get_items(chat_id)
            
            if text == "/done":
                if items:
                    keyboard = build_keyboard(items)
                    send_message("Select an item to delete:", chat_id, keyboard)
                else:
                    send_message("You have no items in your todo list!", chat_id)
                    
            elif text == "/start":
                welcome_msg = (
                    "🔥 Welcome to your personal Todo List Bot! 🔥\n\n"
                    "📝 Send me any text and I'll add it to your todo list\n"
                    "✅ Use /done to mark items as completed\n"
                    "📋 Use /list to see all your items\n\n"
                    "Let's get productive! 💪"
                )
                send_message(welcome_msg, chat_id)
                
            elif text == "/list":
                if items:
                    message = "📋 Your Todo List:\n\n" + "\n".join([f"• {item}" for item in items])
                else:
                    message = "📭 Your todo list is empty! Send me some tasks to add."
                send_message(message, chat_id)
                
            elif text.startswith("/"):
                # Unknown command
                send_message("❓ Unknown command. Use /start for help.", chat_id)
                
            elif text in items:
                # User selected an item to delete
                db.delete_item(text, chat_id)
                items = db.get_items(chat_id)
                
                if items:
                    keyboard = build_keyboard(items)
                    send_message("✅ Item completed! Select another item to delete:", chat_id, keyboard)
                else:
                    send_message("🎉 Great job! All items completed!", chat_id)
                    
            else:
                # Add new item
                db.add_item(text, chat_id)
                items = db.get_items(chat_id)
                message = "✅ Added to your todo list!\n\n📋 Current items:\n" + "\n".join([f"• {item}" for item in items])
                send_message(message, chat_id)
                
        except Exception as e:
            logger.error(f"Error handling update: {e}")


def build_keyboard(items):
    """
    Build inline keyboard for item selection.
    
    Args:
        items (list): List of todo items
        
    Returns:
        str: JSON string of keyboard markup
    """
    keyboard = [[item] for item in items]
    reply_markup = {"keyboard": keyboard, "one_time_keyboard": True}
    return json.dumps(reply_markup)


def send_message(text, chat_id, reply_markup=None):
    """
    Send a message to a Telegram chat.
    
    Args:
        text (str): Message text
        chat_id (int): Chat ID to send to
        reply_markup (str): Optional keyboard markup
    """
    try:
        text = urllib.parse.quote_plus(text)
        url = f"{URL}sendMessage?text={text}&chat_id={chat_id}&parse_mode=Markdown"
        
        if reply_markup:
            url += f"&reply_markup={reply_markup}"
            
        response = get_url(url)
        if response is None:
            logger.error(f"Failed to send message to chat {chat_id}")
            
    except Exception as e:
        logger.error(f"Error sending message: {e}")


def main():
    """
    Main bot loop.
    """
    logger.info("Starting Todo Bot...")
    
    # Setup database
    try:
        db.setup()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Failed to setup database: {e}")
        return
    
    # Validate bot token
    if TOKEN == "YOUR_BOT_TOKEN_HERE":
        logger.error("Please update your bot token in config.py")
        return
    
    last_update_id = None
    logger.info("Bot is running... Press Ctrl+C to stop")
    
    try:
        while True:
            updates = get_updates(last_update_id)
            
            if updates and "result" in updates and len(updates["result"]) > 0:
                last_update_id = get_last_update_id(updates)
                if last_update_id:
                    last_update_id += 1
                handle_updates(updates)
                
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")


if __name__ == '__main__':
    main()
    main()
