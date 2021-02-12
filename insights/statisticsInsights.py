import sqlite3

databasePath = 'D:/git/MAP/data/Economic.db'


def connect_database(databasePath):
    """
    connect to the database
    :param databasePath: file path of the database you wanna connect
    :return conn: connected database instance
    """
    conn = sqlite3.connect(databasePath)
    return conn


def getImpactRating(conn, start_time, end_time):
    cursor = conn.cursor()
    # SELECT i.ImpactRating, COUNT(i.AttackID) from AttackInformation i LEFT JOIN AttackFeatures f ON i.AttackID = f.AttackID WHERE f.StartTimeStamp=? and f.EndTimeStamp=? GROUP BY i.ImpactRating, f.AttackMonth

    impact_rating = cursor.execute("""SELECT i.ImpactRating, f.AttackMonth, COUNT(i.AttackID) from AttackInformation i \
    LEFT JOIN AttackFeatures f ON i.AttackID = f.AttackID WHERE f.StartTimeStamp>=? and f.StartTimeStamp<=? \
    GROUP BY i.ImpactRating, f.AttackMonth;""", (start_time, end_time)).fetchall()
    return impact_rating


def getIncidentEffect(conn, start_time, end_time):
    cursor = conn.cursor()
    # SELECT i.IncidentEffect, COUNT(i.AttackID) from AttackInformation i LEFT JOIN AttackFeatures f ON i.AttackID = f.AttackID WHERE f.StartTimeStamp>=? and f.StartTimeStamp<=? GROUP BY i.IncidentEffect

    incident_effect = cursor.execute("""SELECT i.IncidentEffect, COUNT(i.AttackID) from AttackInformation i LEFT JOIN \
    AttackFeatures f ON i.AttackID = f.AttackID WHERE f.StartTimeStamp>=? and f.StartTimeStamp<=? GROUP BY i.IncidentEffect;""", (start_time, end_time)).fetchall()
    return incident_effect


def getSecurityCompromise(conn, start_time, end_time):
    cursor = conn.cursor()
    # SELECT i.SecurityCompromise, i.IncidentCategory, COUNT(i.AttackID) from AttackInformation i LEFT JOIN AttackFeatures f ON i.AttackID = f.AttackID WHERE f.StartTimeStamp>=? and f.StartTimeStamp<=? GROUP BY i.SecurityCompromise,  i.IncidentCategory

    security_compromise = cursor.execute("""SELECT i.SecurityCompromise, i.IncidentCategory, COUNT(i.AttackID) from \
    AttackInformation i LEFT JOIN AttackFeatures f ON i.AttackID = f.AttackID WHERE f.StartTimeStamp>=? and \
    f.StartTimeStamp<=? GROUP BY i.SecurityCompromise,  i.IncidentCategory;""", (start_time, end_time)).fetchall()
    return security_compromise


def getLossDuration(conn, start_time, end_time):
    cursor = conn.cursor()
    # SELECT  i.IncidentCategory, Average(i.LossDuration,) from AttackInformation i LEFT JOIN AttackFeatures f ON i.AttackID = f.AttackID WHERE f.StartTimeStamp>=? and f.StartTimeStamp<=? GROUP BY i.IncidentCategory

    loss_duration = cursor.execute("""SELECT  i.IncidentCategory, Average(i.LossDuration,) from AttackInformation i \
        LEFT JOIN AttackFeatures f ON i.AttackID = f.AttackID WHERE f.StartTimeStamp>=? and f.StartTimeStamp<=? \
        GROUP BY i.IncidentCategory;""", (start_time, end_time)).fetchall()
    return loss_duration
