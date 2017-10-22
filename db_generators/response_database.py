#!/usr/bin/env python3
import MySQLdb as mdb


with mdb.connect('localhost', 'abi', 'abi123', 'uplift') as cur:
    cur.execute('DROP TABLE IF EXISTS personality')
    cur.execute('CREATE TABLE personality(id INT PRIMARY KEY AUTO_INCREMENT, phenotype_name VARCHAR(150), zero VARCHAR(100), one VARCHAR(100), two VARCHAR(100), three VARCHAR(100), four VARCHAR(100), s_one VARCHAR(1000), s_two VARCHAR(1000), s_three VARCHAR(1000), s_four VARCHAR(1000) )')
    cur.execute('INSERT INTO personality(phenotype_name, zero, one, two, three, four) VALUES(\'Neuroticism\', \'Not easily neurotic\', \'slightly not easily neurotic\', \'intermediatly easily neurotic\', \'somewhat easily neurotic\', \'easily neurotic\')')
    cur.execute('INSERT INTO personality(phenotype_name, zero, one, two, three, four) VALUES(\'Depression\', \'Not easily depressed\', \'slightly not easily depressed\', \'intermediatly easily depressed\', \'somewhat prone to depression\', \'prone to depression\')')
