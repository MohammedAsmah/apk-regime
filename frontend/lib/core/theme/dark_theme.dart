part of index;

ThemeData getDarkTheme() {
  return ThemeData(
    useMaterial3: true,
    brightness: Brightness.dark,
    fontFamily: GoogleFonts.manrope().fontFamily,

    colorScheme: const ColorScheme.dark(
      primary: AppColors.lightSurface, // Lighter green for dark mode
      secondary: Color(0xFF3DC0FF), // Lighter blue for dark mode
      error: Color(0xFFFF5555),
      background: AppColors.darkBackground,
      surface: AppColors.darkSurface,
      onPrimary: Colors.black,
      onSecondary: Colors.black,
      onError: Colors.white,
      onBackground: AppColors.darkTextPrimary,
      onSurface: AppColors.darkTextPrimary,
    ),

    textTheme: GoogleFonts.manropeTextTheme(
      const TextTheme(
        displayLarge: TextStyle(
          fontSize: 32,
          fontWeight: FontWeight.bold,
          color: AppColors.darkTextPrimary,
        ),
        displayMedium: TextStyle(
          fontSize: 24,
          fontWeight: FontWeight.w600,
          color: AppColors.darkTextPrimary,
        ),
        titleLarge: TextStyle(
          fontSize: 18,
          fontWeight: FontWeight.w600,
          color: AppColors.darkTextPrimary,
        ),
        bodyLarge: TextStyle(fontSize: 16, color: AppColors.darkTextPrimary),
        bodyMedium: TextStyle(fontSize: 14, color: AppColors.darkTextPrimary),
        bodySmall: TextStyle(fontSize: 12, color: AppColors.darkTextSecondary),
      ),
    ),

    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ElevatedButton.styleFrom(
        backgroundColor: AppColors.white,
        foregroundColor: Colors.black,
        minimumSize: Size(double.infinity, AppDimensions.buttonHeight),
        padding: EdgeInsets.symmetric(
          horizontal: AppDimensions.l,
          vertical: AppDimensions.s,
        ),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(AppDimensions.radiusFull),
        ),
        elevation: 2,
        textStyle: const TextStyle(
          fontSize: 14,
          fontWeight: FontWeight.w600,
          letterSpacing: 0.5,
        ),
      ),
    ),

    // elevatedButtonTheme: ElevatedButtonThemeData(
    //   style: ElevatedButton.styleFrom(
    //     backgroundColor: const Color(0xFF6FD82C),
    //     foregroundColor: Colors.black,
    //     minimumSize: const Size(double.infinity, AppDimensions.buttonHeight),
    //     padding: const EdgeInsets.symmetric(
    //       horizontal: AppDimensions.l,
    //       vertical: AppDimensions.s,
    //     ),
    //     shape: RoundedRectangleBorder(
    //       borderRadius: BorderRadius.circular(AppDimensions.radiusM),
    //     ),
    //     elevation: 2,
    //     textStyle: const TextStyle(
    //       fontSize: 14,
    //       fontWeight: FontWeight.w600,
    //       letterSpacing: 0.5,
    //     ),
    //   ),
    // ),
    outlinedButtonTheme: OutlinedButtonThemeData(
      style: OutlinedButton.styleFrom(
        foregroundColor: AppColors.white,
        side: const BorderSide(color: AppColors.white),
        minimumSize: Size(double.infinity, AppDimensions.buttonHeight),
        padding: EdgeInsets.symmetric(
          horizontal: AppDimensions.l,
          vertical: AppDimensions.s,
        ),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(AppDimensions.radiusFull),
        ),
        textStyle: const TextStyle(
          fontSize: 14,
          fontWeight: FontWeight.w600,
          letterSpacing: 0.5,
        ),
      ),
    ),

    cardTheme: CardThemeData(
      elevation: 2,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(AppDimensions.radiusL),
      ),
      margin: EdgeInsets.symmetric(
        horizontal: AppDimensions.m,
        vertical: AppDimensions.cardMargin,
      ),
      color: AppColors.darkSurface,
    ),

    inputDecorationTheme: InputDecorationTheme(
      border: OutlineInputBorder(
        borderRadius: BorderRadius.circular(AppDimensions.radiusS),
        borderSide: BorderSide(
          color: AppColors.white.withOpacity(0.5),
        ),
      ),
      focusedBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(AppDimensions.radiusS),
        borderSide: BorderSide(
          color: AppColors.white.withOpacity(0.5),
        ),
      ),
      contentPadding: EdgeInsets.all(AppDimensions.m),
      filled: true,
      focusColor: AppColors.black,
      fillColor: AppColors.white.withOpacity(0.03),
    ),

    appBarTheme: const AppBarTheme(
      backgroundColor: AppColors.darkBackground,
      foregroundColor: AppColors.darkTextPrimary,
      elevation: 0,
    ),
  );
}
