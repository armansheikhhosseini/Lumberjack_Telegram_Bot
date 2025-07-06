"""
Database Helper for Telegram Todo Bot

Handles SQLite database operations for storing and managing todo items.
Each user (identified by chat ID) has their own todo list.

Author: Arman Sheikhhosseini
"""

import sqlite3
import logging

logger = logging.getLogger(__name__)


class DBHelper:
    """Database helper class for managing todo items."""
    
    def __init__(self, dbname="todo.sqlite"):
        """
        Initialize database connection.
        
        Args:
            dbname (str): Database filename
        """
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname, check_same_thread=False)
        
    def setup(self):
        """
        Create database tables and indexes if they don't exist.
        """
        try:
            # Create items table
            tblstmt = "CREATE TABLE IF NOT EXISTS items (description text, owner text)"
            self.conn.execute(tblstmt)
            
            # Create indexes for better performance
            itemidx = "CREATE INDEX IF NOT EXISTS itemIndex ON items (description ASC)"
            ownidx = "CREATE INDEX IF NOT EXISTS ownIndex ON items (owner ASC)"
            self.conn.execute(itemidx)
            self.conn.execute(ownidx)
            
            self.conn.commit()
            logger.info("Database setup completed successfully")
            
        except sqlite3.Error as e:
            logger.error(f"Database setup error: {e}")
            raise

    def add_item(self, item_text, owner):
        """
        Add a new todo item for a user.
        
        Args:
            item_text (str): The todo item description
            owner (str): User's chat ID
        """
        try:
            stmt = "INSERT INTO items (description, owner) VALUES (?, ?)"
            args = (item_text, owner)
            self.conn.execute(stmt, args)
            self.conn.commit()
            logger.info(f"Added item '{item_text}' for user {owner}")
            
        except sqlite3.Error as e:
            logger.error(f"Error adding item: {e}")
            raise

    def delete_item(self, item_text, owner):
        """
        Delete a todo item for a user.
        
        Args:
            item_text (str): The todo item description to delete
            owner (str): User's chat ID
        """
        try:
            stmt = "DELETE FROM items WHERE description = ? AND owner = ?"
            args = (item_text, owner)
            cursor = self.conn.execute(stmt, args)
            self.conn.commit()
            
            if cursor.rowcount > 0:
                logger.info(f"Deleted item '{item_text}' for user {owner}")
            else:
                logger.warning(f"Item '{item_text}' not found for user {owner}")
                
        except sqlite3.Error as e:
            logger.error(f"Error deleting item: {e}")
            raise

    def get_items(self, owner):
        """
        Get all todo items for a user.
        
        Args:
            owner (str): User's chat ID
            
        Returns:
            list: List of todo item descriptions
        """
        try:
            stmt = "SELECT description FROM items WHERE owner = ? ORDER BY rowid"
            args = (owner,)
            cursor = self.conn.execute(stmt, args)
            return [row[0] for row in cursor.fetchall()]
            
        except sqlite3.Error as e:
            logger.error(f"Error getting items: {e}")
            return []
            
    def get_item_count(self, owner):
        """
        Get the count of todo items for a user.
        
        Args:
            owner (str): User's chat ID
            
        Returns:
            int: Number of todo items
        """
        try:
            stmt = "SELECT COUNT(*) FROM items WHERE owner = ?"
            args = (owner,)
            cursor = self.conn.execute(stmt, args)
            return cursor.fetchone()[0]
            
        except sqlite3.Error as e:
            logger.error(f"Error getting item count: {e}")
            return 0
            
    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            logger.info("Database connection closed")
