# Beaute Naturelle - Flutter Frontend

Mobile app for weight loss coaching with AI-powered nutrition tracking.

## Features
- AI Coach with real-time feedback
- Nutrition tracking
- Progress tracking
- Community features
- Real-time chat

## Tech Stack
- Flutter 3.x
- Riverpod state management
- Dio for HTTP
- WebSockets for real-time communication
- Flutter Secure Storage for JWT tokens

## Setup

### Prerequisites
- Flutter 3.x installed
- Dart 3.0+
- Backend running (see ../backend/README.md)

### Installation

1. Clone repository
git clone https://github.com/AGH-Data-Agency-Holding/APK-Regime
cd APK-Regime/frontend

2. Install dependencies
flutter pub get
flutter pub run build_runner build

3. Configure Backend URL
Edit lib/presentation/providers/app_providers.dart:
const baseUrl = 'http://YOUR_MACHINE_IP:8000';

4. Run app
flutter run

## Project Structure
lib/
- main.dart (entry point)
- config/ (theme, routes, constants)
- core/ (API client, utilities)
- data/ (API services, models)
- domain/ (business logic)
- features/ (auth, home, meals, progress, chat, etc.)
- presentation/ (state management)

## API Integration
Backend: https://github.com/AGH-Data-Agency-Holding/APK-Regime/tree/main/backend

## Contributing
1. Create feature branch: git checkout -b feature/name
2. Commit: git commit -m "feat: Add feature"
3. Push: git push origin feature/name
4. Create Pull Request

---
Ready for development!
