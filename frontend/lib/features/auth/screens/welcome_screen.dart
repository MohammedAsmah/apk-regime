part of index;

class WelcomeScreen extends StatefulWidget {
  const WelcomeScreen({super.key});

  @override
  State<WelcomeScreen> createState() => _WelcomeScreenState();
}

class _WelcomeScreenState extends State<WelcomeScreen> {
  @override
  Widget build(BuildContext context) {
    return Consumer<AuthProvider>(
      builder: (context, authProvider, child) {
        var l10n = AppLocalizations.of(context)!;
        return Scaffold(
          backgroundColor: ColorScheme.of(context).background,
          body: SafeArea(
            child: Stack(
              children: [
                Positioned(
                  child: Align(
                    alignment: Alignment.centerRight,
                    child: Padding(
                      padding: EdgeInsets.only(bottom: 100.h),
                      child: Image.asset(
                        'assets/images/ellipse-1.png',
                        width: 300.w,
                      ),
                    ),
                  ),
                ),

                Expanded(
                  child: Container(
                    padding: EdgeInsets.symmetric(
                      horizontal: AppDimensions.screenPaddingHorizontal,
                      vertical: AppDimensions.l,
                    ),
                    alignment: AlignmentGeometry.center,
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      crossAxisAlignment: CrossAxisAlignment.center,
                      children: [
                        SizedBox(height: 48.h),
                        Align(
                          alignment: Alignment.center,
                          child: Image.asset(
                            'assets/images/vector.png',
                            width: 192.w,
                          ),
                        ),
                        Expanded(child: Container()),
                        SizedBox(height: 48.h),
                        Text(
                          l10n.startJourney,
                          style: TextStyle(fontSize: 24.sp),
                        ),
                        SizedBox(height: 12.h),
                        ElevatedButton(
                          onPressed: () {
                            context.push('/auth/login');
                          },
                          child: Text(
                            l10n.login,
                            style: TextStyle(fontSize: 20.sp),
                          ),
                        ),
                        SizedBox(height: 12.h),
                        OutlinedButton(
                          onPressed: () {
                            context.push('/auth/signup');
                          },
                          child: Text(
                            l10n.signup,
                            style: TextStyle(fontSize: 20.sp),
                          ),
                        ),
                        SizedBox(height: 48.h),
                      ],
                    ),
                  ),
                ),
              ],
            ),
          ),
        );
      },
    );
  }
}
