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
      decoration: BoxDecoration(
        color: AppColors.black,
        borderRadius: BorderRadius.only(
          topLeft: Radius.circular(AppDimensions.radiusXL),
          topRight: Radius.circular(AppDimensions.radiusXL),
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
              _buildNavItem(Icons.home_filled, 0),
              _buildNavItem(Icons.self_improvement, 1),
              _buildCenterNavItem(),
              _buildNavItem(Icons.fitness_center, 3),
              _buildNavItem(Icons.person, 4),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildNavItem(IconData icon, int index) {
    final isSelected = currentIndex == index;
    return IconButton(
      onPressed: () => onTap(index),
      icon: Icon(
        icon,
        color: isSelected ? AppColors.white : AppColors.white.withValues(alpha: 0.4),
        size: 28.sp,
      ),
      padding: EdgeInsets.zero,
      constraints: BoxConstraints(
        minWidth: 48.w,
        minHeight: 48.h,
      ),
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
        icon: Icon(
          Icons.add,
          color: AppColors.white,
          size: 32.sp,
        ),
        padding: EdgeInsets.zero,
      ),
    );
  }
}
