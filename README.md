# Thermoplastic Road Markings Chatbot

A specialized AI chatbot for thermoplastic road marking products and applications. Get instant answers about application techniques, specifications, standards, and best practices.

## Features

- Real-time chat interface
- Black and white minimalist design
- Specialized in thermoplastic road markings
- Technical specifications on demand
- Industry standards compliance (ASTM, AASHTO, MUTCD)

## Quick Start

### Backend
```bash
cd backend
pip install -r requirements.txt
python main.py
```
Server runs on http://localhost:8000

### Frontend
```bash
cd frontend
yarn install
yarn dev
```
Frontend runs on http://localhost:3000

### Environment Setup
1. Copy `backend/.env.example` to `backend/.env`
2. Add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Sample Questions

### Application Specifications
- What temperature should I apply thermoplastic at?
- How thick should highway markings be?
- What's the drying time for thermoplastic?
- Can thermoplastic be applied in cold weather?

### Glass Beads & Reflectivity
- What glass bead size is standard?
- How much glass beads should I apply?
- What's the difference between drop-on and premixed beads?
- How do I test retroreflectivity?

### Surface Preparation
- Can thermoplastic be applied on concrete?
- Do I need primer for asphalt?
- How do I prepare the surface before application?
- What's the best way to clean the road surface?

### Product Selection
- What's the difference between Type I, II, and III thermoplastic?
- Which thermoplastic is best for highways?
- What's the best product for parking lot markings?
- How do I choose between water-based and thermoplastic?

### Standards & Compliance
- What MUTCD standards apply to road markings?
- What ASTM standards cover thermoplastic?
- How do I ensure my markings meet AASHTO requirements?
- What reflectivity values are required for highways?

### Troubleshooting
- Why is my thermoplastic peeling off?
- How do I fix thermoplastic that's not adhering?
- Why are my markings fading quickly?
- How do I remove old thermoplastic?

### Cost & Efficiency
- How much thermoplastic do I need per square meter?
- What's the coverage rate for thermoplastic paint?
- How do I calculate material costs for a road project?
- What equipment do I need for thermoplastic application?

## Project Structure

```
├── backend/
│   ├── main.py          # FastAPI server
│   ├── requirements.txt # Python dependencies
│   ├── SKILL.md         # AI prompt for thermoplastic markings
│   └── .env            # Environment variables (GEMINI_API_KEY)
├── frontend/
│   └── src/app/        # Next.js app
├── README.md           # Project documentation
└── .gitignore          # Git ignore rules
```

## API Endpoints

- `POST /api/chat` - Send message and receive AI response
  - Request: `{ "message": "What temperature should I apply thermoplastic at?" }`
  - Response: `{ "reply": "Thermoplastic should be heated to 200-220°C..." }`

- `GET /api/health` - Check server status

## Tech Stack

- **Frontend:** Next.js, React, Tailwind CSS
- **Backend:** Python, FastAPI, Uvicorn
- **AI:** Google Gemini API
- **Styling:** Black and white minimalist theme

## License

MIT