part of 'index.dart';

class ProgressHeader extends StatelessWidget {
  final String userName;

  const ProgressHeader({
    super.key,
    required this.userName,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      crossAxisAlignment: CrossAxisAlignment.center,
      children: [
        Row(
          children: [
            Icon(
              Icons.fitness_center,
              color: AppColors.white,
              size: AppDimensions.iconL,
            ),
            SizedBox(width: AppDimensions.s),
            Text(
              'Progress screen',
              style: theme.textTheme.titleLarge?.copyWith(
                color: AppColors.white,
                fontWeight: FontWeight.w600,
                fontSize: 20.sp,
              ),
            ),
          ],
        ),
        CircleAvatar(
          radius: 20.r,
          backgroundColor: AppColors.darkSurface,
          backgroundImage: AssetImage('assets/images/avatar.png'),
        ),
      ],
    );
  }
}
