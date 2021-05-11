import sqlite3
import yaml


CONFIG_PATH = "./config.yml"
with open(CONFIG_PATH) as f:
    config_yml = yaml.safe_load(f)

path = config_yml['path']['database']
connect = sqlite3.connect(path + '/' + config_yml['state'] + '.db')
cursor = connect.cursor()

cursor.execute("SELECT * FROM sqlite_master WHERE type='table' and name='posts'")
if not cursor.fetchone():
    cursor.execute("CREATE TABLE posts (id INTEGER PRIMARY KEY, user_id varchar(32) NOT NULL, tweet_id varchar(32) NOT NULL, creator_id varchar(32) NOT NULL, time TIMESTAMP DEFAULT (datetime(CURRENT_TIMESTAMP,'localtime')))")
cursor.close()


def add_post(user_id, tweet_id, creator_id):
    cursor = connect.cursor()
    data_str = "('{}','{}','{}')".format(user_id, tweet_id, creator_id)
    cursor.execute("INSERT INTO posts(user_id,tweet_id,creator_id) VALUES "+data_str)
    cursor.close()
    connect.commit()

def get_col_values_of(key):
    cursor = connect.cursor()
    cursor.execute("SELECT DISTINCT {} FROM posts".format(key))
    result = cursor.fetchall()
    cursor.close()

    return result

def get_table():
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM posts")
    result = cursor.fetchall()
    cursor.close()

    return result