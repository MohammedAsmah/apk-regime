# 🥗 APK-Regime / Beauté Naturelle

![Django](https://img.shields.io/badge/Django-5.2.8-092E20?style=for-the-badge&logo=django&logoColor=white)
![Flutter](https://img.shields.io/badge/Flutter-3.x-02569B?style=for-the-badge&logo=flutter&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 📋 Overview

**Beauté Naturelle** (APK-Regime) is an intelligent weight loss and nutrition coaching platform that combines AI-powered dietary guidance with real-time interactive features. The application provides personalized nutrition tracking, meal analysis, progress monitoring, and community support to help users achieve their health and fitness goals.

### Key Features

- 🤖 **AI-Powered Nutrition Coach** - Real-time dietary feedback and personalized recommendations
- 📊 **Smart Nutrition Tracking** - Comprehensive macronutrient analysis and calorie counting
- 📸 **Meal Photo Recognition** - Upload meal photos for instant nutritional analysis
- 💬 **Interactive Chat System** - WebSocket-based real-time communication with AI coach
- 📈 **Progress Tracking** - Visual progress reports with body measurements and weight tracking
- 👥 **Community Features** - Share experiences and connect with other users
- 💳 **Payment Integration** - Subscription management for premium features
- 🔐 **Secure Authentication** - JWT-based authentication with token rotation

## 🏗️ Architecture

This is a full-stack application with a clear separation between frontend and backend:

```
APK-Regime/
├── backend/          # Django REST API + WebSocket server
├── frontend/         # Flutter mobile application
├── LLM-Client/       # (Reserved for future LLM integration)
└── LLM-Server/       # (Reserved for future LLM services)
```

### Technology Stack

#### Backend
- **Framework**: Django 5.2.8 with Django REST Framework
- **Real-time**: Daphne + Django Channels (WebSocket support)
- **Database**: PostgreSQL 15
- **Storage**: AWS S3 / MinIO for media files
- **Authentication**: JWT (SimpleJWT)
- **AI Integration**: OpenAI API for nutrition coaching
- **Cache**: Redis (for WebSocket channels)

#### Frontend
- **Framework**: Flutter 3.x with Dart 3.0+
- **State Management**: Riverpod
- **HTTP Client**: Dio
- **Real-time**: WebSocket client
- **Storage**: Flutter Secure Storage for JWT tokens
- **Platforms**: Android, iOS, Web, Windows, macOS, Linux

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+** (backend)
- **Flutter 3.x** (frontend)
- **PostgreSQL 15** (database)
- **Docker & Docker Compose** (optional, for containerized services)
- **Redis** (for WebSocket channels)

### 1. Clone the Repository

```bash
git clone https://github.com/AGH-Data-Agency-Holding/APK-Regime.git
cd APK-Regime
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create and activate virtual environment (Windows)
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start PostgreSQL and MinIO using Docker Compose
docker-compose up -d

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
daphne -b 0.0.0.0 -p 8000 core.asgi:application
```

The backend API will be available at `http://localhost:8000`

**See [backend/README.md](backend/README.md) for detailed setup instructions.**

### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd ../frontend

# Install dependencies
flutter pub get
flutter pub run build_runner build

# Configure backend URL
# Edit lib/presentation/providers/app_providers.dart
# Set: const baseUrl = 'http://YOUR_MACHINE_IP:8000';

# Run the application
flutter run
```

**See [frontend/README.md](frontend/README.md) for detailed setup instructions.**

## 📦 Project Structure

### Backend Apps

- **`chat/`** - Real-time chat system with AI coach using WebSockets
- **`users/`** - User authentication, profiles, and management
- **`nutrition/`** - Nutrition tracking, meal logging, and food database
- **`progress/`** - Progress tracking with body measurements and reports
- **`community/`** - Social features and community posts
- **`payments/`** - Subscription and payment management
- **`core/`** - Django project settings and configuration

### Frontend Structure

```
lib/
├── main.dart                 # Application entry point
├── config/                   # App configuration, theme, routes
├── core/                     # Core utilities and API client
├── data/                     # API services and data models
├── domain/                   # Business logic layer
├── features/                 # Feature modules
│   ├── auth/                # Authentication screens
│   ├── home/                # Dashboard
│   ├── meals/               # Meal tracking
│   ├── progress/            # Progress tracking
│   ├── chat/                # AI coach chat
│   └── community/           # Community features
└── presentation/            # State management (Riverpod)
```

## 🧠 AI & Nutrition Science

The application uses scientific algorithms for personalized nutrition:

### Basal Metabolic Rate (BMR) Calculation

Uses the **Mifflin-St Jeor Equation** for accurate calorie needs:

$$BMR = 10 \times \text{weight (kg)} + 6.25 \times \text{height (cm)} - 5 \times \text{age (years)} + s$$

Where $s = +5$ for males and $s = -161$ for females.

### Macronutrient Analysis

- **Proteins**: Muscle maintenance and repair
- **Carbohydrates**: Energy management and glycemic index control
- **Fats**: Hormonal balance and vitamin absorption

### AI Coaching

Real-time personalized feedback powered by OpenAI API, providing:
- Meal composition analysis
- Portion size recommendations
- Alternative food suggestions
- Progress insights and motivation

## 🔐 Authentication

The platform uses JWT (JSON Web Tokens) for secure authentication:

1. User registers or logs in
2. Backend issues access token (short-lived) and refresh token (long-lived)
3. Access token stored securely in device storage
4. Tokens automatically refreshed when expired
5. WebSocket connections authenticated with JWT

## 🌐 API Documentation

Once the backend is running, access:
- **Swagger UI**: `http://localhost:8000/swagger/`
- **ReDoc**: `http://localhost:8000/redoc/`

## 🐳 Docker Support

The project includes Docker Compose configuration for easy deployment:

```bash
cd backend
docker-compose up -d
```

Services included:
- **PostgreSQL** (port 5432)
- **MinIO** (ports 9000 for API, 9001 for console)

## 🧪 Testing

### Backend Tests

```bash
cd backend
python manage.py test
```

### Frontend Tests

```bash
cd frontend
flutter test
```

## 📱 Platform Support

The Flutter frontend supports multiple platforms:
- ✅ Android
- ✅ iOS
- ✅ Web
- ✅ Windows
- ✅ macOS
- ✅ Linux

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'feat: Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

### Commit Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):
- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `style:` - Code style changes
- `refactor:` - Code refactoring
- `test:` - Test additions or updates
- `chore:` - Maintenance tasks

## 📄 License

This project is proprietary software. All rights reserved.

## 👥 Team

Developed by **AGH Data Agency Holding**

## 📞 Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Contact the development team

## 🗺️ Roadmap

- [ ] Enhanced AI meal recognition from photos
- [ ] Integration with fitness wearables
- [ ] Social challenges and competitions
- [ ] Recipe recommendations
- [ ] Grocery list generator
- [ ] Multi-language support
- [ ] Offline mode support
- [ ] Advanced analytics dashboard

---

**Built with ❤️ for healthier living**
