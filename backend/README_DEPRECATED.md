# DEPRECATED - Backend Reference Only

This folder is kept for reference only. The backend functionality has been moved to Next.js API routes in the frontend.

## New Structure
- Frontend: `frontend/src/app/api/chat/route.ts` - Contains all backend logic
- No separate backend needed - everything runs in Next.js

## To Deploy
1. Deploy only the `frontend` folder to Vercel
2. Set `GEMINI_API_KEY` in Vercel environment variables
3. No backend deployment needed