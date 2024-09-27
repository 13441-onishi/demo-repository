import sqlite3

def get_user_data(username):
    # SQLインジェクションの脆弱性が存在するコード
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # 問い合わせ実行
    cursor.execute(query)
    result = cursor.fetchall()
    
    conn.close()
    return result

if __name__ == "__main__":
    user_input = input("Enter your username: ")
    print(get_user_data(user_input))

