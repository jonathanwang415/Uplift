#!/usr/bin/env python3
import MySQLdb as mdb
from report_generator import PHENOTYPES, driver
driver.close()

phenotypes = []
for category in ['trait', 'personality', 'allergy', 'disease', 'food_and_nutrition']:
    phenotypes += list(PHENOTYPES[category])
phenotypes.sort()

with mdb.connect('localhost', 'root', 'toor', 'userdb') as cur:
    cur.execute('DROP TABLE IF EXISTS users')
    cur.execute('CREATE TABLE users(name varchar(100) NOT NULL, state INT NOT NULL DEFAULT 0, phone_number VARCHAR(20) NOT NULL PRIMARY KEY);')

    cur.execute('DROP TABLE IF EXISTS scores')
    query = 'CREATE TABLE scores(' + ' TINYINT, '.join(phenotypes).replace('-', '_') + ' TINYINT, phone_number VARCHAR(20) NOT NULL PRIMARY KEY);'
    cur.execute(query)

    cur.execute('DROP TABLE IF EXISTS foodnutrition')
    cur.execute('DROP TABLE IF EXISTS disease')
    cur.execute('DROP TABLE IF EXISTS personality')
    cur.execute(('CREATE TABLE foodnutrition(id INT PRIMARY KEY AUTO_INCREMENT, phenotype_name VARCHAR(150), zero VARCHAR(100),'
                'one VARCHAR(100), two VARCHAR(100), three VARCHAR(100), four VARCHAR(100), s_one VARCHAR(1000), s_two VARCHAR(1000),' 
                's_three VARCHAR(1000), s_four VARCHAR(1000) )'))
    
    F_oneSug = 'Consider including more greens (broccoli, romaine lettuce, spinach) in your diet.'
    F_twoSug = 'Consider eating more avocados to lower your chances of having Folate deficiency.'
    F_threeSug = 'Consider eating citrus fruits.'
    F_fourSug = 'Consider eating more beans, peas, and lentils.'
    cur.execute(('INSERT INTO foodnutrition(phenotype_name, zero, one, two, three, four, s_one, s_two, s_three, s_four) VALUES(\'folate\','
                '\'Prone to Folate deficiency.\', \'Somewhat prone to Folate deficiency.\', \'Intermediatly prone to Folate deficiency.\','
                '\'Slightly prone to Folate deficiency.\', \'Not likely to be prone to Folate deficiency.\','
                 '\'{}\', \'{}\', \'{}\', \'{}\')'.format(F_oneSug, F_twoSug, F_threeSug, F_fourSug)))
    
    C_oneSug = 'Consider eating more kelp.'
    C_twoSug = 'Consider including sardines in your diet.'
    C_threeSug = 'Consider adding sesame seeds to your meals.'
    C_fourSug = 'Consider drinking more milk.'
    cur.execute(('INSERT INTO foodnutrition(phenotype_name, zero, one, two, three, four, s_one, s_two, s_three, s_four) VALUES(\'calcium\','
                '\'Prone to Calcium deficiency.\', \'Somewhat prone to Calcium deficiency.\', \'Intermediatly prone to Calcium deficiency.\',' 
                '\'Slightly prone to Calcium deficiency.\', \'Not likely to be prone to Calcium deficiency.\','
                 '\'{}\', \'{}\', \'{}\', \'{}\')'.format(C_oneSug, C_twoSug, C_threeSug, C_fourSug)))

    cur.execute(('CREATE TABLE disease(id INT PRIMARY KEY AUTO_INCREMENT, phenotype_name VARCHAR(150), zero VARCHAR(100), one VARCHAR(100),'
                'two VARCHAR(100), three VARCHAR(100), four VARCHAR(100), s_one VARCHAR(1000), s_two VARCHAR(1000), s_three VARCHAR(1000),' 
                's_four VARCHAR(1000) )'))
    
    R_oneSug = 'Stay at a healthy weight and avoid weight gain around the midsection which may help lower your risk.'
    R_twoSug = 'Increase intensity and amount of physical activity on a daily basis.'
    R_threeSug = 'Limit red and processed meats while making an attempt to eat more vegetables and fruits.'
    R_fourSug = 'Avoid drinking too much acholoic beverages.'
    cur.execute(('INSERT INTO disease(phenotype_name, zero, one, two, three, four, s_one, s_two, s_three, s_four) VALUES(\'colorectal_cancer\',' 
                '\'Not very prone to Colorectal Cancer.\', \'Slightly prone to Colorectal Cancer.\', \'Intermediatly prone to Colorectal Cancer.\',' 
                '\'Prone to Colorectal Cancer.\', \'Highly prone to Colorectal cancer.\',' 
                '\'{}\', \'{}\', \'{}\', \'{}\')'.format(R_oneSug, R_twoSug, R_threeSug, R_fourSug)))
    
    P_oneSug = 'Watch your calcium intake and do not take supplemental doses far about the recommended daily allowance'
    P_twoSug = 'Eat more fish (evidence and studies suggest that fish can help protect against prostate cancer with good fats'
    P_threeSug = 'Incorporating more cooked tomatoes (cooked with olive) into the daily meals'
    P_fourSug = 'Seek medical treatment for stress, high blood pressure, diabetes, high cholesterol, and depression'
    cur.execute(('INSERT INTO disease(phenotype_name, zero, one, two, three, four, s_one, s_two, s_three, s_four) VALUES(\'prostate_cancer\',' 
                '\'Not very prone to Prostate Cancer.\', \'Slightly prone to Prostate Cancer.\', \'Intermediatly prone to Prostate Cancer.\',' 
                '\'Prone to Prostate Cancer.\', \'Highly prone to Prostate Cancer.\',' 
                '\'{}\', \'{}\', \'{}\', \'{}\')'.format(P_oneSug, P_twoSug, P_threeSug, P_fourSug)))

    Di_oneSug = 'Drink a large glass of water 10 minutes before your meal so you feel less hungry. This will help moderate your portion sizes.'
    Di_twoSug = 'Try filling your plate with 1/4 protien, 1/4 grains, 1/2 vegetables and fruit, dairy low-fat or skim milk.'
    Di_threeSug = 'Turn up the music and jam while doing household chores to help with being active. Do not like chores? March in place while wathing tv.'
    Di_fourSug = 'Here is a yummy meal to try: Serve your favorite vegetable and a sald with low-fat macaroni and cheese.'
    cur.execute(('INSERT INTO disease(phenotype_name, zero, one, two, three, four, s_one, s_two, s_three, s_four) VALUES(\'type_2_diabetes\',' 
                '\'Lower risk of Type-2-Diabetes.\', \'Slightly prone to Type-2-Diabetes\', \'Intermediatly prone to Type-2-Diabetes\',' 
                '\'Prone to Type-2-Diabetes\', \'Highly prone to Type-2-Diabetes\',' 
                '\'{}\', \'{}\', \'{}\', \'{}\')'.format(Di_oneSug, Di_twoSug, Di_threeSug, Di_fourSug)))
    
    L_oneSug = 'Stay away from tobacco. If you stop smoking, your damaged lung tissue slowly starts to repair itself.'
    L_twoSug = 'Avoid Radon. You can reduce your exposure by having your home tested or treated.'
    L_threeSug = 'Some people who get lung cancer do not have any clear risk factors, Although most lung cancers can be prevented, there are still some who cannot'
    L_fourSug = 'Drinking a cup of Green Tea has been shown to prevent damage to cells. Maybe do some more research on this while drinking a cup of tea!'
    cur.execute(('INSERT INTO disease(phenotype_name, zero, one, two, three, four, s_one, s_two, s_three, s_four) VALUES(\'lung_cancer\',' 
                '\'Lower risk of Lung Cancer.\', \'Slightly prone to Lung Cancer.\', \'Intermediatly prone to Lung Cancer.\',' 
                '\'Prone to lung cancer.\', \'Highly prone to lung cancer.\',' 
                '\'{}\', \'{}\', \'{}\', \'{}\')'.format(L_oneSug, L_twoSug, L_threeSug, L_fourSug)))
    
    cur.execute(('CREATE TABLE personality(id INT PRIMARY KEY AUTO_INCREMENT, phenotype_name VARCHAR(150), zero VARCHAR(100),'
                'one VARCHAR(100), two VARCHAR(100), three VARCHAR(100), four VARCHAR(100), s_one VARCHAR(1000), s_two VARCHAR(1000),' 
                's_three VARCHAR(1000), s_four VARCHAR(1000) )'))
    
    N_oneSug = ('You are not alone in having neurotic feelings. Alot of people are somewhat neurotic and are doing a lot of damage because they '
                'do not seek treatment or help.')
    N_twoSug = ('If you are having heavy feelings of anxiety and depressed mood take a small break and go on a walk to help clear your mind.' 
                'Try not to think about what is upsetting you while you walk.')
    N_threeSug = ('Breathing exercises like diaphragmatic breathing, meditation, and progressive muscle relaxation helps you '
                'distance yourself from emotions and see reality in a calmer perspective. Give them a try by following a youtube video.')
    N_fourSug = 'It is normal to need to take one day off...or two...Try taking a day off and treat yourself to an activity you enjoy.'

    cur.execute(('INSERT INTO personality(phenotype_name, zero, one, two, three, four, s_one, s_two, s_three, s_four) VALUES(\'neuroticism\','
                '\'Not easily Neurotic.\', \'Slightly not easily Neurotic.\', \'Intermediatly easily Neurotic.\', \'Somewhat easily Neurotic\','
                 '\'Easily Neurotic\', \'{}\', \'{}\', \'{}\', \'{}\' )'.format(N_oneSug, N_twoSug, N_threeSug, N_fourSug)))

    D_oneSug = ('You are not alone in having feelings of depression. Having a Journal to write negative thoughts and then scribbling those '
                'negative thoughts and writing down positive one is a good exercise to train your mind to think more positively.'
                'You should try it')
    D_twoSug = ('If you are having heavy feelings of depressed mood take a small break and go on a walk to help clear your mind.' 
                'Try not to think about what is upsetting you while you walk.')
    D_threeSug = ('Breathing exercises like diaphragmatic breathing, meditation, and progressive muscle relaxation helps you '
                'distance yourself from emotions and see reality in a calmer perspective. Give them a try by following a youtube video.')
    D_fourSug = 'It is normal to need to take one day off...or two...Try taking a day off and treat yourself to an activity you enjoy.'
    
    cur.execute(('INSERT INTO personality(phenotype_name, zero, one, two, three, four, s_one, s_two, s_three, s_four) VALUES(\'depression\', \'Not easily Depressed.\',' 
                '\'Slightly not easily Depressed.\', \'Intermediatly easily Depressed.\', \'Somewhat prone to Depression.\','
                 '\'Prone to Depression.\', \'{}\', \'{}\', \'{}\', \'{}\')'.format(D_oneSug, D_twoSug, D_threeSug, D_fourSug)))

