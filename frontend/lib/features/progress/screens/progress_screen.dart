part of 'index.dart';

class ProgressScreen extends StatefulWidget {
  const ProgressScreen({super.key});

  @override
  State<ProgressScreen> createState() => _ProgressScreenState();
}

class _ProgressScreenState extends State<ProgressScreen> {
  int _currentBottomNavIndex = 3;

  void _handleBottomNavTap(int index) {
    setState(() {
      _currentBottomNavIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    return Scaffold(
      backgroundColor: theme.colorScheme.surface,
      body: SafeArea(
        child: SingleChildScrollView(
          child: Padding(
            padding: EdgeInsets.symmetric(
              horizontal: AppDimensions.screenPaddingHorizontal,
              vertical: AppDimensions.m,
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                ProgressHeader(userName: 'Mark'),
                SizedBox(height: AppDimensions.l),
                WorkoutProgressCard(
                  workouts: [
                    WorkoutProgress(
                      name: 'cycling',
                      progress: 0.45,
                      color: AppColors.brandBlue,
                    ),
                    WorkoutProgress(
                      name: 'running',
                      progress: 0.29,
                      color: AppColors.successGreen,
                    ),
                    WorkoutProgress(
                      name: 'yoga',
                      progress: 0.18,
                      color: AppColors.accentPurple,
                    ),
                    WorkoutProgress(
                      name: 'walking',
                      progress: 0.25,
                      color: AppColors.accentOrange,
                    ),
                  ],
                ),
                SizedBox(height: AppDimensions.m),
                ChallengesCard(
                  challenges: [
                    Challenge(
                      icon: Icons.star,
                      color: AppColors.accentPurple,
                      isCompleted: true,
                    ),
                    Challenge(
                      icon: Icons.local_fire_department,
                      color: AppColors.accentOrange,
                      isCompleted: false,
                    ),
                    Challenge(
                      icon: Icons.directions_run,
                      color: AppColors.errorRed,
                      isCompleted: false,
                    ),
                    Challenge(
                      icon: Icons.flash_on,
                      color: AppColors.accentOrange,
                      isCompleted: false,
                    ),
                  ],
                ),
                SizedBox(height: AppDimensions.m),
                CalendarEventsCard(
                  selectedDay: 18,
                  currentMonth: 'January',
                  upcomingEvent: 'yoga day and meditation',
                  onAddEvent: () {},
                  onSeeMore: () {},
                ),
                SizedBox(height: AppDimensions.xxl),
              ],
            ),
          ),
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
}

class WorkoutProgress {
  final String name;
  final double progress;
  final Color color;

  WorkoutProgress({
    required this.name,
    required this.progress,
    required this.color,
  });
}

class Challenge {
  final IconData icon;
  final Color color;
  final bool isCompleted;

  Challenge({
    required this.icon,
    required this.color,
    required this.isCompleted,
  });
}
