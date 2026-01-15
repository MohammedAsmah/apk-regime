part of imports;

class AppLayout extends StatefulWidget {
  final Widget child;
  final GoRouterState state;

  const AppLayout({
    super.key,
    required this.child,
    required this.state,
  });

  @override
  State<AppLayout> createState() => _AppLayoutState();
}

class _AppLayoutState extends State<AppLayout> {
  final GlobalKey<ScaffoldState> _scaffoldKey = GlobalKey<ScaffoldState>();
  int _currentBottomNavIndex = 0;

  final Map<String, int> _routeIndexMap = {
    '/home': 0,
    '/progress': 1,
    '/challenges': 3,
    '/profile': 4,
  };

  final Map<String, String> _routeNameMap = {
    '/home': 'Home',
    '/progress': 'Progress',
    '/profile': 'Profile',
    '/auth': 'Auth',
    '/challenges': 'Challenges',
  };

  @override
  void didUpdateWidget(AppLayout oldWidget) {
    super.didUpdateWidget(oldWidget);
    _updateCurrentIndex();
  }

  @override
  void initState() {
    super.initState();
    _updateCurrentIndex();
  }

  void _updateCurrentIndex() {
    final location = widget.state.uri.path;
    setState(() {
      _currentBottomNavIndex = _routeIndexMap[location] ?? 0;
    });
  }

  void _handleBottomNavTap(int index) {
    setState(() {
      _currentBottomNavIndex = index;
    });
  }

  String _getScreenTitle() {
    final location = widget.state.uri.path;
    return _routeNameMap[location] ?? 'TRNX';
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    return Scaffold(
      key: _scaffoldKey,
      backgroundColor: theme.colorScheme.surface,
      drawer: _buildDrawer(context),
      body: SafeArea(
        child: Column(
          children: [
            _buildHeader(context),
            Expanded(child: widget.child),
          ],
        ),
      ),
      floatingActionButtonAnimator: FloatingActionButtonAnimator.scaling,
      floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
      floatingActionButton: CustomBottomNavBar(
        currentIndex: _currentBottomNavIndex,
        onTap: _handleBottomNavTap,
      ),
    );
  }

  Widget _buildHeader(BuildContext context) {
    final theme = Theme.of(context);
    
    return Container(
      padding: EdgeInsets.symmetric(
        horizontal: AppDimensions.screenPaddingHorizontal,
        vertical: AppDimensions.m,
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(
            _getScreenTitle(),
            style: theme.textTheme.headlineLarge?.copyWith(
              fontWeight: FontWeight.bold,
              fontSize: 24.sp,
            ),
          ),
          GestureDetector(
            onTap: () {
              _scaffoldKey.currentState?.openDrawer();
            },
            child: CircleAvatar(
              radius: 20.r,
              backgroundColor: theme.colorScheme.primary,
              child: Icon(
                Icons.person,
                size: 20.sp,
                color: theme.colorScheme.onPrimary,
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildDrawer(BuildContext context) {
    final theme = Theme.of(context);
    
    return Drawer(
      backgroundColor: theme.colorScheme.surface,
      child: SafeArea(
        child: Column(
          children: [
            Container(
              padding: EdgeInsets.all(AppDimensions.l),
              child: Row(
                children: [
                  CircleAvatar(
                    radius: 32.r,
                    backgroundColor: theme.colorScheme.primary,
                    child: Icon(
                      Icons.person,
                      size: 32.sp,
                      color: theme.colorScheme.onPrimary,
                    ),
                  ),
                  SizedBox(width: AppDimensions.m),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          'Mark',
                          style: theme.textTheme.headlineSmall?.copyWith(
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                        Text(
                          'mark@example.com',
                          style: theme.textTheme.bodyMedium?.copyWith(
                            color: theme.colorScheme.onSurface.withValues(alpha: 0.6),
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
            Divider(height: 1),
            _buildDrawerItem(
              context,
              icon: Icons.home,
              title: 'Home',
              onTap: () {
                Navigator.pop(context);
                context.go('/home');
              },
            ),
            _buildDrawerItem(
              context,
              icon: Icons.self_improvement,
              title: 'Daily Login Reward',
              onTap: () {
                Navigator.pop(context);
              },
            ),
            _buildDrawerItem(
              context,
              icon: Icons.store,
              title: 'Trnx Points store',
              onTap: () {
                Navigator.pop(context);
              },
            ),
            _buildDrawerItem(
              context,
              icon: Icons.calendar_today,
              title: 'Calendar',
              onTap: () {
                Navigator.pop(context);
              },
            ),
            _buildDrawerItem(
              context,
              icon: Icons.chat,
              title: 'AI Coach',
              onTap: () {
                Navigator.pop(context);
              },
            ),
            Spacer(),
            Divider(height: 1),
            _buildDrawerItem(
              context,
              icon: Icons.settings,
              title: 'Settings',
              onTap: () {
                Navigator.pop(context);
              },
            ),
            _buildDrawerItem(
              context,
              icon: Icons.logout,
              title: 'Logout',
              onTap: () {
                Navigator.pop(context);
                context.go('/auth');
              },
            ),
            SizedBox(height: AppDimensions.m),
          ],
        ),
      ),
    );
  }

  Widget _buildDrawerItem(
    BuildContext context, {
    required IconData icon,
    required String title,
    required VoidCallback onTap,
  }) {
    final theme = Theme.of(context);
    
    return ListTile(
      leading: Icon(icon, color: theme.colorScheme.onSurface),
      title: Text(
        title,
        style: theme.textTheme.bodyLarge,
      ),
      onTap: onTap,
      contentPadding: EdgeInsets.symmetric(
        horizontal: AppDimensions.l,
        vertical: AppDimensions.xxs,
      ),
    );
  }
}
