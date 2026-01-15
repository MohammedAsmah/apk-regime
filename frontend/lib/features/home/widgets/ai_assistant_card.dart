part of 'index.dart';

class AIAssistantCard extends StatelessWidget {
  final String userName;
  final TextEditingController controller;
  final VoidCallback onSubmit;
  
  const AIAssistantCard({
    Key? key,
    required this.userName,
    required this.controller,
    required this.onSubmit,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final l10n = AppLocalizations.of(context)!;
    final theme = Theme.of(context);

    return GestureDetector(
      onTap: () => context.go('/coach'),
      child: Container(
        padding: EdgeInsets.all(AppDimensions.l),
        decoration: BoxDecoration(
          color: AppColors.black,
          borderRadius: BorderRadius.circular(AppDimensions.radiusL),
        ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Container(
                padding: EdgeInsets.all(AppDimensions.xs),
                decoration: BoxDecoration(
                  color: AppColors.white.withValues(alpha: 0.1),
                  borderRadius: BorderRadius.circular(AppDimensions.radiusS),
                ),
                child: Icon(
                  Icons.psychology,
                  color: AppColors.white,
                  size: AppDimensions.iconM,
                ),
              ),
              SizedBox(width: AppDimensions.s),
              Text(
                l10n.aiAssistant,
                style: theme.textTheme.titleLarge?.copyWith(
                  color: AppColors.white,
                  fontWeight: FontWeight.w600,
                  fontSize: 16.sp,
                ),
              ),
            ],
          ),
          SizedBox(height: AppDimensions.m),
          Text(
            'Hey $userName! ${l10n.howCanIHelpYouToday}',
            style: theme.textTheme.bodyLarge?.copyWith(
              color: AppColors.white,
              fontSize: 14.sp,
            ),
          ),
          SizedBox(height: AppDimensions.m),
          Wrap(
            spacing: AppDimensions.s,
            runSpacing: AppDimensions.s,
            children: [
              _buildAISuggestionChip(
                l10n.foodIdeas,
                AppColors.successGreen,
              ),
              _buildAISuggestionChip(
                l10n.howToReduce,
                AppColors.brandBlue,
              ),
              _buildAISuggestionChip(
                l10n.workoutRoutines,
                AppColors.warningOrange,
              ),
            ],
          ),
          SizedBox(height: AppDimensions.m),
          Container(
            decoration: BoxDecoration(
              color: AppColors.white.withValues(alpha: 0.1),
              borderRadius: BorderRadius.circular(AppDimensions.radiusFull),
            ),
            child: TextField(
              controller: controller,
              style: TextStyle(color: AppColors.white, fontSize: 14.sp),
              decoration: InputDecoration(
                hintText: l10n.whatsOnYourMind,
                hintStyle: TextStyle(
                  color: AppColors.white.withValues(alpha: 0.5),
                  fontSize: 14.sp,
                ),
                border: InputBorder.none,
                contentPadding: EdgeInsets.symmetric(
                  horizontal: AppDimensions.m,
                  vertical: AppDimensions.s,
                ),
                suffixIcon: GestureDetector(
                  onTap: onSubmit,
                  child: Container(
                    margin: EdgeInsets.all(AppDimensions.xxs),
                    decoration: BoxDecoration(
                      color: AppColors.white,
                      shape: BoxShape.circle,
                    ),
                    child: Icon(
                      Icons.arrow_forward,
                      color: AppColors.black,
                      size: 18.sp,
                    ),
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
      ),
    );
  }

  Widget _buildAISuggestionChip(String label, Color color) {
    return Container(
      padding: EdgeInsets.symmetric(
        horizontal: AppDimensions.m,
        vertical: AppDimensions.s,
      ),
      decoration: BoxDecoration(
        color: color.withValues(alpha: 0.2),
        borderRadius: BorderRadius.circular(AppDimensions.radiusFull),
      ),
      child: Text(
        label,
        style: TextStyle(
          color: AppColors.white,
          fontSize: 12.sp,
          fontWeight: FontWeight.w500,
        ),
      ),
    );
  }
}
