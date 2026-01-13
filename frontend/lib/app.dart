part of imports;

class TRNX extends StatelessWidget {
  const TRNX({super.key});

  void _focusOut() {
    // (clear focus completely):
    FocusManager.instance.primaryFocus?.unfocus();
    // FocusScope.of(context).requestFocus(FocusNode());
  }

  @override
  Widget build(BuildContext context) {
    final settingsProvider = context.watch<SettingsProvider>();
    final locale = Locale(settingsProvider.state.localeCode);

    return GestureDetector(
      onTap: _focusOut,

      child: ScreenUtilInit(
        // designSize: const Size(375, 812),
        designSize: const Size(393, 852),
        minTextAdapt: true,
        splitScreenMode: true,
        builder: (context, child) {
          return MaterialApp.router(
            title: 'TRNX',
            debugShowCheckedModeBanner: false,
            locale: locale,
            color: Colors.transparent,
            localizationsDelegates: [
              AppLocalizations.delegate,
              GlobalMaterialLocalizations.delegate,
              GlobalCupertinoLocalizations.delegate,
              if (settingsProvider.state.localeCode == 'ar')
                GlobalWidgetsLocalizations.delegate,
            ],
            supportedLocales: const [Locale('en'), Locale('ar'), Locale('fr')],
            theme: getLightTheme(),
            darkTheme: getDarkTheme(),
            // themeMode: settingsProvider.state.themeMode,
            themeMode: ThemeMode.light,
            routerConfig: goRouter,
          );
        },
      ),
    );
  }
}
