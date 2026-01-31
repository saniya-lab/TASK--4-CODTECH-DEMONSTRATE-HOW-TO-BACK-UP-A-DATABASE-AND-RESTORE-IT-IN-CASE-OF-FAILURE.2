# TASK--4-CODTECH-DEMONSTRATE-HOW-TO-BACK-UP-A-DATABASE-AND-RESTORE-IT-IN-CASE-OF-FAILURE.2
Company: CODTECH IT SOLUTIONS

Name: Shaik Saniya Sulthan

Intern ID: CTIS3401

Domain: SQL

Duration: 4 Weeks

Mentor: Neela Santosh

Project Description – Task 4: Database Backup and Restore Using Python and SQLite

The primary objective of Task-4 was to demonstrate the process of backing up a database and restoring it in the event of failure using Python and SQLite. In modern software development and data management, ensuring the security and reliability of data is one of the most critical responsibilities. Database backups play a vital role in disaster recovery, preventing permanent loss of data in cases such as accidental deletion, corruption, hardware failure, or software issues. Similarly, the ability to restore a database quickly and accurately is essential to maintain business continuity and ensure that applications continue to function correctly.

For this project, Python was chosen as the programming language due to its simplicity, flexibility, and the availability of built-in modules such as sqlite3 for interacting with SQLite databases. SQLite is a lightweight, file-based database system that is ideal for small to medium-scale applications and learning exercises. This project provides practical experience in handling backup and restore operations in a controlled environment, which can later be applied to larger-scale enterprise databases such as MySQL, PostgreSQL, or SQL Server.

The project began with the creation of a sample database named source.db. Using Python scripts, a table called employees was created within the database with three columns: id, name, and department. Sample records were inserted into the table, representing real-world employee data. This initial step ensured that there was meaningful data to work with and provided a baseline for verifying the backup and restore process. The creation of the source database also demonstrated the ability to use Python to interact with SQLite, including table creation and data insertion operations.

Once the database was created, the next step was to implement a backup mechanism. In this project, the backup was performed using Python’s shutil module, which allows file-level copying. The source.db file was copied to a new file named backup.db, creating an exact replica of the original database. This step ensures that, in the event of a failure, the backup file can serve as a reliable copy to restore the original database. SQLite also provides a built-in backup() function that can be used for larger or more complex databases, but the file copy method is simple, efficient, and ideal for this demonstration.

To simulate a real-world failure scenario, the original source.db was deliberately deleted or renamed. This simulated situations such as accidental deletion or database corruption. Following this, the restore process was executed by copying the backup file (backup.db) back to source.db. This effectively recreated the original database, including all tables, structures, and data. The restoration process demonstrated that with a reliable backup, data can be recovered quickly and accurately, minimizing potential disruptions.

Finally, a verification step was implemented using Python. The script connected to the restored database and fetched all records from the employees table. By comparing the restored data with the original records, it was confirmed that all data was preserved and the database integrity was maintained. This step is crucial in real-world scenarios to ensure that no data is lost or corrupted during the backup or restoration process.

Through this task, several key concepts were reinforced, including data reliability, disaster recovery, backup strategies, and database integrity verification. The project not only demonstrated technical skills in Python and SQLite but also emphasized the importance of planning and executing database backup and restoration in a systematic manner. Overall, this task successfully illustrates the practical steps needed to protect data and maintain business continuity in any software or database system.

Technologies Used: Python 3, SQLite3, Windows OS

Outcome: The backup and restore process was executed successfully. All data was preserved during backup, and the restored database contained identical records to the original. This demonstrates a reliable method for disaster recovery and data integrity assurance.

OUTPUT:
<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/7df738dd-7877-4604-b732-83e51587fd52" />

