import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="fixy-db-vishnuap1711-eafd.j.aivencloud.com",
        port="21316",
        user="avnadmin",
        password="AVNS_ZNXoQVjW1IsdYW2bIpW",
        database="FixyDB"
    )
    return connection


