CREATE TABLE avc.opening_day_login (
                                        id NUMBER GENERATED BY DEFAULT AS IDENTITY,
                                        user_name VARCHAR2(50),
                                        login_time DATE,
                                        PRIMARY KEY(id)
);

insert into opening_day_login(user_name, login_time) values('rwalden', sysdate)