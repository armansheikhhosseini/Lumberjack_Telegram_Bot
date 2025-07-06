# Telegram Todo Bot

A simple yet powerful Telegram bot built with Python 3 that helps users manage their personal todo lists.

## Features

- **Personal todo lists**: Each user gets their own private todo list
- **Easy item management**: Add items by sending text, remove with /done command
- **Persistent storage**: Uses SQLite database to store items permanently
- **Inline keyboards**: Interactive buttons for easy item removal
- **Multiple commands**: /start, /list, /done for different functions
- **Error handling**: Robust error handling and logging
- **User-friendly**: Emoji-rich interface for better user experience

## Commands

- `/start` - Welcome message and instructions
- `/list` - Show all current todo items
- `/done` - Remove completed items (shows interactive keyboard)
- Send any text - Adds that text as a new todo item

## Requirements

- Python 3.6+
- requests library
- A Telegram Bot Token

## Setup

1. **Create a Telegram Bot**:
   - Message @BotFather on Telegram
   - Use `/newbot` command
   - Follow the instructions to get your bot token

2. **Configure the Bot**:
   - Copy `config.example.py` to `config.py`
   - Replace `YOUR_BOT_TOKEN_HERE` with your actual bot token

3. **Install Dependencies**:
   ```bash
   pip install requests
   ```

4. **Run the Bot**:
   ```bash
   python todobot.py
   ```

## File Structure

- `todobot.py` - Main bot logic and Telegram API handling
- `dbhelper.py` - Database operations for SQLite
- `config.py` - Configuration file for bot token
- `todo.sqlite` - SQLite database (created automatically)

## Database Schema

The bot uses a simple SQLite database with one table:

```sql
CREATE TABLE items (
    description TEXT,
    owner TEXT
);
```

- `description`: The todo item text
- `owner`: Telegram chat ID (unique for each user)

## Usage Example

1. Start a chat with your bot on Telegram
2. Send `/start` to see the welcome message
3. Send "Buy groceries" - this gets added to your list
4. Send "Walk the dog" - this also gets added
5. Send `/list` to see all your items
6. Send `/done` to mark items as completed

## Error Handling

The bot includes comprehensive error handling for:
- Network connection issues
- Invalid JSON responses
- Database errors
- Missing message fields
- Invalid bot tokens

## Logging

The bot logs important events and errors to help with debugging:
- Bot startup and shutdown
- Database operations
- API errors
- Message processing

## Security Notes

- Keep your bot token secure and never commit it to version control
- The bot only responds to direct messages (no group functionality)
- Each user's data is isolated by their unique chat ID

## Author

Arman Sheikhhosseini

## License

This project is open source and available under the MIT License.