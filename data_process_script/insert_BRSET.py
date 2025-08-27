from data_access.read_db import execute_sql, execute_select
from data_access.db_conn import engine
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, String, Float, Integer, text

# 读取CSV文件
csv_file_path = 'D:\IDLE\projects\med-data\source-data\labels_brset.csv'


df = pd.read_csv(csv_file_path)

# 定义数据库表的名称
table_name = 'brest'

# 获取列名和数据类型（全部设为字符串类型）
columns = df.columns.tolist()
# 对于MySQL，使用反引号或不用引号
column_defs = [f"`{col}` VARCHAR(255)" for col in columns]

# 创建表的SQL语句
create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} (\n"
create_table_sql += ",\n".join(column_defs)
create_table_sql += "\n);"

# 执行创建表的SQL
execute_sql(create_table_sql)
print(f"Table '{table_name}' created successfully.")

# 使用pandas直接写入数据库
from sqlalchemy.types import VARCHAR
df.to_sql(
    name=table_name,
    con=engine,
    if_exists='replace',  # 如果表存在则替换
    index=False,
    dtype={col: VARCHAR(255) for col in df.columns}
)

print(f"Successfully inserted {len(df)} records into {table_name}")


