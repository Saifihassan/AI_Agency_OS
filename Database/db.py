import sqlite3
import os


def get_connection():
    db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'workspaces.db')
    conn = sqlite3.connect(db_path)
    return conn


def init_database():
    con = get_connection()
    cursor = con.cursor()


    cursor.execute( """
        CREATE TABLE IF NOT EXISTS workspaces (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        website TEXT,
        industry TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS company_profile(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        workspace_id INTEGER UNIQUE,
        company_summary TEXT,
        products TEXT,
        services TEXT,
        target_audience TEXT,
        brand_voice TEXT,
        usp TEXT,
        goals TEXT,
        social_links TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        
        """

    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS research_reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workspace_id INTEGER,
            title TEXT,
            content TEXT,
            source TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS competitors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workspace_id INTEGER,
            name TEXT,
            website TEXT,
            summary TEXT,
            strengths TEXT,
            weaknesses TEXT,
            marketing_strategy TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS market_news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workspace_id INTEGER,
            report_data TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS generated_content (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workspace_id INTEGER,
            content_type TEXT,
            title TEXT,
            prompt TEXT,
            content TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
       

    con.commit()
    con.close()
    print("Database initialized successfully")

def add_to_workspace(name, website, industry):
    con = get_connection()
    cursor = con.cursor()

    cursor.execute(
        """
        INSERT INTO workspaces (name, website, industry)
        VALUES (?, ?, ?)
        """,
        (name, website, industry)
    )
    
    workspace_id = cursor.lastrowid
    con.commit()
    con.close()
    
    return workspace_id

def fetch_from_workspaces():
    con = get_connection()
    cursor = con.cursor()
    
    cursor.execute("SELECT * FROM workspaces")
    records = cursor.fetchall()
    
    con.close()
    
    return records

def insert_market_news(workspace_id, report_data):
    con = get_connection()
    cursor = con.cursor()
    cursor.execute(
        """
        INSERT INTO market_news (workspace_id, report_data)
        VALUES (?, ?)
        """,
        (workspace_id, report_data)
    )
    con.commit()
    con.close()

def fetch_market_news(workspace_id):
    con = get_connection()
    cursor = con.cursor()
    cursor.execute(
        """
        SELECT report_data FROM market_news 
        WHERE workspace_id = ?
        ORDER BY created_at DESC LIMIT 1
        """,
        (workspace_id,)
    )
    record = cursor.fetchone()
    con.close()
    return record[0] if record else None
if __name__ == "__main__":
    init_database()




    