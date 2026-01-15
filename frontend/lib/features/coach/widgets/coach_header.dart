part of 'index.dart';

class CoachHeader extends StatefulWidget {
  // final bool isOnline;
  // final ValueChanged<bool> onToggle;
  final String? profileImageUrl;
  const CoachHeader({
    Key? key,
    // required this.isOnline,
    // required this.onToggle,
    this.profileImageUrl,
  }) : super(key: key);

  @override
  State<CoachHeader> createState() => _CoachHeaderState();
}

class _CoachHeaderState extends State<CoachHeader> {
  late bool _isOnline = true;

  _handleToggle(bool value) {
    setState(() {
      _isOnline = value;
    });

    if (!value) {
      OfflineModal.show(context, () {
        setState(() {
          _isOnline = true;
        });
      });
    }
  }


  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final isDark = theme.brightness == Brightness.dark;

    return Expanded(
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Row(
            children: [
              SvgPicture.string(
                TRNXIcons.coachIcon.svg,
                width: AppDimensions.iconL,
                color: theme.colorScheme.onBackground,
              ),
              SizedBox(width: AppDimensions.s),
              Text(
                'AI Assistant',
                style: theme.textTheme.titleLarge?.copyWith(
                  fontWeight: FontWeight.w600,
                  fontSize: 20.sp,
                ),
              ),
              SizedBox(width: AppDimensions.s),
              Transform.scale(
                scale: 0.8,
                child: Switch(
                  value: _isOnline,
                  onChanged: _handleToggle,
                  activeTrackColor: AppColors.successGreen,
                  inactiveThumbColor: AppColors.errorRed,
                  trackOutlineColor: WidgetStateProperty.all(
                    theme.colorScheme.onBackground,
                  ),
                ),
              ),
              SizedBox(width: AppDimensions.s),
            ],
          ),
        ],
      ),
    );
  }
}
