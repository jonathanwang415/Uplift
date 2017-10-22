#!/usr/bin/env python3
import MySQLdb as mdb


with mdb.connect('localhost', 'root', 'simon', 'uplift') as cur:
    cur.execute('DROP TABLE IF EXISTS personalityTable')
    cur.execute('DROP TABLE IF EXISTS foodnutrition')
    cur.execute('DROP TABLE IF EXISTS disease')

    cur.execute('CREATE TABLE personalityTable(id INT PRIMARY KEY AUTO_INCREMENT, phenotype_name VARCHAR(150), zero VARCHAR(100), one VARCHAR(100), two VARCHAR(100), three VARCHAR(100), four VARCHAR(100), s_one VARCHAR(1000), s_two VARCHAR(1000), s_three VARCHAR(1000), s_four VARCHAR(1000) )')
    
    # N_oneSug = 'fdsafgasg'
    # N_twoSug = 'fdsafgasg'
    # N_threeSug = 'fdsafgasg'
    # N_fourSug = 'fdsafgasg'
    cur.execute('INSERT INTO personalityTable(phenotype_name, zero, one, two, three, four) VALUES(\'Neuroticism\', \'Not easily neurotic\', \'slightly not easily neurotic\', \'intermediatly easily neurotic\', \'somewhat easily neurotic\', \'easily neurotic\', \'N_oneSug\', \'N_twoSug\', \'N_threeSug\', \'N_fourSug\')')

    # D_oneSug = 'fdsafgasg'
    # D_twoSug = 'fdsafgasg'
    # D_threeSug = 'fdsafgasg'
    # D_fourSug = 'fdsafgasg'
    cur.execute('INSERT INTO personalityTable(phenotype_name, zero, one, two, three, four) VALUES(\'Depression\', \'Not easily depressed\', \'slightly not easily depressed\', \'intermediatly easily depressed\', \'somewhat prone to depression\', \'prone to depression\', \'D_oneSug\', \'D_twoSug\', \'D_threeSug\', \'D_fourSug\')')
    
    cur.execute('CREATE TABLE foodnutrition(id INT PRIMARY KEY AUTO_INCREMENT, phenotype_name VARCHAR(150), zero VARCHAR(100), one VARCHAR(100), two VARCHAR(100), three VARCHAR(100), four VARCHAR(100), s_one VARCHAR(1000), s_two VARCHAR(1000), s_three VARCHAR(1000), s_four VARCHAR(1000) )')
    
    F_oneSug = 'Consider including more greens (broccoli, romaine lettuce, spinach) in your diet'
    F_twoSug = 'Consider eating more avocados'
    F_threeSug = 'Consider eating citrus fruits'
    F_fourSug = 'Consider eating more beans, peas, and lentils'
    cur.execute('INSERT INTO foodnutrition(phenotype_name, zero, one, two, three, four) VALUES(\'Folate\', \'Prone to Folate deficiency\', \'somewhat prone to Folate deficiency\', \'intermediatly prone to Folate deficiency\', \'slightly prone to Folate deficiency\', \'not likely to be prone to Folate deficiency\', \'F_oneSug\', \'F_twoSug\', \'F_threeSug\', \'F_fourSug\')')
    
    C_oneSug = 'Consider eating more kelp.'
    C_twoSug = 'Consider including sardines in your diet.'
    C_threeSug = 'Consider adding sesame seeds to your meals'
    C_fourSug = 'Consider drinking more milk'
    cur.execute('INSERT INTO foodnutrition(phenotype_name, zero, one, two, three, four) VALUES(\'Calcium\', \'Prone to Calcium deficiency\', \'somewhat prone to Calcium deficiency\', \'intermediatly prone to Calcium deficiency\', \'slightly prone to Calcium deficiency\', \'not likely to be prone to Calcium deficiency\', \'C_oneSug\', \'C_twoSug\', \'C_threeSug\', \'C_fourSug\')')

    cur.execute('CREATE TABLE disease(id INT PRIMARY KEY AUTO_INCREMENT, phenotype_name VARCHAR(150), zero VARCHAR(100), one VARCHAR(100), two VARCHAR(100), three VARCHAR(100), four VARCHAR(100), s_one VARCHAR(1000), s_two VARCHAR(1000), s_three VARCHAR(1000), s_four VARCHAR(1000) )')
    
    R_oneSug = 'Stay at a healthy weight and avoid weight gain around the midsection may help lower your risk'
    R_twoSug = 'Increase intensity and amount of physical activity on a daily basis'
    R_threeSug = 'Limit red and processed meats while making an attempt to eat more vegetables and fruits'
    R_fourSug = 'Avoid drinking too much acholoic beverages'
    cur.execute('INSERT INTO disease(phenotype_name, zero, one, two, three, four) VALUES(\'Colorectal Cancer\', \'Not very prone to Colorectal Cancer\', \'Slightly prone to Colorectal Cancer\', \'intermediatly prone to Colorectal Cancer\', \'Prone to Colorectal Cancer\', \'Highly prone to Colorectal Cancer\', \'R_oneSug\', \'R_twoSug\', \'R_threeSug\', \'R_fourSug\')')
    
    P_oneSug = 'Watch your calcium intake and do not take supplemental doses far about the recommended daily allowance'
    P_twoSug = 'Eat more fish (evidence and studies suggest that fish can help protect against prostate cancer with good fats'
    P_threeSug = 'Incorporating more cooked tomatoes (cooked with olive) into the daily meals'
    P_fourSug = 'Seek medical treatment for stress, high blood pressure, diabetes, high cholesterol, and depression'
    cur.execute('INSERT INTO disease(phenotype_name, zero, one, two, three, four) VALUES(\'Prostate Cancer\', \'Not very prone to Prostate Cancer\', \'Slightly prone to Prostate Cancer\', \'intermediatly prone to Prostate Cancer\', \'Prone to Prostate Cancer\', \'Highly prone to Prostate Cancer\', \'P_oneSug\', \'P_twoSug\', \'P_threeSug\', \'P_fourSug\')')


