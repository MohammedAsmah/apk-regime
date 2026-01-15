part of index;

class SignUpScreen extends StatefulWidget {
  const SignUpScreen({super.key});

  @override
  State<SignUpScreen> createState() => _SignUpScreenState();
}

class _SignUpScreenState extends State<SignUpScreen> {
  late bool _obscureText = true;

  @override
  Widget build(BuildContext context) {
    var l10n = AppLocalizations.of(context)!;

    return Consumer<AuthProvider>(
      builder: (context, authProvider, child) {
        return Scaffold(
          backgroundColor: ColorScheme.of(context).background,
          body: SafeArea(
            child: SingleChildScrollView(
              child: Padding(
                padding: EdgeInsets.symmetric(
                  horizontal: AppDimensions.screenPaddingHorizontal,
                  vertical: AppDimensions.screenPaddingVertical,
                ),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: [
                    Text(
                      l10n.createAccount,
                      style: Theme.of(context).textTheme.headlineLarge!
                          .copyWith(
                            fontWeight: FontWeight.w500,
                            fontFamily: 'Poppins',
                          ),
                    ),
                    SizedBox(height: 10.h),

                    RichText(
                      text: TextSpan(
                        style: Theme.of(context).textTheme.bodyLarge,
                        children: [
                          TextSpan(text: l10n.alreadyHaveAnAccount),
                          TextSpan(
                            text: l10n.logIn,
                            style: Theme.of(context).textTheme.bodyLarge!
                                .copyWith(
                                  decoration: TextDecoration.underline,
                                  fontWeight: FontWeight.w500,
                                ),
                            recognizer: TapGestureRecognizer()
                              ..onTap = () {
                                context.push('/auth/login');
                              },
                          ),
                        ],
                      ),
                    ),

                    SizedBox(height: 30.h),

                    SizedBox(
                      width: 340.w,
                      child: Wrap(
                        children: [
                          Text(
                            l10n.firstName,
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

                    SizedBox(
                      width: 340.w,
                      child: Wrap(
                        children: [
                          Text(
                            l10n.lastName,
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

                    SizedBox(
                      width: 340.w,
                      child: Wrap(
                        children: [
                          Text(
                            l10n.emailAddress,
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

                    SizedBox(
                      width: 340.w,
                      child: Wrap(
                        children: [
                          Row(
                            children: [
                              Text(
                                l10n.password,
                                style: Theme.of(context).textTheme.bodyLarge!
                                    .copyWith(
                                      color: Theme.of(context).hintColor,
                                    ),
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
                        Navigator.push(
                          context,
                          MaterialPageRoute(builder: (ctx) => MoreInfoPage()),
                        );
                      },
                      child: Text(
                        l10n.createAccount,
                        style: TextStyle(fontSize: 20.sp),
                      ),
                    ),

                    SizedBox(height: AppDimensions.m),

                    GestureDetector(
                      onTap: () {
                        context.push('/auth/login');
                      },
                      child: Text(
                        l10n.logInInstead,
                        style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                          decoration: TextDecoration.underline,
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        );
      },
    );
  }
}
