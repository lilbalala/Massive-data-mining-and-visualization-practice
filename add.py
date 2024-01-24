import json
import pymysql

#加载外部json数据
with open('school_names.json', mode='r',encoding='utf-8') as f:
    json_obj = json.load(f)

    #定义sql
    sql = "update school_base set school_id = %s where name = %s"

    with pymysql.connect(host='localhost', user='root', password='', database='spider', charset='utf8') as conn:
        with conn.cursor() as cur:
            schools = json_obj['data']['school']
            for school in schools:
                name = school['name']
                school_id = school['school_id']
                cur.execute(sql, (school_id, name))
        conn.commit()