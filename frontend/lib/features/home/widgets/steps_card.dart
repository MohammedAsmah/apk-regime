part of 'index.dart';

class StepsCard extends StatelessWidget {
  final int steps;
  final double distance;
  final int calories;
  
  const StepsCard({
    Key? key,
    required this.steps,
    required this.distance,
    required this.calories,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context)!;
    final theme = Theme.of(context);

    return Container(
      padding: EdgeInsets.all(AppDimensions.l),
      decoration: BoxDecoration(
        color: AppColors.black,
        borderRadius: BorderRadius.circular(AppDimensions.radiusL),
        border: Border.all(
          color: theme.brightness == Brightness.dark
              ? AppColors.brandBlue
              : Colors.transparent,
          width: 2,
        ),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(
                Icons.directions_walk,
                color: AppColors.white,
                size: AppDimensions.iconL,
              ),
              SizedBox(width: AppDimensions.s),
              Text(
                l10n.stepsWalked,
                style: theme.textTheme.titleLarge?.copyWith(
                  color: AppColors.white,
                  fontWeight: FontWeight.w600,
                  fontSize: 16.sp,
                ),
              ),
            ],
          ),
          SizedBox(height: AppDimensions.l),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            crossAxisAlignment: CrossAxisAlignment.end,
            children: [
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      '${steps.toStringAsFixed(0).replaceAllMapped(RegExp(r'(\d{1,3})(?=(\d{3})+(?!\d))'), (Match m) => '${m[1]},')} ${l10n.steps}',
                      style: theme.textTheme.headlineLarge?.copyWith(
                        color: AppColors.white,
                        fontWeight: FontWeight.bold,
                        fontSize: 24.sp,
                      ),
                    ),
                    SizedBox(height: AppDimensions.xxs),
                    Text(
                      '${distance.toStringAsFixed(1)} ${l10n.km}  |  $calories ${l10n.kcal}',
                      style: theme.textTheme.bodyMedium?.copyWith(
                        color: AppColors.white.withValues(alpha: 0.7),
                        fontSize: 12.sp,
                      ),
                    ),
                  ],
                ),
              ),
              SizedBox(
                height: 80.h,
                width: 180.w,
                child: _buildStepsChart(),
              ),
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildStepsChart() {
    return BarChart(
      BarChartData(
        alignment: BarChartAlignment.spaceAround,
        maxY: 7000,
        barTouchData: BarTouchData(enabled: false),
        titlesData: FlTitlesData(
          show: true,
          bottomTitles: AxisTitles(
            sideTitles: SideTitles(
              showTitles: true,
              getTitlesWidget: (value, meta) {
                const days = ['M', 'T', 'W', 'T', 'F', 'S', 'S'];
                if (value.toInt() >= 0 && value.toInt() < days.length) {
                  return Text(
                    days[value.toInt()],
                    style: TextStyle(
                      color: AppColors.white.withValues(alpha: 0.7),
                      fontSize: 10.sp,
                    ),
                  );
                }
                return const Text('');
              },
            ),
          ),
          leftTitles: AxisTitles(
            sideTitles: SideTitles(showTitles: false),
          ),
          topTitles: AxisTitles(
            sideTitles: SideTitles(showTitles: false),
          ),
          rightTitles: AxisTitles(
            sideTitles: SideTitles(showTitles: false),
          ),
        ),
        gridData: FlGridData(show: false),
        borderData: FlBorderData(show: false),
        barGroups: [
          _buildBarGroup(0, 4500, AppColors.successGreen),
          _buildBarGroup(1, 5200, AppColors.successGreen),
          _buildBarGroup(2, 5500, AppColors.successGreen),
          _buildBarGroup(3, 6000, AppColors.successGreen),
          _buildBarGroup(4, 5800, AppColors.successGreen),
          _buildBarGroup(5, 6500, AppColors.successGreen),
          _buildBarGroup(6, 6200, AppColors.successGreen),
        ],
      ),
    );
  }

  BarChartGroupData _buildBarGroup(int x, double y, Color color) {
    return BarChartGroupData(
      x: x,
      barRods: [
        BarChartRodData(
          toY: y,
          color: color,
          width: 16.w,
          borderRadius: BorderRadius.circular(4.r),
        ),
      ],
    );
  }
}
