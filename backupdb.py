import shutil

# Backup database
shutil.copyfile("source.db", "backup.db")

print("Backup completed successfully!")
