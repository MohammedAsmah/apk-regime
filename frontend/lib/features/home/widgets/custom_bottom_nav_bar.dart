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
        borderRadius: BorderRadius.all(Radius.circular(AppDimensions.radiusXL)),
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
              _buildNavItem(context, TRNXIcons.homeIcon, 0, '/home'),
              _buildNavItem(context, TRNXIcons.coachIcon, 1, '/coach'),
              _buildCenterNavItem(),
              _buildNavItem(context, TRNXIcons.exerciseBikeIcon ,3 ,'/progress'),
              _buildNavItem(context, TRNXIcons.profileIcon, 4, '/profile'),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildNavItem(
    BuildContext context,
    TRNXIcons icon,
    int index,
    String route,
  ) {
    final isSelected = currentIndex == index;
    return IconButton(
      onPressed: () {
        context.go(route);
        onTap(index);
        
      },
      icon: SvgPicture.string(
              icon.svg,
              // colorMapper: const _MyColorMapper(),
              color: isSelected
                  ? AppColors.white
                  : AppColors.white.withValues(alpha: 0.4),
              width: 24.sp,
              height: 24.sp,
            ),
      padding: EdgeInsets.zero,
      constraints: BoxConstraints(minWidth: 48.w, minHeight: 48.h),
    );
  }

  Widget _buildCenterNavItem() {
    return Container(
      width: 48.w,
      height: 48.h,
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
        icon: SvgPicture.string(
          TRNXIcons.scaneIcon.svg,
          color: AppColors.white,
          width: 32.sp,
        ),
        padding: EdgeInsets.zero,
      ),
    );
  }
}

class _MyColorMapper extends ColorMapper {
  const _MyColorMapper();

  @override
  Color substitute(
    String? id,
    String elementName,
    String attributeName,
    Color color,
  ) {
    if (color == const Color(0xFFFF0000)) {
      return Colors.blue;
    }
    if (color == const Color(0xFF00FF00)) {
      return Colors.yellow;
    }
    return color;
  }
}
