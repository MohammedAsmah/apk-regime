part of imports;

class DefHeader extends StatelessWidget {
  final TRNXIcons icon;
  final String title;

  const DefHeader({required this.icon, required this.title});

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    // final l10n = AppLocalizations.of(context)!;
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      crossAxisAlignment: CrossAxisAlignment.center,
      children: [
        Row(
          children: [
            if (icon == TRNXIcons.backIcon)
              GestureDetector(
                onTap: () {
                  context.pop();
                },
                child: SvgPicture.string(
                  icon.svg,
                  width: AppDimensions.iconS,
                  color: theme.colorScheme.onBackground,
                ),
              ),
            if (icon != TRNXIcons.backIcon)
              SvgPicture.string(
                icon.svg,
                width: AppDimensions.iconL,
                color: theme.colorScheme.onBackground,
              ),
            SizedBox(width: AppDimensions.s),
            Text(
              title,
              style: theme.textTheme.titleLarge?.copyWith(
                fontWeight: FontWeight.w600,
                fontSize: 20.sp,
              ),
            ),
          ],
        ),
      ],
    );
  }
}
