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
                      horizontal: AppDimensions.screenPaddingHorizontal.w,
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
                          style: ElevatedButton.styleFrom(
                            minimumSize: Size(double.infinity, 48.h),
                            backgroundColor: AppColors.darkSurface,
                          ),
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
                          style: OutlinedButton.styleFrom(
                            minimumSize: Size(double.infinity, 48.h),
                          ),
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

// class WelcomePage extends StatelessWidget {
//   const WelcomePage({super.key});

//   @override
//   Widget build(BuildContext context) {
//     var l10n = AppLocalizations.of(context)!;

//     return Scaffold(
//       body: SafeArea(
//         child: Column(
//           children: [
//             // first image center
//             Align(
//               alignment: Alignment.center,
//               child: Image.asset('assets/images/vector.png'),
//             ),
//             SizedBox(height: 20),
//             Align(
//               alignment: Alignment.centerRight,
//               child: Image.asset('assets/images/ellipse-1.png', height: 600),
//             ),
//             SizedBox(height: 20),

//             Text(
//               l10n.startJourney,
//               style: Theme.of(context).textTheme.titleLarge!.copyWith(
//                 fontWeight: FontWeight.w600,
//                 fontSize: 27,
//               ),
//             ),
//             SizedBox(height: 20),

//             // login button: add inkwell or gestorD
//             GestureDetector(
//               onTap: () {
//                 Navigator.push(
//                   context,
//                   MaterialPageRoute(builder: (context) => LoginPage()),
//                 );
//               },
//               child: Container(
//                 height: 56,
//                 width: 340,
//                 decoration: BoxDecoration(
//                   borderRadius: BorderRadius.circular(30),
//                   color: Color(0xFF0F0E0E),
//                   boxShadow: [
//                     BoxShadow(
//                       color: Colors.black.withAlpha(64), // 25%
//                       offset: Offset(0, 4),
//                       blurRadius: 4,
//                     ),
//                   ],
//                 ),
//                 child: Center(
//                   child: Text(
//                     l10n.login,
//                     style: Theme.of(context).textTheme.bodyLarge!.copyWith(
//                       fontSize: 20,
//                       color: Colors.white,
//                     ),
//                   ),
//                 ),
//               ),
//             ),
//             SizedBox(height: 20),
//             // sign up button: add inkwell or gestorD
//             GestureDetector(
//               onTap: () {
//                 Navigator.push(
//                   context,
//                   MaterialPageRoute(builder: (context) => SignUpPage()),
//                 );
//               },
//               child: Container(
//                 height: 56,
//                 width: 340,
//                 decoration: BoxDecoration(
//                   borderRadius: BorderRadius.circular(30),
//                   color: Color(0xFFE8E8E8),
//                   boxShadow: [
//                     BoxShadow(
//                       color: Colors.black.withAlpha(64), //25%
//                       offset: Offset(0, 4),
//                       blurRadius: 4,
//                     ),
//                   ],
//                 ),
//                 child: Center(
//                   child: Text(
//                     l10n.signup,
//                     style: Theme.of(context).textTheme.bodyLarge!.copyWith(
//                       fontSize: 20,
//                       color: Colors.black,
//                     ),
//                   ),
//                 ),
//               ),
//             ),
//           ],
//         ),
//       ),
//     );
//   }
// }
