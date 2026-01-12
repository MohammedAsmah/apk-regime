part of 'index.dart';

class CaloriesCard extends StatelessWidget {
  final int current;
  final int goal;
  final VoidCallback onUpdateGoal;
  
  const CaloriesCard({
    Key? key,
    required this.current,
    required this.goal,
    required this.onUpdateGoal,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context)!;
    final theme = Theme.of(context);

    return Container(
      padding: EdgeInsets.all(AppDimensions.m),
      decoration: BoxDecoration(
        color: AppColors.black,
        borderRadius: BorderRadius.circular(AppDimensions.radiusL),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(
                Icons.local_fire_department,
                color: AppColors.warningOrange,
                size: AppDimensions.iconM,
              ),
              SizedBox(width: AppDimensions.xs),
              Expanded(
                child: Text(
                  l10n.caloriesBurned,
                  style: theme.textTheme.bodyLarge?.copyWith(
                    color: AppColors.white,
                    fontWeight: FontWeight.w600,
                    fontSize: 14.sp,
                  ),
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                ),
              ),
            ],
          ),
          SizedBox(height: AppDimensions.m),
          Text(
            '$current / $goal',
            style: theme.textTheme.headlineMedium?.copyWith(
              color: AppColors.white,
              fontWeight: FontWeight.bold,
              fontSize: 22.sp,
            ),
          ),
          Text(
            l10n.kcal,
            style: theme.textTheme.bodyMedium?.copyWith(
              color: AppColors.white.withValues(alpha: 0.7),
              fontSize: 12.sp,
            ),
          ),
          SizedBox(height: AppDimensions.m),
          SizedBox(
            width: double.infinity,
            child: ElevatedButton(
              onPressed: onUpdateGoal,
              style: ElevatedButton.styleFrom(
                backgroundColor: AppColors.warningOrange,
                foregroundColor: AppColors.black,
                padding: EdgeInsets.symmetric(vertical: AppDimensions.s),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(AppDimensions.radiusM),
                ),
              ),
              child: Text(
                l10n.updateGoal,
                style: TextStyle(
                  fontSize: 12.sp,
                  fontWeight: FontWeight.w600,
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
