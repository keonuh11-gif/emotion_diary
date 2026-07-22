import os
import mysql.connector
from dotenv import load_dotenv

# .env 파일 로드  # 얘를 실행시키면 .env읽어와서 환경변수에 저장된다. 그리고 그걸 가져오는게 아래의 함수
load_dotenv()

def get_db_connection():
    """환경 변수에서 정보를 가져와 MySQL에 연결합니다."""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USERNAME", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_DATABASE", "emotion_diary_db"),
        port=int(os.getenv("DB_PORT", 3306))
    )

def init_db():
    """테이블이 없을 경우 초기 생성합니다."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS diaries (
        id INT AUTO_INCREMENT PRIMARY KEY,
        diary_date DATE NOT NULL,
        emotion_score INT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    cursor.close()
    conn.close()