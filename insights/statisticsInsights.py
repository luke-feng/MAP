import sqlite3
from collections import Counter
import os

cwd = os.getcwd()
grader_father = os.path.abspath(os.path.dirname(cwd)+os.path.sep+"..")

databasePath = grader_father+'/data/Economic.db'

# NOTE: start_time & end_time form : unix timestamp (10 numbers)


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

def getMaliciousEmail(conn, start_time, end_time):
    cursor = conn.cursor()
    # SELECT GROUP_CONCAT(MaliciousEmail) FROM AttackInformation

    malicious_email = cursor.execute("""SELECT GROUP_CONCAT(MaliciousEmail) FROM AttackInformation i \
        LEFT JOIN AttackFeatures f ON i.AttackID = f.AttackID WHERE f.StartTimeStamp>=? \
        AND f.StartTimeStamp<=?""", (start_time, end_time)).fetchall()

    if malicious_email[0][0] != None:

        malicious_email_list = malicious_email[0][0].split(",")
        occurrences = Counter(malicious_email_list).most_common()

    else:
        occurrences = None


    return occurrences

def getIPWatchlist(conn, start_time, end_time):
    cursor = conn.cursor()
    # SELECT GROUP_CONCAT(IPWatchlist) FROM AttackInformation

    ip_watchlist = cursor.execute("""SELECT GROUP_CONCAT(IPWatchlist) FROM AttackInformation i \
            LEFT JOIN AttackFeatures f ON i.AttackID = f.AttackID WHERE f.StartTimeStamp>=? \
            AND f.StartTimeStamp<=?""", (start_time, end_time)).fetchall()

    if ip_watchlist[0][0] != None:

        ip_watchlist_list = ip_watchlist[0][0].split(",")

        occurrences = Counter(ip_watchlist_list).most_common()

    else:
        occurrences = None

    return occurrences

def getFileHashWatchlist(conn, start_time, end_time):
    cursor = conn.cursor()
    # SELECT GROUP_CONCAT(FileHashWatchlist) FROM AttackInformation

    file_hash_watchlist = cursor.execute("""SELECT GROUP_CONCAT(FileHashWatchlist) FROM AttackInformation i \
        LEFT JOIN AttackFeatures f ON i.AttackID = f.AttackID WHERE f.StartTimeStamp>=? \
        AND f.StartTimeStamp<=?""", (start_time, end_time)).fetchall()

    if file_hash_watchlist[0][0] != None:

        file_hash_watchlist_list = file_hash_watchlist[0][0].split(",")

        occurrences = Counter(file_hash_watchlist_list).most_common()

    else:
        occurrences = None

    return occurrences

def getDomainWatchlist(conn, start_time, end_time):
    cursor = conn.cursor()
    # SELECT GROUP_CONCAT(DomainWatchlist) FROM AttackInformation

    domain_watchlist = cursor.execute("""SELECT GROUP_CONCAT(DomainWatchlist) FROM AttackInformation i \
             LEFT JOIN AttackFeatures f ON i.AttackID = f.AttackID WHERE f.StartTimeStamp>=? \
             AND f.StartTimeStamp<=?""", (start_time, end_time)).fetchall()

    if domain_watchlist[0][0] != None:

        domain_watchlist_list = domain_watchlist[0][0].split(",")

        occurrences = Counter(domain_watchlist_list).most_common()

    else:
        occurrences = None

    return occurrences

def getURLWatchlist(conn, start_time, end_time):
    cursor = conn.cursor()
    # SELECT GROUP_CONCAT(URLWatchlist) FROM AttackInformation

    url_watchlist = cursor.execute("""SELECT GROUP_CONCAT(URLWatchlist) FROM AttackInformation i \
             LEFT JOIN AttackFeatures f ON i.AttackID = f.AttackID WHERE f.StartTimeStamp>=? \
             AND f.StartTimeStamp<=?""", (start_time, end_time)).fetchall()
    if url_watchlist[0][0] != None:

        url_watchlist_list = url_watchlist[0][0].split(",")

        occurrences = Counter(url_watchlist_list).most_common()

    else:
        occurrences = None

    return occurrences

def getIncidentCategory(conn, start_time, end_time):
    cursor = conn.cursor()
    # SELECT IncidentCategory, count(IncidentCategory)

    incident_category = cursor.execute("""SELECT i.IncidentCategory, count(i.IncidentCategory) FROM AttackInformation i \
        LEFT JOIN AttackFeatures f ON i.AttackID = f.AttackID WHERE f.StartTimeStamp >=? \
        AND f.StartTimeStamp <=? GROUP BY i.IncidentCategory""", (start_time, end_time)).fetchall()

    return incident_category

def getSystemType(conn, start_time, end_time):
    cursor = conn.cursor()

    system_type = cursor.execute("""SELECT i.IncidentCategory, GROUP_CONCAT(i.SystemType) \
        From AttackInformation i LEFT JOIN AttackFeatures f ON i.AttackID = f.AttackID WHERE f.StartTimeStamp >=? \
        AND f.StartTimeStamp <=? GROUP BY i.IncidentCategory  """, (start_time, end_time)).fetchall()

    # for i in range(len(system_type)):
    #     system_type[i][1] = Counter(list(system_type[i][1].split(","))).most_common()

    system_type_dic = dict(system_type)

    for key in system_type_dic.keys():
        occurrences_per_incident_type = Counter(system_type_dic.get(key).split(",")).most_common()
        system_type_dic[key] = occurrences_per_incident_type

    # {incident_category: [('system_type', times), ('system_type', times), ('1', 1)],
    #       3           : [(    '1'      ,   1  ), (      '2'    ,   1  )]
    # }

    return system_type_dic

def getAssetType(conn, start_time, end_time):
    cursor = conn.cursor()

    asset_type = cursor.execute("""SELECT i.IncidentCategory, GROUP_CONCAT(i.AssetType) \
        From AttackInformation i LEFT JOIN AttackFeatures f ON i.AttackID = f.AttackID WHERE f.StartTimeStamp >=? \
        AND f.StartTimeStamp <=? GROUP BY i.IncidentCategory  """, (start_time, end_time)).fetchall()

    asset_type_dic = dict(asset_type)

    for key in asset_type_dic.keys():
        occurrences_per_incident_type = Counter(asset_type_dic.get(key).split(",")).most_common()
        asset_type_dic[key] = occurrences_per_incident_type

    return asset_type_dic


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

def getROSI(conn, start_time, end_time):
    cursor = conn.cursor()
    rosi = cursor.execute("""SELECT  i.IncidentCategory, i.MeasureDescription,  i.ROSI from Measures i \
        LEFT JOIN IncidentCategory f ON i.IncidentCategory = f.IncidentCategoryID \ 
        GROUP BY  i.IncidentCategory, i.MeasureDescription;""").fetchall()
    return rosi

def getNPV(conn, start_time, end_time):
    cursor = conn.cursor()
    npv = cursor.execute("""SELECT  i.IncidentCategory, i.MeasureDescription,  i.NPV from Measures i \
        LEFT JOIN IncidentCategory f ON i.IncidentCategory = f.IncidentCategoryID \ 
        GROUP BY  i.IncidentCategory, i.MeasureDescription;""").fetchall()
    return npv
