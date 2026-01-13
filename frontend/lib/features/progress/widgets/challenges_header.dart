part of 'index.dart';

class ChallengesHeader extends StatelessWidget {
  final String userName;

  const ChallengesHeader({
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
            GestureDetector(
              onTap: () {
                Navigator.of(context).pop();
              },
              child: Icon(
                Icons.arrow_back_ios,
                color: AppColors.white,
                size: AppDimensions.iconM,
              ),
            ),
            SizedBox(width: AppDimensions.s),
            Text(
              'Challenges done',
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
