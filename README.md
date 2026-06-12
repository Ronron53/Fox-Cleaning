# Fox Cleaning

Local cleaning business website for Hertfordshire. Simple lead-generation site built on Flask.

## Local development

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
flask run
```

Visit `http://127.0.0.1:5000`

## Deployment (Railway)

Two Railway services:
- **Staging** → connected to `staging` branch
- **Production** → connected to `main` branch

Environment variables to set in Railway:
- `SECRET_KEY` — random string, keep private
- `SMTP_*` — optional, for email notifications (see app.py comments)

## Git workflow

```bash
# Work on staging first
git checkout staging
git add .
git commit -m "your message"
git push origin staging

# Test on Railway staging URL, then merge to main
git checkout main
git merge staging
git push origin main
```

## Project structure

```
fox-cleaning/
├─ app.py               # Flask app and form handler
├─ requirements.txt
├─ Procfile             # gunicorn start command
├─ templates/
│  └─ index.html        # Single-page site
├─ static/
│  ├─ style.css         # All styles
│  ├─ logo.png          # ← DROP YOUR LOGO HERE
│  └─ images/           # Additional images (optional)
└─ README.md
```

## Logo placeholder

Place your logo file at `static/logo.png`. The site references it at `/static/logo.png`.
If your file is named differently, update the two `<img>` src attributes in `templates/index.html`.