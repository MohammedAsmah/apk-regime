part of 'index.dart';

class WorkoutProgressCard extends StatelessWidget {
  final List<WorkoutProgress> workouts;

  const WorkoutProgressCard({
    super.key,
    required this.workouts,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    return Container(
      padding: EdgeInsets.all(AppDimensions.l),
      decoration: BoxDecoration(
        color: AppColors.black,
        borderRadius: BorderRadius.circular(AppDimensions.radiusL),
        border: Border.all(
          color: AppColors.darkBorder,
          width: 1,
        ),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            'workout progress',
            style: theme.textTheme.bodyLarge?.copyWith(
              color: AppColors.white,
              fontWeight: FontWeight.w600,
              fontSize: 16.sp,
            ),
          ),
          SizedBox(height: AppDimensions.l),
          ...workouts.map((workout) => Padding(
                padding: EdgeInsets.only(bottom: AppDimensions.m),
                child: _buildProgressRow(workout, theme),
              )),
        ],
      ),
    );
  }

  Widget _buildProgressRow(WorkoutProgress workout, ThemeData theme) {
    return Row(
      children: [
        SizedBox(
          width: 70.w,
          child: Text(
            workout.name,
            style: theme.textTheme.bodyMedium?.copyWith(
              color: AppColors.white,
              fontSize: 14.sp,
            ),
          ),
        ),
        SizedBox(width: AppDimensions.m),
        Expanded(
          child: Stack(
            children: [
              Container(
                height: 8.h,
                decoration: BoxDecoration(
                  color: AppColors.darkSurface,
                  borderRadius: BorderRadius.circular(AppDimensions.radiusFull),
                ),
              ),
              FractionallySizedBox(
                widthFactor: workout.progress,
                child: Container(
                  height: 8.h,
                  decoration: BoxDecoration(
                    color: workout.color,
                    borderRadius: BorderRadius.circular(AppDimensions.radiusFull),
                  ),
                ),
              ),
            ],
          ),
        ),
        SizedBox(width: AppDimensions.m),
        Container(
          padding: EdgeInsets.symmetric(
            horizontal: AppDimensions.s,
            vertical: AppDimensions.xxs,
          ),
          decoration: BoxDecoration(
            color: AppColors.white,
            borderRadius: BorderRadius.circular(AppDimensions.radiusFull),
          ),
          child: Text(
            '${(workout.progress * 100).toInt()}%',
            style: theme.textTheme.bodySmall?.copyWith(
              color: AppColors.black,
              fontWeight: FontWeight.w600,
              fontSize: 12.sp,
            ),
          ),
        ),
      ],
    );
  }
}
