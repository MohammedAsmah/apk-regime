part of 'index.dart';

class OfflineModal extends StatelessWidget {
  final VoidCallback onUseOffline;

  const OfflineModal({Key? key, required this.onUseOffline}) : super(key: key);

  static Future<void> show(BuildContext context, VoidCallback onUseOffline) {
    return showDialog(
      context: context,
      barrierDismissible: true,
      builder: (context) => OfflineModal(onUseOffline: onUseOffline),
    );
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final l10n = AppLocalizations.of(context)!;

    return Dialog(
      backgroundColor: AppColors.black,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(AppDimensions.radiusL),
      ),
      child: Padding(
        padding: EdgeInsets.all(AppDimensions.l),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text(
              l10n.aiAssistantIsOffline,
              style: theme.textTheme.titleLarge?.copyWith(
                color: AppColors.white,
                fontWeight: FontWeight.w600,
                fontSize: 18.sp,
              ),
              textAlign: TextAlign.center,
            ),
            SizedBox(height: AppDimensions.l),
            Container(
              padding: EdgeInsets.all(AppDimensions.xl),
              decoration: BoxDecoration(
                color: AppColors.white.withValues(alpha: 0.1),
                borderRadius: BorderRadius.circular(AppDimensions.radiusL),
              ),
              child: SvgPicture.string(
                width: 60.sp,
                color: AppColors.white,
                TRNXIcons.aiIsOffline.svg,
              ),
            ),
            SizedBox(height: AppDimensions.l),
            Text(
              l10n.pleaseConnectWifiOrData,
              style: theme.textTheme.bodyLarge?.copyWith(
                color: AppColors.white,
                fontSize: 14.sp,
              ),
              textAlign: TextAlign.center,
            ),
            SizedBox(height: AppDimensions.l),
            SizedBox(
              width: double.infinity,
              child: ElevatedButton(
                onPressed: () {
                  Navigator.of(context).pop();
                  onUseOffline();
                },
                style: ElevatedButton.styleFrom(
                  backgroundColor: AppColors.white,
                  foregroundColor: AppColors.black,
                  padding: EdgeInsets.symmetric(vertical: AppDimensions.m),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(
                      AppDimensions.radiusFull,
                    ),
                  ),
                ),
                child: Text(
                  l10n.useOfflineAi,
                  style: TextStyle(
                    fontSize: 14.sp,
                    fontWeight: FontWeight.w600,
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
