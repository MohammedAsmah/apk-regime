part of 'index.dart';

class ProfileScreen extends StatefulWidget {
  const ProfileScreen({super.key});

  @override
  State<ProfileScreen> createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final l10n = AppLocalizations.of(context)!;
    final authProvider = context.watch<AuthProvider>();
    final userProfile = authProvider.userProfile;

    if (userProfile == null) {
      return const Center(child: CircularProgressIndicator());
    }

    return SingleChildScrollView(
      child: Padding(
        padding: EdgeInsets.symmetric(
          horizontal: AppDimensions.screenPaddingHorizontal,
          vertical: AppDimensions.m,
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            SizedBox(height: AppDimensions.l),
                Center(
                  child: Stack(
                    children: [
                      GestureDetector(
                        onTap: () => context.push('/profile/edit'),
                        child: Container(
                          width: 120.w,
                          height: 120.w,
                          decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            color: theme.colorScheme.primary,
                            image: userProfile.profileImagePath != null
                                ? DecorationImage(
                                    image: FileImage(
                                      File(userProfile.profileImagePath!),
                                    ),
                                    fit: BoxFit.cover,
                                  )
                                : null,
                          ),
                          child: userProfile.profileImagePath == null
                              ? Icon(
                                  Icons.person,
                                  size: 60.sp,
                                  color: theme.colorScheme.onPrimary,
                                )
                              : null,
                        ),
                      ),
                      Positioned(
                        bottom: 0,
                        right: 0,
                        child: GestureDetector(
                          onTap: () => context.push('/profile/edit'),
                          child: Container(
                            width: 36.w,
                            height: 36.w,
                            decoration: BoxDecoration(
                              color: AppColors.warningOrange,
                              shape: BoxShape.circle,
                              border: Border.all(
                                color: theme.colorScheme.background,
                                width: 3,
                              ),
                            ),
                            child: Icon(
                              Icons.edit,
                              size: 18.sp,
                              color: AppColors.white,
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
                SizedBox(height: AppDimensions.m),
                Center(
                  child: Text(
                    userProfile.name,
                    style: theme.textTheme.headlineLarge?.copyWith(
                      fontWeight: FontWeight.bold,
                      fontSize: 24.sp,
                    ),
                  ),
                ),
                SizedBox(height: AppDimensions.l),
                ProfileHeader(
                  name: userProfile.name,
                  memberSince: userProfile.memberSince,
                  streak: userProfile.streak,
                  weightLost: userProfile.weightLost,
                  actualWeight: userProfile.actualWeight,
                  goalWeight: userProfile.goalWeight,
                  progressPercentage: authProvider.getProgressPercentage(),
                ),
                SizedBox(height: AppDimensions.l),
                Row(
                  children: [
                    Icon(
                      Icons.chat_bubble_outline,
                      size: 20.sp,
                      color: theme.colorScheme.onBackground.withValues(alpha: 0.6),
                    ),
                    SizedBox(width: AppDimensions.xs),
                    Text(
                      l10n.aidSupport,
                      style: theme.textTheme.titleMedium?.copyWith(
                        fontWeight: FontWeight.w600,
                        fontSize: 16.sp,
                      ),
                    ),
                  ],
                ),
                SizedBox(height: AppDimensions.m),
                ProfileMenuItem(
                  icon: Icons.info_outline,
                  title: l10n.helpCenter,
                  onTap: () {},
                ),
                SizedBox(height: AppDimensions.s),
                ProfileMenuItem(
                  icon: Icons.chat_outlined,
                  title: l10n.contactSupport,
                  onTap: () {},
                ),
                SizedBox(height: AppDimensions.l),
                Row(
                  children: [
                    Icon(
                      Icons.description_outlined,
                      size: 20.sp,
                      color: theme.colorScheme.onBackground.withValues(alpha: 0.6),
                    ),
                    SizedBox(width: AppDimensions.xs),
                    Text(
                      l10n.legal,
                      style: theme.textTheme.titleMedium?.copyWith(
                        fontWeight: FontWeight.w600,
                        fontSize: 16.sp,
                      ),
                    ),
                  ],
                ),
                SizedBox(height: AppDimensions.m),
                ProfileMenuItem(
                  icon: Icons.menu_book_outlined,
                  title: l10n.conditionsOfUse,
                  onTap: () {},
                ),
                SizedBox(height: AppDimensions.s),
                ProfileMenuItem(
                  icon: Icons.menu_book_outlined,
                  title: l10n.cancelMembership,
                  onTap: () {},
                ),
                SizedBox(height: AppDimensions.s),
                ProfileMenuItem(
                  icon: Icons.lock_outline,
                  title: l10n.privacyPolicyTitle,
                  onTap: () {},
                ),
            SizedBox(height: AppDimensions.xxl),
          ],
        ),
      ),
    );
  }
}
