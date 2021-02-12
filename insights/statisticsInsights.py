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

    loss_duration = cursor.execute("""SELECT  i.IncidentCategory, AVG(i.LossDuration,) from AttackInformation i \
        LEFT JOIN AttackFeatures f ON i.AttackID = f.AttackID WHERE f.StartTimeStamp>=? and f.StartTimeStamp<=? \
        GROUP BY i.IncidentCategory;""", (start_time, end_time)).fetchall()
    return loss_duration


def getLossProperty(conn, start_time, end_time):
    cursor = conn.cursor()
    loss_property = cursor.execute("""SELECT  i.LossProperty,  i.IncidentCategory,COUNT(i.AttackID) from AttackInformation i \
        LEFT JOIN AttackFeatures f ON i.AttackID = f.AttackID WHERE f.StartTimeStamp>=? and f.StartTimeStamp<=? \
        GROUP BY  i.LossProperty,  i.IncidentCategory;""", (start_time, end_time)).fetchall()
    return loss_property


def getAttackerInfrastructure(conn, start_time, end_time):
    cursor = conn.cursor()
    attacker_infrastructure = cursor.execute("""SELECT  i.AttackerInfrastructure,  i.IncidentCategory,COUNT(i.AttackID) from AttackInformation i \
        LEFT JOIN AttackFeatures f ON i.AttackID = f.AttackID WHERE f.StartTimeStamp>=? and f.StartTimeStamp<=? \
        GROUP BY  i.AttackerInfrastructure,  i.IncidentCategory;""", (start_time, end_time)).fetchall()
    return attacker_infrastructure


def getThreatActorType(conn, start_time, end_time):
    cursor = conn.cursor()
    threat_actor_type = cursor.execute("""SELECT  i.ThreatActorType,  i.IncidentCategory,COUNT(i.AttackID) from AttackInformation i \
        LEFT JOIN AttackFeatures f ON i.AttackID = f.AttackID WHERE f.StartTimeStamp>=? and f.StartTimeStamp<=? \
        GROUP BY  i.ThreatActorType,  i.IncidentCategory;""", (start_time, end_time)).fetchall()
    return threat_actor_type


def getAttackerTool(conn, start_time, end_time):
    cursor = conn.cursor()
    attacker_tool = cursor.execute("""SELECT  i.AttackerTool,  i.IncidentCategory,COUNT(i.AttackID) from AttackInformation i \
        LEFT JOIN AttackFeatures f ON i.AttackID = f.AttackID WHERE f.StartTimeStamp>=? and f.StartTimeStamp<=? \
        GROUP BY  i.AttackerTool,  i.IncidentCategory;""", (start_time, end_time)).fetchall()
    return attacker_tool


def getMalwareType(conn, start_time, end_time):
    cursor = conn.cursor()
    malware_type = cursor.execute("""SELECT  i.MalwareType,  i.IncidentCategory,COUNT(i.AttackID) from AttackInformation i \
        LEFT JOIN AttackFeatures f ON i.AttackID = f.AttackID WHERE f.StartTimeStamp>=? and f.StartTimeStamp<=? \
        GROUP BY  i.MalwareType,  i.IncidentCategory;""", (start_time, end_time)).fetchall()
    return malware_type