part of index;

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  late bool _obscureText = true;

  @override
  Widget build(BuildContext context) {
    var l10n = AppLocalizations.of(context)!;

    return Consumer<AuthProvider>(
      builder: (context, authProvider, child) {
        return Scaffold(
          backgroundColor: ColorScheme.of(context).background,
          body: SafeArea(
            child: Container(
              padding: EdgeInsets.symmetric(
                horizontal: AppDimensions.screenPaddingHorizontal,
                vertical: AppDimensions.screenPaddingVertical,
              ),
              alignment: AlignmentGeometry.center,
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  Text(
                    l10n.login,
                    style: Theme.of(context).textTheme.headlineLarge!.copyWith(
                      fontWeight: FontWeight.w500,
                      fontFamily: 'Poppins',
                    ),
                  ),
                  SizedBox(height: 50.h),

                  // email textFiled
                  SizedBox(
                    width: 340.w,
                    child: Wrap(
                      children: [
                        Text(
                          l10n.emailOrMobile,
                          style: Theme.of(context).textTheme.bodyLarge!
                              .copyWith(color: Theme.of(context).hintColor),
                        ),
                        TextField(
                          decoration: InputDecoration(
                            border: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(
                                AppDimensions.radiusS,
                              ),
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),

                  SizedBox(height: AppDimensions.xs),

                  // Password textFiled
                  SizedBox(
                    width: 340.w,
                    child: Wrap(
                      children: [
                        Row(
                          children: [
                            // password textFiled
                            Text(
                              l10n.password,
                              style: Theme.of(context).textTheme.bodyLarge!
                                  .copyWith(color: Theme.of(context).hintColor),
                            ),
                            Spacer(),
                            IconButton(
                              onPressed: () {
                                setState(() {
                                  _obscureText = !_obscureText;
                                });
                              },
                              icon: Row(
                                children: [
                                  Icon(
                                    _obscureText
                                        ? Icons.visibility_off
                                        : Icons.visibility,
                                  ),
                                  SizedBox(width: 4.w),
                                  Text(
                                    _obscureText ? l10n.show : l10n.hide,
                                    style: Theme.of(context)
                                        .textTheme
                                        .bodyMedium!
                                        .copyWith(
                                          color: Theme.of(context).hintColor,
                                        ),
                                  ),
                                ],
                              ),
                              color: Theme.of(context).hintColor,
                              iconSize: AppDimensions.iconM,
                            ),
                          ],
                        ),
                        TextField(
                          obscureText: _obscureText,
                          decoration: InputDecoration(
                            border: OutlineInputBorder(
                              borderRadius: BorderRadius.circular(
                                AppDimensions.radiusS,
                              ),
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),

                  SizedBox(height: AppDimensions.xl),

                  OutlinedButton(
                    onPressed: () {
                      // #TODO: implement login functionality
                    },
                    child: Text(l10n.login, style: TextStyle(fontSize: 20.sp)),
                  ),

                  RichText(
                    textAlign: TextAlign.center,
                    text: TextSpan(
                      style: Theme.of(
                        context,
                      ).textTheme.bodyMedium!.copyWith(fontSize: 11.sp),
                      children: [
                        TextSpan(text: l10n.byContinuingYouAgreeToThe),
                        TextSpan(
                          text: l10n.termsOfUse,
                          style: const TextStyle(
                            decoration: TextDecoration.underline,
                            fontWeight: FontWeight.w500,
                          ),
                          recognizer: TapGestureRecognizer()
                            ..onTap = () {
                              // #TODO: implement terms of use navigation
                            },
                        ),
                        TextSpan(text: l10n.and),
                        TextSpan(
                          text: l10n.privacyPolicy,
                          style: const TextStyle(
                            decoration: TextDecoration.underline,
                            fontWeight: FontWeight.w500,
                          ),
                          recognizer: TapGestureRecognizer()
                            ..onTap = () {
                              // #TODO: implement privacy policy navigation
                            },
                        ),
                      ],
                    ),
                  ),
                  SizedBox(height: AppDimensions.m),

                  Row(
                    children: [
                      GestureDetector(
                        onTap: () {
                          // todo
                        },
                        child: Text(
                          l10n.otherIssueWithLogin,
                          style: Theme.of(context).textTheme.bodyMedium
                              ?.copyWith(
                                decoration: TextDecoration.underline,
                                fontWeight: FontWeight.w500,
                              ),
                        ),
                      ),
                      Spacer(),
                      GestureDetector(
                        onTap: () {
                          // todo
                        },
                        child: Text(
                          l10n.forgotPassword,
                          style: Theme.of(context).textTheme.bodyMedium
                              ?.copyWith(
                                decoration: TextDecoration.underline,
                                fontWeight: FontWeight.w500,
                              ),
                        ),
                      ),
                    ],
                  ),
                  Expanded(child: Container()),

                  // info
                  Row(
                    children: [
                      Expanded(child: Divider(thickness: 2, color: AppColors.black.withOpacity(0.3))),
                      SizedBox(width: AppDimensions.m),

                      Text(
                        l10n.newToOurCommunity,
                        style: Theme.of(context).textTheme.titleLarge!.copyWith(
                          color: Theme.of(context).hintColor,
                          fontFamily: 'Avenir',
                          fontSize: 22.sp,
                          fontStyle: FontStyle.italic,
                          fontWeight: FontWeight.w400,
                        ),
                      ),
                      SizedBox(width: AppDimensions.m),

                      Expanded(child: Divider(thickness: 2, color: AppColors.black.withOpacity(0.3))),
                    ],
                  ),

                  SizedBox(height: AppDimensions.l),

                  // create account button
                  OutlinedButton(
                    onPressed: () {
                      context.push('/auth/signup');
                    },
                    child: Text(
                      l10n.createAccount,
                      style: TextStyle(fontSize: 20.sp),
                    ),
                  ),
                ],
              ),
            ),
          ),
        );
      },
    );
  }
}
