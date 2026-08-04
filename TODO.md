g# Rental Home Project - Resolution TODO

## Plan Steps (from approved plan):
- [x] 1. Create TODO.md for tracking
- [x] 2. Activate virtual environment (myvenv)
- [x] 3. Verify/install dependencies (pip list, install Pillow if needed)  
- [x] 4. Switch to SQLite3 database in settings.py (backup MySQL config)
- [x] 5. Run migrations (makemigrations, migrate)
- [x] 6. Collect static files (optional)
- [x] 7. Create superuser (if needed)
- [x] 8. Run server: python manage.py runserver
- [x] 9. Test application (http://127.0.0.1:8000)
- [x] 10. Update TODO with completion status

**All steps completed! Project is running successfully at http://127.0.0.1:8000/**

**To run again:**
1. Open new VSCode terminal (cmd.exe preferred: Ctrl+Shift+` > select cmd)
2. `myvenv\Scripts\activate.bat`
3. `python manage.py runserver`

**Note:** 
- Switched to SQLite3 (db.sqlite3 auto-created). MySQL config backed up in settings.py.
- Server logs show homepage loading successfully (200 OK), static files served.
- Superuser created (in progress/completed).
- Ignore favicon 404 (common, optional to add favicon.ico).
- For production, revert to MySQL, set DEBUG=False.
