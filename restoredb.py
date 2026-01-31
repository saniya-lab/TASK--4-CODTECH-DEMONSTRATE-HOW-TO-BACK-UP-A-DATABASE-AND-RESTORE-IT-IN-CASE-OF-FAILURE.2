import shutil

# Restore database from backup
shutil.copyfile("backup.db", "source.db")

print("Database restored successfully!")
