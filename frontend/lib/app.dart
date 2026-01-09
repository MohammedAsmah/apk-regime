
part of imports;

class TRNX extends StatelessWidget {
  const TRNX({super.key});

  @override
  Widget build(BuildContext context) {
    final settingsProvider = context.watch<SettingsProvider>();
    return ScreenUtilInit(
      designSize: const Size(375, 812),
      minTextAdapt: true,
      splitScreenMode: true,
      builder: (context, child) {
        return MaterialApp.router(
          title: 'TRNX',
          debugShowCheckedModeBanner: false,
          theme: getLightTheme(),
          darkTheme: getDarkTheme(),
          themeMode: settingsProvider.state.themeMode,
          routerConfig: goRouter,
        );
      },
    );
  }
}

