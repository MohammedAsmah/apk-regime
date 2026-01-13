part of 'index.dart';

class CustomBottomNavBar extends StatelessWidget {
  final int currentIndex;
  final ValueChanged<int> onTap;

  const CustomBottomNavBar({
    super.key,
    required this.currentIndex,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: EdgeInsets.symmetric(horizontal: AppDimensions.m),
      decoration: BoxDecoration(
        color: AppColors.black,
        borderRadius: BorderRadius.all(
          Radius.circular(AppDimensions.radiusXL),
        ),
      ),
      child: SafeArea(
        top: false,
        child: Container(
          height: 70.h,
          padding: EdgeInsets.symmetric(
            horizontal: AppDimensions.xl,
            vertical: AppDimensions.s,
          ),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              _buildNavItem(context, Icons.home_filled, 0, '/home'),
              _buildNavItem(context, Icons.self_improvement, 1, '/progress'),
              _buildCenterNavItem(),
              _buildNavItem(context, Icons.fitness_center, 3, '/progress'),
              _buildNavItem(context, Icons.person, 4, '/profile'),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildNavItem(BuildContext context, IconData icon, int index, String route) {
    final isSelected = currentIndex == index;
    return IconButton(
      onPressed: () {
        context.go(route);
        onTap(index);
      },
      icon: Icon(
        icon,
        color: isSelected
            ? AppColors.white
            : AppColors.white.withValues(alpha: 0.4),
        size: 28.sp,
      ),
      padding: EdgeInsets.zero,
      constraints: BoxConstraints(minWidth: 48.w, minHeight: 48.h),
    );
  }

  Widget _buildCenterNavItem() {
    return Container(
      width: 60.w,
      height: 60.h,
      decoration: BoxDecoration(
        color: AppColors.white.withValues(alpha: 0.15),
        shape: BoxShape.circle,
        border: Border.all(
          color: AppColors.white.withValues(alpha: 0.3),
          width: 2,
        ),
      ),
      child: IconButton(
        onPressed: () => onTap(2),
        icon: Icon(Icons.add, color: AppColors.white, size: 32.sp),
        padding: EdgeInsets.zero,
      ),
    );
  }
}
