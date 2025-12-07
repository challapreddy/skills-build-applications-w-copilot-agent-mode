# Copilot Agent Instructions — OctoFit Tracker (local guide)

Purpose: give an AI coding agent the minimum, concrete context to be productive in this repo.

1) Big-picture architecture
- Frontend: React app under `frontend/` (components, API calls to backend REST endpoints).
- Backend: Django REST Framework under `backend/` (Django project typically in `backend/octofit_tracker/`).
- Database: MongoDB (djongo/pymongo used in the project requirements).
- Dev environment: GitHub Codespaces / Ubuntu devcontainer in this workspace.

2) Key workflows & commands (explicit, reproducible)
- Always run commands using absolute paths (do NOT change directories when agent mode runs commands). Example:

```bash
python3 -m venv /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/venv
source /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/venv/bin/activate
pip install -r /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/requirements.txt
```

- Ports to expose (Codespaces / devcontainer): `8000` (backend public), `3000` (frontend public), `27017` (MongoDB private). Do not propose other public ports.

3) Project-specific conventions and patterns
- Use Django ORM and DRF serializers/views for data access — avoid writing direct MongoDB shell scripts. The project relies on Django's ORM integration (djongo) for schema and migrations.
- Authentication: this project expects `django-allauth` + `dj-rest-auth` patterns for account endpoints (look for auth-related apps in `backend/`).
- Keep API surface in the Django app (serializers, viewsets, urls) and let React call those endpoints. Prefer REST-style endpoints (GET/POST/PUT/DELETE) and use DRF routers where possible.

4) Integration points & files to inspect
- `docs/octofit_story.md` — product goals, UX constraints, and stack decisions.
- `README.md` — exercise overview and context for Codespaces/Copilot agent mode usage.
- Look for `backend/requirements.txt` and `backend/venv` — the repository's Python env layout and dependencies live there.

5) Agent guidance for code changes
- When creating backend models: add a Django model in `backend/<app>/models.py`, create a corresponding serializer in `backend/<app>/serializers.py`, then expose via `backend/<app>/views.py` or `viewsets.py` and wire into `backend/urls.py` with DRF router.
- When adding frontend components: place them under `frontend/src/components/`, add API helpers under `frontend/src/api/` and keep UI/state logic in React hooks or context. Use `fetch` or `axios` consistent with existing code.
- Tests: no project-wide test framework is enforced; if you add tests, follow Django's `tests.py` style in apps and Jest/React Testing Library for frontend.

6) External services & dependencies
- MongoDB: prefer to run in Codespaces or a local container; check for `mongod` with `ps aux | grep mongod` before attempting connections.
- Key Python packages (expected): Django, djangorestframework, djongo, dj-rest-auth, django-allauth. See `backend/requirements.txt` for exact pinned versions if present.

7) What I searched / assumptions
- No existing `.github/copilot-instructions.md` or AGENT/CLAUDE style files were found in the repo — this file was created to fill that gap.
- This guidance is written from discoverable files: `README.md` and `docs/octofit_story.md` and the repository structure conventions in this exercise.

8) When to ask the maintainer
- If you need the exact Django project name, settings location, or `requirements.txt` contents but they are missing, ask for the path or permission to create the standard `backend/requirements.txt` expected by the project.

If anything above is unclear or you'd like me to include explicit examples (small model+serializer+view boilerplate, or a sample React API hook), tell me which area to expand and I will iterate.
