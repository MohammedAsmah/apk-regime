import 'package:flutter_trnx_project/imports.dart';

final goRouter = GoRouter(
  initialLocation: '/auth',
  routes: [
    GoRoute(
      path: '/auth',
      name: 'auth',
      pageBuilder: (context, state) => CustomTransitionPage(
        key: state.pageKey,
        child: const WelcomeScreen(),
        transitionsBuilder: (context, animation, secondaryAnimation, child) {
          return FadeTransition(
            opacity: animation,
            child: SlideTransition(
              position:
                  Tween<Offset>(
                    begin: const Offset(0, 0.1),
                    end: Offset.zero,
                  ).animate(
                    CurvedAnimation(
                      parent: animation,
                      curve: Curves.easeOutCubic,
                    ),
                  ),
              child: child,
            ),
          );
        },
      ),
      routes: [
        GoRoute(
          path: 'login',
          name: 'login',
          pageBuilder: (context, state) => CustomTransitionPage(
            key: state.pageKey,
            child: const LoginScreen(),
            transitionsBuilder:
                (context, animation, secondaryAnimation, child) {
                  return SlideTransition(
                    position:
                        Tween<Offset>(
                          begin: const Offset(1.0, 0.0),
                          end: Offset.zero,
                        ).animate(
                          CurvedAnimation(
                            parent: animation,
                            curve: Curves.easeOutCubic,
                          ),
                        ),
                    child: child,
                  );
                },
          ),
        ),
        GoRoute(
          path: 'signup',
          name: 'signup',
          pageBuilder: (context, state) {
            // final email = state.extra as String?;
            return CustomTransitionPage(
              key: state.pageKey,
              child: SignUpScreen(),
              transitionsBuilder:
                  (context, animation, secondaryAnimation, child) {
                    return SlideTransition(
                      position:
                          Tween<Offset>(
                            begin: const Offset(1.0, 0.0),
                            end: Offset.zero,
                          ).animate(
                            CurvedAnimation(
                              parent: animation,
                              curve: Curves.easeOutCubic,
                            ),
                          ),
                      child: child,
                    );
                  },
            );
          },
        ),
      ],
    ),
  

GoRoute(
      path: '/home',
      name: 'Home',
      pageBuilder: (context, state) => CustomTransitionPage(
        key: state.pageKey,
        child: const HomeScreen(),
        transitionsBuilder: (context, animation, secondaryAnimation, child) {
          return FadeTransition(opacity: animation, child: child);
        },
      ),
    ),
  
  ],
  errorBuilder: (context, state) =>
      Scaffold(body: Center(child: Text('Page not found: ${state.uri}'))),
);
