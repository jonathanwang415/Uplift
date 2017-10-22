#!/usr/bin/env python3
import MySQLdb as mdb


with mdb.connect('localhost', 'root', 'toor', 'userdb') as cur:
    cur.execute('DROP TABLE IF EXISTS personality')
    cur.execute(('CREATE TABLE personality(id INT PRIMARY KEY AUTO_INCREMENT, phenotype_name VARCHAR(150), zero VARCHAR(100),'
                'one VARCHAR(100), two VARCHAR(100), three VARCHAR(100), four VARCHAR(100), s_one VARCHAR(1000), s_two VARCHAR(1000),' 
                's_three VARCHAR(1000), s_four VARCHAR(1000) )'))
    cur.execute(('INSERT INTO personality(phenotype_name, zero, one, two, three, four) VALUES(\'Neuroticism\', \'Not easily neurotic\',' 
                '\'slightly not easily neurotic\', \'intermediatly easily neurotic\', \'somewhat easily neurotic\', \'easily neurotic\')'))
    cur.execute(('INSERT INTO personality(phenotype_name, zero, one, two, three, four, s_one, s_two, s_three, s_four) VALUES(\'Depression\', \'Not easily depressed\',' 
                '\'slightly not easily depressed\', \'intermediatly easily depressed\', \'somewhat prone to depression\', \'prone to depression\','
                '\'you are not alone in having neurotic feelings. Alot of people are somewhat neurotic and are doing a lot of damage because they '
                'do not seek treatment or help.\', \'If you are having heavy feelings of anxiety and depressed mood '
                'take a small break and go on a walk to help clear your mind. Try not to think about what is upsetting you while you walk.\', '
                '\'Breathing exercises like diaphragmatic breathing, meditation, and progressive muscle relaxation helps you '
                'distance yourself from emotions and see reality in a calmer perspective. Give them a try by following a youtube video.\','
                '\'It is normal to need to take one day off...or two...Try taking a day off and treat yourself to an activity you enjoy.\' )'))

