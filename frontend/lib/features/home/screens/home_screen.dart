part of 'index.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  int _waterIntake = 500;
  final int _waterGoal = 2000;
  final TextEditingController _aiInputController = TextEditingController();
  int _currentBottomNavIndex = 0;

  @override
  void dispose() {
    _aiInputController.dispose();
    super.dispose();
  }

  void _handleWaterIncrement() {
    setState(() {
      if (_waterIntake < _waterGoal) _waterIntake += 250;
    });
  }

  void _handleWaterDecrement() {
    setState(() {
      if (_waterIntake >= 250) _waterIntake -= 250;
    });
  }

  void _handleUpdateGoal() {
  }

  void _handleAISubmit() {
  }

  void _handleBottomNavTap(int index) {
    setState(() {
      _currentBottomNavIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    return Scaffold(
      backgroundColor: theme.colorScheme.background,
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
                HomeHeader(userName: 'Mark'),
                SizedBox(height: AppDimensions.l),
                StepsCard(
                  steps: 5000,
                  distance: 4.6,
                  calories: 280,
                ),
                SizedBox(height: AppDimensions.m),
                Row(
                  children: [
                    Expanded(
                      child: CaloriesCard(
                        current: 280,
                        goal: 500,
                        onUpdateGoal: _handleUpdateGoal,
                      ),
                    ),
                    SizedBox(width: AppDimensions.m),
                    Expanded(
                      child: WaterIntakeCard(
                        currentIntake: _waterIntake,
                        goal: _waterGoal,
                        onIncrement: _handleWaterIncrement,
                        onDecrement: _handleWaterDecrement,
                      ),
                    ),
                  ],
                ),
                SizedBox(height: AppDimensions.m),
                AIAssistantCard(
                  userName: 'Mark',
                  controller: _aiInputController,
                  onSubmit: _handleAISubmit,
                ),
                SizedBox(height: AppDimensions.m),
                WeightLossChartCard(),
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
