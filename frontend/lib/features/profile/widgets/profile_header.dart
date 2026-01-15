part of 'index.dart';

class ProfileHeader extends StatelessWidget {
  final String name;
  final DateTime memberSince;
  final int streak;
  final double weightLost;
  final double actualWeight;
  final double goalWeight;
  final double progressPercentage;

  const ProfileHeader({
    Key? key,
    required this.name,
    required this.memberSince,
    required this.streak,
    required this.weightLost,
    required this.actualWeight,
    required this.goalWeight,
    required this.progressPercentage,
  }) : super(key: key);

  String _formatDate(DateTime date) {
    final months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    return '${months[date.month - 1]} ${date.year}';
  }

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
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                name,
                style: theme.textTheme.titleLarge?.copyWith(
                  color: AppColors.white,
                  fontWeight: FontWeight.bold,
                  fontSize: 20.sp,
                ),
              ),
            ],
          ),
          SizedBox(height: AppDimensions.xs),
          Row(
            children: [
              Text(
                '${l10n.memberSince} ${_formatDate(memberSince)}',
                style: theme.textTheme.bodyMedium?.copyWith(
                  color: AppColors.white.withValues(alpha: 0.7),
                  fontSize: 12.sp,
                ),
              ),
              Text(
                ' - ',
                style: theme.textTheme.bodyMedium?.copyWith(
                  color: AppColors.white.withValues(alpha: 0.7),
                  fontSize: 12.sp,
                ),
              ),
              Icon(
                Icons.local_fire_department,
                color: AppColors.warningOrange,
                size: 16.sp,
              ),
              SizedBox(width: 4.w),
              Text(
                '$streak ${l10n.daysStreak}',
                style: theme.textTheme.bodyMedium?.copyWith(
                  color: AppColors.white.withValues(alpha: 0.7),
                  fontSize: 12.sp,
                ),
              ),
            ],
          ),
          SizedBox(height: AppDimensions.l),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              _buildStatItem(
                context,
                l10n.weightLost,
                '${weightLost.toStringAsFixed(1)} kg',
              ),
              _buildStatItem(
                context,
                l10n.actualWeight,
                '${actualWeight.toStringAsFixed(0)} kg',
              ),
              _buildStatItem(
                context,
                l10n.goal,
                '${goalWeight.toStringAsFixed(0)} kg',
              ),
            ],
          ),
          SizedBox(height: AppDimensions.l),
          Container(
            padding: EdgeInsets.symmetric(
              horizontal: AppDimensions.m,
              vertical: AppDimensions.s,
            ),
            decoration: BoxDecoration(
              color: AppColors.successGreen.withValues(alpha: 0.15),
              borderRadius: BorderRadius.circular(AppDimensions.radiusM),
              border: Border.all(
                color: AppColors.successGreen.withValues(alpha: 0.3),
                width: 1,
              ),
            ),
            child: Row(
              children: [
                Icon(
                  Icons.trending_up,
                  color: AppColors.successGreen,
                  size: 20.sp,
                ),
                SizedBox(width: AppDimensions.s),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        l10n.progressToGoal,
                        style: theme.textTheme.bodyMedium?.copyWith(
                          color: AppColors.white.withValues(alpha: 0.9),
                          fontSize: 12.sp,
                        ),
                      ),
                      SizedBox(height: 4.h),
                      ClipRRect(
                        borderRadius: BorderRadius.circular(AppDimensions.radiusFull),
                        child: LinearProgressIndicator(
                          value: progressPercentage / 100,
                          backgroundColor: AppColors.white.withValues(alpha: 0.2),
                          valueColor: AlwaysStoppedAnimation<Color>(
                            AppColors.successGreen,
                          ),
                          minHeight: 6.h,
                        ),
                      ),
                    ],
                  ),
                ),
                SizedBox(width: AppDimensions.s),
                Text(
                  '${progressPercentage.toStringAsFixed(0)}%',
                  style: theme.textTheme.titleLarge?.copyWith(
                    color: AppColors.successGreen,
                    fontWeight: FontWeight.bold,
                    fontSize: 18.sp,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildStatItem(BuildContext context, String label, String value) {
    final theme = Theme.of(context);
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          label,
          style: theme.textTheme.bodySmall?.copyWith(
            color: AppColors.white.withValues(alpha: 0.6),
            fontSize: 11.sp,
          ),
        ),
        SizedBox(height: 4.h),
        Text(
          value,
          style: theme.textTheme.titleLarge?.copyWith(
            color: AppColors.white,
            fontWeight: FontWeight.bold,
            fontSize: 18.sp,
          ),
        ),
      ],
    );
  }
}
