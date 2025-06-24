# Tripey

**Tripey** is a cross-platform travel-planner app that helps users discover and book customized itineraries in Nepal based on their interests, season, budget, and more.

---

## Table of Contents

1. [About](#about)  
2. [Tech Stack](#tech-stack)  
3. [Phase 1 Roadmap](#phase-1-roadmap)  
4. [Getting Started](#getting-started)  
5. [Configuration](#configuration)  
6. [Branching Strategy](#branching-strategy)  
7. [Contributing](#contributing)  
8. [License](#license)  
9. [Contact](#contact)  

---

## About

Tripey is designed as an MVP in Phase 1 to validate core features:

- **Personalized trip planning** via rule-based logic + optional GPT enrichment  
- **Guide booking**: browse local guides, request bookings  
- **Multilingual UI** (English & Nepali)  
- **Cultural tips** module  
- **Offline PDF export** of itineraries  
- **Emergency SOS** button  

---

## Tech Stack

| Layer              | Tech / Service                 |
|--------------------|--------------------------------|
| Frontend (MVP)     | Flutter (or React + Bootstrap) |
| Backend API        | Python + Flask                 |
| Database           | Firebase Firestore (NoSQL)     |
| Authentication     | Firebase Auth                  |
| CMS                | Notion API or Sanity.io        |
| AI / Content       | OpenAI ChatGPT API             |
| Hosting (frontend) | Netlify                        |
| Hosting (backend)  | Render or Railway              |

---

## Phase 1 Roadmap

We're targeting a 0–6 month MVP build with these 9 steps:

1. **Project Setup & Planning**  
   – GitHub repo, branch strategy, README, `.gitignore`  
2. **Basic Flask Backend API**  
   – `/generate-itinerary`, `/guides`, `/book-guide`, `/cultural-tips`  
3. **Personalized Trip Planning**  
   – Rule-based logic + GPT enhancements  
4. **Guide Booking System**  
   – Guide profiles, ratings, booking requests saved to Firestore  
5. **Multilingual Support**  
   – UI translations (i18n)  
6. **In-App Chat (Lite)**  
   – Embed Sendbird/Twilio SDK  
7. **Cultural Tips Module**  
   – Fetch static content from CMS  
8. **Offline Access**  
   – PDF export of itineraries (wkhtmltopdf / WeasyPrint)  
9. **Emergency SOS Button**  
   – Dial Nepal emergency number + static help locations  

---

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/<your-org>/tripey.git
cd tripey
```

### 2. Create & switch to dev branch
```bash
git checkout -b dev
```

### 3. Setup backend
```bash
cd backend
python3 -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows PowerShell:
.\venv\Scripts\activate

pip install -r requirements.txt
```

### 4. Configure environment

Create a file named `.env.example` inside `backend/` with placeholder values:

```env
FIREBASE_CREDENTIALS=
OPENAI_API_KEY=
# Add other variables here as needed
```

Copy `.env.example` to `.env` locally and fill in real values:

```bash
# On macOS/Linux:
cp backend/.env.example backend/.env

# On Windows PowerShell:
copy backend\.env.example backend\.env
```

In `backend/.env`, set:

```env
FIREBASE_CREDENTIALS=path/to/your/firebase-credentials.json
OPENAI_API_KEY=sk-...
```

Ensure `.gitignore` includes `backend/.env` so real secrets are not committed.

### 5. Run backend
```bash
flask run
```

### 6. Setup & run frontend (Flutter)
```bash
cd ../frontend/flutter_app
flutter pub get
flutter run
```

*(If using React: adjust commands accordingly, e.g., `cd ../frontend/react_app` then `npm install` and `npm start`.)*

---

## Configuration

In `backend/.env` you should have entries like:

```env
FIREBASE_CREDENTIALS=path/to/your/firebase-credentials.json
OPENAI_API_KEY=sk-...
```

**Important:** Do NOT commit `backend/.env` to Git. Instead commit only `backend/.env.example` with blank values.

Ensure your `.gitignore` has a line:
```
backend/.env
```

Place your Firebase credentials JSON in a safe local path, referenced by `FIREBASE_CREDENTIALS`.

---

## Branching Strategy

- **`main`**: always stable, production-ready
- **`dev`**: integration branch for upcoming release
- **`feature/<feature-name>`**: one per new feature or bugfix

### Pull Requests:
- Target `dev` for all new work
- Require at least one code review before merge

---

## Contributing

1. Fork the repo

2. Create a feature branch:
   ```bash
   git checkout -b feature/itinerary-api
   ```

3. Commit your changes & push:
   ```bash
   git add .
   git commit -m "Add itinerary endpoint"
   git push origin feature/itinerary-api
   ```

4. Open a Pull Request against `dev`

5. Address review comments

6. Merge once approved

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Contact

- **Maintainer:** [Your Name]
- **Email:** your.email@example.com
- **Project Wiki / Roadmap:** https://github.com/&lt;your-org&gt;/tripey/wiki