from getFeatureFromFile import DDoSGridFeatures
import sqlite3
databasePath = 'D:/vsproject/secgrid/data/Economic.db'
jsonPath = 'D:/vsproject/secgrid/data/analysis/'
attackId = '7bcb9e6b370349eb573dde4457f8a0b3a0ac6436322d3e235a5b8fa62e8c28c3'


def connect_database(databasePath):
    """
    connect to the database
    :param databasePath: file path of the database you wanna connect
    :return conn: connected database instance
    """
    conn = sqlite3.connect(databasePath)
    print("Opened database successfully")
    return conn


def get_all_features(jsonPath, attackId):
    """
    get all general features from ddosgrid
    :param jsonPath: string format, which is the direction of local files(the analysis direction) 
    :param attackId: string format, which is the attact id, generated from miner module, md5 encrypted
    :return df: ddosgrid features instance
    """
    df = DDoSGridFeatures(jsonPath, attackId)
    return df


def insert_to_database(conn, df):
    """
    insert the features to the database
    :param conn: connected database instance
    :param df: ddosgrid features instance
    """
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO AttackFeatures (AttackID, StartTimeStamp, EndTimeStamp, Duration, NrOfIPpackets,\
    AttackSizeInBytes, NrOfSrcIps, NrOfDstIps, NrOfSrcPort, NrOfDsPort, Top5SrcIP, Top20DesPort,  TopHttpVerb, \
    TopHttpEndpoint,  TopBrowserOS, TopDevice) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);""", (df.id, df.StartTimeStamp, df.EndTimeStamp, df.Duration,
                                                                                              df.NrOfIPpackets, df.AttackSizeInBytes, df.NrOfSrcIps, df.NrOfDstIps, df.NrOfSrcPort, df.NrOfDsPort,
                                                                                              df.Top5SrcIP, df.Top20DesPort, df.TopHttpVerb, df.TopHttpEndpoint, df.TopBrowserOS, df.TopDevice))
    conn.commit()
    conn.close()


conn = connect_database(databasePath)
df = get_all_features(jsonPath, attackId)
insert_to_database(conn, df)
