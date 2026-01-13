part of 'index.dart';

class CalendarEventsCard extends StatelessWidget {
  final int selectedDay;
  final String currentMonth;
  final String upcomingEvent;
  final VoidCallback onAddEvent;
  final VoidCallback onSeeMore;

  const CalendarEventsCard({
    super.key,
    required this.selectedDay,
    required this.currentMonth,
    required this.upcomingEvent,
    required this.onAddEvent,
    required this.onSeeMore,
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
            'calendar and events',
            style: theme.textTheme.bodyLarge?.copyWith(
              color: AppColors.white,
              fontWeight: FontWeight.w600,
              fontSize: 16.sp,
            ),
          ),
          SizedBox(height: AppDimensions.l),
          _buildCalendarGrid(),
          SizedBox(height: AppDimensions.l),
          Text(
            'upcoming event : $upcomingEvent',
            style: theme.textTheme.bodyMedium?.copyWith(
              color: AppColors.white.withValues(alpha: 0.8),
              fontSize: 14.sp,
            ),
          ),
          SizedBox(height: AppDimensions.m),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              _buildActionButton('add event', theme, onAddEvent),
              SizedBox(width: AppDimensions.m),
              _buildActionButton('see more', theme, onSeeMore),
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildCalendarGrid() {
    final days = [15, 16, 17, 18, 19, 20, 21];
    
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceAround,
      children: days.map((day) {
        final isSelected = day == selectedDay;
        return Container(
          width: 40.w,
          height: 40.h,
          decoration: BoxDecoration(
            color: isSelected ? AppColors.errorRed : Colors.transparent,
            shape: BoxShape.circle,
            border: isSelected ? null : Border.all(
              color: AppColors.darkSurface,
              width: 1,
            ),
          ),
          child: Center(
            child: Text(
              day.toString(),
              style: TextStyle(
                color: AppColors.white,
                fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
                fontSize: 14.sp,
              ),
            ),
          ),
        );
      }).toList(),
    );
  }

  Widget _buildActionButton(String label, ThemeData theme, VoidCallback onTap) {
    return GestureDetector(
      onTap: onTap,
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
          label,
          style: theme.textTheme.bodyMedium?.copyWith(
            color: AppColors.black,
            fontWeight: FontWeight.w600,
            fontSize: 14.sp,
          ),
        ),
      ),
    );
  }
}
