import sqlite3
from collections import Counter
import os
import EconomicImpacts as EI

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

def setLoss(conn, start_time, end_time,incident_category):
    cursor = conn.cursor()
    loss_list= cursor.execute("""SELECT CostofRepair,CorporateIncomeLoss,OrganizationProductiveLoss,CostofEquipmentReplacement,SLALoss,IndirectLoss,TimetoRepair_without,TimetoDetect_without from AttackInformation i 
LEFT JOIN AttackFeatures f ON i.AttackID = f.AttackID WHERE i.IncidentCategory==?
GROUP BY  i.IncidentCategory;""",(incident_category,)).fetchall()
    for loss in loss_list:
        l1,l2,l3,l=EI.getLoss(loss)
    cursor.execute("""UPDATE AttackInformation SET L1=?,L2=?,L3=?,Loss_without_measure=? WHERE IncidentCategory=?;""", (l1,l2,l3,l,incident_category,))
    cursor.close()

def setCost(conn, start_time, end_time,incident_category):
    cursor = conn.cursor()
    cost_list= cursor.execute("""SELECT CostofRepair,CorporateIncomeLoss,OrganizationProductiveLoss,CostofEquipmentReplacement,SLALoss,IndirectLoss,TimetoRepair_without,TimetoDetect_without from AttackInformation i 
LEFT JOIN AttackFeatures f ON i.AttackID = f.AttackID WHERE i.IncidentCategory==?
GROUP BY  i.IncidentCategory;""",(incident_category,)).fetchall()
    for cost in cost_list:
        l1,l2,l3,l=EI.getLoss(cost)
    cursor.execute("""UPDATE AttackInformation SET L1=?,L2=?,L3=?,Loss_without_measure=? WHERE IncidentCategory=?;""", (l1,l2,l3,l,incident_category,))
    cursor.close()

def setRisk(conn, start_time, end_time,incident_category):
    cursor = conn.cursor()
    r0= cursor.execute("""SELECT CostofRepair,CorporateIncomeLoss,OrganizationProductiveLoss,CostofEquipmentReplacement,SLALoss,IndirectLoss,TimetoRepair_without,TimetoDetect_without from AttackInformation i 
LEFT JOIN AttackFeatures f ON i.AttackID = f.AttackID WHERE i.IncidentCategory==?
GROUP BY  i.IncidentCategory;""",(incident_category,)).fetchall()
    for cost in cost_list:
        l1,l2,l3,l=EI.getLoss(cost)
    cursor.execute("""UPDATE AttackInformation SET L1=?,L2=?,L3=?,Loss_without_measure=? WHERE IncidentCategory=?;""", (l1,l2,l3,l,incident_category,))
    cursor.close()


conn=connect_database(databasePath)
setLoss(conn,1613131216,1613191218,1)