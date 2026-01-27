# Appcellent Website

Appcellent - Crafting Premium iOS Experiences

## Local Development

### Option 1: Using Vercel CLI (Recommended - supports all routing features)

1. Install Vercel CLI:
```bash
npm install -g vercel
```

2. Run development server:
```bash
npm run dev
# or
vercel dev
```

The site will be available at `http://localhost:3000` with full routing support for all pages.

### Option 2: Using Python HTTP Server (Simple)

```bash
npm start
# or
python3 -m http.server 8000
```

The site will be available at `http://localhost:8000`

## Deployment

This project is automatically deployed to Vercel when you push to the `main` branch.

### Setup GitHub Actions (One-time)

1. Go to your Vercel dashboard and get:
   - VERCEL_TOKEN (Settings > Tokens)
   - VERCEL_ORG_ID (Team Settings > General)
   - VERCEL_PROJECT_ID (Project Settings > General)

2. Add these as secrets in your GitHub repository:
   - Go to Settings > Secrets and variables > Actions
   - Add: `VERCEL_TOKEN`, `VERCEL_ORG_ID`, `VERCEL_PROJECT_ID`

3. Push to main branch - deployment will happen automatically!

## Project Structure

```
appcellent/
├── index.html          # Homepage
├── privacy.html        # Privacy Policy
├── support.html        # Support page
├── terms.html          # Terms of Service
├── scripts/
│   └── app.js         # JavaScript functionality
├── styles/
│   └── main.css       # Main stylesheet
├── studfinder/        # Stud Finder subdomain pages
└── vercel.json        # Vercel configuration
```

## Visual Editor (Cursor)

When using Cursor's visual editor:
1. Make changes to HTML/CSS files
2. Commit and push to main branch
3. Changes will automatically deploy to production via GitHub Actions
