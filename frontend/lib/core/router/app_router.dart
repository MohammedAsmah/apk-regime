import 'package:flutter_trnx_project/imports.dart';

enum TransitionType { fade, slideRight, slideUp, fadeSlide }

typedef TransitionBuilder = Widget Function(
  BuildContext context,
  Animation<double> animation,
  Animation<double> secondaryAnimation,
  Widget child,
);

final Map<TransitionType, TransitionBuilder> _transitions = {
  TransitionType.fade: (context, animation, secondaryAnimation, child) {
    return FadeTransition(opacity: animation, child: child);
  },
  TransitionType.slideRight: (context, animation, secondaryAnimation, child) {
    return SlideTransition(
      position: Tween<Offset>(
        begin: const Offset(1.0, 0.0),
        end: Offset.zero,
      ).animate(
        CurvedAnimation(parent: animation, curve: Curves.easeOutCubic),
      ),
      child: child,
    );
  },
  TransitionType.slideUp: (context, animation, secondaryAnimation, child) {
    return SlideTransition(
      position: Tween<Offset>(
        begin: const Offset(0.0, 1.0),
        end: Offset.zero,
      ).animate(
        CurvedAnimation(parent: animation, curve: Curves.easeOutCubic),
      ),
      child: child,
    );
  },
  TransitionType.fadeSlide: (context, animation, secondaryAnimation, child) {
    return FadeTransition(
      opacity: animation,
      child: SlideTransition(
        position: Tween<Offset>(
          begin: const Offset(0, 0.1),
          end: Offset.zero,
        ).animate(
          CurvedAnimation(parent: animation, curve: Curves.easeOutCubic),
        ),
        child: child,
      ),
    );
  },
};

class RouteConfig {
  final String path;
  final String name;
  final Widget screen;
  final TransitionType transition;
  final Color? barrierColor;

  const RouteConfig({
    required this.path,
    required this.name,
    required this.screen,
    required this.transition,
    this.barrierColor,
  });
}

final Map<String, RouteConfig> _authRoutes = {
  'auth': RouteConfig(
    path: '/auth',
    name: 'auth',
    screen: const WelcomeScreen(),
    transition: TransitionType.fadeSlide,
  ),
  'login': RouteConfig(
    path: 'login',
    name: 'login',
    screen: const LoginScreen(),
    transition: TransitionType.slideRight,
  ),
  'signup': RouteConfig(
    path: 'signup',
    name: 'signup',
    screen: SignUpScreen(),
    transition: TransitionType.slideRight,
  ),
};

final Map<String, RouteConfig> _mainRoutes = {
  'home': RouteConfig(
    path: '/home',
    name: 'Home',
    screen: const HomeScreen(),
    transition: TransitionType.fade,
    barrierColor: Colors.transparent,
  ),
  'coach': RouteConfig(
    path: '/coach',
    name: 'Coach',
    screen: const CoachScreen(),
    transition: TransitionType.slideRight,
  ),
  'progress': RouteConfig(
    path: '/progress',
    name: 'Progress',
    screen: const ProgressScreen(),
    transition: TransitionType.fade,
  ),
  'challenges': RouteConfig(
    path: '/challenges',
    name: 'Challenges done',
    screen: const ChallengesScreen(),
    transition: TransitionType.slideRight,
  ),
  'profile': RouteConfig(
    path: '/profile',
    name: 'Profile',
    screen: const ProfileScreen(),
    transition: TransitionType.fade,
  ),
  
};

final Map<String, RouteConfig> _standaloneRoutes = {
  'editProfile': RouteConfig(
    path: '/profile/edit',
    name: 'EditProfile',
    screen: const EditProfileScreen(),
    transition: TransitionType.slideUp,
  ),
};

GoRoute _buildRoute(RouteConfig config, {List<GoRoute>? routes}) {
  return GoRoute(
    path: config.path,
    name: config.name,
    pageBuilder: (context, state) => CustomTransitionPage(
      key: state.pageKey,
      barrierColor: config.barrierColor,
      child: config.screen,
      transitionsBuilder: _transitions[config.transition]!,
    ),
    routes: routes ?? [],
  );
}

final goRouter = GoRouter(
  initialLocation: '/auth',
  routes: [
    _buildRoute(
      _authRoutes['auth']!,
      routes: [
        _buildRoute(_authRoutes['login']!),
        _buildRoute(_authRoutes['signup']!),
      ],
    ),
    ShellRoute(
      builder: (context, state, child) {
        return AppLayout(state: state, child: child );
      },
      routes: _mainRoutes.values.map((config) => _buildRoute(config)).toList(),
    ),
    ..._standaloneRoutes.values.map((config) => _buildRoute(config)),
  ],
  errorBuilder: (context, state) =>
      Scaffold(body: Center(child: Text('Page not found: ${state.uri}'))),
);
