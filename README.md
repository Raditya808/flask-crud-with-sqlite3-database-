# Flask SQLite3 Database
![Bochi](./assets/bochi.png)

Making Simple Database — But idk if it's safe or not.

A small Flask application demonstrating a lightweight SQLite3-backed database. This repo is intended for learning and experimentation only — not production use. Use at your own risk.

## Features
- Simple Flask app structure
- SQLite3 as the database engine (file-based)
- Basic CRUD examples (Create, Read, Update, Delete)
- Minimal HTML + CSS front-end for testing

## Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/Raditya808/flask-sqlite3-database-.git
cd flask-sqlite3-database-
```

### 2. Add the Bochi image
Create an `assets/` folder in the repo root and add your `bochi.png` there:
```bash
mkdir -p assets
# copy or move your bochi image into assets/bochi.png
```
If you use a different filename or location, update the image path at the top of this README.

### 3. Set up a Python virtual environment
Recommended: use a virtual environment to isolate dependencies.

On macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies
If there's a `requirements.txt`:
```bash
pip install -r requirements.txt
```
If there is no requirements file, install minimal dependencies:
```bash
pip install Flask python-dotenv
```

### 5. Environment variables
Create a `.env` file in the project root (Flask + python-dotenv will load this automatically if used):

```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=replace-with-a-secret
DATABASE=instance/database.db
```

Adjust `FLASK_APP` if your application entrypoint file is named differently (e.g., `run.py` or `app/__init__.py`).

### 6. Initialize the database
If your app provides an initialization script (e.g., `init_db()`), run it as documented in the project. If there is no script, you can create the SQLite file manually:

```bash
mkdir -p instance
touch instance/database.db
```

If your app uses SQLAlchemy or a migration tool, follow those steps (example with Flask-Migrate would be `flask db init`, `flask db migrate`, `flask db upgrade`).

### 7. Run the app
With the virtualenv active:
```bash
# Option A — Flask CLI (macOS / Linux)
export FLASK_APP=app.py
export FLASK_ENV=development
flask run

# Windows (cmd)
set FLASK_APP=app.py
set FLASK_ENV=development
flask run

# Option B — direct Python (if app has __main__ or run block)
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## Usage
- Use the web UI to add, edit, and delete records (if provided).
- Inspect `instance/database.db` with sqlite3 or a GUI tool:
```bash
sqlite3 instance/database.db
# run SQL queries interactively
```

## Project Structure (example)
- `app.py` — Flask application entrypoint
- `templates/` — HTML templates
- `static/` — CSS, JS, images
- `assets/bochi.png` — hero image referenced in README
- `instance/database.db` — SQLite database file (gitignore recommended)

Adjust these paths to match your repo’s actual layout.

## Security & Notes
- SQLite is file-based and fine for demos, but not recommended for high-load or multi-user production systems.
- This project is for learning; do not store secrets or sensitive data in plaintext.
- Use a strong `SECRET_KEY` for session security.
- Consider adding `instance/database.db` and `.env` to `.gitignore`.

## .gitignore suggestion
```
instance/
.env
*.pyc
__pycache__/
instance/database.db
```

## Contributing
Feel free to open issues or PRs. Keep changes small and document behavior in code or comments.

## License
Add a LICENSE file if you want to choose an open-source license (MIT, Apache-2.0, etc.). If unsure, add `LICENSE: Unlicensed` or create one later.

## Contact
Owner: Raditya808
Repository: https://github.com/Raditya808/flask-sqlite3-database-
