part of 'index.dart';

class ChallengesScreen extends StatefulWidget {
  const ChallengesScreen({super.key});

  @override
  State<ChallengesScreen> createState() => _ChallengesScreenState();
}

class _ChallengesScreenState extends State<ChallengesScreen> {
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
        child: Column(
          children: [
            Padding(
              padding: EdgeInsets.symmetric(
                horizontal: AppDimensions.screenPaddingHorizontal,
                vertical: AppDimensions.m,
              ),
              child: ChallengesHeader(userName: 'Mark'),
            ),
            Expanded(
              child: SingleChildScrollView(
                child: Padding(
                  padding: EdgeInsets.symmetric(
                    horizontal: AppDimensions.screenPaddingHorizontal,
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      SizedBox(height: AppDimensions.m),
                      ChallengeDetailCard(
                        icon: Icons.star,
                        iconColor: AppColors.accentPurple,
                        title: 'Getting Started',
                        subtitle: 'You\'ve logged your first meal!',
                        description: 'Welcome aboard, every journey starts with one bite 🍽️',
                        isCompleted: true,
                      ),
                      SizedBox(height: AppDimensions.m),
                      ChallengeDetailCard(
                        icon: Icons.local_fire_department,
                        iconColor: AppColors.accentOrange,
                        title: 'Consistency Champ',
                        subtitle: 'You completed 5 workout sessions this week!',
                        description: 'Balance between food and movement legendary stuff 💪',
                        isCompleted: true,
                      ),
                      SizedBox(height: AppDimensions.m),
                      ChallengeDetailCard(
                        icon: Icons.directions_run,
                        iconColor: AppColors.errorRed,
                        title: '10K Achiever',
                        subtitle: 'You\'ve conquered 10K — that\'s next level!',
                        description: 'Keep going, your discipline shows 🔥',
                        isCompleted: true,
                      ),
                      SizedBox(height: AppDimensions.m),
                      ChallengeDetailCard(
                        icon: Icons.self_improvement,
                        iconColor: AppColors.accentOrange,
                        title: 'Yoga Flow Master',
                        subtitle: 'You finished 10 yoga sessions!',
                        description: 'Calm mind, strong body, balanced soul 🧘✨',
                        isCompleted: true,
                      ),
                      SizedBox(height: AppDimensions.m),
                      ChallengeDetailCard(
                        icon: Icons.air,
                        iconColor: AppColors.successGreen,
                        title: 'Stretch & Breathe',
                        subtitle: 'You practiced yoga three days in a row!',
                        description: 'Peace through movement 🕊️',
                        isCompleted: true,
                      ),
                      SizedBox(height: AppDimensions.m),
                      ChallengeDetailCard(
                        icon: Icons.military_tech,
                        iconColor: AppColors.brandBlue,
                        title: 'Workout Warrior',
                        subtitle: 'You hit your workout goals this week!',
                        description: 'No excuses, just progress 💪',
                        isCompleted: true,
                      ),
                      SizedBox(height: AppDimensions.xxl),
                    ],
                  ),
                ),
              ),
            ),
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
}
