part of 'index.dart';

class WaterIntakeCard extends StatelessWidget {
  final int currentIntake;
  final int goal;
  final VoidCallback onIncrement;
  final VoidCallback onDecrement;
  
  const WaterIntakeCard({
    Key? key,
    required this.currentIntake,
    required this.goal,
    required this.onIncrement,
    required this.onDecrement,
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
                Icons.water_drop,
                color: AppColors.brandBlue,
                size: AppDimensions.iconM,
              ),
              SizedBox(width: AppDimensions.xs),
              Expanded(
                child: Text(
                  l10n.waterIntake,
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
            '$currentIntake',
            style: theme.textTheme.headlineMedium?.copyWith(
              color: AppColors.white,
              fontWeight: FontWeight.bold,
              fontSize: 22.sp,
            ),
          ),
          Text(
            l10n.ml,
            style: theme.textTheme.bodyMedium?.copyWith(
              color: AppColors.white.withValues(alpha: 0.7),
              fontSize: 12.sp,
            ),
          ),
          SizedBox(height: AppDimensions.m),
          Container(
            padding: EdgeInsets.symmetric(
              horizontal: AppDimensions.s,
              vertical: AppDimensions.xxs,
            ),
            decoration: BoxDecoration(
              color: AppColors.brandBlue.withValues(alpha: 0.2),
              borderRadius: BorderRadius.circular(AppDimensions.radiusFull),
            ),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                IconButton(
                  onPressed: onDecrement,
                  icon: Icon(
                    Icons.remove,
                    color: AppColors.white,
                    size: 18.sp,
                  ),
                  padding: EdgeInsets.zero,
                  constraints: const BoxConstraints(),
                ),
                Text(
                  '1 ${l10n.cup}',
                  style: theme.textTheme.bodyMedium?.copyWith(
                    color: AppColors.white,
                    fontWeight: FontWeight.w600,
                    fontSize: 12.sp,
                  ),
                ),
                IconButton(
                  onPressed: onIncrement,
                  icon: Icon(
                    Icons.add,
                    color: AppColors.white,
                    size: 18.sp,
                  ),
                  padding: EdgeInsets.zero,
                  constraints: const BoxConstraints(),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
