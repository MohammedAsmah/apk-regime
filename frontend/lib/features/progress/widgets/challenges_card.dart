part of 'index.dart';

class ChallengesCard extends StatelessWidget {
  final List<Challenge> challenges;

  const ChallengesCard({
    super.key,
    required this.challenges,
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
            'Challenges',
            style: theme.textTheme.bodyLarge?.copyWith(
              color: AppColors.white,
              fontWeight: FontWeight.w600,
              fontSize: 16.sp,
            ),
          ),
          SizedBox(height: AppDimensions.l),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: challenges.map((challenge) => _buildChallengeBadge(challenge)).toList(),
          ),
          SizedBox(height: AppDimensions.l),
          Center(
            child: GestureDetector(
              onTap: () {
                context.push('/challenges');
              },
              child: Container(
                padding: EdgeInsets.symmetric(
                  horizontal: AppDimensions.l,
                  vertical: AppDimensions.s,
                ),
                decoration: BoxDecoration(
                  color: AppColors.white,
                  borderRadius: BorderRadius.circular(AppDimensions.radiusFull),
                ),
                child: Text(
                  'see more',
                  style: theme.textTheme.bodyMedium?.copyWith(
                    color: AppColors.black,
                    fontWeight: FontWeight.w600,
                    fontSize: 14.sp,
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildChallengeBadge(Challenge challenge) {
    return Container(
      width: 60.w,
      height: 60.h,
      decoration: BoxDecoration(
        color: challenge.color.withValues(alpha: 0.2),
        shape: BoxShape.circle,
        border: Border.all(
          color: challenge.color,
          width: 3,
        ),
      ),
      child: Stack(
        alignment: Alignment.center,
        children: [
          Icon(
            challenge.icon,
            color: challenge.color,
            size: 30.sp,
          ),
          if (challenge.isCompleted)
            Positioned(
              bottom: -5,
              child: Container(
                padding: EdgeInsets.all(4.w),
                decoration: BoxDecoration(
                  color: challenge.color,
                  shape: BoxShape.circle,
                ),
                child: Icon(
                  Icons.check,
                  color: AppColors.white,
                  size: 12.sp,
                ),
              ),
            ),
        ],
      ),
    );
  }
}
