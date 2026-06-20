# MedRemind IoT — Streamlit Deployment

This package wraps your existing `dashboard.html` (the ESP32 Smart
Medication Reminder & Dispensing dashboard) so it can be deployed on
**Streamlit Community Cloud** (share.streamlit.io). The dashboard itself is
untouched — `app.py` simply loads it and renders it full-screen inside the
Streamlit page.

## Files

| File | Purpose |
|---|---|
| `app.py` | Streamlit entry point. Loads `dashboard.html` and renders it. |
| `dashboard.html` | Your original dashboard (HTML/CSS/JS), unmodified. |
| `requirements.txt` | Python dependency (`streamlit`). |
| `.streamlit/config.toml` | Theme + server settings. |

## Deploy on Streamlit Community Cloud

1. **Create a GitHub repo** and push all four files/folders above to it,
   keeping the same names and the `.streamlit/` folder structure
   (e.g. repo name `medremind-iot-dashboard`).

   ```bash
   git init
   git add .
   git commit -m "MedRemind IoT dashboard for Streamlit"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-repo>.git
   git push -u origin main
   ```

2. Go to **[share.streamlit.io](https://share.streamlit.io)** and sign in
   with GitHub.

3. Click **"New app"**, then select:
   - Repository: `<your-username>/<your-repo>`
   - Branch: `main`
   - Main file path: `app.py`

4. Click **Deploy**. Streamlit Cloud installs `streamlit` from
   `requirements.txt` and launches the app — your dashboard will be live at
   a URL like `https://<your-app-name>.streamlit.app`.

## Run locally first (optional, recommended)

```bash
pip install -r requirements.txt
streamlit run app.py
```

This opens the dashboard at `http://localhost:8501`.

## Notes

- The dashboard is currently a **frontend-only demo**: all data (medicines,
  notifications, compartment state, etc.) lives in JavaScript variables in
  `dashboard.html` and resets on every page reload — there's no backend or
  database yet, and no live connection to a real ESP32 device. That's true
  whether you open the HTML file directly or run it through Streamlit; this
  packaging step only changes *how* it's hosted, not *what* it does.
- If you later want the dashboard to show live sensor data or accept
  commands from a real ESP32, you'd need to add a backend (e.g. a small
  FastAPI/Flask service or Streamlit's own Python side using
  `st.session_state` and rewriting the UI in native Streamlit widgets) plus
  the ESP32 firmware to talk to it over MQTT/HTTP. Happy to help build that
  next if/when you're ready.
- To update the dashboard later, just edit `dashboard.html` and push the
  change to GitHub — Streamlit Cloud auto-redeploys on every push to the
  connected branch.
