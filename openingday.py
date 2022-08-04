# file location  \\staff-l1.avc.edu\FastWebDocs\hello.avc.edu\docs

import cx_Oracle


class OracleConnect:
    def __init__(self):

        self.user = 'generic_user'
        self.password = 'N07h1ng1553cur3bu7l0ngp455w0rd5c4nb3fun!'
        self.dsn_tns = cx_Oracle.makedsn('bandb-at1.test.avc.edu', '1521', 'avcprep')
        self.engine_connection = self.connection()

    def connection(self):
        try:
            _connection = cx_Oracle.connect(self.user, self.password,
                                            dsn=self.dsn_tns,
                                            encoding="UTF-8")
            return _connection

        except Exception as e:
            print(e)

    def db_query(self, _select, _from, _where):
        _select = f"""select  {_select}"""
        _from = f"""from {_from}"""
        _where = (f"""where {_where}""" if _where else '')
        _query = f"""{_select} {_from} {_where} """
        app_data = self.execute_sql_query(_query)

        return app_data

    def execute_sql_query(self, _query):
        print(_query)
        with self.engine_connection.cursor() as _cur:
            _cur.execute(_query)
            app_data = _cur.fetchall()

        return app_data

    def db_insert(self, my_insert, my_values):
        _insert = f"""into {my_insert}"""
        _value = f"""values({my_values})"""
        insert_statement = f"""insert {_insert} {_value}"""
        _result = self.execute_sql_insert(insert_statement)

        return _result

    def execute_sql_insert(self, insert_statement):
        print(insert_statement)
        with self.engine_connection.cursor() as _cur:
            try:
                _cur.execute(insert_statement)
                _result = self.engine_connection.commit()
            except Exception as e:
                self.engine_connection.rollback()
                return e

        return _result
