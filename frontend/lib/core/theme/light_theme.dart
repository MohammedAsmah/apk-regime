part of index;

ThemeData getLightTheme() {
  return ThemeData(
    useMaterial3: true,
    brightness: Brightness.light,
    fontFamily: GoogleFonts.manrope().fontFamily,
    
    colorScheme: const ColorScheme.light(
      primary: AppColors.white,
      secondary: AppColors.brandBlue,
      error: AppColors.errorRed,
      background: Color(0xFFF7F3EB),
      surface: AppColors.lightSurface,
      onPrimary: Colors.white,
      onSecondary: Colors.white,
      onError: Colors.white,
      onBackground: AppColors.lightTextPrimary,
      onSurface: AppColors.lightTextPrimary,
    ),
    
    textTheme: GoogleFonts.manropeTextTheme(
      TextTheme(
        displayLarge: TextStyle(
          fontSize: 32.sp,
          fontWeight: FontWeight.bold,
          color: AppColors.lightTextPrimary,
        ),
        displayMedium: TextStyle(
          fontSize: 24.sp,
          fontWeight: FontWeight.w600,
          color: AppColors.lightTextPrimary,
        ),
        titleLarge: TextStyle(
          fontSize: 18.sp,
          fontWeight: FontWeight.w600,
          color: AppColors.lightTextPrimary,
        ),
        bodyLarge: TextStyle(
          fontSize: 16.sp,
          color: AppColors.lightTextPrimary,
        ),
        bodyMedium: TextStyle(
          fontSize: 14.sp,
          color: AppColors.lightTextPrimary,
        ),
        bodySmall: TextStyle(
          fontSize: 12.sp,
          color: AppColors.lightTextSecondary,
        ),
      ),
    ),
    
    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ElevatedButton.styleFrom(
        backgroundColor: AppColors.black,
        foregroundColor: Colors.white,
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
    

    outlinedButtonTheme: OutlinedButtonThemeData(
      style: OutlinedButton.styleFrom(
        foregroundColor: AppColors.black,
        side: const BorderSide(color: AppColors.black),
        minimumSize: Size(double.infinity, AppDimensions.buttonHeight),
        padding:  EdgeInsets.symmetric(
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
      elevation: 1,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(AppDimensions.radiusL),
      ),
      margin: EdgeInsets.symmetric(
        horizontal: AppDimensions.m,
        vertical: AppDimensions.cardMargin,
      ),
    ),
    
    inputDecorationTheme: InputDecorationTheme(
      border: OutlineInputBorder(
        borderRadius: BorderRadius.circular(AppDimensions.radiusS),
        borderSide: BorderSide(
          color: AppColors.black.withOpacity(0.5),
        ),
      ),
      focusedBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(AppDimensions.radiusS),
        borderSide: BorderSide(
          color: AppColors.black.withOpacity(0.5),
        ),
      ),
      contentPadding: EdgeInsets.all(AppDimensions.s),
      filled: true,
      fillColor: AppColors.black.withOpacity(0.03),
    ),
    
    appBarTheme: const AppBarTheme(
      backgroundColor: AppColors.lightBackground,
      foregroundColor: AppColors.lightTextPrimary,
      elevation: 0,
    ),
  );
}

