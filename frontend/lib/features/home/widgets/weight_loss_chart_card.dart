part of 'index.dart';

class WeightLossChartCard extends StatelessWidget {
  const WeightLossChartCard({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context)!;
    final theme = Theme.of(context);

    return Container(
      padding: EdgeInsets.all(AppDimensions.l),
      decoration: BoxDecoration(
        color: AppColors.black,
        borderRadius: BorderRadius.circular(AppDimensions.radiusL),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            l10n.weightLossJourney,
            style: theme.textTheme.titleLarge?.copyWith(
              color: AppColors.white,
              fontWeight: FontWeight.w600,
              fontSize: 16.sp,
            ),
          ),
          SizedBox(height: AppDimensions.l),
          SizedBox(
            height: 200.h,
            child: _buildWeightLossChart(),
          ),
          SizedBox(height: AppDimensions.m),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              _buildChartLegend(l10n.lastMonth, AppColors.brandBlue),
              SizedBox(width: AppDimensions.l),
              _buildChartLegend(l10n.currentMonth, AppColors.successGreen),
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildChartLegend(String label, Color color) {
    return Row(
      children: [
        Container(
          width: 12.w,
          height: 12.h,
          decoration: BoxDecoration(
            color: color,
            shape: BoxShape.circle,
          ),
        ),
        SizedBox(width: AppDimensions.xs),
        Text(
          label,
          style: TextStyle(
            color: AppColors.white.withValues(alpha: 0.7),
            fontSize: 11.sp,
          ),
        ),
      ],
    );
  }

  Widget _buildWeightLossChart() {
    return LineChart(
      LineChartData(
        gridData: FlGridData(
          show: true,
          drawVerticalLine: false,
          horizontalInterval: 20,
          getDrawingHorizontalLine: (value) {
            return FlLine(
              color: AppColors.white.withValues(alpha: 0.1),
              strokeWidth: 1,
            );
          },
        ),
        titlesData: FlTitlesData(show: false),
        borderData: FlBorderData(show: false),
        minX: 0,
        maxX: 6,
        minY: 60,
        maxY: 100,
        lineBarsData: [
          LineChartBarData(
            spots: [
              FlSpot(0, 80),
              FlSpot(1, 88),
              FlSpot(2, 75),
              FlSpot(3, 72),
              FlSpot(4, 70),
              FlSpot(5, 78),
              FlSpot(6, 85),
            ],
            isCurved: true,
            color: AppColors.brandBlue,
            barWidth: 3,
            isStrokeCapRound: true,
            dotData: FlDotData(
              show: true,
              getDotPainter: (spot, percent, barData, index) {
                return FlDotCirclePainter(
                  radius: 4,
                  color: AppColors.brandBlue,
                  strokeWidth: 2,
                  strokeColor: AppColors.black,
                );
              },
            ),
            belowBarData: BarAreaData(
              show: true,
              color: AppColors.brandBlue.withValues(alpha: 0.3),
            ),
          ),
          LineChartBarData(
            spots: [
              FlSpot(0, 85),
              FlSpot(1, 82),
              FlSpot(2, 88),
              FlSpot(3, 78),
              FlSpot(4, 75),
              FlSpot(5, 72),
              FlSpot(6, 95),
            ],
            isCurved: true,
            color: AppColors.successGreen,
            barWidth: 3,
            isStrokeCapRound: true,
            dotData: FlDotData(
              show: true,
              getDotPainter: (spot, percent, barData, index) {
                return FlDotCirclePainter(
                  radius: 4,
                  color: AppColors.successGreen,
                  strokeWidth: 2,
                  strokeColor: AppColors.black,
                );
              },
            ),
            belowBarData: BarAreaData(
              show: true,
              color: AppColors.successGreen.withValues(alpha: 0.3),
            ),
          ),
        ],
      ),
    );
  }
}
