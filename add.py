import psycopg2
import pickle


def add():
    with open('names.data', 'rb') as filehandle:
        # read the data as binary data stream
        names = pickle.load(filehandle)

    with open('embeddings.data', 'rb') as filehandle:
        # read the data as binary data stream
        embeddings = pickle.load(filehandle)

    try:
        connection = psycopg2.connect(user="jhcczpalikdmre",
                                      password="9c13f335038b70092acfb67e5ae100cc94f990400d60be83d7166c272a141cf2",
                                      host="ec2-54-247-94-127.eu-west-1.compute.amazonaws.com",
                                      port="5432",
                                      database="d9qqpi5k7s7ek2")

        cursor = connection.cursor()
        for n, e in zip(names, embeddings):
            postgres_insert_query = "INSERT INTO \"Person\" (name, embeddings) VALUES (%s,%s)"
            record_to_insert = (n, e.tolist())
            cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


if __name__ == '__main__':
    add()
